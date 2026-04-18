# Integrated Engine CLI Deposit Candidate

- source_session_id: `cli_20260416T115112Z_d1256d58`
- backend_kind: `codex`
- task_type: `reread`
- requested_by_surface: `user_surface`
- requested_by_page: `scripts/run_integrated_engine_language_loop.py`
- status: `done`

## Task Purpose
Internal language Koreanization data loop 7: collect Korean operating-language data from bounded context.

## Used Context Refs
- `docs/reports/integrated_engine_line_connection_axis_to_shared_language_map_v0.md`
- `docs/reports/integrated_engine_internal_language_grammar_candidate_v0.md`

## Result Summary
atch-before-check 금지 설명 필요
- next reread question: `지원`과 `보조` 중 어느 쪽이 중심-보조 관계를 더 잘 보존하는가
- suggested next use: validation target

9.
- internal phrase or signal observed: `bridge-before-flatten`
- source context where it appeared: bridge-before-flatten grammar
- internal meaning / operational role: 쉬운 표현으로 줄이기 전에 route, authority, state, boundary, support 관계를 보존해야 한다는 번역 순서
- Koreanization candidate, not final UI copy: `평탄화 전 연결`, `단순화 전 브리지`
- Korean preservation requirement: bridge work가 내부 문법을 대체하지 않고 이후 layer임을 보존해야 함
- risky Korean flattening to avoid: `쉽게 바꾸기`, `사용자 친화 표현`
- why this helps the user operate: 쉬워진 말 때문에 운영 권한이나 경로 의미가 사라지는 것을 막음
- what meaning gets lost if shortened: 내부 movement를 보존한 뒤 외부 표현을 만든다는 단계성
- repeated connection it belongs to: friction terms collection, bridge wording boundary
- emerging axis candidate: bridge preservation axis
- surface exposure note: vectorfl / codex 중심, user-facing 전 단계
- external expression support needed, if any: later bridge package에서만 외부 표현화 필요
- next reread question: `평탄화`가 내부 용어로 유지 가능한가, 아니면 `단순화`가 더 읽히는가
- suggested next use: deposit candidate

- uncertainty or failure notes
  - `reflux`는 한국어 후보가 아직 약함. `재유입`은 route 의미는 살리지만 성숙 재료 보존의 뉘앙스가 부족할 수 있음.
  - `anchor`는 `앵커` 보존과 `기준점` 번역 사이에서 결정 필요. 내부 정밀도는 `앵커`, 사용자 즉시 이해는 `기준점` 쪽이 강함.
  - `watch keep`은 한국어 단일 명사화가 어렵고, 상태 설명형 후보가 필요함.
  - `bridge-before-flatten`은 최종 외부 표현으로 쓰기보다 내부 번역 원칙명으로 유지하는 편이 안전함.

- suggested next use: validation target
  - 다음 reread target: `reflux`, `watch keep`, `anchor drift`, `bridge-before-flatten`
  - implementation return: 없음
  - validation target: Koreanization 후보가 route / authority / state / boundary / support 의미를 잃지 않는지 검증
  - deposit candidate: `hold / watch keep / not promoted`, `bridge-before-flatten`, `support reread recovery`


## Important Diffs / Findings / Outputs
- not separated in package 1 return


## Uncertainty / Failure Notes
- none recorded


## Suggested Next Use
validation_target
