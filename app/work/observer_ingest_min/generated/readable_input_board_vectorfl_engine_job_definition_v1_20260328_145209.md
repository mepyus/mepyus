# readable input board / vectorfl_engine_job_definition_v1_20260328_145209

## 1. 입력 정보
- input_id: `vectorfl_engine_job_definition_v1`
- label: `vectorfl_engine_job_definition_v1`
- source_path: `/Users/sungsookim/universe/vectorfl_replica/source_assets/baselines/vectorfl_engine_job_definition_v1.md`
- input_kind: `mixed`
- detected_profile: `note`

## 2. split 결과
- split_mode_used: `heading`
- raw_line_count: `199`
- unit_count: `24`

## 3. unit 목록 요약
- unit_001 — heading_block / preamble ~ preamble — "[[A]] [[OBJ:vectorfl_engine_job_definition_v1]] [[SEM:engine_role_definition_object_growth_relation_translation_memory]]..."
- unit_002 — heading_block / VectorFL 엔진 직무 정의서 v1 ~ VectorFL 엔진 직무 정의서 v1 — "# VectorFL 엔진 직무 정의서 v1..."
- unit_003 — heading_block / 0. 목적 ~ 0. 목적 — "## 0. 목적 이 문서는 “우리 엔진이 정확히 무슨 일을 맡는가”를 잠그기 위한 정의서다. 핵심은, 엔진을 단순 검색기/요약기/자동화기가 아니라 **객체를 키우고, 관계를 만들고, 상태를 읽고, 사용자 질문을 더 ..."
- unit_004 — heading_block / 1. 엔진의 최상위 임무 ~ 1. 엔진의 최상위 임무 — "## 1. 엔진의 최상위 임무 > **엔진은 입력을 객체 성장 사건으로 받아들이고, > 객체의 상태를 읽고, > 의미 관계를 형성/누적하며, > 그 결과를 사용자 질문의 층위로 번역하고, > 원본과 로그를 바닥으로 ..."
- unit_005 — heading_block / 2. 엔진이 해야 할 일 ~ 2. 엔진이 해야 할 일 — "## 2. 엔진이 해야 할 일..."
- unit_006 — heading_block / 2-1. 입력 수용 ~ 2-1. 입력 수용 — "### 2-1. 입력 수용 입력을 단순 문서 추가로 보지 않는다. 입력은 아래처럼 읽는다. - 어떤 객체를 두껍게 하는가 - 어떤 새 층위를 붙이는가 - 어떤 관계를 보강/반박/분기시키는가 - 어떤 residue를 ..."
- unit_007 — heading_block / 2-2. 객체 상태 판독 ~ 2-2. 객체 상태 판독 — "### 2-2. 객체 상태 판독 엔진은 객체마다 현재 상태를 읽어야 한다. 최소 판독 대상: - 이미 두꺼운 층 - 아직 빈 층 - 반복 강화된 층 - residue 간섭 - 사용자 질문과 잘 붙는 층 - 아직 약한..."
- unit_008 — heading_block / 2-3. 관계 생성 및 누적 ~ 2-3. 관계 생성 및 누적 — "### 2-3. 관계 생성 및 누적 연결은 단순 공출현으로 보지 않는다. 엔진은 관계를 아래처럼 읽고 남겨야 한다. - 보강 - 대비 - 반례 - 시간 변화 - 실행화 - 규칙화 - 질문 생성 - 상위 응결핵으로 상..."
- unit_009 — heading_block / 2-4. 사용자 층위 번역 ~ 2-4. 사용자 층위 번역 — "### 2-4. 사용자 층위 번역 엔진 내부값은 그대로 유지할 수 있다. 하지만 출력은 사용자 질문의 의미 층위로 번역되어야 한다. 예: - review -> 설명/해석 층 - impl -> 구현/실행 층 - evi..."
- unit_010 — heading_block / 2-5. 기억 바닥 유지 ~ 2-5. 기억 바닥 유지 — "### 2-5. 기억 바닥 유지 엔진은 나중에 구조가 바뀌어도 다시 올라올 수 있게 바닥을 유지해야 한다. 영속적으로 붙잡을 것: - 원본 - append-only log - provenance - 객체 identi..."
- unit_011 — heading_block / 3. 엔진이 직접 맡지 말아야 할 일 ~ 3. 엔진이 직접 맡지 말아야 할 일 — "## 3. 엔진이 직접 맡지 말아야 할 일..."
- unit_012 — heading_block / 3-1. 성급한 고정 ontology화 ~ 3-1. 성급한 고정 ontology화 — "### 3-1. 성급한 고정 ontology화 객체를 처음부터 단일 위계와 단일 관계망에 가두지 않는다...."
- unit_013 — heading_block / 3-2. 중간값 절대화 ~ 3-2. 중간값 절대화 — "### 3-2. 중간값 절대화 axis / label / anchor / gloss는 현재 해석을 위한 감지기/투영값이지 최종 truth가 아니다...."
- unit_014 — heading_block / 3-3. 무차별 자료 적재 ~ 3-3. 무차별 자료 적재 — "### 3-3. 무차별 자료 적재 문서를 많이 먹는 것이 목적이 아니다. 객체와 관계의 의미 밀도를 높이는 것이 목적이다...."
- unit_015 — heading_block / 3-4. 조기 일반화 ~ 3-4. 조기 일반화 — "### 3-4. 조기 일반화 local success를 곧바로 보편 구조로 승격하지 않는다...."
- unit_016 — heading_block / 3-5. residue의 성급한 제거 ~ 3-5. residue의 성급한 제거 — "### 3-5. residue의 성급한 제거 먼저 분해하고, 후순위화하고, 간섭 위치를 읽는다. ---..."
- unit_017 — heading_block / 4. 엔진의 내부 구조를 직무로 재해석 ~ 4. 엔진의 내부 구조를 직무로 재해석 — "## 4. 엔진의 내부 구조를 직무로 재해석..."
- unit_018 — heading_block / 영속층 ~ 영속층 — "### 영속층 - 원본 - 로그 - provenance - 객체 identity - 관계 변화 이력..."
- unit_019 — heading_block / 파생층 ~ 파생층 — "### 파생층 - axis - label - anchor - summary - gloss - packet - report surface..."
- unit_020 — heading_block / 현재 역할 ~ 현재 역할 — "### 현재 역할 - 영속층을 보존한다 - 파생층을 통해 현재 상태를 감지한다 - 필요하면 파생층은 다시 생성 가능해야 한다 ---..."
- unit_021 — heading_block / 5. 엔진과 도구의 관계 ~ 5. 엔진과 도구의 관계 — "## 5. 엔진과 도구의 관계 도구는 외부 기능이 아니라 **공간의 부속 기능 / 기관 / 역할자**로 본다. 예: - gap reader - external enricher - validator - logger -..."
- unit_022 — heading_block / 6. 좋은 엔진 출력의 기준 ~ 6. 좋은 엔진 출력의 기준 — "## 6. 좋은 엔진 출력의 기준 좋은 출력은 단순히 분류가 잘 된 출력이 아니다. 좋은 출력은 아래를 만족해야 한다. - 객체가 더 두꺼워진다 - 사용자 질문이 더 잘 열린다 - 다음 탐색 질문이 자연스럽게 생긴다..."
- unit_023 — heading_block / 7. 미래 확장 관점에서의 엔진 ~ 7. 미래 확장 관점에서의 엔진 — "## 7. 미래 확장 관점에서의 엔진 현재 엔진은 완성형이 아니다. 현재 엔진은 **전이형 구조**다. 즉 지금 엔진은 나중에 아래로 이행 가능해야 한다. - 객체 중심 의미 공간 - 객체 상태장 - 관계장 - pa..."
- unit_024 — heading_block / 8. 한 줄 최종 정의 ~ 8. 한 줄 최종 정의 — "## 8. 한 줄 최종 정의 > **VectorFL 엔진은 입력을 객체 성장 사건으로 받아들여 객체 상태를 읽고 관계를 누적하며, 그것을 사용자 질문의 의미 층위로 번역하고, 원본과 로그를 바닥으로 유지하는 공간 운..."

## 4. 당장 읽히는 흐름
- 앞쪽은 소개/문제제기, 중간은 설명 확장, 뒤로 갈수록 주제 전환이 생기는 흐름으로 읽힌다.

