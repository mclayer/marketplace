# mclayer marketplace

[mclayer](https://github.com/mclayer) 조직의 Claude Code 플러그인을 모아 노출하는 marketplace.

## 네이밍 규약

- **GitHub 리포 이름**: `mclayer/plugin-<X>` (단, marketplace 자체는 `plugin-` prefix 미사용 — 본 리포 `mclayer/marketplace`)
- **Plugin manifest name**: `<X>` (예: `mclayer/plugin-codeforge` → manifest name `codeforge`)
- **Marketplace name**: `mclayer`
- **Install identifier**: `<X>@mclayer` (예: `codeforge@mclayer`)

## 등재 플러그인

`codeforge` 가 entry point. ζ arc 완료(CFP-40, 2026-04-29) 후 wrapper-only(Agent 0개)이며 6개 lane plugin 과 함께 설치돼야 동작한다. 6 lane plugin 미설치 시 SessionStart 의존성 체크에서 부재가 보고되며 해당 lane 진행 불가.

| Plugin | Repo | 설명 |
|---|---|---|
| `codeforge` | [mclayer/plugin-codeforge](https://github.com/mclayer/plugin-codeforge) | 7-lane orchestration entry point (wrapper-only, Agent 0개) — protocol/CI/schemas/bootstrap/Orchestrator instructions 보유. 아래 6 lane plugin 의존 |
| `codeforge-requirements` | [mclayer/plugin-codeforge-requirements](https://github.com/mclayer/plugin-codeforge-requirements) | Requirements lane — RequirementsPL + Domain + Analyst + Researcher 4 agent 병렬 (CFP-37) |
| `codeforge-design` | [mclayer/plugin-codeforge-design](https://github.com/mclayer/plugin-codeforge-design) | Design lane — ArchitectPL + ArchitectAgent (chief author) + 5 deputies + Change Plan / ADR templates (CFP-40) |
| `codeforge-review` | [mclayer/plugin-codeforge-review](https://github.com/mclayer/plugin-codeforge-review) | Review subsystem (3 PL + 2 lane-agnostic worker) — design/code/security 공통 (CFP-29 + CFP-35) |
| `codeforge-develop` | [mclayer/plugin-codeforge-develop](https://github.com/mclayer/plugin-codeforge-develop) | Develop lane — DeveloperPL + QADev + 3 role:dev core + presets/webapp (CFP-39) |
| `codeforge-test` | [mclayer/plugin-codeforge-test](https://github.com/mclayer/plugin-codeforge-test) | Test lane — TestAgent (functional + performance subset 병렬, test_verdict v1) (CFP-38) |
| `codeforge-pmo` | [mclayer/plugin-codeforge-pmo](https://github.com/mclayer/plugin-codeforge-pmo) | Cross-cutting PMO — Epic 분해 자문 + Story 회고 + Cross-Story 패턴 분석 + ADR 후보 발의 (CFP-36) |

## 사용자 설치

### One-shot (codeforge ζ arc 풀 셋)

```bash
/plugins marketplace add mclayer/marketplace
/plugins install codeforge@mclayer
/plugins install codeforge-requirements@mclayer
/plugins install codeforge-design@mclayer
/plugins install codeforge-review@mclayer
/plugins install codeforge-develop@mclayer
/plugins install codeforge-test@mclayer
/plugins install codeforge-pmo@mclayer
```

### `~/.claude/settings.json` 영구 등록

```jsonc
{
  "extraKnownMarketplaces": {
    "mclayer": {
      "source": { "source": "github", "repo": "mclayer/marketplace" }
    }
  },
  "enabledPlugins": {
    "codeforge@mclayer": true,
    "codeforge-requirements@mclayer": true,
    "codeforge-design@mclayer": true,
    "codeforge-review@mclayer": true,
    "codeforge-develop@mclayer": true,
    "codeforge-test@mclayer": true,
    "codeforge-pmo@mclayer": true
  }
}
```

## 신규 플러그인 등재 절차

1. 새 리포 `mclayer/plugin-<X>` 생성, `.claude-plugin/plugin.json` 작성 (`name: "<X>"`)
2. 본 리포 [`.claude-plugin/marketplace.json`](.claude-plugin/marketplace.json) `plugins[]`에 항목 추가:
   ```json
   {
     "name": "<X>",
     "description": "...",
     "version": "<X-plugin.json의 version>",
     "author": { "name": "Josh" },
     "source": { "source": "github", "repo": "mclayer/plugin-<X>" }
   }
   ```
3. 본 README "등재 플러그인" 표 + "사용자 설치" 스니펫에도 같은 PR 안에서 행/줄 추가
4. PR 머지 후 사용자는 `/plugins install <X>@mclayer`로 설치

## 버전 동기화

각 plugin 리포 `plugin.json`의 **mirrored 필드 — `name` · `version` · `description` · `author`** 와 본 marketplace.json `plugins[]` 의 동일 필드는 같은 값이어야 함. plugin 리포에서 mirrored 필드 변경 PR merge 직후 즉시 본 리포에 동기화 PR 을 open·merge 한다 (codeforge core [`CLAUDE.md`](https://github.com/mclayer/plugin-codeforge/blob/main/CLAUDE.md) "Marketplace cross-repo 동기화 의무" SSOT). 비-mirrored 필드(`keywords` 등 marketplace.json schema 비대상) 만 변경 시 sync 면제.

향후 cross-repo CI (github tag fetch + parity check) 를 도입할 후보.
