#!/usr/bin/env python3
"""Valida estrutura, frontmatter e links relativos das skills em skills/."""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
# Campos aceitos pelo padrão Agent Skills fora do Claude Code (claude.ai, Skills API, skill-creator).
ALLOWED_KEYS = {"name", "description", "license", "allowed-tools", "metadata", "compatibility"}
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
LINK_RE = re.compile(r"\]\(([^)#\s]+)")
FENCE_RE = re.compile(r"^(```|~~~).*?^\1", re.S | re.M)


def frontmatter(text):
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 4)
    if end == -1:
        return None
    fields = {}
    for line in text[4:end].splitlines():
        match = re.match(r"^([A-Za-z_-]+):\s*(.*)$", line)
        if match:
            fields[match.group(1)] = match.group(2).strip().strip("\"'")
    return fields


def check_links(path, errors):
    text = FENCE_RE.sub("", path.read_text(encoding="utf-8"))
    for target in LINK_RE.findall(text):
        if re.match(r"^[a-z]+:", target):
            continue
        if not (path.parent / target).exists():
            shown = path.relative_to(ROOT) if path.is_relative_to(ROOT) else path
            errors.append(f"{shown}: link quebrado para {target}")


def validate(skill, errors):
    skill_md = skill / "SKILL.md"
    if not skill_md.exists():
        errors.append(f"{skill.name}: SKILL.md ausente")
        return
    fields = frontmatter(skill_md.read_text(encoding="utf-8"))
    if fields is None:
        errors.append(f"{skill.name}: frontmatter ausente ou malformado")
        return
    for key in sorted(set(fields) - ALLOWED_KEYS):
        errors.append(f"{skill.name}: campo de frontmatter não portável: {key}")
    name = fields.get("name", "")
    if name != skill.name or not NAME_RE.match(name) or len(name) > 64:
        errors.append(f"{skill.name}: name deve ser igual à pasta, em minúsculas com hífens e até 64 caracteres")
    description = fields.get("description", "")
    if not description or len(description) > 1024 or "<" in description or ">" in description:
        errors.append(f"{skill.name}: description vazia, com mais de 1024 caracteres ou com < >")
    if not (skill / "agents" / "openai.yaml").exists():
        errors.append(f"{skill.name}: agents/openai.yaml ausente")
    for md in skill.rglob("*.md"):
        check_links(md, errors)


def main():
    targets = [Path(arg).resolve() for arg in sys.argv[1:]] or sorted((ROOT / "skills").iterdir())
    errors = []
    for skill in targets:
        if skill.is_dir():
            validate(skill, errors)
    for doc in ("README.md", "CONTRIBUTING.md"):
        check_links(ROOT / doc, errors)
    for error in errors:
        print(error)
    print("OK" if not errors else f"{len(errors)} problema(s) encontrado(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
