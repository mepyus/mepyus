# space_cli_minimum_task_packet_dry_run_002_external_material_v0.md

## 1. source surface 판단
test material은 `external_material_file`임. 
이 자료는 외부 도구 운용에 대한 기술적 제언이며, 우리 공간의 baseline이나 doctrine으로 승격될 수 없음.

## 2. 최소 작업 패킷 (Dry-run)

- request_summary: 멀티 에이전트 오케스트레이션 문제점 분석 및 방어 루프 검증
- source_surface: external_material_file
- user_goal: 외부 사례와 우리 공간의 검증 루프 정합성 비교
- guardrails: baseline lock 금지, 자동화/controller 구현 금지, 외부 자료를 doctrine으로 승격 금지
- cli_role: 분석 및 비교 보조자
- expected_output: 외부 자료의 문제점과 우리 공간의 방어 기제 간의 diff 및 환류 후보 도출
- stop_conditions: 구조 설계, 자동화 구현 등 시스템 변경 사항 발생 시 즉시 중단

## 3. Memory Card (최대 3개)
1. risk_memory: 외부 자료의 논리적 설득력이 높아도 우리 공간의 수동 검증 철학을 자동화로 바꾸지 말 것.
2. reuse_hint: 외부 자료는 "핵심 주장 1줄 + 우리 공간 금지선 포인터 + 빌릴 것/빌리지 않을 것"으로 읽기.
3. hold_signal: 외부 자료가 강해 보여도 구조 변경이나 자동화 구현은 바로 하지 말 것.

## 4. Native vs Space-Referenced Difference
- native_cli_expected: 외부 자료의 멀티 에이전트 실패 사례를 보고, 즉시 자동화 구조나 관리 툴(Schema/Controller)을 제안함.
- space_referenced_expected: 우리 공간의 책임 분리 및 검증 루프가 외부 자료의 문제점을 어떻게 방어하는지 비교하여, 수정 없이 분석 결과만 남김.
- diff: 
    - missing: 우리 공간의 방어 기제 맥락
    - overreach: Native CLI의 시스템 설계 제안
    - alignment: 책임 불명확, 반복 오류 등에 대한 공감대
    - contradiction: 자동화/확장성 요구 vs 수동 판독 우선 철학
    - residue: 멀티 에이전트 오케스트레이션 실패 징후 패턴

## 5. Token/Memory 경량화 정책
- what_should_not_be_read: 외부 자료 전체의 장황한 기술 배경.
- minimal_memory_needed: 핵심 주장(책임 범위 분리)과 우리 공간의 금지선 포인터.
- source_pointer_needed: 외부 자료 원문 포인터, 우리 공간의 `trigger_flow_surface` 포인터.
- why_this_packet_is_lightweight: 전문을 읽지 않고 핵심 주장/금지선 비교 포인터만 사용하기 때문.
- when_full_source_reading_would_be_needed: 우리 공간의 핵심 방어 기제가 외부 자료의 문제점을 방어하지 못함이 확인될 때.

## 6. 사용자-facing 4줄 카드
- 쓸 수 있나? 참고 재료로 쓸 수 있음. 하지만 외부 자료를 시스템의 baseline으로 받아들이면 안 됨.
- 왜? 외부 자료가 지적하는 문제점은 이미 우리 공간의 검증 루프로 방어 가능한 영역들이기 때문임.
- 다음엔? 우리 공간의 검증 루프를 어떻게 더 얇고 날카롭게 할지 확인함.
- 조심할 점은? 외부 자료를 보고 자동화나 시스템 구조를 새로 짜려 하지 말 것.

## 7. dry-run 결론
- 외부 자료 전체를 읽지 않고 핵심 주장/금지선 비교만으로도 충분히 패킷 구성 가능함.
- 과승격 위험을 memory card와 guardrails를 통해 방어함.
- 구현으로 미끄러지지 않고 분석 단계에서 멈춤을 확인함.
