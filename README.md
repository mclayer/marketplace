# mclayer marketplace

[mclayer](https://github.com/mclayer) 조직의 Claude Code 플러그인을 모아 노출하는 marketplace.

## 네이밍 규약

- **GitHub 리포 이름**: `mclayer/plugin-<X>` (단, marketplace 자체는 `plugin-` prefix 미사용 — 본 리포 `mclayer/marketplace`)
- **Plugin manifest name**: `<X>` (예: `mclayer/plugin-codeforge` → manifest name `codeforge`)
- **Marketplace name**: `mclayer`
- **Install identifier**: `<X>@mclayer` (예: `codeforge@mclayer`)

## 등재 플러그인

| Plugin | Repo | 설명 |
|---|---|---|
| `codeforge` | [mclayer/plugin-codeforge](https://github.com/mclayer/plugin-codeforge) | 24 core agents · 7-lane orchestration · overlay/preset |

## 사용자 설치

### One-shot

```bash
/plugins marketplace add mclayer/marketplace
/plugins install codeforge@mclayer
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
    "codeforge@mclayer": true
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
3. PR 머지 후 사용자는 `/plugins install <X>@mclayer`로 설치

## 버전 동기화

각 plugin 리포의 `plugin.json`의 `version`과 본 marketplace.json의 `plugins[].version`은 같은 값이어야 함. plugin 리포에서 release 발생 시 본 리포에 PR로 version 반영.

향후 cross-repo CI(github tag fetch + parity check)를 도입할 후보.
