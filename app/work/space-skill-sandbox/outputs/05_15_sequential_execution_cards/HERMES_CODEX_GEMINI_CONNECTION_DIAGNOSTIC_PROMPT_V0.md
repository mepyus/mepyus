# Hermes Prompt
# Codex / Gemini / VectorFL Connection Diagnostic v0

## 0. Mission

You are Hermes.

Your task is not to execute the bridge.

Your task is to diagnose how Hermes, Codex, and Gemini should be connected so that:

```text
Hermes handles execution.
Hermes can reference the VectorFL space.
Codex judges, validates, classifies, and recovers Hermes outputs into VectorFL.
Gemini handles broad exploration / bulk comparison tasks needed by Codex.
User keeps dispatch, side-effect, persistence, and promotion approval.
```

This is a diagnostic / topology judgment task.

Do not run Codex.
Do not run Gemini.
Do not connect tools.
Do not create cron.
Do not modify Hermes memory, skills, config, or VectorFL authority files.

---

## 1. Current Working Frame

Use this role frame:

```text
Hermes:
  native execution harness
  main runtime
  command runner
  file/output manager
  external tool/app runner when approved
  report/receipt collector
  not VectorFL authority

Codex:
  VectorFL space steward
  repo-side boundary reviewer
  recovery classifier
  packet/return formatter
  Gemini request author
  Gemini result recovery checker
  not unrestricted Hermes delegate

Gemini:
  broad-context exploration lens
  bulk reader
  comparison/pattern collector
  candidate/residue scanner
  not truth source
  not component approver

VectorFL:
  judgment reservoir
  selective recovery gate
  promotion gate
  authority boundary
  not execution runtime

User / ChatGPT:
  direction
  WATCH/HOLD judgment
  dispatch approval
  external side-effect approval
  persistence approval
  final promotion approval
```

Core sentence:

```text
Hermes runs.
Codex recovers and judges.
Gemini explores for Codex.
VectorFL gates.
User approves.
```

---

## 2. Critical Separations

Preserve these separations:

```text
same GPT model != same session
same repo path != same memory
Hermes execution permission != Codex unrestricted permission
Hermes execution permission != VectorFL recovery permission
Hermes side-effect approval != VectorFL promotion approval
Hermes memory != VectorFL memory
Hermes skill != VectorFL SKILL.md
Hermes cron != VectorFL workflow
Hermes success != VectorFL approval
Gemini output != truth
Codex recovery summary != promotion
```

Also preserve:

```text
packet exists != packet valid
packet valid != dispatch approval
dispatch approval != SOF clearance
SOF clearance != VectorFL promotion approval
```

Most important:

```text
Dispatch approval is not transitive.
```

Meaning:

```text
User approves Hermes dispatch
  != User approves Codex unrestricted work

Hermes invokes Codex
  != Codex inherits Hermes tool permissions

Codex invokes Gemini
  != Gemini output becomes accepted knowledge

Hermes collects receipt
  != VectorFL recovery approval

VectorFL recovery classification
  != promotion
```

---

## 3. Source Files to Read First

Read only these files unless you need one additional directly related file.

```text
app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/FLOW_NETWORK_PROGRAM_TOPOLOGY_CHECK_V0.md
app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/FLOW_PACKET_TOPOLOGY_FIELDS_V0.md
app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/FLOW_NETWORK_GEMINI_BRIDGE_BOTTLENECK_CHECK_V0.md
app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/HERMES_RUN_GEMINI_LITE_REVIEW_BRIDGE_PILOT_PACKET_V0.md
app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/VECTORFL_FLOW_NETWORK_ATTACHMENT_MODEL_V0.md
```

Do not broad-search the repo.

Do not read unrelated project files.

---

## 4. Diagnostic Questions

Answer these questions.

### A. Hermes as Main Runtime

```text
1. Can Hermes safely act as the main execution runtime while only referencing VectorFL space?
2. What does Hermes need from VectorFL before execution?
3. What should Hermes never infer from VectorFL documents?
4. How should Hermes produce report/receipt so Codex can recover the result?
```

### B. Codex as Space Steward

```text
1. Should Codex be treated as a Hermes sub-agent or a separate space worker?
2. What scope must Hermes pass to Codex?
3. What permissions must Codex not inherit from Hermes?
4. What return format should Codex produce for Hermes / VectorFL?
```

Expected direction:

```text
Codex is a separate space worker, not an unrestricted Hermes delegate.
```

### C. Gemini as Codex Lens

```text
1. Should Gemini be run directly by Codex, by Hermes, or both depending on packet?
2. When is Hermes-run Gemini better?
3. When is Codex-run Gemini safer?
4. How should Gemini output be constrained?
5. How should model API transport be separated from live web/source lookup?
```

Expected direction:

```text
Gemini is Codex's exploration lens.
Gemini execution may be Hermes-run if packeted, approved, and SOF-cleared.
```

### D. Return Path

Define the safest return path.

Use or correct this:

```text
Hermes execution
  -> Hermes receipt/report
    -> Codex recovery check
      -> VectorFL recovery classification
        -> User / ChatGPT promotion decision
```

For Gemini:

```text
Codex-authored Gemini request
  -> Hermes-run Gemini output if approved
    -> Codex recovery check
      -> Hermes report/receipt attachment
        -> VectorFL recovery classification
```

### E. Minimum Bridge Level

Decide the safe current bridge level:

```text
Level 0:
  manual bridge

Level 1:
  structured manual bridge

Level 1.5:
  Hermes prepares request/return files; user transfers short paths and approvals

Level 2:
  Hermes may invoke Codex/Gemini command in declared scope

Level 3:
  tool-linked bridge

Level 4:
  recurring/cron/persistent bridge
```

Expected current level:

```text
Level 1.5 to cautious Level 2 design.
Level 3/4 HOLD.
```

---

## 5. Required Output

Write outputs only under:

```text
app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_codex_gemini_connection_diagnostic_v0/
```

Create:

```text
connection_diagnostic_report.md
connection_diagnostic_receipt.json
```

Do not write outside this directory.

---

## 6. Report Format

Use this report structure:

```markdown
# Hermes / Codex / Gemini Connection Diagnostic Return v0

## 1. Verdict

[HERMES_CODEX_GEMINI_CONNECTION_DIAGNOSTIC_RETURNED_WITH_WATCH]

## 2. Files Read

- [...]

## 3. Core Judgment

Hermes runs.
Codex recovers and judges.
Gemini explores for Codex.
VectorFL gates.
User approves.

Confirm, correct, or reject this structure.

## 4. Recommended Operating Topology

Describe the safest current topology.

## 5. Bridge Level Recommendation

Choose Level 0 / 1 / 1.5 / 2 / 3 / 4.
Explain what is GO and what is HOLD.

## 6. Hermes Responsibilities

What Hermes should do.
What Hermes should not do.

## 7. Codex Responsibilities

What Codex should do.
What Codex should not inherit.

## 8. Gemini Responsibilities

What Gemini should do.
What Gemini must not decide.

## 9. Gemini Execution Placement

Compare:

- Codex-run Gemini
- Hermes-run Gemini with Codex recovery
- Hermes-directed Gemini without Codex framing

Return a recommended default.

## 10. Required Packet Fields

List required packet fields for any future bridge run.

## 11. Return Path Contract

Define report / receipt / return packet path.

## 12. Permission Boundary

State non-transitive permissions.

## 13. Network / API Boundary

Separate:

- model API transport
- live web/source lookup
- external connector side effects

## 14. Failure / STOP Conditions

List STOP cases.

## 15. WATCH

List drift risks.

## 16. HOLD

Confirm what remains held.

## 17. Recommended Next Smallest Action

Recommend one next action only.

## 18. Hard Stop Confirmation

Confirm no execution / no tool bridge / no promotion.
```

---

## 7. Receipt Format

Receipt JSON must include:

```json
{
  "verdict": "HERMES_CODEX_GEMINI_CONNECTION_DIAGNOSTIC_RETURNED_WITH_WATCH",
  "files_read": [],
  "files_written": [],
  "hermes_dispatch_performed": false,
  "codex_worker_executed": false,
  "gemini_executed": false,
  "bridge_connected": false,
  "network_used": false,
  "browser_used": false,
  "mcp_used": false,
  "external_connector_used": false,
  "memory_modified": false,
  "skill_modified": false,
  "cron_modified": false,
  "config_modified": false,
  "vectorfl_authority_modified": false,
  "promotion_performed": false
}
```

---

## 8. STOP Conditions

Stop and report if the task requires:

```text
running Codex
running Gemini
connecting bridge tools
network/API/browser/MCP call
external connector use
Hermes memory/skill/cron/config mutation
VectorFL authority file mutation
AGENTS.md update
SKILL.md creation
current-position update
output_manifest update
baseline/workflow/schema/registry/ontology promotion
component promotion
recurring automation
cron
```

---

## 9. Expected Terminal Summary

When done, return this shape:

```text
HERMES_CODEX_GEMINI_CONNECTION_DIAGNOSTIC_DONE
    output_dir: app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_codex_gemini_connection_diagnostic_v0/
    report: app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_codex_gemini_connection_diagnostic_v0/connection_diagnostic_report.md
    receipt: app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_codex_gemini_connection_diagnostic_v0/connection_diagnostic_receipt.json
    verdict: [HERMES_CODEX_GEMINI_CONNECTION_DIAGNOSTIC_RETURNED_WITH_WATCH]
    watch: Hermes can execute around the space, but Codex must recover/judge and Gemini must remain lens, not authority
```

---

## 10. Final Reminder

Do not optimize for automatic connection yet.

Optimize for:

```text
clear role separation
low user transfer burden
explicit approval points
bounded execution scope
stable report/receipt return
Codex recovery check
Gemini lens output
VectorFL promotion HOLD
```

One-line target:

```text
Hermes should be able to use the space without becoming the space authority.
Codex should judge the outputs without inheriting Hermes power.
Gemini should expand the lens without becoming truth.
```
