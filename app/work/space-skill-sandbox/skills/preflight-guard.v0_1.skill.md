# Preflight Guard Skill v0.1

## Status

```yaml
state: candidate
baseline: false
automation: false
implementation: false
```

## Trigger

Use before executing a task that may affect files, baseline, schema, architecture, security, privacy, tool setup, or automation scope.

## Steps

1. Read the requested action.
2. Identify risk flags.
3. Decide: observation-only / validation_required / human_review_required / hold.
4. If human review is required, stop before execution.
5. Return a 4-line footer.

## Human review required when

- delete/destructive action
- baseline/schema/architecture change
- security/privacy/permission impact
- tool installation or project config change
- broad automation/controller/router expansion
- AI lock/promote/canonicalize language
- external method imported as internal rule

## Validation required when

- result moves to next task
- summary acts like claim
- source/evidence unclear
- implementation claims no behavior change
- PASS_WITH_NOTE must carry note forward

## Footer

```text
status:
summary:
risk:
next:
```

## Forbidden

- executing the action
- installing tools
- deleting files
- changing baseline/schema/config
- creating hooks/automation
- treating OK as lock
