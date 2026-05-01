# External Material Intake Skill v0.1

## Status

```yaml
state: candidate
baseline: false
automation: false
```

## Trigger

Use for one external material.

## Steps

1. Read the material's problem, structure, flow, assumptions, and risks.
2. Reference at most two internal criteria.
3. Classify: Same / Similar but dangerous / Different / Borrow later / Reject for now.
4. Make one tiny translation or dry-run example.
5. Self-check for implementation drift and external authority bias.
6. Return a 4-line footer.

## Required output

```text
material:
internal_refs:
same:
similar_but_dangerous:
different:
borrow_later:
reject_for_now:
tiny_dry_run:
self_check:
footer:
  status:
  summary:
  risk:
  next:
```

## Forbidden

- implementation
- file changes outside sandbox
- baseline/schema/automation
- tool adoption mandate
- hook/MCP/watch mode
- whole-space processing
