# mclayer marketplace bootstrap — plan

[spec](../specs/2026-04-28-marketplace-bootstrap-design.md) 참조.

## 작업 단계

### 1. 리포 생성 ✅
- [x] `gh repo create mclayer/marketplace --public --description "..."`
- [x] clone to `/Users/1111971/workspace/mctrader/plugins/marketplace`
- [x] default branch `master` → `main` rename

### 2. 파일 작성 ✅
- [x] `.claude-plugin/marketplace.json` — name=mclayer, plugins=[codeforge github source]
- [x] `README.md` — 네이밍 규약 + install 명령 + 신규 plugin 등재 절차 + 버전 동기화 정책
- [x] `.gitignore` — macOS·editor·.claude-work

### 3. spec/plan 기록 ✅
- [x] `docs/superpowers/specs/2026-04-28-marketplace-bootstrap-design.md`
- [x] `docs/superpowers/plans/2026-04-28-marketplace-bootstrap.md` (본 파일)

### 4. 검증
- [ ] `python3 -m json.tool .claude-plugin/marketplace.json` 통과
- [ ] manifest schema 정합 (name 필수·plugins[].name 필수·plugins[].source 필수 — 모두 충족)
- [ ] github source `repo` 형식 (`owner/repo`) 정합

### 5. 첫 commit + push
- [ ] `git add .`
- [ ] `git commit -m "feat: bootstrap mclayer marketplace + codeforge 등재"`
- [ ] `git push -u origin main` (PR 없이 main 직커밋 — 빈 리포 부트스트랩)

### 6. PR 흐름 활성화 (본 commit 직후 이후부터)
- 차후 변경(신규 plugin 등재·codeforge version bump 등)은 feature branch + PR
- main branch protection은 본 bootstrap 직후 수동 적용 권장 (require linear history 등)

## 검증 plan

`/plugins marketplace add mclayer/marketplace` → `/plugins install codeforge@mclayer` 시도. 성공 시 codeforge가 enabledPlugins로 등록되어야 함. 본 plan 외부 (사용자 측) 검증 단계.

## 후속 트랙 (본 plan 미포함)

1. codeforge 리포 README/CHANGELOG에 marketplace 노출 사실 명시 (별도 PR)
2. cross-repo version parity CI
3. plugin 분리 의제 복원
