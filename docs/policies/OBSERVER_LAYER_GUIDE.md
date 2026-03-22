# Observer Layer Guide

## 목적

이 문서는 `vectorfl_replica`에서 observer layer를 어떻게 써야 하는지 정리한 짧은 운영 가이드다.

observer layer의 목적은
current 값을 바로 바꾸는 것이 아니라,

- 왜 값을 바꾸려는지
- 왜 연결을 미루는지
- 왜 연결을 거절하는지

를 기록으로 남기는 것이다.

즉 observer layer는 정답 확정층이 아니라
보류 / 판단 / 반성 / 차후 검토를 남기는 층이다.

## 현재 지원하는 observer 기록

현재 지원하는 measurement type은 아래 두 가지다.

### 1. revision_judgment

의미:
- 현재 값은 아직 유지하되
- 왜 다른 값으로 고치고 싶은지 기록한다

예:
- source.* anchor가 과하게 강함
- semantic이 너무 일반적임
- structural role이 빠짐
- fragment boundary가 잘못됨

### 2. connection_observation

의미:
- 두 fragment 사이 관계를 확정하지 않고 관찰로 남긴다

지원 상태:
- `accepted_connection`
- `deferred_connection`
- `rejected_connection`

현재 Replica에서는 특히
- `deferred_connection`
- `rejected_connection`

기록이 중요하다.

## current / history / observation 구분

observer layer를 쓸 때 가장 중요한 기준은 이 셋을 섞지 않는 것이다.

### current

지금 대표로 읽히는 값.

예:
- 현재 primary anchor
- 현재 processing values

### history

값이 붙고 바뀐 이력.

예:
- measurement history
- ingest history
- anchor history

### observation

아직 확정은 아니지만 남겨야 하는 판단.

예:
- revision_judgment
- deferred_connection
- rejected_connection
- ambient_anchor_probe

observer layer는 이 셋 중 `observation`에 속한다.

즉 observer 기록은 current를 바로 덮으면 안 된다.

## 템플릿 위치

기본 템플릿 파일:

- `data/exports/observer_templates.json`

이 파일에는 아래 두 묶음이 들어간다.

- `revision_judgments`
- `connection_observations`

## 기록 스크립트

기록 스크립트:

- `scripts/record_observer_template.py`

사용 형식:

```bash
PYTHONPATH=/Users/sungsookim/universe/vectorfl_replica \
python3 /Users/sungsookim/universe/vectorfl_replica/scripts/record_observer_template.py \
  /Users/sungsookim/universe/vectorfl_replica/runtime \
  /Users/sungsookim/universe/vectorfl_replica/data/exports/observer_templates.json
```

이 스크립트는 template JSON을 읽어서 observer measurement를 저장한다.

## observer 기록 시 반드시 넣어야 할 것

### revision_judgment

- `fragment_id`
- `column_key`
- `previous_value`
- `new_value`
- `reason`

권장:
- `reason_family`
- `operator`
- `notes`
- `confidence`

### connection_observation

- `fragment_id`
- `counterpart_fragment_id`
- `relation_status`
- `reason`

권장:
- `reason_family`
- `shared_signals`
- `missing_signals`
- `operator`
- `notes`
- `confidence`

## reason_family 권장 예시

revision 쪽:

- `source_anchor_overweight`
- `semantic_overgeneralization`
- `missing_structural_role`
- `fragment_boundary_problem`
- `context_loss`

connection 쪽:

- `false_resonance`
- `insufficient_semantic_alignment`
- `missing_structural_match`
- `cross_source_weak_signal`

## observer layer 사용 원칙

### 원칙 1
current를 바로 덮어쓰지 않는다.

### 원칙 2
애매함을 버리지 않고 observation으로 남긴다.

### 원칙 3
연결 실패도 기록한다.

### 원칙 4
reason 없는 observer 기록은 피한다.

### 원칙 5
observer는 stable truth가 아니라 review material이다.

## source view 반영

observer 기록은 source fragment view에서도 요약된다.

현재 보이는 요약:

- `revision_count`
- `deferred_count`
- `rejected_count`

즉 fragment를 읽을 때
"이 값은 왜 수정 후보가 되었는가"
"왜 이 연결은 보류 / 거절되었는가"
를 바로 볼 수 있다.

## 한 줄 정리

observer layer는 값을 바로 바꾸는 층이 아니라,
바꾸고 싶음 / 아직 못 붙임 / 붙이지 않음의 이유를 잃지 않고 남기는 층이다.
