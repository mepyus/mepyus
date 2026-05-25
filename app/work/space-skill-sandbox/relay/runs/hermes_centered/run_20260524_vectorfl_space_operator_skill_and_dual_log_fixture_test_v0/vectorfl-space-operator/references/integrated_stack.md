# Integrated Stack

Hermes accepted Codex space governance as the policy layer with HOLD.

Layer order:
1. `L0_USER_ORIGINAL`: Hermes preserves original and decides if fresh space reference is needed.
2. `L1_SPACE_GOVERNANCE`: Codex classifies input, judges space delta, decides Gemini exploration need, and defines maturation boundary.
3. `L2_OPERATION_ROUTER`: Codex maps user/Hermes instruction to one of four routes.
4. `L3_DUAL_LOG_HANDOFF`: Hermes and Codex avoid log collision through `hermes_exec/`, `codex_space/`, and `shared_handoff/`.
5. `L4_HERMES_EXECUTION`: Hermes merges original + retrieved space + model reasoning and executes or holds with trace.
6. `L5_CODEX_MATURATION`: Codex reads Hermes reentry and proposes HOLD-only space maturation.
7. `L6_OPTIONAL_WIDE_LENS`: Gemini is used only through Codex when bounded records cannot resolve layer/space ambiguity.

Conflict policy:
- Governance decides role and boundary.
- Router decides route-specific reads and return fields.
- Dual-log decides namespace, immutability, sha256, and cross-read rules.
- If Codex proposes apply but Hermes lacks user approval, Hermes records HOLD receipt only.
