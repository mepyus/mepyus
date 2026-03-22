# Document Fragment Sheet: doc_001

이 문서는 공통 절단 기준이 아니라, 원문을 읽은 뒤 Codex가 참고용으로 남긴 기준선 메모다.
실제 비교 실험에서는 ChatGPT, Gemini, Codex가 각자 원문을 스스로 fragment로 자른다.

## 문서 메타

- input_doc_id: `doc_001`
- input_bundle_id: `bundle_compare_v1`
- source_type: `reference_article`
- fragment_version: `v1`
- source_doc: `inputs/source_docs/doc_001.txt`

## Codex 기준선 Fragment 메모

### fragment 1
- fragment_id: `doc_001_frag_001`
- fragment_text: `온톨로지(Ontology)란 사람들이 세상에 대하여 보고 듣고 느끼고 생각하는 것에 대하여 서로 간의 토론을 통하여 합의를 이룬 바를, 개념적이고 컴퓨터에서 다룰 수 있는 형태로 표현한 모델로, 개념의 타입이나 사용상의 제약조건들을 명시적으로 정의한 기술이다. 온톨로지는 일종의 지식표현(knowledge representation)으로, 컴퓨터는 온톨로지로 표현된 개념을 이해하고 지식처리를 할 수 있게 된다. 프로그램과 인간이 지식을 공유하는데 도움을 주기 위한 온톨로지는, 정보시스템의 대상이 되는 자원의 개념을 명확하게 정의하고 상세하게 기술하여 보다 정확한 정보를 찾을 수 있도록 하는데 목적이 있다. 온톨로지는 시맨틱 웹을 구현할 수 있는 도구로서, 지식개념을 의미적으로 연결할 수 있는 도구로서 RDF, OWL, SWRL 등의 언어를 이용해 표현한다.`
- note: `정의, 목적, 표현 언어까지 이어지는 하나의 설명 묶음이므로 한 fragment로 유지`

### fragment 2
- fragment_id: `doc_001_frag_002`
- fragment_text: `온톨로지는 일단 합의된 지식을 나타내므로 어느 개인에게 국한되는 것이 아니라 그룹 구성원이 모두 동의하는 개념이다. 그리고 프로그램이 이해할 수 있어야 하므로 여러 가지 정형화가 존재한다.`
- note: `합의성과 정형화 가능성에 초점을 둔 보충 설명 묶음`

## 체크

- 각 fragment는 하나의 로컬 의미 움직임을 유지한다.
- fragment 내부에서 evidence_text를 직접 뽑을 수 있다.
- 실제 비교 실험에서는 세 처리자가 위 fragment_id와 fragment_text를 그대로 사용할 필요가 없다.
- 비교기는 같은 원문 파일 안에서 fragment_text 유사도로 후매칭한다.
