#!/usr/bin/env python3
"""CFP-609 marketplace description re-copy from wrapper plugin.json (UTF-8 강제)."""
import json
import sys

WRAPPER_PLUGIN = r"C:\Users\mccho\.claude\worktrees\plugin-codeforge\cfp-609\.claude-plugin\plugin.json"
MARKETPLACE = r"C:\workspace\mclayer\marketplace\.claude-plugin\marketplace.json"

with open(WRAPPER_PLUGIN, encoding="utf-8") as f:
    wrapper = json.load(f)
wrapper_desc = wrapper["description"]

with open(MARKETPLACE, encoding="utf-8") as f:
    market = json.load(f)

for plugin in market["plugins"]:
    if plugin["name"] == "codeforge":
        plugin["description"] = wrapper_desc
        plugin["version"] = wrapper["version"]
        break

with open(MARKETPLACE, "w", encoding="utf-8", newline="\n") as f:
    json.dump(market, f, indent=4, ensure_ascii=False)
    f.write("\n")

sys.stdout.buffer.write(f"PASS -- codeforge description re-mirrored (UTF-8, {len(wrapper_desc)} chars, version={wrapper['version']})\n".encode("utf-8"))
