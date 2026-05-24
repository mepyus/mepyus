# Line / Axis Linkage Gate Candidate Spec v0

## 1. Status
**STATUS: LINE_AXIS_LINKAGE_GATE_CANDIDATE_SPEC_COMPLETE**

## 2. Sources used
- `docs/reports/integrated_engine_component_map_and_part_spec_reading_v0.md`
- `docs/reports/standardized_intake_packet_candidate_spec_v0.md`
- `docs/reports/line_to_axis_formation_process_asset_dry_run_packaging_v0.md`
- `docs/reports/pipeline_candidate_list_v0.md`
- `docs/reports/whole_space_four_maturation_axes_orientation_candidate_v0.md`
- `docs/reports/four_axis_whole_space_reading_pass_v0.md`
- `docs/reports/function_process_formation_prework_candidate_v1.md`
- `docs/reports/function_process_formation_prework_real_test_round1_closeout_v0.md`
- `docs/reports/pipeline_creation_elements_maturity_reread_packaging_v0.md`
- `docs/reports/whole_space_second_pass_structural_synthesis_note_v0.md`

**Sources missing:**
- None.

## 3. Executive summary
이 연결 게이트(Linkage Gate)는 입력된 재료가 단순한 1회성 노트인지, 아니면 우리 공간의 핵심적인 '흐름(Line)'이나 '판단 렌즈(Axis)'로 성장할 후보인지를 식별하는 **'구조적 연결 확인대'**입니다. 이 게이트를 통해 우리는 공간에 들어온 재료를 바로 법이나 온톨로지로 승격시키지 않고, 기존 재료와의 연결성을 검증하는 '후보 단계'에 머물게 함으로써 공간의 성숙도를 유지합니다.

## 4. Candidate gate purpose
이 게이트는 재료(Material)가 들어온 후(Intake Packet), 그것이 어떻게 우리 공간의 기존 선(Line)이나 축(Axis)에 닿는지 검토합니다.

**판단 기준:**
- 1회성 참조인가?
- 기존 라인을 강화하는 연결 씨앗(Connection Seed)인가?
- 새로운 축을 제안하는 후보인가?
- 주의 깊게 봐야 할 정보인가(Watch/Hold)?

**금지 사항:**
- 공식 온톨로지(Ontology)화 금지.
- 자동으로 라인/축 승격 금지.
- 강제적인 구조화 금지.

## 5. State model

| State | Meaning | Entry condition | Evidence needed | Output | Must not become |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **LOCAL_NOTE** | 1회성 참조 | Intake 이후 연결 미비 | 무 | 결과 노트 | 온톨로지 |
| **CONNECTION_SEED** | 라인의 시작 | 2개 이상의 재료와 연결 | 연결성 입증 | 연결 seed | 라인 인덱스 |
| **LINE_CANDIDATE** | 반복 흐름 후보 | 여러 상황에서 반복 발견 | 3개 이상의 반복 사례 | 라인 후보 기록 | 필수 워크플로우 |
| **AXIS_CANDIDATE** | 더 큰 질문 후보 | 여러 라인이 수렴 | 질문의 유용성 | 축 후보 기록 | 공식 법 |
| **WATCH / HOLD** | 위험/주의 | 모호하거나 성격이 튐 | 보류 사유 | 경고 노트 | 차단 대상 |

## 6. Gate questions
1. 어떤 자료가 이 게이트를 촉발했나?
2. 반복적인 연결이 발견되는가?
3. 어떤 과거의 재료들과 연결되는가? (Prior records)
4. 이 연결은 지역적인가, 재사용 가능한가?
5. 여러 사례를 독해하는 데 도움이 되는가?
6. 이것이 단순히 렌즈인가, 아니면 '선'이라 부를 수 있는가?
7. 축 명명이 너무 빠르지 않은가?
8. 어떤 증거가 추가로 필요한가?

## 7. Evidence requirement

| Level | Minimum evidence | Example | Insufficient case |
| :--- | :--- | :--- | :--- |
| **connection seed** | 2개 이상의 관련성 | A와 B의 연결점 | 막연한 추측 |
| **line candidate** | 반복 흐름(3개 이상) | 워커 실행 반복 양상 | 단 1개의 성공 사례 |
| **axis candidate** | 구조적 질문(3개 이상 라인) | Harness-Orientation | 연결성 없는 개념 나열 |

## 8. Linkage template

```markdown
# Line / Axis Linkage Check

## 1. Trigger material
- source/result:
- why it matters:
- related intake/prework:

## 2. Possible connection
- connects to:
- connection type:
- repeated before?:
- evidence:

## 3. Line candidate check
- proposed line name:
- what flow does it describe?:
- cases it helps read:
- missing evidence:
- state:

## 4. Axis candidate check
- possible axis / orientation surface:
- larger question:
- other lines connected:
- why axis naming may be premature:
- state:

## 5. Boundary
- must not become:
- watch items:
- User decision needed:
- next natural trigger:
```

## 9. Relation to existing parts

| Existing part | Connection | Boundary |
| :--- | :--- | :--- |
| **Intake Packet** | 입력된 재료의 초기 속성 전달 | Packet은 게이트에 정보를 제공한다. |
| **Formation Prework** | 후보 재료의 형성 역할 결정 | Prework는 판단을 위한 게이트다. |
| **Reusable Settings** | 연결된 라인이 설정화되는 종착점 | Setting은 강제 법이 아니다. |
| **Worker Evidence Pkg** | 연결 검증용 실제 관찰 데이터 | Packaging은 증거다. |

## 10. Line / Axis support
- **Line finding:** Intake 패킷의 `user_intent`와 `re-entry anchors`를 비교하여 라인을 찾습니다.
- **Axis testing:** 4대 축(Orientation Axis)에 비추어 질문이 '전체 공간'을 읽는 데 유용한지 테스트합니다.
- **Orphan avoidance:** 모든 연결되지 않은 노트를 'Residue'로 분류하여 고립을 방지합니다.

## 11. Final status
**STATUS: LINE_AXIS_LINKAGE_GATE_CANDIDATE_SPEC_COMPLETE**
