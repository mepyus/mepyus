# Integrated Engine External Analysis Lens Fragment Inventory v0

## 1. Verdict

PASS_WITH_NOTE

`gemini/external_analysis` contains useful lens material, but it should be treated as a precedent pool, not an implementation source and not a final lens registry.

Current status:

```text
lens fragments identified
not promoted
not canonical
not implementation-authorizing
```

## 2. Source Scope

Read source folder:

- `gemini/external_analysis/`

Files read:

- `agent_skills_dna_20260415.md`
- `autoresearch_dna_20260415.md`
- `claude_code_dna_20260415.md`
- `claude_code_v2_dna_20260415.md`
- `openclaw_dna_20260415.md`
- `openharness_structural_dna_20260415.md`
- `openharness_study_20260415.md`
- `paperclip_dna_20260415.md`
- `qmd_dna_20260415.md`
- `ralph_dna_20260415.md`

## 3. Reading Rule

Use this folder as:

```text
external precedent source -> lens fragment mining -> internal fit check -> hold / vary / reuse
```

Do not use it as:

```text
external feature -> direct adoption -> implementation instruction
```

## 4. Lens Fragment Inventory

| id | working lens fragment | source files | what it reads | useful for | current status |
| --- | --- | --- | --- | --- | --- |
| LF01 | Contract Lens | `openclaw_dna`, `openharness_structural_dna` | What contract an object must satisfy before it can touch engine/packet/control layers | bridge contract, CLI adapter, process camera, packet readiness | hold / usable fragment |
| LF02 | Envelope Lens | `openclaw_dna` | How raw input becomes normalized engine-readable material | lower input organ, source manifest, label packet, upper packet input | hold / strong fragment |
| LF03 | Compliance Lens | `claude_code_dna`, `agent_skills_dna` | Whether a rule is testable and followed, not just stated | stop rules, checklist, camera review validation, anti-pattern control | hold / strong fragment |
| LF04 | Memory / Progress Lens | `ralph_dna`, `openharness_study`, `autoresearch_dna` | What is retained from attempts, failures, and decisions | worklog, return record, redeposit, local wisdom | hold / strong fragment |
| LF05 | Bounded Loop Lens | `autoresearch_dna`, `ralph_dna`, `qmd_dna` | Whether iteration has budget, checkpoint, stop condition, and completion signal | language loop, probe loop, bridge maturation, internal reread loop | hold / usable fragment |
| LF06 | Segmentation / Chunking Lens | `qmd_dna` | Where input should be cut by semantic structure rather than token count | lower split units, line evidence, reading segment structure | hold / strong fragment |
| LF07 | Inbox / Decision Surface Lens | `paperclip_dna` | What belongs on user decision surface vs internal trace surface | User surface, internal team assignment, pending work, approval/hold | hold / strong fragment |
| LF08 | Adapter / Provider Lens | `paperclip_dna`, `openclaw_dna` | Whether tools/backends sit behind a stable interface | Codex/Gemini CLI adapter, provider registry, VectorFL host | hold / usable fragment |
| LF09 | Permission / Governance Lens | `openharness_structural_dna`, `agent_skills_dna` | What action is allowed, denied, or requires confirmation, and why | authority boundary, user decision, protected zones, no-promotion guards | hold / strong fragment |
| LF10 | Persona / Role Lens | `claude_code_v2_dna`, `ralph_dna`, `paperclip_dna` | Which role/camera should read a task and with what responsibility | internal teams, language 담당, reviewer/executor split, handoff | hold / usable fragment |

## 5. Fragment Notes

### LF01 Contract Lens

- Core question: What does this object have to satisfy before it may be consumed?
- Strong fit: lower-to-upper bridge control contract, execution packet schema.
- Misread risk: turning every useful pattern into a rigid global protocol.
- Hold reason: needs internal fit trials before becoming a named working lens.

### LF02 Envelope Lens

- Core question: What wrapper gives raw input source, actor, context, boundary, and route?
- Strong fit: lower input output bundle and upper packet input.
- Misread risk: treating envelope as meaning extraction.
- Hold reason: useful now, but not yet tested across multiple internal input types.

### LF03 Compliance Lens

- Core question: How do we know the rule was followed?
- Strong fit: checklist, stop rule, validation gate.
- Misread risk: compliance theater, where checklists exist but are not evidence-led.
- Hold reason: should be paired with actual validation examples.

### LF04 Memory / Progress Lens

- Core question: What from this attempt becomes future-readable?
- Strong fit: worklogs, closeouts, failed probe records, return records.
- Misread risk: logging everything without deciding what is reusable.
- Hold reason: needs redeposit criteria before stronger promotion.

### LF05 Bounded Loop Lens

- Core question: What allows the loop to continue, and what stops it?
- Strong fit: language loop and probe cycles.
- Misread risk: automatic looping without clear stop condition.
- Hold reason: must be tied to bounded run control before automation.

### LF06 Segmentation / Chunking Lens

- Core question: What boundary is meaningful enough to become a unit?
- Strong fit: lower input split units and line evidence.
- Misread risk: split unit becomes line artifact too early.
- Hold reason: ready as reading lens, not as line-promotion lens.

### LF07 Inbox / Decision Surface Lens

- Core question: What does the user actually need to decide?
- Strong fit: User surface redesign, internal team/담당 assignment, pending decisions.
- Misread risk: making another dashboard of everything.
- Hold reason: should be applied with surface separation rules.

### LF08 Adapter / Provider Lens

- Core question: Is this backend hidden behind a stable interface?
- Strong fit: Codex/Gemini CLI host and provider boundary.
- Misread risk: generic plugin framework too early.
- Hold reason: useful after first bounded CLI-host path stabilizes.

### LF09 Permission / Governance Lens

- Core question: Who allowed this action, under what reason and boundary?
- Strong fit: authority state, protected baseline, no-canonicalization, no-promotion.
- Misread risk: permissions become abstract policy instead of per-action decision.
- Hold reason: needs decision-object style internal fit.

### LF10 Persona / Role Lens

- Core question: Which role should read this, and what must that role not do?
- Strong fit: internal team structure and role-specific work assignment.
- Misread risk: role names without responsibility, activation condition, or anti-pattern.
- Hold reason: should be tied to task routing / surface projection.

## 6. Candidate Grouping

### Strongest Near-Term Lens Fragments

- LF02 Envelope Lens
- LF03 Compliance Lens
- LF06 Segmentation / Chunking Lens
- LF07 Inbox / Decision Surface Lens
- LF09 Permission / Governance Lens

These directly match current lower-input, bridge, and surface-division work.

### Useful But Needs More Internal Trial

- LF01 Contract Lens
- LF04 Memory / Progress Lens
- LF05 Bounded Loop Lens
- LF08 Adapter / Provider Lens
- LF10 Persona / Role Lens

These are valuable, but need bounded internal application before stronger status.

## 7. What This Inventory Is Not

This is not:

- final lens registry
- external feature adoption list
- implementation roadmap
- UI redesign instruction
- automation permission
- glossary
- canonical engine language

## 8. Recommended Next Use

Use this inventory as a precedent source when opening a bounded internal lens trial.

Safest next action:

```text
run one internal lens fit trial using one fragment, preferably Envelope Lens or Inbox / Decision Surface Lens
```

Reason:

- both have immediate relevance
- both can be tested against existing lower input / surface assets
- neither requires implementation or external adoption

## 9. Validation

- External adoption block: passed. Source patterns are kept as fragments.
- Lens promotion block: passed. No lens is marked final or canonical.
- Internal fit requirement: passed. Each fragment requires hold/reuse/variation decision before stronger use.

