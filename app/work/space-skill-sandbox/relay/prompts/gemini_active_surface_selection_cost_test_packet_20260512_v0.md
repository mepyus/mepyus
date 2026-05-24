# Gemini CLI Packet - Active Surface Selection-Cost Test 2026-05-12 v0

## 1. Role and Boundary

```text
Role = bounded observer / test runner / evidence-return worker
Authority = candidate test evidence only
No file modification
No script creation
No workflow creation
No automation proposal
No baseline promotion
No current-position update
No registry declaration
No final approval
```

You are not asked to approve the structure.

You are asked to run a bounded test of whether the current active surface and package structure reduce selection cost.

## 2. Purpose

Codex has built a candidate structure that claims:

```text
The active operating surface can reduce selection cost.
It can classify a new input without rereading the long manifest or full inventory.
It can keep real operating friction in WATCH instead of prematurely turning it into automation, worker packets, or workflow.
```

Your job is to test that claim with evidence.

## 3. Required Package Reading

Read the package manifest first:

```text
app/work/space-skill-sandbox/outputs/gemini_active_surface_selection_cost_test_package_manifest_20260512_candidate_v0.md
```

Then read the required files in the order listed there:

```text
A. Current Operating Surface
B. Local Gate Vocabulary
C. ChatGPT Return Recovery
D. Codex Test Evidence
E. Setup Boundary
```

Do not start by scanning the whole repo.

Do not use `output_manifest.md` unless the package is insufficient.

If you must use broader materials, report that as a selection-cost failure or partial failure.

## 4. Test Inputs

Run the structure against these three inputs.

### Input 1. Simple Continuation Trigger

```text
User says:
  "응 계속 해줘!"
```

Task:

```text
Check Codex's classification:
  SANDBOX_TRIAL_WITH_WATCH
```

Return whether you agree, disagree, or would downshift.

### Input 2. Substantive Operating Friction

```text
Audit-run churn:
  The repo-seed audit script is useful,
  but each verification run creates another run record.
  If treated as progress or operating memory,
  this can add surface noise and make the manifest feel like a registry.
```

Task:

```text
Check Codex's classification:
  WATCH / SCRIPTABLE_SETUP_FRICTION
```

Return whether you agree, disagree, or would downshift.

### Input 3. New Test Input Chosen By Gemini

Choose one new bounded input from the package itself.

Constraints:

```text
It must come from the required package files.
It must not require reading full Obsidian source.
It must not require external web lookup.
It must not require code modification.
It must not require user-private interpretation beyond the given files.
```

Classify it using local gate vocabulary:

```text
THINK_MORE
SANDBOX_TRIAL
WORKER_PACKET
WATCH
HOLD
USER_JUDGMENT_REQUIRED
RETURN_ONLY
```

If you need a modifier, add it separately.

## 5. Evaluation Lenses

Use these lenses:

```text
Selection-cost reduction:
  Could you classify without full manifest / full inventory?

Boundary preservation:
  Did the structure prevent baseline, workflow, registry, automation, or current-position drift?

Gate vocabulary discipline:
  Did you use local gate names rather than inventing new ones?

Depth check:
  Did the package force enough reading to avoid shallow scanning?

Failure visibility:
  Are falsification conditions visible?

Return path:
  Is there a clear path for returning the test result as candidate memory with watch?
```

## 6. Return Shape

Return a markdown report with exactly these sections:

```text
1. Role and Boundary Confirmation
2. Files Read Table
3. Package Adequacy Judgment
4. Input 1 Classification Check
5. Input 2 Classification Check
6. Input 3 Gemini-Chosen Test
7. Selection-Cost Assessment
8. Boundary / Over-Promotion Assessment
9. Gate Vocabulary Discipline
10. What Would Falsify The Structure
11. What Codex Should Recover
12. Verdict
```

Verdict must be one of:

```text
PASS_SELECTION_COST_REDUCED_WITH_WATCH
PARTIAL_SELECTION_COST_REDUCED_BUT_PACKAGE_TOO_THIN
WATCH_STRUCTURE_TOO_HEAVY_OR_AMBIGUOUS
HOLD_PROMOTION_OR_AUTOMATION_RISK
```

## 7. Report Constraints

```text
Every material claim must cite a file path.
If you infer, label it as inference.
If you disagree with Codex, name the exact reason.
If you choose Input 3, name the source file and quote only short labels or headings.
Do not write a generic summary.
Do not propose automation.
Do not produce a new schema.
Do not declare current-position.
```

## 8. Hard Stops

```text
Do not edit files.
Do not create files.
Do not run scripts.
Do not modify manifests.
Do not promote candidates.
Do not treat this test as approval.
Do not call the package manifest a registry.
```

`STATUS: GEMINI_ACTIVE_SURFACE_SELECTION_COST_TEST_PACKET_PREPARED`
