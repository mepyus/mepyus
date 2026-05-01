# Space Function Test Package for Gemini v0

## 1. package purpose

This package is not a Gemini execution environment.

It is not a bridge, packet store, JSON return system, script plan, or automation loop.

This package tests how the space behaves when real material is put into it through the user-facing flow:

```text
공간에 넣어보기
```

The purpose is to check whether the space can read, separate, judge, compress, and route material without over-promoting the material into baseline, controller, schema, or final authority.

Gemini is used only as a bounded verification worker that can quickly run draft-only space-function trials.

## 2. target space functions

The test target is the space's internal reading and judgment behavior, not Gemini infrastructure.

Functions to test:

- material intake: judge whether material can enter the space
- source surface reading: distinguish what kind of material is being read now
- lens order application: apply the correct reading order for that source surface
- risk detection: detect over-promotion, baseline lock, controllerization, or authority drift
- residue capture: capture traces that may matter later without forcing a full record
- next move shaping: propose a small next action
- user-facing compression: return a plain 4-line user card
- internal/user split: keep internal working labels separate from user-facing output

Default user-facing card:

```text
쓸 수 있나?
왜?
다음엔?
조심할 점은?
```

Internal labels such as `source_surface`, `lens_order`, `worker_return`, `generated_report`, and `runtime_event` remain internal unless the task explicitly asks for them.

## 3. Gemini role

Gemini may do only this:

- read the given test material quickly
- propose a source surface candidate
- apply the provided lens order
- draft the 4-line user-facing card
- mark risk, residue, and next move briefly
- return `HOLD` or `PASS_WITH_NOTE` when its judgment is weak

Gemini must not:

- change the space structure
- baseline lock anything
- create a controller
- modify scripts or code
- modify, delete, overwrite, or move files
- propose Gemini execution bridges
- propose packet or return automation
- claim final judgment authority

Gemini's useful output is a draft reading of space function behavior, not a final decision.

## 4. meaning of test results

Gemini results are not decisions.

Gemini results are first-pass evidence about how the space function appears when applied to actual material.

Codex, assistant, and user must reread Gemini output as `worker_return` before accepting, refining, holding, or rejecting it.

The important question is not "Did Gemini say PASS?"

The important questions are:

- Did Gemini preserve source surface separation?
- Did Gemini apply the lens order without flattening?
- Did Gemini keep the 4-line user-facing card separate from internal notes?
- Did Gemini mark risk and residue without over-promoting them?
- Did Gemini suggest a small next move?
- Did Gemini avoid structure, script, runtime, schema, or controller design?

## 5. default test posture

Use small tests.

Give Gemini one case or a batch of two to three cases.

Require draft-only output.

Require one card per material.

Require `PASS_WITH_NOTE` or `HOLD` when uncertain.

Then reread the result as `worker_return`.

This keeps the space first and the tool second.
