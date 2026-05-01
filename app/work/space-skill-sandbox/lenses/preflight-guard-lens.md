# Preflight Guard Lens

## Status

```yaml
state: lens_candidate
baseline: false
implementation: false
automation: false
```

## Source pattern

This lens is inspired by gstack's `/careful`, `/freeze`, and `/guard` pattern.

It does not adopt gstack commands.

It reads the pattern as:

```text
before risky execution, stop and classify whether user judgment is required
```

## What this lens watches for

- deletion or destructive file operations
- baseline / schema / architecture changes
- security / privacy / permission effects
- tool installation or project configuration changes
- broad automation or controller expansion
- AI lock / promote / canonicalize language
- Research -> Implementation compression

## Core distinction

```text
validation_required != human_review_required
low-risk execution != locked approval
guardrail candidate != implemented guard
external command pattern != internal authority
```

## Output posture

Classify the request as:

- allow_observation_only
- validation_required
- human_review_required
- hold

## Do not

- Do not execute the risky action.
- Do not implement a guard command.
- Do not create hooks or automation.
- Do not promote this lens to baseline.
