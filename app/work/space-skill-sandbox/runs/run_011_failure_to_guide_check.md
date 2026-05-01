# run_011_failure_to_guide_check

## 1. Run Declaration
과거 샌드박스 런의 validation note 및 클로즈아웃 카드에 포함된 실패/위험 소재를 failure-to-guide.v0_1.skill을 활용하여 가이드 후보 문장으로 변환하는 테스트를 수행함.

## 2. Input Materials
- `review/validation_round_4` ~ `11`
- `review/space_skill_sandbox_v0_2_closeout_card.md`
- `worker_guides/worker_guide_v0_2_candidate.md`

## 3. Skill Used
failure-to-guide.v0_1.skill.md

## 4. Failure Materials Selected
- **FM_01**: 완료를 승인으로 오해하는 위험 (Source: `validation_round_6`)
- **FM_02**: source-claimed를 진실로 과잉 해석하는 위험 (Source: `validation_round_10`)
- **FM_03**: inferred-pattern 엣지를 고정된 기준으로 취급하는 위험 (Source: `validation_round_10`)
- **FM_04**: ambiguous-link를 단순히 무시하려는 경향 (Source: `validation_round_10`)
- **FM_05**: 분석 중 도구 설치나 자동화로 이탈하는 현상 (Source: `validation_round_7`)
- **FM_06**: 낮은 위험의 읽기 작업을 과도하게 중단시키는 현상 (Source: `validation_round_4`)
- **FM_07**: [[SYNTH]] 노드를 원문 용어로 오독하는 위험 (Source: `run_009`)

## 5. Failure-to-Guide Conversion Table

| Failure Material | Risk if Repeated | Guide Candidate | Status | Action |
|---|---|---|---|---|
| 완료를 승인/lock/baseline처럼 읽힐 위험 | 작업 종료를 최종 권한 획득으로 오해하여 후속 검증 누락 | 완료는 작업 종료 신호일 뿐, 승인/lock/baseline이 아니다. | candidate | worker guide 후보로 보관 |
| source-claimed가 사실 확정처럼 읽힐 위험 | 원문의 주관적 주장을 시스템의 객관적 사실로 오염시킴 | source-claimed는 원문이 그렇게 주장했다는 뜻이지, 사실 확정이 아니다. | candidate | worker guide 후보로 보관 |
| inferred-pattern edge가 기준처럼 굳을 위험 | 가변적인 추론 패턴을 영구적인 시스템 규칙으로 고정시킴 | inferred-pattern은 반복 패턴 추론이지 baseline이 아니다. | candidate | worker guide 후보로 보관 |
| ambiguous-link를 무시하고 넘어갈 위험 | 약한 고리 속에 숨겨진 잠재적 충돌이나 위험 신호를 놓침 | ambiguous-link는 버릴 것이 아니라 추가 검증이 필요한 연결이다. | candidate | worker guide 후보로 보관 |
| Graphify/gstack 등을 바로 설치하거나 자동화하려는 위험 | 샌드박스 연구 범위를 벗어나 시스템 형상 변동 및 의존성 발생 | 도구 설치, hook, MCP, 자동화는 sandbox run이 아니라 사용자 판단 필요 지점이다. | candidate | 사용자 판단 필요로 상시 노출 |
| 낮은 위험의 읽기 작업까지 사용자 판단 필요로 올릴 위험 | 불필요한 에스컬레이션으로 사용자 피로도 증가 및 작업 지연 | 파일 존재 여부 등 낮은 위험의 read-only 확인은 observation-only로 허용할 수 있다. | candidate | worker guide 후보로 보관 |
| [[SYNTH]] node가 원문 용어처럼 굳을 위험 | 인위적 해석 용어와 원본 데이터를 혼동하여 데이터 무결성 훼손 | [[SYNTH]] node는 우리가 붙인 해석명이며 원문 용어가 아니다. | candidate | worker guide 후보로 보관 |

## 6. Borrow / Hold / Reject

### Borrow (가이드 후보로 채택)
- FM_01~04, FM_06, FM_07에 기반한 가이드 문장들. (실무적이고 명확한 행동 지침임)

### Hold (추가 관찰 필요)
- FM_05 (설치/자동화): 이미 preflight-guard에서 다루고 있으나, 중복 강조가 필요한지 검토 필요.

### Reject (기각)
- 없음 (선정된 모든 소재가 샌드박스 안전에 기여함)

## 7. Risk Check
- **Baseline Drift**: 생성된 가이드 문장이 '후보'임을 명시하고 있으며, 본체 가이드를 직접 수정하지 않음.
- **Overgeneralization**: 각 문장이 특정 실패 사례(FM)에 긴밀히 앵커링되어 있음.
- **Auto-Update**: 자동화 없이 수동 변환 및 기록으로 수행됨.

## 8. 4-line Footer
status: 검증 필요
summary: validation note와 반복 위험을 failure material로 읽고, 다음 작업자가 참고할 가이드 후보(Guide Candidate)로 변환함
risk: 실패 하나가 곧바로 baseline이나 source-space rule처럼 굳어질 수 있음
next: validation_round_12에서 과잉 일반화와 baseline drift 여부를 검증
