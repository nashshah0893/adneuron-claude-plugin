#!/usr/bin/env python3
"""Validate package consistency; optionally sync rules or check a tools/list export."""

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOOL = re.compile(
    r"`((?:get|list|preview|create|execute|prepare|select|search|discover|sync|connect|"
    r"explain|compare|scan|research|analyze|submit)_[a-z0-9_]+|help_user_upload)`"
)


def check(*, sync_rules=False, catalog=None):
    errors = []
    manifest = json.loads((ROOT / ".claude-plugin/plugin.json").read_text())
    marketplace = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text())
    entries = marketplace.get("plugins", [])
    if len(entries) != 1:
        errors.append("Expected one marketplace entry")
    else:
        entry = entries[0]
        for key in ("name", "version", "description"):
            if entry.get(key) != manifest.get(key):
                errors.append(f"Manifest/marketplace mismatch: {key}")
        if entry.get("source") != "./":
            errors.append("Marketplace must reference this package root")
    if not re.fullmatch(r"\d+\.\d+\.\d+", manifest.get("version", "")):
        errors.append("Expected a semantic package version")
    connection = json.loads((ROOT / ".mcp.json").read_text())
    if connection != {
        "mcpServers": {"adneuron": {"type": "http", "url": "https://mcp.adneuron.ai/mcp"}}
    }:
        errors.append("Unexpected hosted MCP connection or credential configuration")
    rules = (ROOT / "references/adneuron-rules.md").read_text()
    skills = sorted((ROOT / "skills").glob("*/SKILL.md"))
    if not skills:
        errors.append("No skills packaged")
    references = set()
    for skill in skills:
        text = skill.read_text()
        reference = skill.parent / "references/adneuron-rules.md"
        if sync_rules:
            reference.parent.mkdir(parents=True, exist_ok=True)
            reference.write_text(rules)
        if not reference.exists() or reference.read_text() != rules:
            errors.append(f"Unsynchronized rules: {reference.relative_to(ROOT)}")
        front = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
        if not front:
            errors.append(f"Missing skill frontmatter: {skill.parent.name}")
            continue
        name = re.search(r"^name: (.+)$", front[1], re.M)
        description = re.search(r"^description: (.+)$", front[1], re.M)
        if not name or name[1] != skill.parent.name:
            errors.append(f"Skill name/directory mismatch: {skill.parent.name}")
        if not description or len(description[1]) > 1024:
            errors.append(f"Missing/oversized skill description: {skill.parent.name}")
        if re.search(r"^allowed-tools:", front[1], re.M):
            errors.append(f"This package must not pre-approve tool calls: {skill.parent.name}")
        if "references/adneuron-rules.md" not in text:
            errors.append(f"Skill does not load shared rules: {skill.parent.name}")
        references.update(TOOL.findall(text))
    references.update(TOOL.findall(rules))
    references.update(TOOL.findall((ROOT / "README.md").read_text()))
    # Relative documentation links must stay inside the shipped package and exist.
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", path.read_text()):
            if re.match(r"[A-Za-z][A-Za-z0-9+.-]*:", target) or target.startswith("#"):
                continue
            destination = (path.parent / target.split("#")[0]).resolve()
            if not destination.is_relative_to(ROOT) or not destination.exists():
                errors.append(f"Broken/escaping relative link: {path.relative_to(ROOT)}: {target}")
    if catalog:
        payload = json.loads(catalog.read_text())
        envelope = payload.get("result", payload) if isinstance(payload, dict) else None
        tools = envelope.get("tools") if isinstance(envelope, dict) else None
        if not isinstance(tools, list) or not all(
            isinstance(t, dict) and isinstance(t.get("name"), str) for t in tools
        ):
            errors.append("Catalog must be MCP tools/list result JSON with a tools array")
        else:
            names = {t["name"] for t in tools}
            errors.extend(
                "Tool not in supplied catalog: " + name for name in sorted(references - names)
            )
    if errors:
        raise ValueError("\n".join(errors))
    return (
        f"PASS: {len(skills)} skills, matching {manifest['version']} manifests, "
        "synchronized rules, "
        f"{len(references)} tool references" + (" checked against catalog" if catalog else "")
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--sync-rules", action="store_true", help="Copy shared rules into each skill"
    )
    parser.add_argument("--catalog", type=Path, help="Validate references against tools/list JSON")
    args = parser.parse_args()
    try:
        print(check(sync_rules=args.sync_rules, catalog=args.catalog))
    except (ValueError, KeyError, OSError, TypeError) as exc:
        parser.exit(1, f"FAIL: {exc}\n")


if __name__ == "__main__":
    main()
