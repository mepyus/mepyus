# folder_role_table_v1

## 0. 목적

이 문서는 프로그램급 작업공간으로 승격하는 과정에서
각 폴더가 무엇을 담당하는지, 무엇을 두면 안 되는지,
새 파일이 생겼을 때 어디로 배치해야 하는지를 빠르게 판단하기 위한
**폴더 역할표 v1** 이다.

이 문서는 “폴더 트리를 예쁘게 보이게 하는 문서”가 아니라,
**입력 증가 / 산출물 증가 / 스크립트 증가 속에서도 난잡함을 막기 위한 책임표**다.

## 1. 최상위 폴더 읽기

| 폴더 | 역할 | 여기에 들어오는 것 | 들어오면 안 되는 것 | 한 줄 판단 |
|---|---|---|---|---|
| `app/` | 엔진 본체 | core logic, runtime logic, schema/model, registry/provenance/event 처리 코드 | 일회성 실험 메모, 외부 원문, 최신 요약 문서 남발 | 엔진 몸체 |
| `scripts/` | 실행 팔(operating arms) | intake 실행, sync, observer, validate, batch run, compare, render 계열 실행 스크립트 | 정책 문서, 원본 자료, 장기 기준문 | 실행 손발 |
| `source_assets/` | 기준 입력 자산층 | declaration, baseline, directive, handoff, external case input source | runtime latest, 실행 결과 보고서, raw log | 운영 기준 입력층 |
| `docs/` | 정책/명세/가이드/리포트 문서 | policy, spec, guide, report | 원본 데이터, runtime latest 결과, append-only raw log | 상위 문서층 |
| `runtime/` | 최신 읽기면/운영 결과면 | latest boards, rendered status, current summary, compacted surface, receipts/views | 본체 코드, 원본 자료, 실험 초안 장기보관 | 읽기면 |
| `references/` | 참고 자산/비교 기준/외부 참조 구조화본 | reference docs, calibration assets, bounded reference preprocess 결과 | 엔진 본체 코드, 실행 최신면 남발 | 참고 기억층 |
| `inputs/` 또는 `sources/` 계열 | 원본 입력 자산 | 외부자료 원문, 사용자 원문, canonical input files | 요약본 latest, 중간 가공본 다수, 실험 산출물 | 원본 창고 |
| `work/` 또는 `app/work/` | 실험/임시/검증 중 자산 | 실험 스크립트, 시험 산출물, 비교 결과, 아직 잠기지 않은 보조 파일 | 기준문 SSOT, 장기 latest, 엔진 핵심 고정 자산 | 실험장 |
| `logs/` | 로그/실행 기록 | run logs, process logs, debug traces | 기준문, 원본 자료, 사람이 읽는 핵심 요약 문서 | 로그층 |

## 2. app/ 하위 역할

| 경로 | 역할 | 둬야 하는 것 | 두면 안 되는 것 | 비고 |
|---|---|---|---|---|
| `app/core/` | 핵심 구조/핵심 계약 | schema, registry core, provenance core, event core, routing core, atomic io | 임시 observer 스크립트, 일회성 비교 코드 | 가장 보수적 |
| `app/runtime/` 또는 `app/core/runtime/` | 실행 중 참조되는 runtime 구성 | live space, review state, runtime helpers, render/input runtime adapters | 최신 markdown 결과물 직접 저장 | runtime logic only |
| `app/models/` 또는 `app/core/models/` | 데이터 구조 정의 | dataclass/pydantic/schema/typed models | 실행 절차 문서 | 구조 정의 |
| `app/controllers/` / `app/services/` | 흐름 제어/서비스 조합 | orchestration, service glue, app-layer control | 원본 자료, 최신 리포트 파일 | controller/service layer |
| `app/work/` | 엔진 내부 실험장 | stage experiments, observer experiments, compare helpers, temporary readers | lock된 baseline 대체물 | work는 work로 남김 |
| `app/common/` | 공통 유틸 | shared helpers, constants, reusable utils | 도메인별 실험 로직 | 공통화될 때만 |

## 3. scripts/ 하위 역할

| 경로 | 역할 | 둬야 하는 것 | 두면 안 되는 것 | 한 줄 판단 |
|---|---|---|---|---|
| `scripts/intake/` | 입력 수용 실행 | process input, classify lane, canonicalize source, produce receipt | 기준문 md, 외부 원문 | 입력 받는 팔 |
| `scripts/registry/` | registry/provenance/event 처리 실행 | append, repair, compact, sync, check | 사람이 읽는 summary md를 주력으로 두는 것 | 장부 다루는 팔 |
| `scripts/runtime/` | latest/read surface 생성 | render latest status, board generation, compacted view creation | core schema 정의 | 읽기면 만드는 팔 |
| `scripts/validate/` | 검증 | consistency checks, schema checks, path checks, orphan checks | 원본 자료 저장 | 점검 팔 |
| `scripts/compare/` | 비교/분석 | diff, compare, bounded analysis, report generation | 기준문 잠금 파일 | 비교 팔 |
| `scripts/dev/` 또는 `scripts/tmp/` | 임시 개발용 | one-off helpers, migration helper, local patch scripts | 장기 운영 핵심 스크립트 | 오래 두지 않음 |

## 4. source_assets/ 하위 역할

| 경로 | 역할 | 둬야 하는 것 | 두면 안 되는 것 | 비고 |
|---|---|---|---|---|
| `source_assets/declarations/` | 방향/존재 이유 source | 선언문 원문, 방향 선언 입력 자산 | runtime current view, 실행 결과 보고 | 기준 입력 자산 |
| `source_assets/baselines/` | 기준 source | baseline 원문, pack 정의, 잠금 기준 입력 자산 | latest 변화 요약, 읽기면 | 기준 입력 자산 |
| `source_assets/directives/` | 운영 지시 source | Codex 지시서, 체크리스트, bounded repair 지시 | 결과 보고서, runtime current view | active guidance source |
| `source_assets/handoffs/` | handoff source | 세션 handoff, 다음 턴 연결 지시 | latest status, raw input | 연결 자산 |
| `source_assets/external_case_inputs/` | 외부 사례 input source | external case first-pass input md, canonical source 설명 자산 | 외부 원문 txt 자체, exploration result report | 외부사례 입력 메타 |
| `source_assets/session_notes/` | 세션 메모 source | 세션 close note, bounded session memo | current official surface | 보조 source |

## 5. docs/ 하위 역할

| 경로 | 역할 | 둬야 하는 것 | 두면 안 되는 것 | 비고 |
|---|---|---|---|---|
| `docs/policies/` | 상위 운영 기준 | baseline, policy, constitution-like docs, lane rules, workspace rules | 일회성 작업 결과 요약 | 가장 먼저 참조 |
| `docs/specs/` | 계약/명세 | field contracts, folder specs, naming specs, runtime contracts | 임시 생각 메모 | 구조 계약 |
| `docs/guides/` | 사용 가이드 | how-to, operator guide, workflow guide, reader guide | 기준 변경 자체를 담는 문서 | 쓰는 법 |
| `docs/reports/` | 정적 보고 | bounded assessment, feasibility, summarized findings, check reports | directive/declaration source 자체, latest/current 운영표면 | 결과 문서 보관 |

## 6. runtime/ 하위 역할

| 경로 | 역할 | 둬야 하는 것 | 두면 안 되는 것 | 한 줄 판단 |
|---|---|---|---|---|
| `runtime/views/` | 사람이 읽는 최신 요약면 | latest board, latest commands, compacted status, current summaries | 원본 전체 복사본, 엔진 핵심 코드 | 최신 읽기판 |
| `runtime/receipts/` | 실행 영수증 | intake receipts, process receipts, run receipt md/json | 기준문, 원문 소스 | 무엇이 돌았는지 |
| `runtime/logs/` | raw append-only 기록 | delta raw log, process append log, machine-facing raw trace | current reality surface, 결과 보고서 | 원시 기록층 |
| `runtime/events/` | runtime event snapshots or rendered event outputs | readable event slices, selected event surfaces | core raw registry 대체물 | 보여주는 이벤트면 |
| `runtime/tmp/` | 임시 runtime 산출물 | transient outputs, staging views, short-lived artifacts | 장기 latest SSOT | 곧 사라질 면 |
| `runtime/rendered/` | 렌더링 결과 | html/md/json rendered surfaces | 본체 입력 데이터 저장 | 보여주기용 |

## 7. inputs/ 계열 역할

| 경로 | 역할 | 둬야 하는 것 | 두면 안 되는 것 | 한 줄 판단 |
|---|---|---|---|---|
| `inputs/external_cases/` | 외부 원문 입력 자산 | txt, raw transcript, article raw, canonical external input | report, observation result, source directive | 외부 원본 |
| `inputs/internal_notes/` | 내부 원문 입력 자산 | user notes raw, idea memo, structured input originals | 파생 비교 리포트 | 내부 원본 |
| `inputs/reference_docs/` | 참고용 입력 자산 | 정리된 참고 문서, 비교용 md, 재사용 reference input | official current runtime surface | 참고 입력 |
| `inputs/external_cases/` 내부 residue | 과거 혼합 흔적 | legacy mixed md, 잔존 파생 md | current official canonical input과 혼동되게 두는 것 | residue는 residue로 본다 |

## 8. references/ 하위 역할

| 경로 | 역할 | 둬야 하는 것 | 두면 안 되는 것 | 한 줄 판단 |
|---|---|---|---|---|
| `references/calibration/` | 보정 기준 자산 | calibration docs, boundary cases, anchor guidance | 엔진 최신판 SSOT 대체물 | 보정 기억 |
| `references/cases/` | 참고 사례 정리본 | external case summaries, case maps, bounded extracted notes | 원본 canonical source 자체의 유일 저장 위치 | 참고 케이스 |
| `references/preprocessed/` | reference sidecar/preprocess 결과 | preprocessed json, fragment sidecar for references | 엔진 본체 registry | 참고 전처리 |

## 9. work/ 또는 app/work/ 하위 역할

| 경로 | 역할 | 둬야 하는 것 | 두면 안 되는 것 | 원칙 |
|---|---|---|---|---|
| `work/experiments/` | 실험 묶음 | temporary experiments, test scenarios, sandbox runs | SSOT 기준문 | 실험은 실험 |
| `work/reports/` | 실험 보고 | one-off result notes, compare reports, exploratory summaries | latest current board | 실험 결과 |
| `work/tmp/` | 매우 임시 자산 | scratch files, quick transforms, local test data | 재사용될 핵심 자산 | 빨리 정리 |
| `app/work/...` | 엔진 가까운 실험 | observer, meaning-layer probe, stage-min trial, bounded repair | core contract로 착각될 파일 | 승격 전 단계 |

## 10. official / residue / result 구분

### official source
- source_assets 아래 기준 입력 자산
- inputs 아래 raw/canonical input

### official read surface
- runtime/views 아래 current/delta/latest surface

### execution evidence
- runtime/receipts
- runtime/logs

### result report
- docs/reports

### residue / no-longer-primary
- 과거 mixed md
- legacy latest
- 더 이상 current primary가 아닌 자산

원칙:
- residue는 historical / cleanup 대상으로 읽고
- official source나 official read surface와 같은 위상으로 읽지 않는다

## 11. 파일 배치 빠른 판단표

### 9-1. 이 파일이 원문인가
그렇다면 `inputs/` 계열로 간다.

### 9-2. 이 파일이 엔진이 실제로 사용하는 코드인가
그렇다면 `app/` 또는 `scripts/` 로 간다.

### 9-3. 이 파일이 상위 규칙/지침/기준인가
정책/명세면 `docs/` 계열,
운영 기준 입력 자산이면 `source_assets/` 계열로 간다.

### 9-4. 이 파일이 사람이 빠르게 읽는 최신 상태면인가
그렇다면 `runtime/views` 또는 `runtime/rendered` 로 간다.

### 9-5. 이 파일이 추적 기록인가
그렇다면 `runtime/receipts`, `runtime/logs`, 또는 registry/provenance/event 계열로 간다.

### 9-6. 이 파일이 아직 실험 중인가
그렇다면 `work/` 또는 `app/work/` 로 간다.

## 12. 새 폴더 생성 전 체크

새 폴더를 만들기 전에 아래를 순서대로 본다.

1. 기존 폴더 역할 안에 들어갈 수 없는가
2. 반복적으로 같은 유형이 발생하는가
3. 단순 편의가 아니라 책임이 분리되는가
4. “이 폴더는 무엇을 담당한다”를 한 문장으로 말할 수 있는가
5. 원본/실험/latest/정책 문서가 섞이지 않게 해주는가

위 5개 중 3개 이상이 애매하면
새 폴더를 만들지 말고 기존 폴더에 두는 쪽이 낫다.

## 13. 폴더 운영 금지선

### 금지 1
원본, latest, 실험본을 한 폴더에 섞지 않는다.

### 금지 2
비슷한 정책 문서를 여러 폴더에 중복 생성하지 않는다.

### 금지 3
일회성 스크립트를 장기 운영 스크립트 폴더에 오래 방치하지 않는다.

### 금지 4
runtime latest를 원본 보관 위치처럼 쓰지 않는다.

### 금지 5
work 산출물을 lock된 기준 자산처럼 취급하지 않는다.

## 14. 현재 추천 SSOT 문서 배치

### 정책
- `docs/policies/engine_input_lane_baseline_v1.md`
- `docs/policies/codex_baseline_program_grade_workspace_upgrade_v1.md`

### 지시
- `source_assets/directives/...`

### 선언
- `source_assets/declarations/...`

### 명세
- `docs/specs/folder_role_table_v1.md`

즉 이 문서 자체는
`docs/specs/folder_role_table_v1.md`
에 둔다.

현재 맥락상 이 문서는
**역할 명세에 가깝기 때문에 `docs/specs/`**
쪽이 가장 맞다.

## 13. 최종 잠금

폴더는 단순 저장통이 아니다.
폴더는 역할과 책임 경계를 고정하는 구조 단위다.

따라서 앞으로 새 입력, 새 문서, 새 스크립트, 새 산출물이 생길 때마다
먼저 “무엇을 만들까”보다
**“이 자산은 어느 역할층에 속하는가”** 를 먼저 판단한다.

한 줄로 잠그면:

**입력 증가와 기능 증가를 견디려면, 파일보다 먼저 폴더의 책임 경계를 고정해야 한다.**
