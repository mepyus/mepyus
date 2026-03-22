# STAGE0 SPACE HANDOFF CONTRACT v0

## 0. 목적
이 문서는 `vectorfl`의 앞단 분해 감각과 `vectorfl_next`의 공간 형성 엔진을 접합하기 위한 최소 handoff 계약이다.

목적은 두 엔진을 통복사하거나 섞는 것이 아니라,
아래 역할 분리를 고정하는 것이다.

- Stage0: 원본 입력을 사건/조각/후보로 정규화
- Space Engine: 정규화된 단위를 살아 있는 공간으로 형성

---

## 1. 역할 분리

### Stage0가 담당하는 것
- 원본 문서 보존
- `event` 생성
- `fragment` 생성
- `candidate` 생성
- giant collapse 위험 노출
- provenance 고정

### Space Engine이 담당하는 것
- `material`
- `trace`
- `point_seed`
- `space_cell`
- `local_space`
- `bridge_trace`

판정:

**원본 문서를 직접 space engine의 material 하나로 넣지 않는다.**

---

## 2. 최소 흐름

`source_document -> event -> fragment -> candidate -> handoff_material -> trace -> point_seed -> space_cell -> local_space -> bridge_trace`

---

## 3. 최소 handoff 단위

1차 handoff 단위는 `candidate`다.

즉:

- `candidate 1개 = vectorfl_next material 1개`

단, 원본 문서와 fragment 계보는 metadata/support로 반드시 살아 있어야 한다.

---

## 4. handoff payload

```json
{
  "source_document_id": "doc_xxx",
  "source_type": "memo|paper|review|code",
  "source_ref": "paper-20260316-120102",
  "event_id": "evt_xxx",
  "fragment_id": "frag_xxx",
  "candidate_id": "cand_xxx",
  "candidate_text": "정규화된 후보 텍스트",
  "candidate_index": 1,
  "fragment_count": 3,
  "candidate_count": 2,
  "source_refs": ["source_document:paper-20260316-120102"],
  "parent_refs": ["evt_xxx", "frag_xxx"],
  "bridge_status": "BRIDGE_READY|HOLD",
  "decomposition_kind": "minimal_fragment_probe"
}
```

---

## 5. vectorfl_next 매핑 규칙

### material
- `candidate_text -> material.raw_payload`
- `source_ref -> material.source_ref`
- `source_type -> material.source_type`

### material metadata
- `source_document_id`
- `event_id`
- `fragment_id`
- `candidate_id`
- `candidate_index`
- `fragment_count`
- `candidate_count`
- `bridge_status`
- `decomposition_kind`

### trace support
- `candidate_id`
- `fragment_id`
- `event_id`
- `source_document_id`

---

## 6. 금지
- 원본 전체를 material 하나로 직접 주입
- fragment 없이 candidate 생성 사실을 숨김
- Stage0 bridge를 vectorfl_next bridge_trace로 즉시 승격
- provenance 없는 handoff

---

## 7. 1차 구현 원칙
- Stage0 분해기는 최소 분해기여도 된다.
- fragment는 우선 빈 줄/문단 기반 최소 조각화로 시작 가능하다.
- 너무 짧은 조각은 인접 조각과 병합 가능하다.
- candidate가 여러 개면 material도 여러 개가 된다.
- viewer/server는 handoff된 material 다수를 그대로 공간 형성으로 보낸다.

---

## 8. 후속 확장
이 계약은 1차 최소 결합용이다.

후속 단계에서 확장 가능한 것:
- fragment_kind 판정
- bucket 계층 추가
- candidate fitness 강화
- 원본 내부 그래프 뷰
- Stage0/space engine 간 재유입 루프
