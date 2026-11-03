"""Integration checks for portable installation, dependency closure and safety."""

import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from install_skills import REPO, SKILLS, install
from validate_bundle import validate_bundle


class InstallSkillsTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.project = Path(self.tmp.name)

    def test_all_agents_install_complete_portable_bundle(self):
        self.assertGreater(install(self.project, ["codex", "cursor", "claude-code"], True), 0)
        for directory in (".agents/skills", ".claude/skills"):
            root = self.project / directory
            self.assertEqual({p.name for p in root.iterdir()}, set(SKILLS))
            self.assertEqual(validate_bundle(root), [])
            for name in SKILLS:
                for original in (REPO / "skills" / name).rglob("*"):
                    if original.is_file():
                        copy = root / name / original.relative_to(REPO / "skills" / name)
                        self.assertEqual(copy.read_bytes(), original.read_bytes())
        self.assertTrue((self.project / "AGENTS.md").is_file())
        self.assertTrue((self.project / ".claude/rules/ai-design-routing.md").is_file())
        self.assertTrue((self.project / ".cursor/rules/ai-design-routing.mdc").is_file())
        self.assertEqual(install(self.project, ["codex", "cursor", "claude-code"], True), 0)

    def test_existing_instructions_are_preserved_and_not_duplicated(self):
        target = self.project / "AGENTS.md"
        existing = "# Правила проекта\r\nСохрани существующие компоненты.".encode("utf-8")
        target.write_bytes(existing)
        install(self.project, ["codex"], True)
        self.assertTrue(target.read_bytes().startswith(existing))
        once = target.read_bytes()
        self.assertEqual(install(self.project, ["codex"], True), 0)
        self.assertEqual(target.read_bytes(), once)

    def test_conflict_aborts_before_other_files_are_written(self):
        target = self.project / ".agents/skills/monitoring-ui/SKILL.md"
        target.parent.mkdir(parents=True)
        target.write_text("user customization", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "differs"):
            install(self.project, ["codex"], True)
        self.assertEqual(target.read_text(), "user customization")
        self.assertFalse((self.project / ".agents/skills/design-core").exists())
        self.assertFalse((self.project / "AGENTS.md").exists())

    def test_rule_conflict_also_prevents_install(self):
        target = self.project / ".cursor/rules/ai-design-routing.mdc"
        target.parent.mkdir(parents=True)
        target.write_text("user rule", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "differs"):
            install(self.project, ["cursor"], True)
        self.assertFalse((self.project / ".agents").exists())

    def test_no_rules_without_option(self):
        install(self.project, ["codex", "claude-code", "cursor"])
        self.assertFalse((self.project / "AGENTS.md").exists())
        self.assertFalse((self.project / ".claude/rules").exists())
        self.assertFalse((self.project / ".cursor").exists())

    def test_incomplete_source_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "Incomplete source"):
            install(self.project, ["codex"], source=self.project)
        self.assertEqual(list(self.project.iterdir()), [])

    def test_missing_project_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "does not exist"):
            install(self.project / "missing", ["codex"])

    def test_changed_managed_block_is_not_overwritten(self):
        target = self.project / "AGENTS.md"
        content = "<!-- ai-design-skills:start -->\ncustom\n<!-- ai-design-skills:end -->\n"
        target.write_text(content, encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "routing block differs"):
            install(self.project, ["codex"], True)
        self.assertEqual(target.read_text(), content)
        self.assertFalse((self.project / ".agents").exists())

    def test_symlink_destination_is_rejected(self):
        with tempfile.TemporaryDirectory() as outside:
            try:
                (self.project / ".agents").symlink_to(outside, target_is_directory=True)
            except OSError as exc:
                self.skipTest(f"OS does not permit symlink creation: {exc}")
            with self.assertRaisesRegex(ValueError, "linked destination"):
                install(self.project, ["codex"])
            self.assertEqual(list(Path(outside).iterdir()), [])

    def test_missing_dependency_detected_after_install(self):
        install(self.project, ["codex"])
        root = self.project / ".agents/skills"
        (root / "design-core/SKILL.md").unlink()
        errors = validate_bundle(root)
        self.assertTrue(any("missing local link" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
