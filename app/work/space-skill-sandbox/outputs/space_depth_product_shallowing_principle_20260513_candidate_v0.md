# Space Depth / Product Shallowing Principle
# 2026-05-13 Candidate v0

## 1. Status

Document:
  candidate implementation guardrail note

Authority:
  orientation and product-shaping support only

Not:
  product architecture
  workflow
  registry
  schema
  ontology
  baseline
  current-position
  output_manifest
  automation plan

Placement:
  RETURN_TO_SPACE_VALUE_WITH_WATCH

---

## 2. Core Judgment

VectorFL space can be deep.

The product or program built from it should stay shallow enough to use, revise, test, and finish.

Short rule:

공간은 깊이를 보존하고,
제품은 그 깊이를 얕게 접어 사용 가능하게 만든다.

English rule:

Space can be deep.
Product should stay shallow enough to use.

---

## 3. Why This Exists

The VectorFL space contains more than repo assets.

It contains:

- process
- trace
- failures
- successful corrections
- philosophy
- operating principles
- runs
- packages
- buildup
- user judgment
- recovered decisions
- external references
- implementation attempts

This depth is useful for orientation, judgment, and cost control.

But if a program copies the full depth of the space, the program can become too heavy to finish.

Risk pattern:

1. A product task begins.
2. Space context is read too literally.
3. The implementation absorbs too many layers.
4. The UI or program becomes structurally deep.
5. More review, testing, correction, and direction-setting are needed.
6. The work produces more structure instead of a finished usable product.

---

## 4. Stable Distinction

Space:
  stores depth
  preserves process
  keeps trace
  holds failures and corrections
  supports multiple lenses
  keeps recovered judgments
  allows re-entry compression

Product / Program:
  presents a shallow usable surface
  supports a clear user action
  exposes only necessary state
  keeps fewer abstractions
  stays easy to revise
  stays easy to test
  avoids copying the full space structure

Important:
  The product should be informed by the space.
  The product should not become the space.

---

## 5. Operating Board v0 Example

Initial drift:
  The first board attempt followed the existing React app / repo affordance too quickly.

Correction:
  The board was moved to a standalone HTML output.

Second drift:
  The board still felt too repo-shaped and heavy.

Second correction:
  The board was reduced to a one-input manual operating surface.

Web-informed test:
  AgentOps / HITL references supported trace, pause, resume, and human decision points.
  They did not require a full observability dashboard.

Style test:
  BMW design reference improved visual precision.
  It remained visual treatment only.

Recovered product-shaping judgment:
  The useful product surface is:
    one input
    current state
    pause reason
    recovered judgment
    WATCH
    HOLD
    next action

  The risky product surface is:
    all runs
    all lenses
    all packets
    all agent states
    all workflows
    all space layers

---

## 6. Before Program Implementation

Before implementing a program-level feature, answer:

1. What space depth is relevant?
2. What lens should be attached?
3. What should be compressed before execution?
4. What should remain hidden from the product surface?
5. What is the shallowest usable product form?
6. What repo affordance might pull the implementation off course?
7. What should stay HOLD?

If the answers require broad rereading, create or read a small re-entry compression note first.

---

## 7. Product Shallowing Rule

When building from VectorFL space:

- do not expose every layer
- do not mirror every folder
- do not show every run
- do not turn every process word into UI state
- do not build a dashboard just because traces exist
- do not create a workflow just because steps exist
- do not create a registry just because many artifacts exist
- do not create automation just because handoff is visible

Prefer:

- one clear user action
- one current item
- one recovered judgment
- one pause reason
- one next small action
- expandable detail only when needed

---

## 8. WATCH

- Program becoming as deep as the space.
- UI becoming a mirror of internal folders.
- Product dashboard drift.
- Trace visibility becoming full observability tooling.
- Human gate becoming approval system.
- Implementation absorbing too many operating terms.
- Testing and review producing more structure than usable product.
- Re-entry notes becoming product requirements.

---

## 9. HOLD

- product architecture promotion
- workflow engine
- registry / schema / ontology
- automation
- backend / database / auth unless separately approved
- current-position update
- output_manifest update
- baseline promotion
- broad app integration before standalone usefulness is proven

---

## 10. Do Not Promote

- space depth ≠ product depth
- product surface ≠ space map
- operating board ≠ product dashboard
- trace panel ≠ observability platform
- human gate ≠ approval system
- shallow product ≠ loss of space memory
- standalone preview ≠ app architecture
- implementation guardrail ≠ workflow

---

## 11. Next Use

Use this note before program-level work when:

- the task could become a full app feature
- repo affordance may pull the work into an existing app structure
- the space has many relevant traces and artifacts
- the user wants a usable product, not more structure
- the implementation should stay easy to revise and test

Recommended next use:
  Before extending VectorFL Operating Board v0, decide the shallowest usable surface first, then edit only that surface.

