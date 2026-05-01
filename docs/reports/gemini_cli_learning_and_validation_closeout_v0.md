# Gemini CLI Learning and Validation Closeout v0

## 1. status

```yaml
closeout_status: gemini_cli_onboarding_closeout
verdict: PASS_WITH_NOTE
baseline_lock: false
schema_enforcement: false
controller_implementation: false
gemini_final_judge: false
```

## 2. conclusion

Gemini is not the final judge of this space.

Gemini should first be used as:

- fast trial executor
- batch formatter
- simple validation runner
- 4-line card drafter
- separation checker

Gemini's speed is useful. Its judgment depth and accuracy must be validated separately.

Gemini can receive broad batches, but every batch must require material separation and self-check.

## 3. current usable areas

Gemini can be used for:

- adding live trials in a fixed format
- preserving trial note format
- drafting user-facing 4-line cards
- separating multiple materials
- simple validation against existing docs
- writing self-checks
- running repeated checks
- producing PASS / PASS_WITH_NOTE / HOLD candidates

## 4. areas not yet delegated to Gemini

Do not assign Gemini:

- structure design
- source surface taxonomy changes
- final philosophical interpretation
- baseline confirmation
- controller implementation
- code/helper modification
- index or microspace auto-update
- space direction redefinition
- final promotion decisions

## 5. next validation style

The next Gemini test should not be a simple PASS output.

Use a skeptical self-check task:

- Ask Gemini to reread its own batch result.
- Ask whether every `yes` in self-check is actually justified.
- Require at least three HOLD possibilities to be considered.
- Separate format compliance from judgment compliance.
- Ask Gemini to identify possible source surface confusion.

## 6. validation questions for Gemini returns

When Gemini returns work, Codex/assistant should reread it as `worker_return` and ask:

- What was expected?
- What was observed?
- Did Gemini preserve material separation?
- Did Gemini over-promote anything?
- Did Gemini keep the 4-line user card?
- Did Gemini create files outside scope?
- Did Gemini use PASS where PASS_WITH_NOTE or HOLD was safer?
- Is the result usable as-is, or only as note_only residue?

## 7. compressed role statement

```text
Codex organizes structure.
Gemini executes and validates quickly.
User and assistant supervise direction and judgment.
Gemini can read a lot, but should not be trusted a lot without validation.
Gemini may process broad batches, but must preserve separation and self-check.
```

## 8. do not

- Do not baseline lock.
- Do not make Gemini final judge.
- Do not let Gemini design schema.
- Do not let Gemini implement controller.
- Do not let Gemini update index or microspace.
- Do not let Gemini redefine the space.
- Do not replace 공간에 넣어보기 with a new Gemini-specific system.
- Do not treat Gemini speed as judgment authority.

## 9. next move

Next Gemini task should be bounded:

```text
Give Gemini one material-trial packet.
Require one file modification at most.
Require a 4-line card.
Require self-check with yes / partial / no.
Reread Gemini's return as worker_return before accepting it.
```
