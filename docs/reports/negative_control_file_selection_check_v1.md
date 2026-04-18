# negative control file selection check

## candidate A
- file: `claude_code_index.txt`
- topic distance from transformer: YES
- technical explanatory structure: YES
- comparable explanatory flow: YES
- rhetoric vs structure separable: PARTIAL
- bounded length suitability: YES
- canonical input suitability: YES
- note:
  - transformer와는 다른 코드 에이전트/프로젝트 운영 설명 주제다.
  - 루트 디렉토리, `CLAUDE.md`, 명령어/패턴/컨벤션 같은 운영 구조 설명 흐름이 살아 있다.
  - 다만 강의형 소개와 생산성 강조가 꽤 섞여 있어 rhetoric 제거 작업이 `graphrag_neosh.txt`보다 조금 더 필요하다.

## candidate B
- file: `graphrag_neosh.txt`
- topic distance from transformer: YES
- technical explanatory structure: YES
- comparable explanatory flow: YES
- rhetoric vs structure separable: YES
- bounded length suitability: YES
- canonical input suitability: YES
- note:
  - transformer와는 다른 graph / retrieval / architecture 주제다.
  - 문제/구성요소/관계 추출/그래프 구조/검색 활용 흐름이 드러나 negative control에 적합하다.
  - 설명형 구조가 살아 있어 same-topic transformer frame이 “기술 설명 일반 frame”인지 보는 비교 재료로 쓰기 좋다.

## selection note
- preferred negative control: `graphrag_neosh.txt`
- reason:
  - `claude_code_index.txt`도 적합하지만, `graphrag_neosh.txt`는 graph / retrieval / architecture 중심이라 rhetoric보다 구조 비교에 더 바로 들어가기 쉽다.
  - 그래서 same-topic transformer frame이 “기술 설명 일반 frame”인지 보는 첫 negative control로는 `graphrag_neosh.txt`가 조금 더 깨끗한 후보다.
- do not test both now unless clearly needed
