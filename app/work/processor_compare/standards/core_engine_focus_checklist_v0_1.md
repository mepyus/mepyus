# Core Engine Focus Checklist v0.1

목적:
- 지금부터 작업 목표를 `입력기 + 라벨기 + 앵커기` 확정으로 고정한다.
- 표현층, terrain, atlas는 보조로 보고 우선순위에서 내린다.
- 체크리스트를 기준으로 진행 상태를 확인한다.

---

## 0. 목표 고정

최종 목표:
- 입력 자료를 안정적으로 fragment로 자른다
- 각 fragment에 scene / role / score를 일관되게 붙인다
- weak anchor를 제거하고 strong canonical anchor를 승격한다
- region 대표 anchor와 cross-doc shared anchor가 사람이 읽히는 형태로 나온다

운영 원칙:
- 입력기 + 라벨기 = `codex_like + chatgpt_like + gemini_like`
- merged 기준선 = `codex_like + chatgpt_like`
- Gemini-like = 보조 관측기
- 앵커기 = 공통 규칙 기반 canonical engine

---

## 1. 현재 상태 요약

### 입력기
- [x] observer-like feature extractor 존재
- [x] fragment 단위 처리 가능
- [ ] 문서 타입별 boundary rule 정교화 부족
- [ ] retry12 / boundary case 기준 입력기 회귀 검증 자동화 부족

현재 구현:
- [feature_extractor.py](/Users/sungsookim/universe/vectorfl_replica/app/work/processor_compare/observer_engine/feature_extractor.py)

### 라벨기
- [x] scene base rule 존재
- [x] role base rule 존재
- [x] score base rule 존재
- [x] codex/chatgpt/gemini like profile 존재
- [ ] scene 경계 보정 규칙 추가 필요
- [ ] role 경계 보정 규칙 추가 필요
- [ ] ambiguity/stability guardrail 강화 필요

현재 구현:
- [scene_rules.py](/Users/sungsookim/universe/vectorfl_replica/app/work/processor_compare/observer_engine/rules/scene_rules.py)
- [role_rules.py](/Users/sungsookim/universe/vectorfl_replica/app/work/processor_compare/observer_engine/rules/role_rules.py)
- [score_rules.py](/Users/sungsookim/universe/vectorfl_replica/app/work/processor_compare/observer_engine/rules/score_rules.py)
- [profiles](/Users/sungsookim/universe/vectorfl_replica/app/work/processor_compare/observer_engine/profiles)

### 앵커기
- [ ] canonical normalization 없음
- [ ] weak anchor filter 없음
- [ ] anchor typing 실질 구현 없음
- [ ] strong score 없음
- [ ] promoted anchor 개념 없음
- [ ] region representative scoring 없음
- [ ] bridge shared anchor scoring 없음

현재 구현:
- [anchor_rules.py](/Users/sungsookim/universe/vectorfl_replica/app/work/processor_compare/observer_engine/rules/anchor_rules.py)

판단:
- 현재 가장 약한 곳은 앵커기다.
- 라벨기는 보정 대상이고, 앵커기는 재구성이 필요하다.

---

## 2. 우선순위

### Priority A — 앵커기 재구성
- [ ] 조사/어미 제거
- [ ] alias / canonical normalization
- [ ] discourse stopwords filter
- [ ] generic noun weak penalty
- [ ] anchor type 분류
- [ ] specificity score
- [ ] strong score
- [ ] promoted anchor만 region/bridge 후보로 사용

### Priority B — 라벨기 보정
- [ ] explanation vs reflection 경계 강화
- [ ] explanation vs comparison 경계 강화
- [ ] support vs expansion 경계 강화
- [ ] contrast vs expansion 경계 강화
- [ ] problem vs support 경계 강화
- [ ] ambiguity를 boundary case에서 더 정직하게 남기도록 수정

### Priority C — 입력기 미세 조정
- [ ] 요약/정의 경계 규칙 보강
- [ ] 문제/해법 경계 규칙 보강
- [ ] 메커니즘/가치 경계 규칙 보강
- [ ] 대화형 문서에서 화제 묶음 기준 보강

---

## 3. 앵커기 구현 체크리스트

### 3.1 파일 구조
- [ ] `anchor_engine/dictionaries/discourse_stopwords_ko.json`
- [ ] `anchor_engine/dictionaries/weak_generic_nouns_ko.json`
- [ ] `anchor_engine/dictionaries/particle_suffixes_ko.json`
- [ ] `anchor_engine/dictionaries/ending_suffixes_ko.json`
- [ ] `anchor_engine/dictionaries/alias_dictionary.json`
- [ ] `anchor_engine/dictionaries/anchor_type_dictionary.json`
- [ ] `anchor_engine/dictionaries/acronym_whitelist.json`
- [ ] `anchor_engine/normalize.py`
- [ ] `anchor_engine/weak_filter.py`
- [ ] `anchor_engine/typing.py`
- [ ] `anchor_engine/score.py`
- [ ] `anchor_engine/pipeline.py`

### 3.2 기능
- [ ] candidate extraction
- [ ] surface cleaning
- [ ] Korean particle stripping
- [ ] ending nominalization
- [ ] canonical key generation
- [ ] alias merge
- [ ] weakness penalty
- [ ] type assignment
- [ ] strong score
- [ ] promotion
- [ ] region representative scoring
- [ ] bridge shared anchor scoring

### 3.3 acceptance
- [ ] `데이터/데이터는/데이터를` canonical merge
- [ ] `그래서/그런데/것처럼` 대표 anchor 배제
- [ ] `Graph RAG/온톨로지/카프카/Action Type` promoted=true
- [ ] region 대표 anchor 3~5개가 읽힘
- [ ] bridge hint가 weak surface token이 아니라 canonical anchor 중심으로 바뀜

---

## 4. 라벨기 구현 체크리스트

### scene
- [ ] reflection은 쉽게 주지 않기
- [ ] comparison은 쉽게 주지 않기
- [ ] evidence는 실제 장면/근거가 있을 때만 주기
- [ ] explanation 기본값을 더 안정화

### role
- [ ] support vs example
- [ ] support vs expansion
- [ ] contrast vs expansion
- [ ] problem vs support
- [ ] thesis vs expansion

### scores
- [ ] ambiguity high should remain high for boundary cases
- [ ] stability high but mixed suppression
- [ ] confidence high + ambiguity low 조합 억제

### acceptance
- [ ] retry12 기준 ChatGPT drift 감소 유지
- [ ] Gemini는 보조 관측기로만 사용
- [ ] merged output이 Codex-like/ChatGPT-like 합의 중심으로 작동

---

## 5. 입력기 구현 체크리스트

### segmentation policy
- [ ] 요약/정의 분리 후보
- [ ] 문제/해법 분리 후보
- [ ] 메커니즘/가치 분리 후보
- [ ] 대화 문서의 화제 전환 감지

### acceptance
- [ ] doc_005/006/007/008/009 기준 boundary drift 재점검
- [ ] overly merged / overly segmented 후보를 문서 타입별로 설명 가능

---

## 6. 바로 다음 액션

순서:
1. 앵커기 파일 구조 생성
2. normalize / weak_filter / typing / score 초안 구현
3. doc_001~009에 재적용
4. region/bridge anchor 결과 확인
5. 그다음 라벨기 보정

중요:
- 지금은 terrain/atlas를 더 예쁘게 만드는 것이 목표가 아니다.
- anchor engine을 고치지 않으면 region/bridge도 계속 약한 단어로 오염된다.
