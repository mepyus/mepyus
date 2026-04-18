# folder_structure_recheck_v1

## 목적
현재 폴더 트리를 다시 점검해서
- 정상 역할 분리
- 실제 수정 대상
- 지금은 그대로 두는 것이 맞는 혼합 상태
를 다시 구분한다.

## 1. 전체 판단
현재 구조는 전반적으로 안정적이다.

핵심 4축이 이미 분리되어 있다.
- `inputs/`
  - 사람이 넣는 raw 입력
- `source_assets/`
  - Codex가 만드는 source md
- `docs/`
  - 사람이 읽는 설명 / 예시 / 기준
- `runtime/`
  - 엔진 기록 / observer / contracts / receipts

즉 지금 구조의 문제는 “전체 설계가 흔들린다”가 아니라,
일부 폴더에서 과거 자산과 새 운영 기준이 함께 보여 혼선이 생긴다는 점이다.

## 2. 이번 점검에서 바로 수정한 것
- `.DS_Store` 삭제
- `inputs/external_cases/README.md` 보강
  - 새 raw input과 예전 md 혼합 자산을 어떻게 읽어야 하는지 명시

## 3. 정상으로 보는 것

### 3-1. `source_assets/` 와 `docs/examples/` 와 `runtime/*`의 병행 존재
이건 중복이 아니다.

- `source_assets/`
  - source input / 선언문 / 기준문 / 지시서
- `docs/examples/`
  - 사람이 읽는 first-pass 사례 문서
- `runtime/observer/exploration/`
  - observation sidecar
- `runtime/contracts/`
  - checklist / repeat-check / trigger 판독 결과

즉 같은 사례가 여러 곳에 보이는 것은 역할 분리다.

### 3-2. 루트에 남은 일부 reference 문서
다음 파일들은 현재 그대로 둬도 괜찮다.
- `CURRENT.md`
- `vectorfl_status.md`
- `codex_content_pack.md`
- `codex_processor_standard.md`
- `vectorfl_philosophical_interpretation_v1.md`
- `tech_analysis_saltlux_goover_ontology_based_multi_agent_system_v1.md`
- `external_case_example_saltlux_goover_relation_reading_v0.md`

이들은 입력함 혼선보다 reference / interpretation 성격이 더 강하다.

## 4. 아직 혼합 상태지만 당장 이동하지 않은 곳

### 4-1. `inputs/external_cases/`
현재 이 폴더에는 아래가 함께 있다.
- 새 canonical raw input `txt`
- 예전 운영에서 들어온 `md`
- README / status

이건 약한 혼합 상태지만 당장 물리 이동하지는 않았다.
이유는:
- 이미 운영 흐름에 쓰였을 수 있고
- 지금은 “새 입력 기준을 더 명확히 하는 것”이 먼저이기 때문이다.

현재 해석:
- 새 raw source는 여기 둔다
- 기존 md는 `legacy mixed inputs`로 읽는다

## 5. 지금 기준으로 가장 좋은 운영 규칙
- 외부 원문 / transcript / raw text: `inputs/external_cases/`
- 내부 메모 / 초안: `inputs/internal_notes/`
- 구조화된 참고 문서: `inputs/reference_docs/`
- Codex가 만든 source input md: `source_assets/external_case_inputs/`
- 사람이 읽는 사례 정리: `docs/examples/`
- 엔진 판독 기록: `runtime/observer/exploration/`, `runtime/contracts/`

## 6. 다음에 손볼 수 있는 후보
지금 당장 필수는 아니지만, 나중에 한 번 더 정리할 수 있는 후보는 있다.

### low-priority
- `inputs/external_cases/` 안의 예전 `md` 자산을
  - `inputs/reference_docs/`
  - 또는 `source_assets/external_case_inputs/`
  로 재분류할지 검토

### keep-as-is
- `docs/examples/`
- `runtime/observer/exploration/`
- `runtime/contracts/`
- `source_assets/`

이쪽은 현재 역할 분리가 잘 되어 있어 굳이 손댈 이유가 크지 않다.

## 7. 최종 판정
현재 폴더 구조는 “복잡해져서 위험한 상태”가 아니라,
핵심 분리는 이미 잘 잡혀 있고 일부 입력 폴더만 과거 자산 때문에 약간 혼합되어 보이는 상태다.

따라서 지금 가장 맞는 조치는:
- 전체 재편이 아니라
- 입력함 기준을 더 명확히 하고
- 불필요한 잡파일을 지우고
- 혼합 폴더는 문서 기준으로 먼저 잠그는 것

이다.
