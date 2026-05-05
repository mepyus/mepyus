# EXTERNAL_PROGRAM_PATTERN_MAP_V0

| External Program | Recovered Pattern | VectorFL Equivalent | Status |
| :--- | :--- | :--- | :--- |
| **OmX** | Codex Workflow Layer | Read-only Adapter | Recover |
| **Hermes** | Memory/Mission Sep. | Mission Packet Interface | Recover |
| **OpenClaw** | Gateway/Control Plane | Future Reference | HOLD |
| **Codex** | File-based worker | Space Reader/Critique | Recover |
| **Gemini** | Meta-analysis/Support | External Analysis/Critique | Recover |

## 상세 회수 전략
- **OmX**: Codex를 감싸는 워크플로우 레이어로서, VectorFL의 작업을 Codex가 읽기 좋은 형태로 구조화하는 'Exploration Harness'로 사용.
- **Hermes**: 런타임 미션(Mission Packet)과 공간의 기록(Standing Context)을 분리하는 구조를 적용하여 세션 독립성을 확보.
- **OpenClaw**: 게이트웨이 및 대몬 기능은 과도한 제어권 드리프트를 유발하므로 현재는 미래 확장성을 위한 개념 참조로만 유지.
- **Codex/Gemini**: 각각 내부 공간 읽기 및 외부 비교 분석의 특수 목적 도구로 한정.
