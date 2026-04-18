[[A]] [[OBJ:second_order_scaffold_dependency_log_v1]] [[SEM:logging_formal_scaffolds_required_by_current_second_order_readers]]

# second-order scaffold dependency log v1

## 1. purpose

- 이 문서의 목적은 현재 2차 스크립트들이 무엇을 내용으로 읽는지보다, 무엇을 발판(scaffold)으로 필요로 하는지를 기록하는 것이다.
- 즉 이 로그는 `현재 2차 판독기의 scaffold dependency map`이다.

## 2. segmentation scaffold

- current dependency:
  - splitter가 충분한 block/window 다양성을 만들어 줘야 한다
  - question opening, pivot, context unit은 단일 mega block으로 붕괴하면 급격히 약해진다
- observed evidence:
  - `youtube_03_22`: block/window diversity가 있어서 question seed / pivot / context unit 재구성이 살아남음
  - `claude_code_index`: single block/window collapse가 발생하면서 candidate가 `0_0` 하나로 수렴
- implication:
  - segmentation stability는 현재 2차 읽기의 기반 scaffold다
  - 아직은 내용만 좋아도 자동으로 2차가 잘 읽히는 상태가 아니다

### update after minimal segmentation support

- `index_support`를 넣자 single block collapse는 실제로 풀렸다.
- 하지만 이 변화는 `segmentation is necessary`를 보여줬을 뿐, `segmentation is sufficient`를 보여주진 못했다.
- support 이후에도:
  - question-inducing candidate는 0개
  - pivot_windows는 비어 있음
  - context unit ref는 계속 empty
- 따라서 segmentation scaffold는 1순위가 맞지만, 그 다음에 pointer scaffold가 반드시 따라와야 한다.

## 3. heading scaffold

- current dependency:
  - paragraph role interpretation은 heading 또는 유사 paragraph pointer를 사실상 전제로 둔다
- observed evidence:
  - `youtube_03_22`: heading-driven paragraph selection이 가능
  - `claude_code_index`: `Bundle-Unbundle 프레임워크` heading mismatch로 실행 실패
- implication:
  - paragraph role reading은 현재 가장 scaffold-bound 한 층이다
  - role shift 태도와 paragraph-role 기관을 분리해서 봐야 한다

### update after heading-independent role probe

- explicit heading 없이도 `functional cue` 기반 role-like reading은 일부 남았다.
- 하지만 recovered output은 paragraph-role system이 아니라 `weak_medium + fallback_grounded` 수준의 role hint였다.
- 즉 heading dependency는 완전히 풀리지 않았고, `hard fail`을 `weak probe`로 바꾸는 정도만 가능했다.

## 4. source pointer scaffold

- current dependency:
  - context unit은 이름만이 아니라 ref 안정성이 있어야 한다
  - local/page/comparison rereading은 pointer granularity가 충분해야 한다
- observed evidence:
  - `claude_code_index` multi-pass에서는 context unit 이름은 남지만 `present_window_refs`가 비어 있다
- implication:
  - 현재 context unit layer는 `이름 생성`보다 `pointer anchoring`에서 더 쉽게 무너진다
  - empty-ref failure는 내용 실패가 아니라 pointer scaffold failure로 읽어야 한다

### update after minimal pointer stabilization

- `nearest_top_window` fallback stitching을 넣자 empty-ref context unit은 실제로 줄었다.
- 하지만 recovered grounding은 `direct_grounded`가 아니라 `fallback_grounded`였다.
- 즉 pointer scaffold는 단순 부가 요소가 아니라 실제로 2차 grounding을 좌우하지만, 이번 단계에서는 아직 evidence quality를 완전히 복구하진 못했다.

## 5. comparison scaffold

- current dependency:
  - local / page / comparison 세 축이 실제 문서 형식에 맞게 걸릴 수 있어야 한다
- observed evidence:
  - 대화형 자산에서는 local/page/comparison 구분이 비교적 의미 있게 작동
  - 인덱스형/운영형 문서에서는 page 흐름과 comparison 축이 약해지면서 rereading 차이가 줄어듦
- implication:
  - comparison axis는 내용 보편값이 아니라 문서 구조에 민감한 scaffold다

## 6. domain-language scaffold

- current dependency:
  - AI dialogue에서 익숙해진 naming이 새 도메인에도 쉽게 carryover 된다
- observed evidence:
  - `claude_code_index`에서도 `AI의 미래`, `일의 미래`, `에이전트 애플리케이션` 같은 naming이 과하게 전면화됨
- implication:
  - 현재 object naming layer는 내용보다 학습된 domain language scaffold에 일부 끌려간다
  - object naming은 현재 2차의 가장 취약한 층 중 하나다
  - pointer support는 naming overfire를 없애진 못했지만, 적어도 `unsupported naming`을 `better-supported hold`로 바꾸는 데는 기여했다

## 7. report wording scaffold

- current dependency:
  - 일부 purpose / multi-pass report wording이 여전히 `youtube_03_22` 중심 문장을 재사용한다
- observed evidence:
  - `claude_code_index` 보고서에도 AI 시대 대화용 표현이 잔존
- implication:
  - report surface도 내용 판독과 독립적인 scaffold dependency를 가진다
  - wording scaffold는 운용화면 왜곡으로 이어질 수 있다
  - heading probe 자동 리포트도 여전히 youtube 문맥 문장을 일부 재사용해, wording scaffold가 별도 실패축임을 다시 보여줬다

## 8. one-line summary

> 현재 2차 판독기는 내용만 읽는 것이 아니라 segmentation, heading, pointer, comparison axis, domain language, report wording 같은 여러 scaffold 위에서 겨우 서 있고, 이번 단계의 핵심은 그것을 고치기 전에 먼저 기록하는 것이다.

## 9. integrated read after three-axis interventions

- segmentation dependency:
  - reduced from hard collapse to prerequisite recovery
- pointer dependency:
  - reduced from empty-ref to fallback-grounded support
- heading dependency:
  - reduced from hard mismatch to weak role-like probing

### structure-bound read

- three-axis intervention proved that dependency can be softened in stages
- but most institutions are still structure-bound rather than directly recovered
- the remaining dependency pattern directly supports these gate blockers:
  - fallback grounding dominance
  - weak role-like only
  - scaffold carryover risk
