# Gemini CLI No Delete / No Overwrite Policy v0

## 1. status

```yaml
policy_status: no_delete_no_overwrite
default_permission: no-write
deletion_allowed: false
overwrite_allowed: false
move_allowed: false
baseline_lock: false
```

## 2. absolute prohibitions

Gemini must never perform:

- file deletion
- folder deletion
- file movement
- file rename
- overwrite of an existing file
- partial deletion from an existing file
- rewrite of an existing section
- automatic cleanup
- unnecessary file removal
- whole-repo formatting
- import cleanup
- unused-code removal
- repo cleanup

This applies even when Gemini believes the change is safe.

## 3. prohibited commands and effects

The following commands, or commands with equivalent effects, are forbidden:

```text
rm
rm -rf
mv
git reset
git checkout
git clean
sed -i
perl -pi
truncate
apply_patch
python scripts that rewrite existing files without explicit sandbox output
> existing_file
cat > existing_file
cp source existing_file
```

Also forbidden:

```text
black .
prettier --write .
eslint --fix .
npm run format
repo cleanup scripts
```

## 4. when a change seems needed

Gemini must not apply the change.

Return only:

```text
Suggested change:
Target file:
Reason:
Risk:
Patch proposal:
Do not apply automatically.
```

The patch proposal is advisory text, not an applied patch.

## 5. when deletion seems needed

Gemini must not delete.

Return only:

```text
Deletion candidate:
Why it looks removable:
Why deletion is risky:
Required human/Codex confirmation:
Do not delete automatically.
```

## 6. required safety report

After any Gemini run, Gemini must report:

```text
Files modified:
Files deleted:
Files moved:
Files overwritten:
```

Expected safe output:

```text
Files modified: none
Files deleted: none
Files moved: none
Files overwritten: none
```

If any field is not `none`, the return must be treated as HOLD or FAIL until Codex/user reviews it.

## 7. do not

- Do not silently assume deletion is harmless.
- Do not delete generated files.
- Do not clean cache folders unless explicitly instructed by Codex/user in a separate action.
- Do not rewrite existing documents.
- Do not treat append permission as edit permission.
