# Source Authority Ladder v0

## Purpose

merge/diff/hold 전에 공간 근거의 권위 순서를 고정한다. 이 ladder는 existing baseline을 뒤집지 않고, Codex가 비교할 때의 기본 판단 순서를 제공한다.

## Execution

Authority levels:

1. `locked_baseline`
   - `CURRENT.md`
   - `source_assets/baselines/*`
   - 명시적으로 baseline/lock으로 선언된 정책 문서
2. `current_working_baseline`
   - `vectorfl_status.md`의 current pointer
   - current PASS baseline / working candidate로 명시된 문서
3. `policy_or_contract`
   - `docs/policies/*`
   - `docs/contracts/*`
   - `docs/specs/*` 중 contract/spec 역할 문서
4. `guide_or_index`
   - `docs/guides/*`
   - `docs/indexes/*`
   - `folder_status.md`
5. `report_or_observation`
   - `docs/reports/*`
   - `docs/notes/*`
   - observer/readout/validation result
6. `runtime_artifact`
   - `runtime/contracts/*`
   - `runtime/manifests/*`
   - `runtime/events/*`
   - `runtime/views/*`
   - latest는 현재 상태면이지 영구 권위가 아니다.
7. `experiment_or_reference`
   - `references/*`
   - experimental work files
   - legacy comparison assets

Conflict handling:

- Higher authority wins only when the same meaning is directly in conflict.
- Lower authority can expose a gap or newer operational condition.
- If higher authority is silent and lower authority is concrete, use lower authority as `PROVISIONAL`.
- If two high-authority sources conflict, mark `HOLD` and request user decision.

## Interpretation

authority ladder가 merge/diff의 선행조건인 이유는 Codex 판단과 공간 근거를 같은 층으로 놓으면 안 되기 때문이다. Codex는 일반 판단을 제공할 수 있지만, 공간이 이미 잠근 기준을 임의로 대체할 수 없다. 반대로 공간의 낮은 권위 report가 높은 baseline의 빈틈을 드러낼 수도 있으므로 낮은 자료를 버리지 않고 relation을 붙여야 한다.

## Validation

- SSOT와 참고자료를 분리했다.
- latest/runtime view를 원장으로 보지 않게 했다.
- conflict를 삭제하지 않고 hold 또는 provisional로 처리한다.
- 사용자 승인 필요 지점은 high-authority conflict에 한정된다.

## Stage 1 Closeout

- Verdict: `PASS_WITH_NOTE`
- Files created: `docs/specs/source_authority_ladder_v0.md`
- Key decisions: current working baseline은 final lock보다 낮지만 일반 report보다 높다.
- Risks: 일부 기존 문서는 title과 위치가 다를 수 있어 asset별 판독이 필요하다.
- Entry condition for next stage: question packet은 expected authority level과 search target을 표현할 수 있어야 한다.
