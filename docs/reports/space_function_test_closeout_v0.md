# Space Function Test Closeout v0

## 1. current conclusion

Now is not the time to design a Gemini execution system.

The next useful step is to test whether the space's `공간에 넣어보기` function works reliably in front of actual material.

The center is the space function:

```text
material intake
-> source surface reading
-> lens order application
-> 4-line user card
-> risk/residue/next move
-> reread the result as worker_return
```

Gemini is useful here only as a bounded draft worker that can quickly apply the fixed test format.

## 2. next usage

Ask Gemini only in this style:

- give one case, or a batch of two to three cases
- require draft-only output
- forbid file modification
- require one user-facing 4-line card per material
- require internal risk, residue, and next move
- require `PASS_WITH_NOTE` or `HOLD` when uncertain
- reread Gemini's result as `worker_return`

Do not ask Gemini to design bridges, packet storage, JSON return automation, scripts, runtime structures, schemas, controllers, or index updates.

## 3. success criteria

This package succeeds if Gemini can:

- avoid mixing source surfaces
- separate the 4-line user card from internal judgment
- mark over-promotion risk
- propose a small next move
- use `HOLD` or `PASS_WITH_NOTE` when it does not know
- avoid file edits and structure design suggestions

It is acceptable for Gemini to be imperfect.

The point is to reveal how the space function behaves, not to trust Gemini as final judge.

## 4. final compression

Do not automate Gemini first.

Test the space function first.

Gemini is a helper for quickly running bounded material trials.

The space comes first.

The tool comes later.

## 5. closeout verdict

```yaml
verdict: PASS_WITH_NOTE
package_created: true
gemini_execution_setup: false
automation_design: false
scripts_created: false
runtime_modified: false
code_modified: false
baseline_lock: false
next_allowed_move: give_gemini_one_space_function_test_case_draft_only
```
