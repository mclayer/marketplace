"""ADR-061 정합 external Python script — marketplace.json codeforge-develop entry sync.

PR #23 의 plugin-codeforge-develop plugin.json description SSOT 를 verbatim 적용 +
version 0.6.0 → 0.7.0. mojibake (cp1252 corrupted UTF-8) 정정 동시 수행.
"""

import json
import sys

sys.stdout.reconfigure(encoding="utf-8")

NEW_DESCRIPTION = (
    "codeforge ζ arc Develop lane plugin (CFP-39) — DeveloperPLAgent + QADeveloperAgent + "
    "3 role:dev core (Developer/DataEng/InfraEng) + presets/webapp (Backend/Frontend Developer). "
    "동적 roster discovery + Story §8/§8.5 self-write + Phase 2 PR open. codeforge core 의존. "
    "+ CFP-317 DeveloperPLAgent PR pre-flight guard: main push 방지 + --base main 강제 (2026-05-10). "
    "+ CFP-307 DocsAgent 잔존 참조 제거 (2026-05-10). "
    "+ CFP-379 DeveloperPLAgent Opus 승격 + Sonnet agent rate-limit→Opus fallback 정책 적용 "
    "(ADR-057, 2026-05-11). "
    "+ CFP-448 sibling: DeveloperPLAgent model Opus → Sonnet "
    "(ADR-042 Amendment 5 §결정 1 (b), 2026-05-12). "
    "+ CFP-462-followup phase-gate-mergeable workflow sync "
    "(CFP-113/123/133/342/499 backport, 2026-05-13). "
    "+ CFP-507 DeveloperPLAgent Phase 2 PR body composition convention section 신설 "
    "(Lane evidence heading 1회 inject + 7-row format SSOT, "
    "codeforge wrapper §14 manual append 정책 cross-ref, CFP-490 §7.5 carrier — 2026-05-13). "
    "+ CFP-609 DeveloperPLAgent 자율 병렬 결정 tree 4-분기 신설 "
    "(parallel-dispatch-protocol-v1 §5 sibling sync — wrapper canonical mclayer/plugin-codeforge "
    "docs/inter-plugin-contracts/parallel-dispatch-protocol-v1.md, 2026-05-14)."
)
NEW_VERSION = "0.7.0"

path = ".claude-plugin/marketplace.json"
with open(path, encoding="utf-8") as f:
    data = json.load(f)

target = next(p for p in data["plugins"] if p["name"] == "codeforge-develop")
old_version = target["version"]
target["description"] = NEW_DESCRIPTION
target["version"] = NEW_VERSION

with open(path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")

print(f"version: {old_version} -> {NEW_VERSION}")
print(f"description length: {len(NEW_DESCRIPTION)}")
print(f"description sample: {NEW_DESCRIPTION[:150]}...")
