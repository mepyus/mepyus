[[A]] [[OBJ:common_vs_asset_specific_failure_surface_split_v1]] [[SEM:split_between_repeated_gate_failures_and_asset_specific_failure_surfaces]]

# common vs asset-specific failure surface split v1

## 1. purpose

- 이번 문서의 목적은 gated validation에서 반복적으로 나타나는 실패면과, 자산 형식 때문에 특수하게 나타나는 실패면을 분리하는 것이다.

## 2. common failure surface

- `question-inducing candidate = 0`
- `fallback-grounded` 중심 recovery
- `weak role-like reading` 또는 role-like reading 부재
- `pivot / compression` 반복 회복 실패
- `scaffold carryover` 위험

## 3. asset-specific failure surface

### 3-1. code index type

- asset:
  - `claude_code_index.txt`
- 특수 실패면:
  - single operational block collapse 극단화
  - AI object vocabulary overfire
  - heading mismatch가 role failure로 직접 연결

### 3-2. instructional transcript type

- asset:
  - `graphrag_neosh.txt`
- 특수 실패면:
  - segmentation 이전 단일 운영 블록 수렴
  - role-like reading이 살아나도 scaffold carryover가 의미 회복보다 앞섬

### 3-3. enterprise dialogue type

- asset:
  - `enterprise.txt`
- 특수 실패면:
  - question opening은 풍부하지만 candidate emergence가 닫혀 있음
  - dialogue closure/transition 약점이 남음

### 3-4. mid-structure engineering article type

- asset:
  - `openai_02_11.md`
- 특수 실패면:
  - segmentation 문제는 약하지만 direct grounding / role recovery가 여전히 부족
  - 즉 건강한 구조에서도 gate blocker가 그대로 남는다는 점이 드러남

## 4. why this split matters

- 공통 실패면은 gate blocker 요약과 직접 연결된다.
- 자산별 실패면은 heuristic tuning을 부르는 유혹이 있지만, 지금 단계에서는 generalization 근거가 아니라 failure contour 자료다.

## 5. operator read

- 운영자는 공통 실패면을 보고 gate 상태를 판단해야 한다.
- 자산별 실패면은 “왜 이 자산이 더 안 읽히는가”를 이해하는 보조 자료로만 봐야 한다.

## 6. one-line summary

> 지금 필요한 것은 자산별 실패를 하나의 문제로 뭉개는 것도, 공통 blocker를 자산 고유 문제로 착각하는 것도 아니며, 반복되는 gate blocker와 자산별 failure contour를 분리해서 보는 것이다.
