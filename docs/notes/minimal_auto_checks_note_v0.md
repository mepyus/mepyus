# minimal auto checks note v0

## 1. Purpose

This note records the smallest automatic checks that can be attached immediately without building a new evaluation platform.

## 2. Principles

- Do not build a new evaluation framework.
- Do not move into a generic CI platform design.
- Only automate checks that can be judged as present or absent.
- Start as a warning device, not as the final PASS judge.

## 3. Minimum auto checks

### 3.1 trace_completeness_check

Targets:

- phase decision log
- hold log
- rejection log

Checks:

- required fields exist
- fields that must not be empty are present
- allowed log types are respected

### 3.2 manual_assignment_guard

Targets:

- phase state
- decision apply path

Checks:

- direct state assignment patterns
- setter presence
- forbidden mutable access traces

### 3.3 allowed_types_compliance

Targets:

- phase decision log
- rejection log

Checks:

- whether an unapproved log type is written

## 4. Simple example helpers

```python
def verify_required_fields(entry: dict, required: list[str]) -> list[str]:
    errors = []
    for field in required:
        if field not in entry or entry[field] in ("", None, []):
            errors.append(f"missing required field: {field}")
    return errors
```

```python
ALLOWED_PHASE_LOG_TYPES = {
    "phase_decision",
    "hold_entered",
    "hold_reviewed",
}

ALLOWED_REJECTION_LOG_TYPES = {
    "rejection_entered",
    "rejection_reviewed",
    "rejection_reopened",
}
```

## 5. What not to automate

- final intent fidelity judgment
- final structural responsibility judgment
- final baseline spirit judgment
- final generic drift judgment

Those remain with the supervisor.

## 6. One-line conclusion

> The current automation layer should only do minimal structure-violation detection and trace preservation checks, while intent-fit and direction judgment remain with the supervisory layer.
