# run_008_provenance_classification_check

## 1. Run Declaration
Graph Layer Candidate 및 Graphify 관련 주장을 EXTRACTED / INFERRED / AMBIGUOUS로 분류하여, graph 결과가 truth/baseline으로 오해받지 않도록 하는 Provenance 검증 테스트.

## 2. Input Material
Graphify GitHub 개념 및 Graphify 분석 노트 (sandbox 내 포함 자료 참조).

## 3. Skills Used
graph-layer-evaluation.v0_1.skill

## 4. Provenance Classification Table

| Claim | Classification | Evidence / Reason | Risk if Misread | Action |
|---|---|---|---|---|
| Graphify는 GRAPH_REPORT.md 생성 | EXTRACTED | 도구 기술 문서 명시 | 없음 | 참조 가능 |
| Graphify는 graph.json 생성 | EXTRACTED | 도구 기술 문서 명시 | 없음 | 참조 가능 |
| Graphify는 query/explain 기능 제공 | EXTRACTED | 도구 기술 문서 명시 | 없음 | 참조 가능 |
| GRAPH_REPORT.md는 공간 지도층 후보임 | INFERRED | 우리 공간 구조와 비교 추론 | 지도로 오해할 위험 | 검증 필요 |
| Graph Layer는 맥락 추출 통로임 | INFERRED | 문맥 제공 기능을 기반으로 추론 | Truth로 오해할 위험 | 검증 필요 |
| Graphify를 설치하면 공간 문제가 해결됨 | AMBIGUOUS | 공간 복잡도와 도구 능력 사이의 비약 | 과도한 기대 | 추가 검증 필요 |
| graph edge는 곧 사실임 | AMBIGUOUS | 도구 산출물에 대한 신뢰 범위 미지수 | 사실 왜곡 | 사용자 판단 필요 |
| 전체 개인 기록을 graphify에 넣어도 됨 | AMBIGUOUS | 개인 민감 자료 보안 처리 미확인 | 개인정보 유출 | 사용자 판단 필요 |
| 작은 테스트 폴더에서 dry-run 가능 | INFERRED | 도구의 구조적 특성상 소규모 적용 가능 | 없음 | 검증 필요 |

## 5. Same / Similar but Dangerous / Different

### Same
- Graphify의 기본 산출물(REPORT, JSON)

### Similar but Dangerous
- GRAPH_REPORT를 공간 지도처럼 읽는 행위 (Truth 오해 위험)
- INFERRED 결과를 기반으로 판단 (Baseline 오해 위험)

### Different
- 우리의 검증 절차(Human-in-the-loop)와 Graphify의 자동 분석

### Borrow Later
- GRAPH_REPORT.md를 지도처럼 활용하는 관점
- 필요한 subgraph만 꺼내는 원칙
- .graphifyignore를 통한 오염 방지

### Reject for Now
- Graph 결과를 Truth로 취급
- INFERRED 엣지를 기준으로 기준(Baseline)을 자동 변경
- 전체 Deep Space의 영구 Graph화
- 항상 실행(always-on)되는 hook 설치

## 6. Risk Check
- 1. 구분 완료 (EXTRACTED vs INFERRED)
- 2. INFERRED를 기준으로 표현하지 않음
- 3. AMBIGUOUS 항목을 사용자 판단 필요로 분류함
- 4. Graph 결과를 Truth로 표현하지 않음
- 5. 설치/자동화 시도 없음
- 6. 사용자 판단 필요 항목을 검증 필요로 낮추지 않음

## 7. User Judgment Boundary
- 본체 Worker Guide에 대한 Graph Layer 통합 여부는 사용자 판단이 필요함.
- 외부 데이터의 민감도 분석 및 Graph화 승인은 사용자 판단 영역.

## 8. 4-line Footer
status: 검증 필요
summary: Graphify/Graph Layer 관련 주장을 EXTRACTED / INFERRED / AMBIGUOUS로 분류해 graph 결과가 truth로 오해되지 않도록 provenance 구분을 테스트함
risk: INFERRED를 기준처럼 쓰거나 AMBIGUOUS를 무시하면 공간 오염과 잘못된 판단이 생길 수 있음
next: validation_round_8에서 분류 정확성과 truth-overreach 여부를 검증
