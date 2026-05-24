# Gemini Lite Output Contract v0

## 1. Verdict

```text
GEMINI_LITE_OUTPUT_CONTRACT_V0_DRAFTED_AS_TEMPLATE_ONLY_WITH_REAL_GEMINI_HOLD
```

## 2. Status

```text
status: lite_output_contract_candidate
authority: sandbox-local candidate
scope: bounded Gemini/script-lens output for Codex recovery
execution_status: template only
promotion_status: no promotion
```

This is not a Gemini execution request.
This is not a model API transport approval.
This is not a truth schema, registry, ontology, workflow, baseline, or component.

## 3. Purpose

Define the compact output shape Gemini or a Gemini-like script lens should produce so Codex can perform recovery without rereading the entire raw output by default.

Core rule:

```text
Gemini lite output is evidence for Codex recovery, not truth.
```

## 4. Required JSON Shape

```json
{
  "format": "GEMINI_BULK_REVIEW_LITE_V0",
  "status": "draft | returned_with_watch | stopped",
  "request_id": "[request id]",
  "source_scope": "[declared files/assets only]",
  "observed_files": [
    {
      "path": "[exact path or label]",
      "chars": 0,
      "lines": 0,
      "role": "source | packet | prior_report | receipt | other"
    }
  ],
  "repeated_patterns": [
    {
      "pattern": "[short pattern]",
      "evidence": ["[file/line/label]"],
      "confidence": "low | medium | high"
    }
  ],
  "candidate_items": [
    {
      "item": "[candidate only]",
      "why_candidate": "[reason]",
      "not_component_because": "[reason]"
    }
  ],
  "uncertainties": [
    "[unknown or evidence gap]"
  ],
  "possible_risks": [
    "[risk]"
  ],
  "questions_for_codex": [
    "[question Codex should resolve]"
  ],
  "do_not_promote": [
    "[what must not be promoted]"
  ],
  "negative_evidence": {
    "promotion_claimed": false,
    "component_approval_claimed": false,
    "workflow_schema_registry_ontology_baseline_claimed": false,
    "truth_claimed": false,
    "live_web_source_lookup_used": false,
    "external_connector_used": false,
    "memory_skill_cron_config_instruction_present": false
  },
  "receipt_conflict_check": {
    "receipt_path": "[exact path or none]",
    "conflicts_with_receipt": false,
    "conflict_items": ["[field or claim that conflicts]"],
    "conflict_resolution_required_by_codex": false
  },
  "raw_audit_trigger": {
    "required": false,
    "reasons": ["missing_required_field | over_promotion_language | receipt_conflict | uncertainty | user_requested_raw_audit"]
  },
  "raw_limits": [
    "[scope limitation]"
  ],
  "stop_flags": [
    "[STOP condition if any]"
  ]
}
```

## 5. Required Semantics

The lite output must include:

```text
scope evidence
pattern summary
candidate-only items
uncertainties
risks
questions for Codex
explicit do-not-promote lines
field-level negative evidence for no-promotion / no-truth / no-component claims
receipt conflict check when a receipt is provided
raw audit trigger and reasons
raw limitations
```

The lite output must not include:

```text
official truth claims
component approval
workflow approval
schema/registry/ontology language
baseline language
memory/skill/config/cron instructions
external connector instructions
promotion requests
```

## 6. Codex Recovery Expectations

Codex should use this lite output to:

```text
confirm scope
confirm output shape
filter over-promotion language
restore WATCH/HOLD
classify recovery hint
identify next smallest action
```

Codex should open raw output only when:

```text
lite output is missing required fields
lite output contains over-promotion language
lite output conflicts with receipt
negative_evidence is missing or internally inconsistent
raw_audit_trigger.required is true
uncertainty requires audit
user explicitly asks for raw audit
```

## 7. WATCH

```text
lite output becoming truth
candidate_items becoming component
confidence being mistaken for approval
questions_for_codex being skipped
raw output never being audited when needed
negative_evidence omitted or contradicted by prose
receipt conflict being ignored
model API transport being confused with live web/source lookup
```

## 8. HOLD

```text
real Gemini execution
model API transport
live web/source lookup
external connector
promotion
```
