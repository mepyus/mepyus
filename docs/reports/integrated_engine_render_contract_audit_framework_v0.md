# Integrated Engine Render Contract Audit Framework v0

Date: 2026-04-15

## 0. verdict

PASS

This framework defines a read-only audit method for checking whether the current three scaffold surfaces satisfy the v1 candidate minimum render contract.

It does not change scaffold files, manifest shapes, read mappings, tokens, panels, or extension status.

## 1. audit purpose

The purpose is to check whether each scaffold panel makes its intended question and manifest read visible enough to support current working baseline operation.

The audit asks:

- Does each panel answer the right baseline question?
- Does the central panel remain the strongest reader of its surface?
- Does the panel show enough display purpose to satisfy the v1 candidate?
- Are support layers visibly subordinate?
- Are manifest reads visible without implying runtime binding or live truth?

## 2. contract axes

### panel question clarity

Check:

- Does the panel copy state the panel's question or display purpose?
- Can a reader infer what the panel is for without opening the manifest?

PASS:

- panel title, summary, badge, or explicit question makes the purpose clear

PASS_WITH_NOTE:

- purpose is legible but relies on surrounding context or support note

HOLD:

- panel appears as generic card or visual block without a clear question

### central gravity fidelity

Check:

- Does the surface center match the v1 candidate central panel?
- Is the central panel visually and semantically strongest?

PASS:

- central panel is both ordered and emphasized as center

PASS_WITH_NOTE:

- central panel is semantically correct but layout or support density could dilute it

HOLD:

- support layer or optional selector reads stronger than the central panel

### panel role boundary clarity

Check:

- Does each panel stay within anchor / maturation / operating expression boundaries?

PASS:

- panel role and copy match the expression class

PASS_WITH_NOTE:

- boundary is mostly clear but wording could be tightened

HOLD:

- panel mixes anchor, maturation, and operating objects without distinction

### support-layer subordination

Check:

- Do support notes, strips, selectors, or side inspection remain secondary?

PASS:

- support layer is visibly smaller, quieter, or explicitly subordinate

PASS_WITH_NOTE:

- support layer is safe but could still draw visual attention

HOLD:

- support layer reads as a core panel or primary source of truth

### manifest-read evidence readability

Check:

- Does the scaffold show the mapped manifest path, read role, and read reason?

PASS:

- read role, path, and reason are visible per panel

PASS_WITH_NOTE:

- evidence is visible but render-field specificity is still thin

HOLD:

- manifest read is hidden or replaced by ungrounded display state

### request / return / reflux compatibility

Check:

- Does the surface preserve request / return / reflux separation?

PASS:

- request, return, and reflux are named or routed without completion/bypass drift

PASS_WITH_NOTE:

- compatibility is present but relies on visual strip or support copy

HOLD:

- return reads as final completion, request reads as raw engine command, or reflux reads as generic feedback

### object-class separation where applicable

Check:

- Does VectorFL preserve anchor / maturation / operating object separation?

PASS:

- object-class labels and copy separate criteria, body, and route

PASS_WITH_NOTE:

- separation is visible but could use tighter wording later

HOLD:

- object classes collapse into one undifferentiated visual grammar

## 3. surface-specific audit lens

### user surface

Protected center:

- `operating_flow_panel`

Lens:

- Does the user surface read as operating / distribution / decision?
- Does `operating_flow_panel` answer where the request / return / reflux loop is?
- Do request organization, anchor support, and return decision remain support around the operating center?
- Does optional distribution stay subordinate?

### VectorFL surface

Protected center:

- `maturation_canvas_panel`

Lens:

- Does the VectorFL surface read as mediation / validation / maturation?
- Does `maturation_canvas_panel` answer what maturation object body is being read?
- Are anchor criteria, maturation body, and operating route visually separate?
- Does line / axis support selection remain support-only?

### engine surface

Protected center:

- `execution_state_panel`

Lens:

- Does the engine surface read as processing / execution / return-draft?
- Does `execution_state_panel` answer where processing is now?
- Do work input, result return, and execution history remain support around execution state?
- Does return material avoid final-completion language?

## 4. verdict criteria

### PASS

Use PASS when:

- central gravity is correct
- read mappings are visible and unchanged
- panel questions are legible
- support layers are subordinate
- request / return / reflux separation remains intact
- no runtime/governance/extension drift appears

### PASS_WITH_NOTE

Use PASS_WITH_NOTE when:

- structure is correct
- no forbidden drift appears
- but one or more contract areas remain thin, especially render-field specificity, support wording, or panel-question explicitness

### HOLD

Use HOLD when:

- read-only evidence cannot support a safe verdict
- central gravity is ambiguous
- support layer reads as core
- object classes collapse
- request / return / reflux separation is weakened
- a safe fix would require read-map change, manifest change, new panel, runtime binding, or extension promotion

## 5. audit boundary

This audit may recommend wording-only or boundary-emphasis refinement later.

It may not recommend:

- new panels
- shared components
- manifest shape changes
- read-map changes
- runtime binding
- extension promotion
- watcher / supervisor / bridge / governance authority
