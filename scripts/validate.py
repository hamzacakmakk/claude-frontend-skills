"""Validate the skills in this repo.

Checks:
- every skills/<name>/SKILL.md starts with YAML frontmatter containing `name` and `description`
- `name` matches the folder name and uses lowercase letters, digits and hyphens (max 64 chars)
- `description` is non-empty and at most 1024 characters
- every relative link in every Markdown file points to a file that exists
- every `references/*.md` path mentioned in a SKILL.md exists

Run:  python scripts/validate.py
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS = os.path.join(ROOT, "skills")
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
REF_RE = re.compile(r"`(references/[A-Za-z0-9_\-./]+\.md)`")

errors = []


def rel(p):
    return os.path.relpath(p, ROOT).replace("\\", "/")


def frontmatter(path):
    text = open(path, encoding="utf-8").read()
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---", 4)
    if end == -1:
        return None, text
    fields = {}
    for line in text[4:end].splitlines():
        if ":" in line:
            key, _, value = line.partition(":")
            fields[key.strip()] = value.strip().strip('"').strip("'")
    return fields, text


skill_dirs = sorted(d for d in os.listdir(SKILLS) if os.path.isdir(os.path.join(SKILLS, d)))
if not skill_dirs:
    errors.append("no skills found under skills/")

for d in skill_dirs:
    path = os.path.join(SKILLS, d, "SKILL.md")
    if not os.path.isfile(path):
        errors.append(f"skills/{d}: missing SKILL.md")
        continue
    fm, text = frontmatter(path)
    if fm is None:
        errors.append(f"{rel(path)}: missing YAML frontmatter")
        continue
    name, desc = fm.get("name", ""), fm.get("description", "")
    if name != d:
        errors.append(f"{rel(path)}: name '{name}' does not match folder '{d}'")
    if not NAME_RE.match(name) or len(name) > 64:
        errors.append(f"{rel(path)}: name '{name}' must be lowercase letters, digits and hyphens (max 64)")
    if not desc:
        errors.append(f"{rel(path)}: description is empty")
    elif len(desc) > 1024:
        errors.append(f"{rel(path)}: description is {len(desc)} characters (max 1024)")
    for ref in REF_RE.findall(text):
        if not os.path.isfile(os.path.join(SKILLS, d, ref)):
            errors.append(f"{rel(path)}: mentions {ref}, which does not exist")

md_files = []
for base, dirs, files in os.walk(ROOT):
    dirs[:] = [x for x in dirs if not x.startswith(".")]
    md_files += [os.path.join(base, f) for f in files if f.endswith(".md")]

for path in md_files:
    text = open(path, encoding="utf-8").read()
    text = re.sub(r"```.*?```", "", text, flags=re.S)        # ignore code blocks
    for target in LINK_RE.findall(text):
        if re.match(r"^[a-z]+:", target) or target.startswith("#"):
            continue                                          # URLs, mailto:, anchors
        target = target.split("#")[0]
        if target and not os.path.exists(os.path.join(os.path.dirname(path), target)):
            errors.append(f"{rel(path)}: broken link -> {target}")

if errors:
    print("\n".join(errors))
    sys.exit(1)
print(f"OK: {len(skill_dirs)} skills, {len(md_files)} Markdown files checked")
