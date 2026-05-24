# Candidate Reading Lens Catalog v0

## 1. Status

Status: candidate asset catalog
Authority: candidate reference / not baseline / not official workflow
Purpose: catalog durable reading lenses and candidate signals produced during whole-space and formation-prework rounds

## 2. Core Reading Axes (Maturing)

These four axes provide the primary structural lenses for reading the current space.

### 2.1 Harness-Orientation
- **Concept:** Operating environment and role boundaries must be set *before* worker execution.
- **Reading Angle:** "Is the worker bounded by a safe harness?"
- **Protects:** Model capability becoming autonomous authority.

### 2.2 Affordance-Program
- **Concept:** External tools and programs are read as materials with specific affordances and permissions.
- **Reading Angle:** "What is the tool's visible form (affordance) to the caller?"
- **Protects:** Tool adoption or implementation drift.

### 2.3 Signal-Memory
- **Concept:** Failure, friction, and session-loss are not errors to be deleted, but signals to be capitalized.
- **Reading Angle:** "How does this failure support future re-entry?"
- **Protects:** Process-memory loss and latest-run bias.

### 2.4 Provenance-Integrity
- **Concept:** Every judgment must be grounded in explicit source refs and authority status.
- **Reading Angle:** "Why is this judgment grounded? What is its origin?"
- **Protects:** LLM-manufactured meaning and structural drift.

## 3. Candidate Comparison Lenses (New from Round 1)

These were produced during Formation Prework Round 1 (MCP and AWS tests).

### 3.1 Resource vs. Tool (The MCP Lens)
- **Concept:** Distinction between read-only context (Resource) and executable action (Tool).
- **Reading Angle:** "Is this candidate mainly Space-side material or Execution-side capability?"
- **Use when:** Evaluating CLI, API, repo, or Skill candidates.

### 3.2 Plan before Execution (The AWS Signal)
- **Concept:** Separation of plan formation from its actual execution.
- **Reading Angle:** "Does this task need a separate Plan Packet review before Gemini execution?"
- **Use when:** Designing multi-step worker pipelines or high-risk coordination tasks.

## 4. Operational Lenses (Internal Aids)

### 4.1 Bounded Retrieval
- **Reading Angle:** "What is the minimum necessary retrieval scope for this task?"
- **Use when:** Applying `retrieval_scope_boundary` in Prework v1.

### 4.2 Description as Affordance
- **Reading Angle:** "Does the task/tool description provide clear behavioral guidance (form) to the worker?"
- **Use when:** Designing worker packets or skill READMEs.

## 5. Catalog Usage Rules

1.  **Lenses are questions, not laws.** Use them to provoke structural rereading.
2.  **Do not overfit.** If a lens doesn't apply naturally, do not force it.
3.  **Preserve candidate status.** Listing here is for discoverability, not promotion to baseline.
4.  **Maturation path.** When a lens is used successfully 3+ times, consider promoting it to a "Reusable Setting candidate."

## 6. What Must Not Be Inferred

- no baseline promotion
- no mandatory workflow
- no required ontology or schema
- no automation trigger
- no official system law

## 7. Next Safe Action

Retrieve this catalog at the start of any new "Formation Prework" or "Structural Synthesis" task.

STATUS: CANDIDATE_READING_LENS_CATALOG_V0_PREPARED
