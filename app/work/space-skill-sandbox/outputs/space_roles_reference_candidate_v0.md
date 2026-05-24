# Space Roles Reference Candidate v0

## 1. Document Status

```text
Document = Space Roles Reference Candidate
Status = CANDIDATE_REFERENCE
Authority = reference / orientation support
Not baseline
Not official workflow
Not source-space policy
Not schema
Not automation
Not permission system
```

Purpose:

```text
Clarify what each operating word in the space is allowed to do, what authority it has, what it must not become, who decides promotion, and how ChatGPT / Codex / Gemini / CLI should read it.
```

## When in Doubt

Use this reference to prevent role confusion, not to grant authority.

If a material is useful, treat it as a candidate reference until the User explicitly promotes it.
If a risk is repeated, treat it as a watch item until the User explicitly turns it into a rule.
If a worker can do something, do not treat that capability as permission.
If a run record exists, do not treat it as approval.
If a current-position or summary points somewhere, do not treat it as a registry, index, or task queue.
If a principle sounds right, do not treat it as policy.
If a helper reduces friction, do not treat it as workflow or automation.

When unsure, stop and ask for User purpose or User decision.

## 2. Why This Document Exists

The space contains many kinds of operating language.

Some language guides judgment.
Some constrains behavior.
Some records history.
Some preserves watch risks.
Some supports re-entry.
Some is only candidate/reference material.

If these roles are confused, candidate material can be mistaken for approval, principles can be mistaken for policy, watch items can be mistaken for hard law, and helper utilities can be mistaken for workflow or automation.

This document defines the roles so future readers and workers do not over-promote or misread them.

## 3. Highest-Level Orientation

```text
User decision gate remains final.
Baseline / constitution has the highest authority only when explicitly established.
Rules bind only within their declared scope.
Principles guide judgment but do not automatically command action.
Operating 15 are audit lenses, not law.
Sandbox rules bind sandbox work only.
Run records preserve traces, not approval.
Candidate references support future reread, not adoption.
Watch items preserve risk, not prohibition.
Current-position supports re-entry, not registry/index.
Worker capability is not permission.
```

## 4. Role Table

| Role name | Plain-language meaning | Primary function | Authority level | Can do | Must not become | Who can promote/change it | Example from current space | Common drift risk | Required guardrail |
|---|---|---|---|---|---|---|---|---|---|
| Philosophy | Deep reason and direction behind how the space thinks and operates | Give orientation and meaning | High orientation value | Help interpret why the space exists and what movement is desirable | Direct implementation command, schema, automation plan, or vague justification for any action | User, with ChatGPT validation if needed | Whole-space purpose language | Philosophy used to justify unscoped action | Translate into scoped principle/rule before action |
| Constitution / baseline | Highest stable operating authority when explicitly established | Protect non-negotiable constraints | Highest only when explicitly locked or approved by User | Override lower-level candidate materials when conflict exists | Casual sandbox output, local note, or generated authority | User explicitly | None created by this document | Candidate reference mistaken for baseline | No implicit baseline promotion |
| Principle | Direction for judgment | Explain why to read or decide a certain way | Interpretive unless explicitly promoted | Guide interpretation, review, and alignment | Automatic rule, policy, schema, workflow, or implementation instruction | User explicitly; ChatGPT can validate wording | Operating order principles | Principle becomes policy | Label as judgment direction |
| Rule | Scoped boundary about what may or may not happen | Constrain action | Binding only within declared scope | Prevent unsafe movement and clarify allowed/disallowed behavior | Broad architecture or global law by implication | User or explicit scoped instruction | no Package movement / no Run 117 approval | Rule becomes architecture | Always state scope |
| Operating 15 | Fifteen audit lenses for rereading the space | Detect drift and guide review | Review support / audit lens | Check whether an action violates operating attitude | Law, workflow, schema, ontology, task queue, source-space policy | User if promoted; otherwise remains audit support | `operating_order_principles_v0.md`, operating model | Audit lens becomes law | Keep as review lens |
| Sandbox principle | Local experimental attitude for sandbox work | Guide how sandbox experiments are interpreted | Sandbox-local candidate unless promoted | Help bound sandbox work and reduce unsafe promotion | Global project law or source-space policy | User explicitly | `operating_order_principles_v0.md` | Sandbox attitude becomes source-space law | Keep sandbox scope visible |
| Sandbox rule | Local operational constraint inside sandbox | Limit file movement, package promotion, worker authority, and experiment scope | Binding inside sandbox scope | Bind sandbox behavior when explicitly declared | Universal rule outside sandbox | User or explicit sandbox instruction | package movement boundaries | Local rule becomes global rule | Declare sandbox scope |
| Current-position entry | Latest place to re-enter the work | Tell next reader where the active state is | Orientation anchor | Preserve current state, latest anchor, next valid movement, and boundaries | Registry, official index, task queue, approval record, package movement trigger | User/Codex may update only when directed or clearly required | `current_position_entry_after_external_material_gate_v0.md` | Anchor becomes registry/index | Orientation only, not authority database |
| Process-memory | Memory of why things happened, stopped, changed, or stayed watch-only | Preserve judgment path | Memory/reference | Help future readers understand reasoning and reuse lessons | Official ledger, immutable law, single source of truth | User decides if memory becomes higher authority | agent-work-mem round as `PROCESS_MEMORY_LIGHT` | Memory becomes ledger | Preserve reasoning, separate authority |
| Run record | Trace of one bounded action, review, or stop | Record what was done and why | Trace / evidence record | Preserve provenance and judgment path | Approval, policy, package movement trigger, official ledger | User if converting into higher-level decision | `run_213` to `run_218` | Run existence becomes authority | Trace is not approval |
| Closeout note | Note that closes a bounded round | Mark what was closed, open, and not inferred | Round memory | Prevent accidental continuation or promotion | Permission to continue, approval, movement trigger | User decides next movement | `run_216_package_034_035_036_preflight_round_closeout.md` | Closeout becomes movement | Close does not promote |
| Next-chat re-entry summary | Compact handoff for a future chat/session | Reduce re-explanation burden | Handoff memory | Summarize latest anchor, closed rounds, open items, safe options | Official protocol, registry, index, task queue, source of truth | User/Codex when summary is requested | `next_chat_reentry_summary_after_package_preflight_round_v0.md` | Summary becomes task queue | Handoff only |
| Candidate reference | Useful material kept for possible future comparison | Support later reread or bounded review | Candidate-only | Provide examples, lessons, or comparison material | Approved design, adopted structure, package approval, implementation plan, baseline | User explicitly | Package 035 / Package 036 candidate references | Useful reference becomes approval | Mark candidate-only |
| Watch item | Risk signal to carry forward | Warn future readers about possible drift | Warning / review flag | Keep risks visible | Hard prohibition, policy, law, or automatic blocker unless User promotes it into rule | User explicitly | helper becoming automation | Watch becomes law | Risk flag only |
| External reference comparison | Way to read outside material without adopting it | Compare external material with our concepts | Comparison memory | Preserve inspiration and contrast | Adoption plan, protocol import, installation plan, authority source | User explicitly | `agent-work-mem` comparison | Reference becomes adoption | Inspiration-only unless approved |
| Package candidate | Bounded package material under review | Be inspected, held, or kept as candidate reference | Candidate package material | Support preflight or bounded review | Package movement, approval, implementation, transition target by implication | User explicitly | Package 034/035/036 preflight | Candidate becomes transition target | Review only unless approved |
| Package closeout | Package-level closure/status record | Preserve package outcome and boundaries | Package review trace | Say whether package material is held, candidate reference, or closed | Source-space promotion, package approval, implementation trigger | User explicitly | Package 035 closeout | Closeout becomes approval | Status is not movement |
| Reusable setting | Useful operating pattern that may be reused | Reduce repeated setup effort | Candidate reusable support | Help future rounds reuse a proven shape | Fixed template, mandatory workflow, automation, policy | User explicitly if hardened | `reusable_operating_settings_catalog_v0.md` | Shape becomes workflow | Copy shape, change details |
| Worker role boundary | Boundary saying what each worker may do in this round | Separate capability, role, and permission | Role guardrail | Keep User / ChatGPT / Codex / Gemini / CLI distinct | Formal permission system, autonomous routing, worker-to-worker authority | User controls final scope | role split in current-position entries | Capability becomes permission | User decision gate remains visible |
| User decision gate | User remains final controller | Prevent automatic promotion, approval, movement, escalation | Final decision | Approve, reject, select purpose, or stop | Hidden automation or delegated authority | User only | all "User = final control" records | User bypassed by agent confidence | No approval by inference |
| ChatGPT role | Direction, validation, interpretation, philosophy-check surface | Help User judge direction and detect drift | Advisor / validator | Prepare instructions, review outputs, explain meaning, protect boundaries | Autonomous implementer, package mover, source-space authority | User controls final decision | review/verdict turns | Validation becomes execution | Keep advisor/validator role |
| Codex role | Structuring, packaging, documentation, bounded review, edits only when explicitly instructed | Operate on files and produce structured records under scope | Worker under explicit scope | Read, summarize, compare, create run records, perform bounded edits when approved | Autonomous authority, self-scope expander, package approver, Gemini router, default implementation authority | User sets scope | run records / candidate docs | Structure becomes implementation | Do not self-promote |
| Gemini role | Read-heavy observer, executor, evidence collector when explicitly assigned | Perform token-heavy reading, observation, repeated checking | Observer/executor under explicit scope | Return observations and evidence | Verified truth source, final reviewer, autonomous designer, approval authority | User/Codex packet only when approved | Gemini bounded checks | Observation becomes proof | Evidence is not approval |
| CLI role | Optional execution tool | Run concrete commands when explicitly allowed | Tool only | Execute bounded operations | Automatic system owner, permission source, proof that execution is approved | User / scoped instruction | future CLI/tool boundary notes | Availability becomes permission | Capability is not permission |
| Four-line user-facing card | Simple user-facing thinking aid | Help User see current state, possible movement, risk, next judgment | Usage aid | Make space reading easier | Mandatory workflow, protocol, task queue, automation surface | User if hardened; otherwise aid only | `operating_model_user_facing_usage_flow_v0.md` | Card becomes workflow | Optional aid only |

## 5. Common Confusions to Avoid

```text
principle != policy
rule != architecture
Operating 15 != law
sandbox rule != source-space law
candidate reference != approval
watch item != prohibition
run record != authority
closeout != permission to continue
current-position != registry/index
next-chat summary != task queue
helper utility != official tool layer
handoff != routing
capability != permission
CLI availability != execution approval
Gemini observation != verified truth
Codex review != implementation authority
four-line card != workflow
```

## 6. How Workers Should Use This Document

### ChatGPT

```text
Use this document to detect role drift and explain the current state to the User.
Do not treat candidate references as approval.
Do not collapse watch items into hard law.
```

### Codex

```text
Read this document before creating or reviewing sandbox records.
When creating outputs, label whether material is principle, rule, candidate reference, watch item, run record, closeout, or current-position.
Do not promote materials without explicit User decision.
```

### Gemini

```text
Use this document to understand observation scope.
Return evidence and uncertainty.
Do not treat observations as verified truth or approval.
```

### CLI

```text
CLI executes only explicit bounded commands.
Tool availability is not permission.
Do not infer execution approval from role/capability language.
```

## 7. Reread of Current Space

| Item | Correct role | Current status | Main drift risk | Guardrail | Action |
|---|---|---|---|---|---|
| agent-work-mem comparison | external reference comparison | closed as process-memory light | adoption / protocol import | inspiration-only, no installation | `KEEP_AS_CANDIDATE_REFERENCE` |
| append-only trace discipline | inspiration-only process-memory lesson | preserved as narrow inspiration | process-memory becomes ledger or correction blocked | preserve judgment path without hard law | `WATCH_ONLY` |
| explicit handoff file | inspiration-only handoff lesson | preserved with watch | handoff becomes approval/routing | separate handoff from permission | `WATCH_ONLY` |
| agent identity / capability declaration | role-boundary inspiration | preserved with watch | capability becomes permission | keep User decision gate visible | `WATCH_ONLY` |
| Package 035 | candidate reference | `SAFE_WITH_WATCH / KEEP_AS_CANDIDATE_REFERENCE` | helper becomes workflow/automation/tool layer | bounded helper reference only | `KEEP_AS_CANDIDATE_REFERENCE` |
| Package 036 | candidate reference / audit support | `SAFE_WITH_WATCH / KEEP_AS_CANDIDATE_REFERENCE` | principle becomes policy, interface language becomes schema/law | audit support only | `KEEP_AS_CANDIDATE_REFERENCE` |
| Package 034 | package candidate source unknown | `HOLD_AS_SOURCE_UNKNOWN` | Run 034 inferred as Package 034 | require explicit Package 034 source | `HOLD` |
| Operating 15 | audit lenses | candidate review support | law/workflow/schema drift | audit lens only | `WATCH_ONLY` |
| four-line card | user-facing usage aid | usable with watch | mandatory workflow/protocol | optional aid only | `WATCH_ONLY` |
| current-position | re-entry anchor | latest anchor remains external material gate entry | registry/index/task queue drift | orientation anchor only | `KEEP_AS_IS` |
| next-chat summaries | handoff memory | prepared for agent-work-mem and package preflight rounds | task queue / approval drift | summary is not movement | `KEEP_AS_IS` |
| run records | provenance trace | preserve bounded reviews and closeouts | run existence becomes authority | trace is not approval | `WATCH_ONLY` |
| watch items | risk flags | carried across rounds | warning becomes hard law | User must promote before rule status | `CLARIFY_WORDING_LATER` |

## 8. Promotion Rule

```text
Nothing in this document promotes any material.
Promotion requires explicit User decision.
A candidate reference does not become a rule because it is useful.
A watch item does not become law because it is repeated.
A run record does not become authority because it exists.
A helper does not become workflow because it reduces friction.
A principle does not become policy because it sounds correct.
```

## 9. Current-Position Decision

```text
NO_CURRENT_POSITION_UPDATE_REQUIRED
```

Reason:

```text
This document clarifies role interpretation but does not change the latest anchor, move packages, approve packages, approve Run 117, or create a new operating authority.
```

## 10. Recommendation

```text
KEEP_AS_ROLE_REFERENCE_CANDIDATE
```

Reason:

```text
The document is useful as an agent-readable role reference candidate. It should be reviewed by User/ChatGPT before any later decision about baseline/reference promotion.
```

## 11. Boundary Confirmation

```text
no baseline promotion
no official workflow creation
no architecture finalization
no source-space policy creation
no interface schema creation
no automation/router/controller
no registry/index/ledger promotion
no formal permission system
no Package 034/035/036 movement
no Package approval
no Run 117 approval
no Gemini broad run
no Codex implementation authority
no current-position update unless explicitly required
```

`STATUS: SPACE_ROLES_REFERENCE_CANDIDATE_PREPARED`
