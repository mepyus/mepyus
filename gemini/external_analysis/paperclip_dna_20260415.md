# Paperclip Structural DNA & Axis Analysis

Date: 2026-04-15
Actor: Gemini-CLI
Source: `references/git_search/paperclip-master/ui/`
Reason: Structural decomposition of Paperclip for selective adoption into VECTORFL User Surface.

## 1. Taxonomic Objects of Paperclip

### A. The "Inbox" Object (Axis of Triage)
- **DNA**: `Centralized Inbound Management`.
- **Structural Setting**:
  - `ui/src/pages/Inbox.tsx`: Aggregates `approvals`, `issues`, `alerts`, and `failed_runs`.
  - Uses `InboxCategoryFilter` to switch between different types of "Pending Work".
- **Meaning**: The UI is a "Command Center" where raw requests are turned into actionable tickets.

### B. The "Adapter" Object (Axis of Engine Unification)
- **DNA**: `Pluggable Agent Interface`.
- **Structural Setting**:
  - `ui/src/adapters/adapter-display-registry.ts`: Maps internal engine types (`claude_local`, `gemini_local`) to visual metadata (Icons, Labels).
  - `ui/src/adapters/registry.ts`: Manages dynamic loading of these connectors.
- **Meaning**: The UI remains engine-agnostic; agents are just providers of a specific interface.

### C. The "Design System" Object (Axis of Visual Integrity)
- **DNA**: `Constraint-based Visual Grammar`.
- **Structural Setting**:
  - `ui/src/pages/DesignGuide.tsx`: A live document of all UI atoms.
  - `ui/src/components/StatusBadge.tsx`: Enforces consistent state representation.
- **Meaning**: Information density is managed through a strict visual token system.

## 2. Structural Patterns for Potential Adoption (Filtering)

| Paperclip Pattern | Structural Axis | Recommended VECTORFL Application |
| :--- | :--- | :--- |
| **Inbox Pattern** | Operating Flow | Structure the `User Surface` as an Inbox for matured fragments needing human decision. |
| **Adapter Display Registry** | Multi-Agent Sync | Use a registry to define how `Gemini` and `Codex` outputs are styled differently in the `Engine Surface`. |
| **Breadcrumb Navigation** | Deep Context | Adopt the complex breadcrumb logic for navigating from a `Matured Line` back to its `Source Fragment`. |
| **Identity Component** | Provenance | Reuse the `Identity` component pattern to show who (User/Gemini/Codex) last touched a fragment. |

## 3. Gemini's Judgment
Paperclip에서 가장 가져와야 할 핵심 구조는 **"복잡한 상태(Status)를 시각적 아이콘과 배지(Badge)로 정량화하여 한눈에 파악하게 만드는 '인박스 운영 철학'"**입니다. 이는 VECTORFL의 사용자면이 단순한 리포트 뷰어가 아닌, 실제 **'판단과 제어의 표면'**으로 기능하게 만드는 핵심 DNA가 될 것입니다.

---
*Note: This analysis is stored in `gemini/external_analysis/` as per the current session protocol. No files outside `gemini/` were modified.*
