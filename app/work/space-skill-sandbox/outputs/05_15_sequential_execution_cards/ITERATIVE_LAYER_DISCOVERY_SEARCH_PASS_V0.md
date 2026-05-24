# Iterative Layer Discovery Search Pass v0
# 05-15 Candidate Adapter Surfaces

## 1. Status

Status:
  ITERATIVE_LAYER_DISCOVERY_SEARCH_PASS_COMPLETED_WITH_WATCH

Purpose:
  Test the current layer/digit hypothesis through repeated search, filtering, and rereading.

Boundary:
  This is discovery material only.
  It is not baseline, workflow, schema, registry, ontology, automation, eval infrastructure, AGENTS.md instruction, SKILL.md, current-position update, or output_manifest update.

## 2. Why this pass was needed

The `MINIMAL_LAYER_DIGIT_SYSTEM_V0.md` document is useful, but still too clean.

The user correction is valid:

```text
층위는 쉽게 보이지 않는다.
검색으로 자료를 충분히 확보하고,
추리고,
다시 검색하고,
다시 추리는 과정을 몇 번 거쳐야
반복해서 남는 층위와 임의로 붙인 층위가 갈라진다.
```

This pass therefore does not try to prove the 0-9 system.
It stress-tests it.

## 3. Search cycle 1 — governance / decision / risk

Search focus:

```text
decision making framework
risk assessment
decision rights
governance
evidence
authority
monitoring
follow-up
```

Sources inspected:

- Health Canada decision-making framework:
  https://www.canada.ca/en/health-canada/services/science-research/science-advice-decision-making/decision-making-framework-science-research.html
- Decision rights / accountability framework reference:
  https://umbrex.com/resources/frameworks/organization-frameworks/mckinsey-decision-rights-and-accountability-framework/
- NIST/RMF-adjacent and audit/risk checklist search results

What survived filtering:

```text
issue identification
context
risk/benefit assessment
options
strategy/action
implementation
monitor/evaluate
decision owner
accountability
escalation
evidence trail
```

Layer implication:

```text
0 관찰:
  issue identification

1 프레임:
  put issue into context

2 근거:
  evidence, risk/benefit assessment

3 경계:
  risk threshold, controls, constraints

4 권한:
  decision rights, accountable owner, escalation

5 행동:
  strategy/action/implementation

6 후속:
  monitor/evaluate

7 승격:
  governance log, formal operating model, standing forum
```

Correction to 0-9:
  `권한` and `후속` are not optional decorations.
  They repeatedly appear in governance and risk materials as distinct operating layers.

## 4. Search cycle 2 — support quality / customer response QA

Search focus:

```text
customer support QA scorecard
accuracy
resolution
tone
empathy
escalation
follow-up
compliance
auto-fail
```

Sources inspected:

- Customer support AI evaluation:
  https://eval.qa/learn/eval-customer-support.html
- Call center QA program guide:
  https://globalify.com/blog/call-center-quality-assurance-guide
- Customer service QA scorecard and ticket-quality search results

What survived filtering:

```text
factual accuracy
resolution effectiveness
tone / empathy
escalation quality
compliance
closing / follow-up
auto-fail conditions
calibration
business outcome correlation
```

Layer implication:

```text
2 근거:
  factual accuracy against ground truth

5 행동:
  resolution effectiveness

1/8 프레임/렌즈:
  customer emotional state changes how the reply should be read

4 권한:
  escalation quality

3 경계:
  compliance, confidentiality, making up answers

6 후속:
  follow-up ticket rate, closing, customer confirmation

9 의미 차이:
  fast polite answer can still be failure if it solves nothing
```

Correction to 0-9:
  `tone` is not its own universal layer.
  Tone is a lens that changes framing, authority, escalation, or action depending on the input.

Also:
  Some failures are auto-fail, not weighted score issues.
  This supports keeping `경계` separate from normal scoring.

## 5. Search cycle 3 — sensemaking / reframing / learning

Search focus:

```text
sensemaking
data-frame theory
reframing
wicked problems
single-loop learning
double-loop learning
assumptions
action
frame
```

Sources inspected:

- Sensemaking / data-frame descriptions:
  https://en.wikipedia.org/wiki/Sensemaking_%28information_science%29
- Argyris single-loop / double-loop learning summary:
  https://umbrex.com/resources/frameworks/organization-frameworks/argyris-single-and-double-loop-learning-model/
- Wicked problem and reframing search results

What survived filtering:

```text
data and frame fit each other
frames select and connect data
new data can force frame revision
single-loop changes action within assumptions
double-loop changes assumptions/governing variables
wicked problems have contested frames
```

Layer implication:

```text
0 관찰 and 1 프레임:
  not linear; they co-select each other

8 렌즈 이동:
  frame shift is not always needed, but becomes necessary when current frame no longer fits data

9 의미 차이:
  the real meaning is often the gap between the arrival frame and the shifted frame

7 승격/기억:
  double-loop learning can alter governing variables, so it approaches promotion/memory/policy
```

Correction to 0-9:
  The digit system must not be read as a pipeline.
  `0 -> 1` is a loop, not a one-way step.

Also:
  `8` and `9` are not extra fields.
  They are the mechanisms by which layered meaning appears.

## 6. What repeated across cycles

The following repeatedly survived:

```text
input / issue / observation
frame / context
evidence / ground truth
boundary / control / compliance / auto-fail
authority / owner / escalation / decision rights
action / resolution / implementation
follow-up / monitor / evaluate / learning
promotion / governing variable / formal structure
frame shift / reframing
meaning delta / changed interpretation
```

This supports the 0-9 set as a useful candidate.

But the cycles also show that the 0-9 set must be corrected:

```text
0 and 1 are coupled, not sequential.
8 and 9 are not optional decoration; they are the layer-reading mechanism.
3 can override scoring through auto-fail.
4 is distinct from 5; permission is not action.
6 is necessary to prevent action from becoming untested truth.
7 must remain explicit because promotion can happen by implication.
```

## 7. Revised minimal model after iterative filtering

The earlier model:

```text
0 -> 1 -> 2/3/4 -> 5 -> 6
with 7 held
and 8/9 used only when meaning changes by layer shift
```

Revised model:

```text
(0 <-> 1)
  observation and frame co-shape each other

2
  evidence tests the frame

3
  boundary can stop everything

4
  authority decides whether action is allowed

5
  action is the smallest safe move

6
  follow-up tests whether action changed reality

7
  promotion/memory is always explicit HOLD unless approved

8 -> 9
  lens shift reveals meaning delta when the input layer and shifted layer diverge
```

Short form:

```text
(0<->1) + 2 + [3/4 gate] + 5 + 6
with 7 held
and 8/9 used when frame shift reveals different meaning
```

## 8. What should be removed or downgraded

Downgrade:

```text
tone:
  not a base digit.
  It is a domain signal that may affect 1, 4, 5, or 8/9.

card proliferation:
  new cards should not be created until repeated real inputs show that the same digit pattern is too dense for the existing card.

weighted scoring:
  useful for QA programs, but not necessary for this candidate layer system yet.

full taxonomy:
  still HOLD.
```

Keep:

```text
customer response safety:
  strong candidate skin over the digit system

decision memo review:
  likely strong future skin

operational exception triage:
  likely strong future skin

external tool pre-use:
  strong because 3/4/7 risks are high
```

## 9. Resulting principle

The useful structure is not:

```text
one card per use case
```

or:

```text
one linear workflow for all inputs
```

The useful structure is:

```text
small reusable layer digits
read through arrival layer and possible shifted layer
then act only where evidence, boundary, authority, and follow-up allow
```

This preserves the user's point:

```text
층위는 쉽게 보이지 않는다.
층위는 반복 수집과 추림 속에서 남는 관계다.
```

## 10. Next search/filter pass

Recommended next pass:

```text
Search domain:
  incident triage / emergency medicine triage / service desk incident severity

Why:
  It will stress-test whether 3 경계, 4 권한, 5 행동, 6 후속 are enough under urgency.

Expected test:
  operational exception triage using 0-9 digits.
```

Do not promote anything before that pass.

## 11. Hard stop confirmation

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

`STATUS: ITERATIVE_LAYER_DISCOVERY_SEARCH_PASS_COMPLETED_WITH_WATCH`
