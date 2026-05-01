# Mini Graph Provenance Format Candidate v0

## 1. Purpose
이 포맷은 Graph Layer 실험 중 발생하는 노드와 엣지의 근거(Provenance)를 명확히 구분하여, 그래프 결과가 실제 시스템 구조(Baseline)나 절대적 사실(Truth)로 오해받는 것을 방지하는 데 목적이 있다.

## 2. Scope
- Sandbox 내 Mini Graph Map 수동 작성 및 분석.
- 외부 자료 비교 분석을 통한 구조적 패턴 추출.
- Graphify 등 외부 도구 도입 전의 안전한 데이터 분류.

## 3. Node Types
- **Original Node**: 원문(Source Document)에 실제로 등장한 고유 명사나 핵심 용어.
- **[[SYNTH]] Synthesized Node**: 여러 자료를 비교 분석하여 우리가 부여한 해석적 명칭. 원문의 용어가 아니며 추론의 도구로만 사용함.
- **Working Node**: 반복 검증 전, 분석 편의를 위해 설정한 임시 연결점.

## 4. Edge Classification
- **source-claimed**: 원문이 직접 인과관계나 소속 관계를 주장한 내용.
- **inferred-pattern**: 여러 자료의 반복되는 구조적 특징을 보고 우리가 추론한 관계.
- **ambiguous-link**: 연결 가능성은 있으나 데이터가 부족하거나 논리적 비약이 있는 관계.

## 5. Source Anchor Fields
*이 필드는 확정된 스키마가 아니며, 추적 가능성을 위한 후보 필드이다.*
- **source_file**: 근거가 되는 파일 경로.
- **source_section**: 근거 내용이 포함된 세션 제목.
- **claim_type**: 원문 주장(stated), 구조적 특징(structural), 관측된 사실(observed).
- **quoted_or_paraphrased_claim**: 원문 인용 또는 요약된 주장 내용.
- **classification**: source-claimed / inferred-pattern / ambiguous-link.
- **confidence_note**: 분류 결정의 확실성 정도 및 근거.

## 6. Risk Rules
- **source-claimed ≠ truth**: 원문이 그렇게 주장했을 뿐, 그것이 항상 사실임을 의미하지 않음.
- **inferred-pattern ≠ baseline**: 우리의 추론 결과가 시스템의 공식 기준이 될 수 없음.
- **ambiguous-link ≠ 무시해도 됨**: 약한 연결도 잠재적 위험이나 기회가 될 수 있으므로 기록함.
- **[[SYNTH]] node ≠ 원문 용어**: 우리가 만든 용어를 원본 데이터에 섞지 않음.
- **Mini Graph Map ≠ source-space ontology**: 이 지도는 탐색을 위한 보조 도구일 뿐, 시스템의 온톨로지가 아님.

## 7. Output Example
- **node**: Thin Harness
- **node_type**: [[SYNTH]]
- **source_anchor**: Browser Harness + mini-swe-agent 반복 패턴
- **note**: 실행 환경을 얇게 유지하려는 두 프로젝트의 공통 구조를 우리가 명명함.

## 8. Not a Baseline Notice
이 포맷은 샌드박스 내 실험을 위한 후보 포맷이며, 프로젝트의 공식 taxonomy, schema, baseline이 아님을 명시한다.

## 9. 4-line Footer
status: 후보화 완료
summary: Graph Layer의 안전한 활용을 위해 노드 타입과 엣지 분류를 정의한 Mini Graph Provenance Format Candidate v0를 작성함
risk: 포맷 자체를 공식 기준으로 오해할 수 있으나, 이는 샌드박스 내 실험용 가이드임
next: run_009에서 이 포맷의 반복 가능성을 검증함
