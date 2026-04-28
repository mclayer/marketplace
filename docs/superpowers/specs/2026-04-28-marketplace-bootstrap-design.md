# mclayer marketplace bootstrap — spec

## 1. 요건 (사용자 원문 정렬)

- mclayer 조직의 Claude Code 플러그인 marketplace를 단일 진입점으로 노출
- 네이밍 규약: `mclayer/plugin-<X>` 리포 = `<X>` 플러그인. marketplace name = `mclayer`. install identifier = `<X>@mclayer`
- 첫 등재 plugin = `codeforge` (`mclayer/plugin-codeforge`, v0.14.1)
- marketplace.json은 wrapper-only — plugin 소스는 각 plugin 리포 (github source)
- 본 리포는 plugin 분리(예정 의제) 시에도 단일 marketplace 진입점 유지

## 2. 배경

`mclayer/plugin-codeforge` v0.14.1까지 release됐지만 marketplace로 노출된 적 없어 사용자가 `/plugins install`로 부르려면 GitHub 원본 리포 좌표를 직접 알아야 했음. 또한 향후 `mclayer/plugin-<Y>`가 추가될 때 source of truth 충돌을 피하려면 marketplace.json은 단일 마스터여야 함 → 별도 wrapper 리포로 분리.

## 3. 비목표

- plugin 분리 (별도 의제, Apr 27 audit 휘발 상태 — 본 spec 이후 별도 트랙)
- 현 codeforge 리포 내부 구조 변경 (plugin.json·CHANGELOG 등은 후속 PR로 marketplace 노출 사실 명시만)
- cross-repo CI 자동화 (parity check 자동화) — 본 bootstrap 범위 외, 후보로만 기록

## 4. 결정사항

| 항목 | 결정 |
|---|---|
| 리포 이름 | `mclayer/marketplace` (`plugin-` prefix 의도적 미사용 — plugin 아닌 wrapper 명시) |
| 가시성 | public (사용자 install fetch에 필요) |
| marketplace name | `mclayer` |
| 첫 plugin source | `github` source pointing at `mclayer/plugin-codeforge` |
| LICENSE | 부재 (현 codeforge도 부재 — 동일 정책) |
| 버전 동기화 | 수동 (plugin 리포 release → 본 리포 PR로 version 반영). cross-repo CI는 후속 |

## 5. 산출물

- `.claude-plugin/marketplace.json` — codeforge 1건 등재
- `README.md` — 사용자 install 명령 + 신규 plugin 등재 절차
- `.gitignore` — 기본 (macOS·editor·.claude-work)
- `docs/superpowers/specs/<본 파일>` + `docs/superpowers/plans/<plan>`

## 6. 사용자 영향

- 신규 사용자: `/plugins marketplace add mclayer/marketplace` → `/plugins install codeforge@mclayer`로 설치 가능
- 기존 codeforge 사용자 (직접 GitHub 좌표 등록): 영향 없음. 점진적으로 marketplace 등록으로 이주 권장 (codeforge 리포 README가 후속 PR에서 안내 추가)

## 7. 후속 작업 (본 spec 외)

1. **codeforge 리포 측**: README 설치 섹션 갱신 + CHANGELOG에 marketplace 노출 사실 기록 (별도 PR · plugin-meta-na 패턴 적용 후보)
2. **invariant ratchet**: 본 리포에 `plugins[name=codeforge].version`이 codeforge 리포 `.claude-plugin/plugin.json` `version`과 일치하는지 cross-repo CI 추가
3. **plugin 분리 의제 복원**: Apr 27 audit 결과 → spec/plan 트랙 진입. 분리된 sub-plugin들은 본 marketplace.json `plugins[]`에 차례로 등재

## 8. 위험 / 가정

- 가정: `gh repo create` 가 mclayer org 권한으로 통과 (확인됨)
- 가정: github source의 marketplace fetch는 default branch (`main`) tip을 가져옴. plugin 리포 release tag 기반 fetch는 향후 invariant ratchet에서 검토
- 위험: marketplace.json `plugins[].version`과 plugin.json `version` drift — 사람의 PR 의무에 의존. 자동화 안 될 시 stale version 가능. 본 bootstrap 후 후속 작업 #2로 처리
