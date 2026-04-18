# OpenClaw Structural DNA & Axis Analysis

Date: 2026-04-15
Actor: Gemini-CLI
Source: `references/git_search/openclaw-main/src/`
Reason: Structural decomposition of OpenClaw for selective adoption into VECTORFL.

## 1. Taxonomic Objects of OpenClaw

### A. The "Contract" Object (Axis of Capability Abstraction)
- **DNA**: `API-Baseline + Channel-Contract`.
- **Structural Setting**:
  - `src/plugin-sdk/api-baseline.ts`: Defines the minimum viable interface for all plugins.
  - `src/plugin-sdk/channel-contract.ts`: Standardizes how different messaging platforms talk to the core.
- **Meaning**: Capability is not a feature; it's a fulfilled contract.

### B. The "Envelope" Object (Axis of Inbound Normalization)
- **DNA**: `Inbound-Envelope + Account-Resolution`.
- **Structural Setting**:
  - `src/plugin-sdk/inbound-envelope.ts`: Wraps raw external requests into a standard data structure.
  - `src/plugin-sdk/account-lookup.ts`: Maps platform-specific IDs to a universal identity.
- **Meaning**: The engine never sees "raw" external data; it only sees normalized envelopes.

### C. The "Pipeline" Object (Axis of Response Flow)
- **DNA**: `Channel-Reply-Pipeline + Sequential Transformation`.
- **Structural Setting**:
  - `src/plugin-sdk/channel-reply-pipeline.ts`: Manages the flow from engine result back to user-facing output.
- **Meaning**: Output is a controlled process, not a direct side-effect.

## 2. Structural Patterns for Potential Adoption (Filtering)

| OpenClaw Pattern | Structural Axis | Recommended VECTORFL Application |
| :--- | :--- | :--- |
| **Contract-First SDK** | Plugin Isolation | Define a `FragmentOperatorContract` that all internal/external tools must implement to touch Fragments. |
| **Inbound Normalization** | Request Standard | Use an `Envelope` structure for any external input (e.g., WashTank logs, interview transcripts) before it hits the Ingest Layer. |
| **Universal Identity** | Provenance Axis | Map all actors (Gemini, Codex, User) to a single `UniversalActorID` to track provenance consistently. |
| **Activation Boundary** | Security/Integrity | Implement a `Boundary` object that prevents external scripts from modifying the `Constitution` or `Baseline`. |

## 3. Gemini's Judgment
OpenClaw에서 우리가 가져와야 할 가장 가치 있는 구조는 **"복잡한 외부 세계와 엔진 사이에 '계약(Contract)'과 '봉투(Envelope)'라는 두 개의 완충 지대를 두는 것"**입니다. 이는 VECTORFL의 안정성을 확보하면서도 무한한 확장성을 가질 수 있게 하는 핵심 설계 축이 될 것입니다.

---
*Note: This analysis is stored in `gemini/external_analysis/` as per the current session protocol. No files outside `gemini/` were modified.*
