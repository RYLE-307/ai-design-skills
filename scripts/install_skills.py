#!/usr/bin/env python3
"""Install the complete web suite without overwriting existing user files.

Python 3.10+, standard library only. Paths resolve from the script location.
Identical files are skipped. A conflicting file aborts before any writes.
Optional routing rules are added separately; existing AGENTS.md text is retained.
"""

import argparse
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
SKILLS = (
    "design-router", "design-core", "landing-page-design", "web-app-design",
    "dashboard-design", "admin-panel-design", "forms-settings",
    "data-table-design", "monitoring-ui",
)
AGENT_DIRS = {
    "codex": ".agents/skills",
    "claude-code": ".claude/skills",
    "cursor": ".agents/skills",
}
START = "<!-- ai-design-skills:start -->"
END = "<!-- ai-design-skills:end -->"


def routing_text(skill_dir):
    return (
        "For requests to build, change or review a web interface, read "
        f"`{skill_dir}/design-router/SKILL.md` and follow its routing. "
        "Load core once and only relevant specialists. Preserve the user's "
        "scope and existing project conventions. Skip backend-only work and "
        "native Figma editing.\n"
    )


def install(project, agents, with_router_rule=False, source=REPO):
    project = Path(project).expanduser().resolve()
    source = Path(source).resolve()
    if not project.is_dir():
        raise ValueError(f"Project directory does not exist: {project}")
    if not agents or any(agent not in AGENT_DIRS for agent in agents):
        raise ValueError("Choose codex, claude-code or cursor")
    planned = {}

    def plan(target, data, allow_append=False):
        # Refuse path redirection, even symlinks that happen to point inside.
        for part in (target, *target.parents):
            if part == project:
                break
            if part.is_symlink() or getattr(part, "is_junction", lambda: False)():
                raise ValueError(f"Refusing linked destination: {part}")
        if not target.resolve().is_relative_to(project):
            raise ValueError(f"Destination escapes project: {target}")
        if target.exists():
            if not target.is_file():
                raise ValueError(f"Expected file: {target}")
            current = target.read_bytes()
            if current == data:
                return
            if not allow_append:
                raise ValueError(f"Existing file differs; review it before updating: {target}")
        planned[target] = data

    destinations = sorted({AGENT_DIRS[agent] for agent in agents})
    for destination in destinations:
        for name in SKILLS:
            folder = source / "skills" / name
            if not (folder / "SKILL.md").is_file() or not (folder / "LICENSE.txt").is_file():
                raise ValueError(f"Incomplete source skill: {folder}")
            for path in sorted(folder.rglob("*")):
                if path.is_symlink():
                    raise ValueError(f"Refusing linked source: {path}")
                if path.is_file():
                    plan(project / destination / name / path.relative_to(folder), path.read_bytes())

    if with_router_rule:
        if "codex" in agents:
            target = project / "AGENTS.md"
            # Check target safety before reading it.
            if target.is_symlink():
                raise ValueError(f"Refusing linked destination: {target}")
            current = target.read_bytes() if target.is_file() else b""
            block = (START + "\n" + routing_text(".agents/skills") + END + "\n").encode()
            if START.encode() in current or END.encode() in current:
                if current.count(START.encode()) != 1 or current.count(END.encode()) != 1 or block not in current:
                    raise ValueError("Existing AI design routing block differs; review AGENTS.md")
            else:
                separator = b"\n\n" if current and not current.endswith(b"\n") else b"\n" if current else b""
                plan(target, current + separator + block, allow_append=True)
        if "claude-code" in agents:
            plan(project / ".claude/rules/ai-design-routing.md", routing_text(".claude/skills").encode())
        if "cursor" in agents:
            text = "---\ndescription: Route web UI work to the design suite\nalwaysApply: true\n---\n\n"
            plan(project / ".cursor/rules/ai-design-routing.mdc", (text + routing_text(".agents/skills")).encode())

    # All conflicts are checked before writing. IO failures can leave a partial
    # install; rerunning safely completes identical files after the cause is fixed.
    for target, data in planned.items():
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
    return len(planned)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", required=True, type=Path, help="Existing target project")
    parser.add_argument("--agent", required=True, action="append", choices=AGENT_DIRS)
    parser.add_argument("--with-router-rule", action="store_true", help="Add a scoped routing instruction for each agent")
    args = parser.parse_args(argv)
    try:
        count = install(args.project, args.agent, args.with_router_rule)
    except (OSError, ValueError) as exc:
        parser.exit(1, f"Install failed: {exc}\n")
    print(f"Installed {len(SKILLS)} skills; wrote {count} files. Existing identical files were kept.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
