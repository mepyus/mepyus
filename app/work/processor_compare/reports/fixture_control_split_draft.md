# fixture control split draft

## 1. current diagnosis
- 현재 `doc_004`, `doc_005`는 control 역할을 잘 하고 있다
- 하지만 이들은 `current engine limitation` 위에 서 있는 control 이라서, 시스템이 좋아지면 상태가 바뀔 수 있다
- 따라서 지금 control 은 두 층으로 분리해야 한다
  - immutable regression fixture
  - mutable exploration control

## 2. split proposal

### immutable regression fixture
- 목적:
  - 회귀 테스트
  - 엔진 훼손 감지
  - 기준점 유지
- 특징:
  - 상태 기대값을 고정
  - 버전 고정
  - 상태가 바뀌면 regression 경고

### mutable exploration control
- 목적:
  - 현재 엔진 한계 관찰
  - 비교 실험
  - 병목 확인
- 특징:
  - 상태가 바뀔 수 있음
  - 바뀌는 것 자체가 전진일 수 있음

## 3. current case tagging

### immutable regression fixture candidate
- `doc_004 -> doc_005`
  - 기대 상태: `canonical`
- `doc_005 -> doc_006`
  - 기대 상태: `canonical`
- `test_live_space_sync_20260321 -> test_canonical_ingest_20260321`
  - 기대 상태: `canonical`

### mutable exploration control candidate
- `engine_phase1_observer_probe_20260321 -> doc_005`
  - 현재 상태: `translation_missing`
  - future change allowed: yes
- `engine_phase1_observer_probe_20260321 -> doc_004`
  - 현재 상태: `translation_missing`
  - future change allowed: yes

### mutable exploration review candidate
- `engine_phase1_observer_probe_20260321 -> doc_006`
  - 현재 상태: `space pre-entry review candidate`
  - future change allowed: yes

## 4. minimal fixture set

### regression fixture set v0
1. canonical-stable fixture
   - `doc_004 -> doc_005`
2. canonical-stable fixture
   - `doc_005 -> doc_006`
3. canonical-stable fixture
   - `test_live_space_sync_20260321 -> test_canonical_ingest_20260321`

### exploration control set v0
1. `engine_phase1_observer_probe_20260321 -> doc_005`
2. `engine_phase1_observer_probe_20260321 -> doc_004`
3. `engine_phase1_observer_probe_20260321 -> doc_006`

## 5. expectation statement

### immutable fixtures
- canonical 유지가 기대값이다
- 상태가 바뀌면 regression 검사 대상으로 본다

### mutable controls
- 상태 변화 허용
- 변화 자체가 전진일 수 있다
- 이들은 현재 시스템 한계를 비추는 탐사용 샘플이다

## 6. why this matters
- control이 전부 mutable인데 regression 기준으로 쓰이면 기준점이 흔들린다
- regression fixture가 없으면 다음 phase 정책 변경이 실제 개선인지 훼손인지 판단이 어려워진다
- 따라서 다음 phase 전에는 최소 fixture set을 고정하는 것이 맞다

## 7. what not changed
- 실제 fixture runner 안 만듦
- 대규모 test suite 안 만듦
- 상태 자동 검증 로직 안 붙임

## 8. next recommendation
- 다음 실제 코드화는 작은 regression manifest 부터 가는 것이 좋다
- 예:
  - fixture id
  - expected tier
  - mutable/immutable flag

## 9. final sentence
- 앞으로 `control` 이라는 단어는 하나로 쓰지 않는다
- `immutable regression fixture` 와 `mutable exploration control` 을 분리해서 읽는다
