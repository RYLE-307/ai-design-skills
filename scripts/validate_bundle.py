#!/usr/bin/env python3
"""Check local Markdown dependency links and installed license files."""

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

from install_skills import SKILLS


def validate_bundle(root):
    root = Path(root)
    errors = []
    for name in SKILLS:
        folder = root / name
        for required in ("SKILL.md", "LICENSE.txt"):
            if not (folder / required).is_file():
                errors.append(f"{name}: missing {required}")
    for path in root.rglob("*.md"):
        text = re.sub(r"```.*?```", "", path.read_text(encoding="utf-8"), flags=re.S)
        for target in re.findall(r"\[[^\]]*\]\(([^\s)]+)\)", text):
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            destination = (path.parent / unquote(parsed.path)).resolve()
            if not destination.is_relative_to(root.resolve()):
                errors.append(f"{path}: link escapes installed bundle: {target}")
            elif not destination.exists():
                errors.append(f"{path}: missing local link: {target}")
    return errors


if __name__ == "__main__":
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("skills")
    errors = validate_bundle(root)
    for error in errors:
        print(error)
    print(f"Bundle dependency checks: {len(errors)} problem(s).")
    raise SystemExit(bool(errors))
