# Integrated Engine Process Lens Registry v0

## 1. Status

Status: working registry, sample-grounded where noted.

This registry separates process skeleton from lens variation.
It does not claim all lenses are equally validated.

## 2. Lens Principle

The process camera skeleton stays stable:

```text
intake -> scope -> discover -> compare -> evidence -> gate -> decision -> packet -> return
```

The lens changes what the process emphasizes when reading a target object.

Lens changes:

- what evidence is foregrounded
- what fit means
- what risk is checked first
- what expected return shape is suitable

Lens does not change:

- status locks
- authority boundaries
- need for evidence
- validation gate requirement
- return record requirement

## 3. Process Lenses

| lens | role | what it changes | what it does not change | target types | grounding |
|---|---|---|---|---|---|
| evidence lens | foreground source trace and grounding sufficiency | asks whether evidence bundle is enough | does not decide promotion | review note, asset selection, line candidate, instruction support | sample-grounded through `base_content_trace` validation |
| compatibility lens | foreground fit between target and frame/template/camera | asks whether a candidate fits directly / weakly / not yet | does not make weak fit strong | camera, lens, review guideline, reusable asset | sample-grounded through shadow-fit cycle |
| boundary lens | foreground what is excluded and what must not be inferred | strengthens authority and scope limits | does not create new target object | all candidate handling targets | sample-grounded through `what_this_is_not` and status locks |
| rollback lens | foreground invalid shape, forcing, hidden partial/missing, promotion drift | decides where to stop or hold | does not create standalone rollback protocol | review note, rollback rule asset, procedure, validation gate | sample-grounded inside review-stage |
| reuse lens | foreground whether structure travels across target roles | separates original-note strength from adjacency weakness | does not authorize rollout | candidate review, template fit, process asset extraction | sample-grounded through three shadow-fits |
| implementation lens | foreground whether a bounded action packet can be formed | asks if worker can act without full chat reread | does not implement UI or automation | CLI/sub-agent tasks, worker packets | provisional; derived in this package |
| comparison lens | foreground candidate set and selection/rejection reasons | improves candidate discovery and selection | does not widen scan without guard | candidate discovery, asset selection, shadow-fit target choice | sample-grounded through candidate scans |

## 4. Lens Use Rules

- Pick one primary lens.
- Add supporting lenses only when needed.
- Mark each lens as sample-grounded or provisional.
- If lens choice depends on name appeal rather than target need, hold.
- If lens changes authority boundary, stop.

## 5. Sample-Grounded vs Provisional

Sample-grounded:

- evidence lens
- compatibility lens
- boundary lens
- rollback lens
- reuse lens
- comparison lens

Provisional:

- implementation lens

Reason:

- implementation lens is needed for packetization but has not yet been exercised on a live CLI/sub-agent run in this process-camera package.

## 6. Phase 2 Validation

Fake universality check:

- registry does not claim all lenses are validated equally

Skeleton separation check:

- lenses modify reading emphasis, not process stages or authority boundaries

