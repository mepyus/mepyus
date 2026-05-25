# HERMES_CODEX_DUAL_LOG_COLLISION_FREE_SETUP_V0

verdict: PASS_DUAL_LOG_COLLISION_FREE_SETUP_WITH_HOLD

## 핵심 역할 정리

지금부터 역할은 이렇게 분리한다.

- Hermes: 실행에 공간을 어떻게 가져올 것인가를 셋업한다.
- Codex CLI: 실행에 관여한 공간을 어떻게 숙성시킬 것인가를 셋업한다.

이유는 실행과 공간 숙성이 서로 같은 로그/파일/권한을 건드리면 병목과 충돌이 생기기 때문이다.

## 충돌 방지 원칙

1. Hermes와 Codex는 서로 다른 namespace에 쓴다.
   - Hermes: `hermes_exec/`
   - Codex: `codex_space/`
   - 공용 handoff: `shared_handoff/`

2. 서로의 파일은 read-only로 읽는다.

3. return/trace/receipt는 한 번 publish되면 수정하지 않는다.
   새 버전은 `*_vN` 또는 새 timestamp 파일로 만든다.

4. 공용 latest pointer는 sha256이 있는 immutable artifact만 가리킨다.

5. cross-read는 반드시 다음을 남긴다.
   - source_handle
   - source_sha256
   - used_for
   - changed_judgment
   - owner_namespace
   - read_only_assertion

## 처리 흐름

1. Hermes가 run manifest를 만들고 원본을 보존한다.
2. Hermes가 fresh space reference 필요 여부를 판단한다.
3. 필요할 때만 Codex에 space reference request를 쓴다.
4. Codex는 selected/rejected refs와 changed_judgment를 반환한다.
5. Hermes는 원본+공간+모델 판단을 merge하고 실행/보류 trace를 쓴다.
6. Hermes는 Codex-readable reentry index를 만든다.
7. Codex는 reentry를 읽고 HOLD-only maturation proposal을 쓴다.
8. Hermes는 Codex proposal을 evidence로 merge/receipt 처리한다.

## 병목 방지

- Codex는 fresh space reference가 필요할 때만 Hermes 실행 전에 붙는다.
- 공간 숙성은 Hermes 실행 이후 reentry 기반으로 비동기/HOLD 처리한다.
- Gemini는 Hermes 경로에 넣지 않는다.
- Gemini는 Codex가 layer ambiguity를 판단했을 때 Codex-side script-chain에서만 사용한다.

## HOLD

이 설계는 실행 로그/공간 숙성 로그의 충돌 방지 구조 proposal이다.
실제 authority/current-position/registry/folder/source mutation은 없다.
