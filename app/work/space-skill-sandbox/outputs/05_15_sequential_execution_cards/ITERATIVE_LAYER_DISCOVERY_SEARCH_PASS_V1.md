# Iterative Layer Discovery Search Pass v1
# 05-15 Candidate Adapter Surfaces

## 1. Status

Status:
  ITERATIVE_LAYER_DISCOVERY_SEARCH_PASS_V1_COMPLETED_WITH_WATCH

Purpose:
  Continue the search/filter cycle using the revised layer model as the search criterion.

Previous basis:
  `ITERATIVE_LAYER_DISCOVERY_SEARCH_PASS_V0.md`

Boundary:
  Discovery material only.
  Not baseline, workflow, schema, registry, ontology, automation, eval infrastructure, AGENTS.md instruction, SKILL.md, current-position update, or output_manifest update.

## 2. Revised criterion being tested

From v0:

```text
(0<->1) + 2 + [3/4 gate] + 5 + 6
with 7 held
and 8/9 used when frame shift reveals different meaning
```

Question for this pass:

```text
Does this structure survive when searched against:
  sensemaking / data-frame theory
  safety-critical threat/error management
  incident severity and postmortem practice
```

## 3. Search cycle 4 — data/frame sensemaking

Search focus:

```text
data-frame theory
frame/data co-evolution
plausibility judgment
anomaly
frame revision
AI-assisted decision making
```

Sources inspected:

- Frontiers, plausibility transition model for sensemaking:
  https://www.frontiersin.org/articles/10.3389/fpsyg.2023.1160132/full
- UCL Discovery, empirical test of Data-Frame theory:
  https://discovery.ucl.ac.uk/id/eprint/1464567/
- Sensemaking / data-frame search results

What survived filtering:

```text
existing frame can become inadequate
anomalies trigger questioning
plausibility judgments test whether a story/frame still fits
data quality matters
reframing may seek a new frame
frame and data shape each other
```

Layer implication:

```text
0<->1 is confirmed:
  observation and frame are mutually shaping, not linear.

2 is strengthened:
  evidence is not just source citation; it includes data quality and plausibility.

8/9 are strengthened:
  reframing is the operation, and meaning delta is the value of the operation.
```

Correction:
  Add `plausibility` as a quality of 2/8/9, not as a new digit.

## 4. Search cycle 5 — safety-critical threat/error management

Search focus:

```text
threat and error management
crew resource management
avoid trap mitigate
identify error
take corrective action
check effectiveness
situation recognition
```

Sources inspected:

- SKYbrary / aviation threat and error management material:
  https://skybrary.aero/sites/default/files/bookshelf/3602.pdf
- Threat/Error Management and Crew Resource Management search results

What survived filtering:

```text
identify situations that could lead to errors
avoid conditions that promote errors
identify/trap errors
take corrective action
check effectiveness
situation recognition failures are dangerous
rules and procedures trap residual errors
```

Layer implication:

```text
0<->1:
  situation recognition is a frame problem.

3:
  boundary/control/checklist can trap errors before they become harm.

5:
  corrective action must be specific.

6:
  check effectiveness is explicit and unavoidable.

8/9:
  "what we think the situation is" vs "actual situation" is a layer/delta problem.
```

Correction:
  `3 boundary` is not just a prohibition.
  It is also an error-trap surface.

## 5. Search cycle 6 — incident severity / postmortem

Search focus:

```text
incident severity
impact urgency matrix
incident commander
communication lead
postmortem
follow-up actions
blameless learning
```

Sources inspected:

- Giva, incident severity matrix:
  https://www.givainc.com/blog/incident-severity-levels/
- Atlassian, incident postmortems:
  https://www.atlassian.com/incident-management/handbook/postmortems
- Google SRE incident management guide:
  https://sre.google/resources/practices-and-processes/incident-management-guide/
- ITIL incident priority matrix search results

What survived filtering:

```text
impact and urgency must be assessed independently
severity is a combination, not an emotion
assign/document reasoning
clear roles are needed during action
communication is separate from technical mitigation
postmortem records impact, actions, root cause, follow-up
follow-up actions need owners and completion tracking
learning should be blameless and system-focused
```

Layer implication:

```text
0:
  incident signal / alert / customer report

1:
  severity frame, but only after separating inputs

2:
  impact evidence, urgency evidence, affected users, workaround, security/data risk

3:
  severity threshold and hard boundaries

4:
  incident commander, communications lead, owner, approver

5:
  mitigation / communication / workaround

6:
  postmortem, action tracking, outcome verification

7:
  recurring postmortem trends may become process changes, but only explicitly

8/9:
  "feels urgent" vs "high impact" reveals classification delta
```

Correction:
  Split some digit readings into paired axes when needed.

Examples:

```text
severity:
  impact + urgency

customer response:
  emotion + authority

tool use:
  task + permission

content:
  claim + evidence
```

## 6. What changed from v0

v0 model:

```text
(0<->1) + 2 + [3/4 gate] + 5 + 6
with 7 held
and 8/9 used when frame shift reveals different meaning
```

v1 keeps this, but adds:

```text
2 includes:
  evidence quality + plausibility

3 includes:
  boundary + trap/control/checklist

4 includes:
  decision owner + role separation + communication owner where relevant

6 includes:
  effectiveness check + postmortem/follow-up tracking where relevant

8/9 includes:
  not just different reading, but mismatch between perceived situation and actual/grounded situation
```

## 7. Refined model v1

```text
(0<->1)
  observe/frame loop
  preserve arrival layer
  detect anomalies

2
  evidence quality
  plausibility
  source/ground truth

3
  boundary
  trap/control/checklist
  auto-fail where necessary

4
  authority
  role/owner
  escalation/communication split

5
  smallest safe action
  corrective action / mitigation / draft / rewrite

6
  effectiveness check
  follow-up owner
  postmortem or learning loop when triggered

7
  promotion/memory/process change
  explicit HOLD unless approved

8/9
  lens shift + meaning delta
  especially where perceived situation differs from grounded situation
```

## 8. Implication for adapter work

The system should not grow by adding more card types first.

It should grow by testing whether an input needs:

```text
basic read:
  0,1,5

grounded review:
  0,1,2,5

risk/authority review:
  0,1,2,3,4,5

learning loop:
  0,1,2,3,4,5,6

promotion question:
  7 appears, stop

layer-shift question:
  8/9 appears, record delta before action
```

## 9. Best next stress test

The best next test is no longer only customer refund response.

A stronger test is:

```text
Operational Exception Triage

Input:
  "A customer says checkout failed twice, support says it is only one account,
   but three more tickets arrive in 10 minutes and a manager asks for urgent refund promises."

Why:
  This forces:
    0<->1 situation recognition
    2 evidence quality
    3 trap/boundary
    4 authority/owner/communication split
    5 mitigation
    6 follow-up
    8/9 perceived vs actual severity delta
```

Do not create an official triage card yet.
Run it as a sandbox-local stress test first.

## 10. Hard stop confirmation

```text
no AGENTS.md update
no SKILL.md creation
no eval creation
no automation script
no current-position update
no output_manifest update
no baseline promotion
no workflow/schema/registry/ontology creation
no external dispatch
no platform/API/browser/account/credential action
no official customer-service policy
no refund/SLA/legal authority
```

`STATUS: ITERATIVE_LAYER_DISCOVERY_SEARCH_PASS_V1_COMPLETED_WITH_WATCH`
