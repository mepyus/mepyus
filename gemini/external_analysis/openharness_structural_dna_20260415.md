# OpenHarness Structural DNA & Axis Analysis

Date: 2026-04-15
Actor: Gemini-CLI
Source: `references/git_search/openharness-main/src/openharness/`
Reason: Structural decomposition of OpenHarness for selective adoption into VECTORFL.

## 1. Taxonomic Objects of OpenHarness

### A. The "Skill" Object (Axis of Knowledge Maturation)
- **DNA**: `Frontmatter (Metadata) + Markdown (Tactics)`.
- **Structural Setting**:
  - `loader.py`: Parses YAML for `name` and `description`.
  - `registry.py`: Holds these as singleton-like objects for the agent context.
- **Meaning**: Knowledge is not just text; it's a registered capability with a clear "Why" and "How".

### B. The "Memory" Object (Axis of Persistent Indexing)
- **DNA**: `Atomic Files + Central Entrypoint (MEMORY.md)`.
- **Structural Setting**:
  - `manager.py`: Implements `atomic_write_text` and `exclusive_file_lock` to prevent memory corruption.
  - `scan.py`: Injects these fragments into the system prompt.
- **Meaning**: Memory is a searchable atlas, not a single monolithic log.

### C. The "Decision" Object (Axis of Governance)
- **DNA**: `PermissionDecision(allowed, requires_confirmation, reason)`.
- **Structural Setting**:
  - `checker.py`: Matches `SENSITIVE_PATH_PATTERNS` before any logic.
  - `modes.py`: Defines states like `PLAN` and `FULL_AUTO`.
- **Meaning**: Every action must have a justified "Reason" string, even if denied.

## 2. Structural Patterns for Potential Adoption (Filtering)

| OpenHarness Pattern | Structural Axis | Recommended VECTORFL Application |
| :--- | :--- | :--- |
| **Frontmatter Parsing** | Knowledge Schema | Automate loading of `vectorfl/skills/` into an active agent registry. |
| **Exclusive File Lock** | State Integrity | Use when Gemini and Codex access the same `RUNLOG.jsonl` or `MEMORY.md`. |
| **Reason-Based Decision** | Governance | Enhance our RPC calls to return a `Decision` object containing the specific constitutional clause that allowed it. |
| **Atomic Memory Index** | Provenance | Maintain a `runtime/memory/index.md` that points to all "matured" fragments. |

## 3. Gemini's Judgment on "What to Borrow"
우리는 OpenHarness의 **"기억을 인덱싱하고(MEMORY.md), 판단의 이유를 객체화하는(PermissionDecision)"** 구조를 차용해야 합니다. 이는 VECTORFL의 "행동 전 기록(Log Before Action)"과 "유래 보존(Provenance)" 원칙을 물리적으로 구현하는 가장 세련된 방식입니다.

---
*Note: This analysis is stored in `gemini/` as per the current session protocol. No files outside `gemini/` were modified.*
