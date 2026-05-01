# Gemini CLI Command Allowlist / Denylist v0

## 1. status

```yaml
policy_status: command_allowlist_denylist
default_permission: no-write
execution_allowed: bounded
baseline_lock: false
schema_enforcement: false
```

## 2. generally allowed read commands

Read-centered commands:

```text
cat
head
tail
rg
grep
find [limited path only]
ls
wc
pwd
```

Rules:

- use specified paths only
- do not scan the whole repo unless explicitly instructed
- do not combine read commands with write redirects

## 3. generally allowed check commands

Allowed only when explicitly relevant:

```text
python <script> --help
python <script> --dry-run
python <script> --check
node <script> --help
pytest [specific test file only, when explicitly allowed]
npm test -- --runInBand [only when explicitly allowed]
```

Rules:

- whole test suites are forbidden by default
- if output files may be created, use an explicit sandbox output path
- do not fix failures automatically

## 4. conditionally allowed commands

Allowed only with explicit instruction:

```text
python existing_script.py --input <specified_input> --output <sandbox_output>
node existing_script.js --input <specified_input> --output <sandbox_output>
pytest specific/test_file.py
```

Conditions:

- script already exists
- script is not modified
- input is specified
- output path is sandbox-only
- existing file overwrite is forbidden

## 5. denied commands

Forbidden:

```text
rm
mv
git reset
git checkout
git clean
sed -i
perl -pi
truncate
apply_patch
black .
prettier --write .
eslint --fix .
npm run format
python scripts that rewrite repo files
```

Also deny any command that:

- deletes
- moves
- overwrites
- rewrites existing files
- reformats broad paths
- updates index/microspace
- creates runtime manifest
- modifies helper/code

## 6. pre-run check format

Before running a command, Gemini must internally check:

```text
command:
purpose:
read paths:
write paths:
expected output:
risk:
allowed_level:
```

If `write paths` includes existing repo files, Gemini must not run the command.

## 7. post-run return format

Gemini must return:

```text
command_run:
exit_code:
stdout_summary:
stderr_summary:
files_modified:
files_created:
files_deleted:
risk:
next:
```

For safe read-only runs, expected file fields are:

```text
files_modified: none
files_created: none
files_deleted: none
```

## 8. do not

- Do not use shell redirection into existing files.
- Do not use formatters.
- Do not use cleanup commands.
- Do not run broad tests without explicit permission.
- Do not rerun with broader permissions after failure.
