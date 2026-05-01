# Worker Guide v0.1

## Status

```yaml
state: guide_candidate
baseline: false
automation: false
```

## Use

Read this before a sandbox run.

Use one skill only.

## Available candidate skills

```text
external_material_intake:
  use_when: one external material should be read against space criteria
  file: skills/external-material-intake.v0_1.skill.md

preflight_guard:
  use_when: a task may affect files, baseline, schema, architecture, security, privacy, tool setup, or automation scope
  file: skills/preflight-guard.v0_1.skill.md
```

## Selection rules

- External URL/material -> `external_material_intake`
- Delete / baseline / schema / architecture / tool install / security / privacy / automation expansion -> `preflight_guard`
- Low-risk read-only status check -> observation-only; no skill needed unless user asks for a report
- If unsure whether user authority is needed -> `preflight_guard`

## General rules

1. Do not read the whole Deep Space.
2. Use at most two internal references.
3. Do not implement unless the selected task explicitly allows implementation.
4. Do not install tools or change project config.
5. Do not create schema, automation, hook, MCP, or baseline.
6. Separate useful value from adoption.
7. Treat summary without evidence as a claim.
8. Return a 4-line footer.

## Footer

```text
status:
summary:
risk:
next:
```

## Status choices

```text
완료
검증 필요
사용자 판단 필요
보류
```

## Human review boundary

Escalate to user judgment when:

- baseline/schema/architecture changes appear
- delete/destructive action appears
- tool installation or project config change appears
- hook/MCP/automation expansion appears
- security/privacy/permission impact appears
- external method is being imported as rule

## Do not

- Do not treat this guide as baseline.
- Do not add commands or automation.
- Do not update source-space docs.
- Do not promote candidate skills without review.
