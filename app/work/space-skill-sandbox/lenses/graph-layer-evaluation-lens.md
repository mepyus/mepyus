# Graph Layer Evaluation Lens

## 1. Lens Name
Graph Layer Evaluation Lens

## 2. Purpose
Deep Space(원자료)와 Worker(실행자) 사이의 중간 지도층(Graph Layer)이 우리 공간에 적합한지 평가하고, 필요한 맥락만 안전하게 꺼내기 위한 기준을 마련한다.

## 3. Problem this lens reads
- Deep Space의 정보량이 많아 CLI/Worker가 맥락을 찾기 어려움.
- 정보 검색을 위해 매번 전체 문서를 읽는 것은 비효율적임.
- 그래프 도구 도입 시 발생할 수 있는 공간 오염, 권한 drift, truth 왜곡 위험.

## 4. What Graph Layer means in our space
- Deep Space를 대체하는 층이 아니다.
- Deep Space 위에 놓이는 탐색 가능한 '지도층 후보'이다.
- 토큰 절감보다는 필요한 맥락(Context)을 추출하는 통로(Context Injection)이다.

## 5. What to evaluate
- 구조적 연결이 필요한 맥락인가?
- Provenance(근거)가 명확하게 구분되는가? (EXTRACTED / INFERRED / AMBIGUOUS)
- 사용자 판단을 강제하는가, 아니면 보조하는가?

## 6. What must not be assumed
- Graph node = 사실(Truth)이 아니다.
- Graph edge = 확정 관계(Fact)가 아니다.
- INFERRED edge = 신뢰할 수 있는 기준(Baseline)이 아니다.

## 7. Borrow / Hold / Reject frame
- Borrow: GRAPH_REPORT.md를 지도처럼 활용, 필요한 subgraph만 추출, EXTRACTED/INFERRED/AMBIGUOUS 구분, .graphifyignore 적용.
- Hold: 실제 도구 설치, MCP 연결, 전체 공간 Graph화, always-on hook 설치.
- Reject for now: Graph 결과의 Truth 취급, INFERRED 기반의 자동 반영, 민감 자료의 무검토 Graph화, graphify-out의 본체 커밋.

## 8. User-language summary
Graph Layer는 우리가 전체 공간을 매번 읽지 않고도 필요한 맥락만 찾아내기 위한 '지도'입니다. 이 지도를 만들 때 가장 중요한 것은 그래프가 현실 그 자체가 아니라는 점을 인지하고, 추론과 근거를 분리하여 사용자가 최종 판단을 내릴 수 있도록 돕는 것입니다.
