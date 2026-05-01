# Space-CLI Scenario Test Closeout v0

## 1. core conclusion

The purpose of space-CLI attachment is not only to improve CLI performance.

The core purpose is to reflux CLI answers, executions, failures, and differences back into the space as operating memory.

That memory should change how the next input is read.

The useful unit is:

```text
CLI answer
+ difference from space-referenced answer
+ reflux candidate
```

## 2. conclusion on space weight

The space must not read the whole source every time.

The lightweight order is:

```text
input routing
-> memory card retrieval
-> pointer-based source check
-> full source reading only when needed
```

This keeps the space from becoming heavy.

It also keeps the CLI from receiving a large onboarding payload for every task.

## 3. conclusion on CLI token cost

Do not feed the whole space to the CLI.

Give the CLI only the minimum work packet needed for the current task:

- purpose
- source surface
- relevant lines
- relevant axes
- guardrails
- reference pointers
- expected output
- stop conditions

The CLI should receive bounded context, not inherited authority.

## 4. next step

The next step is not implementation.

The next step is a dry thought test with the same input through two routes:

1. native CLI expected response
2. space-referenced expected response

Then record the difference through:

- missing
- overreach
- alignment
- contradiction
- compression gain
- token cost
- reflux value

## 5. Codex / Gemini position

Codex may help with:

- structuring
- documentation
- patching approved documents
- final judgment support

Gemini may help with:

- fast draft-only tests
- batch comparison drafts
- listing
- self-check drafts

Neither Codex nor Gemini replaces the space.

Both are workers attached to the space.

## 6. final compression

Plain CLI creates answers.

Space-attached CLI creates answers and differences.

Those differences can reflux back into space memory.

The space does not read more.

The space retrieves less, precisely.

## 7. closeout verdict

```yaml
verdict: PASS_WITH_NOTE
package_created: true
tool_setup: false
bridge_design: false
scripts_created: false
runtime_structure_design: false
verification_packet_or_return_design: false
code_modified: false
baseline_lock: false
next_allowed_move: run_native_vs_space_referenced_dry_thought_test
```
