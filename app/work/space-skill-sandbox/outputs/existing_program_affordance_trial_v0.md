# Existing Program Lens Application Trial v0

## 1. Target
- name: scripts/sandbox/run_gemini_packet.sh
- source: scripts/sandbox/run_gemini_packet.sh
- type: Bash Runner Script

## 2. Caller Shift Analysis
- **Human Caller Assumption**: Usage 가이드를 읽고 유효한 RUN_ID와 PACKET_PATH를 수동으로 제공할 것으로 기대함 (Evidence: 14-25행).
- **Agent Caller Risk**: 에이전트가 `RUN_ID`에 쉘 메타문자(예: `;`, `&`, `|`)를 주입하여 임의 명령 실행을 시도할 위험. 현재 스크립트(114-117행)는 `/`와 `..`만 방어하고 있어 쉘 주입(Shell Injection)에 취약함. 인간은 "상식적으로" 이런 짓을 하지 않지만, 에이전트는 효율을 위해 "실수로" 혹은 "의도적으로" 시도할 수 있음.

## 3. Tool Affordance
- **Preflight Handle**: `--preflight` 옵션(126-140행)이 에이전트가 실행 환경(API Key, 바이너리, 권한 등)의 가용성을 스스로 체크할 수 있는 훌륭한 "안전 손잡이"임.
- **Allowed Use Case**: `Relay Session`이 정해진 `app/work/...` 경로 내에서 패킷 결과를 저장할 때만 사용해야 함.
- **Forbidden Use Case**: 에이전트가 직접 `RUN_ID`를 생성하여 다른 폴더에 쓰기를 시도하는 행위.
- **Preflight Stop Point**: `--preflight` 결과 중 `outbox_directory_writable`이 false이거나 `GEMINI_API_KEY`가 absent인 경우 즉시 중단해야 함.

## 4. Session Role Fit
- **Role**: `Relay Session`
- **Reason**: 외부 패킷(Inbox)을 받아 실행하고 결과를 Outbox로 전달하는 전형적인 가교 기능을 수행함 (Evidence: 154-156행 경로 고정).

## 5. Evidence
- **Evidence A**: 스크립트 14-25행 (Manual Usage 가이드 및 수동 트리거 선언)
- **Evidence B**: 스크립트 114-117행 (RUN_ID 검사 로직 - `/`와 `..`만 제한됨을 확인)
- **Evidence C**: 스크립트 126-140행 (Preflight 로직 - 환경 상태 노출)
- **Evidence D**: 스크립트 154-156행 (출력 경로 고정 - `app/work/...`)

## 6. Conclusion
- Lens v0는 기존 프로그램의 "상식적 구멍(쉘 주입 취약성)"과 "제어 가능한 손잡이(Preflight)"를 식별하는 데 매우 효과적임.
- 현재 스크립트는 Relay Session으로 사용하기에 "위험하지만 관찰 가능한" 상태임.

## 7. Next Action Recommendation
- **PASS_WITH_NOTE**: 렌즈 실험 결과는 성공적임. 다만 식별된 쉘 주입 위험에 대한 보완(Sanitization 강화)이 이루어지기 전까지는 에이전트에 의한 자동 호출을 HOLD할 것.
