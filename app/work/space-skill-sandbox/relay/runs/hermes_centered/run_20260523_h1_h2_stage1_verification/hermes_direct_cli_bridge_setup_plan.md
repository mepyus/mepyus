# Hermes Direct CLI Bridge Setup Plan

status: SETUP_PLAN_ONLY_WITH_HOLD

## Verdict

CODEX_AND_GEMINI_BINARIES_AVAILABLE_FOR_PACKET_BOUND_HERMES_INVOCATION

## Local Discovery Addendum

### codex_exec_help

```bash
codex exec --help 2>&1 | sed -n '1,140p' || true
```

exit_code: 0

```text
Run Codex non-interactively

Usage: codex exec [OPTIONS] [PROMPT]
       codex exec [OPTIONS] <COMMAND> [ARGS]

Commands:
  resume  Resume a previous session by id or pick the most recent with --last
  review  Run a code review against the current repository
  help    Print this message or the help of the given subcommand(s)

Arguments:
  [PROMPT]
          Initial instructions for the agent. If not provided as an argument (or if `-` is used),
          instructions are read from stdin. If stdin is piped and a prompt is also provided, stdin
          is appended as a `<stdin>` block

Options:
  -c, --config <key=value>
          Override a configuration value that would otherwise be loaded from `~/.codex/config.toml`.
          Use a dotted path (`foo.bar.baz`) to override nested values. The `value` portion is parsed
          as TOML. If it fails to parse as TOML, the raw string is used as a literal.
          
          Examples: - `-c model="o3"` - `-c 'sandbox_permissions=["disk-full-read-access"]'` - `-c
          shell_environment_policy.inherit=all`

      --enable <FEATURE>
          Enable a feature (repeatable). Equivalent to `-c features.<name>=true`

      --disable <FEATURE>
          Disable a feature (repeatable). Equivalent to `-c features.<name>=false`

      --strict-config
          Error out when config.toml contains fields that are not recognized by this version of
          Codex

  -i, --image <FILE>...
          Optional image(s) to attach to the initial prompt

  -m, --model <MODEL>
          Model the agent should use

      --oss
          Use open-source provider

      --local-provider <OSS_PROVIDER>
          Specify which local provider to use (lmstudio or ollama). If not specified with --oss,
          will use config default or show selection

  -p, --profile <CONFIG_PROFILE>
          Configuration profile from config.toml to specify default options

      --profile-v2 <CONFIG_PROFILE_V2>
          Layer $CODEX_HOME/<name>.config.toml on top of the base user config

  -s, --sandbox <SANDBOX_MODE>
          Select the sandbox policy to use when executing model-generated shell commands
          
          [possible values: read-only, workspace-write, danger-full-access]

      --dangerously-bypass-approvals-and-sandbox
          Skip all confirmation prompts and execute commands without sandboxing. EXTREMELY
          DANGEROUS. Intended solely for running in environments that are externally sandboxed

      --dangerously-bypass-hook-trust
          Run enabled hooks without requiring persisted hook trust for this invocation. DANGEROUS.
          Intended only for automation that already vets hook sources

  -C, --cd <DIR>
          Tell the agent to use the specified directory as its working root

      --add-dir <DIR>
          Additional directories that should be writable alongside the primary workspace

      --skip-git-repo-check
          Allow running Codex outside a Git repository

      --ephemeral
          Run without persisting session files to disk

      --ignore-user-config
          Do not load `$CODEX_HOME/config.toml`; auth still uses `CODEX_HOME`

      --ignore-rules
          Do not load user or project execpolicy `.rules` files

      --output-schema <FILE>
          Path to a JSON Schema file describing the model's final response shape

      --color <COLOR>
          Specifies color settings for use in the output
          
          [default: auto]
          [possible values: always, never, auto]

      --json
          Print events to stdout as JSONL

  -o, --output-last-message <FILE>
          Specifies file where the last message from the agent should be written

  -h, --help
          Print help (see a summary with '-h')

  -V, --version
          Print version
```

### codex_review_help

```bash
codex review --help 2>&1 | sed -n '1,120p' || true
```

exit_code: 0

```text
Run a code review non-interactively

Usage: codex review [OPTIONS] [PROMPT]

Arguments:
  [PROMPT]
          Custom review instructions. If `-` is used, read from stdin

Options:
  -c, --config <key=value>
          Override a configuration value that would otherwise be loaded from `~/.codex/config.toml`.
          Use a dotted path (`foo.bar.baz`) to override nested values. The `value` portion is parsed
          as TOML. If it fails to parse as TOML, the raw string is used as a literal.
          
          Examples: - `-c model="o3"` - `-c 'sandbox_permissions=["disk-full-read-access"]'` - `-c
          shell_environment_policy.inherit=all`

      --strict-config
          Error out when config.toml contains fields that are not recognized by this version of
          Codex

      --enable <FEATURE>
          Enable a feature (repeatable). Equivalent to `-c features.<name>=true`

      --uncommitted
          Review staged, unstaged, and untracked changes

      --base <BRANCH>
          Review changes against the given base branch

      --disable <FEATURE>
          Disable a feature (repeatable). Equivalent to `-c features.<name>=false`

      --commit <SHA>
          Review the changes introduced by a commit

      --title <TITLE>
          Optional commit title to display in the review summary

  -h, --help
          Print help (see a summary with '-h')
```

### codex_doctor_head

```bash
codex doctor 2>&1 | sed -n '1,120p' || true
```

exit_code: 0

```text
Codex Doctor v0.133.0 · macos-x86_64

Environment
  ✓ runtime      brew
      version                  0.133.0
      install method           brew
      commit                   unknown
      executable               /usr/local/bin/codex
  ✓ install      consistent
      context                  brew
      managed by               npm: no · bun: no · package root —
      PATH entries (1)         /usr/local/bin/codex
  ✓ search       ripgrep 14.1.1 (system, `rg`)
      search command           rg
      search provider          system
      search command readiness ripgrep 14.1.1
  ✓ terminal     Apple Terminal 455.1
      terminal                 Apple Terminal
      TERM_PROGRAM             Apple_Terminal
      terminal version         455.1
      stdin is terminal        false
      stdout is terminal       false
      stderr is terminal       false
      terminal size            80x24
      color output             disabled (stdout is not a terminal)
      effective locale         ko_KR.UTF-8
  ✓ state        databases healthy
      CODEX_HOME               ~/.codex (dir)
      log dir                  ~/.codex/log (dir)
      sqlite home              ~/.codex (dir)
      state DB                 ~/.codex/state_5.sqlite (file) · integrity ok
      log DB                   ~/.codex/logs_2.sqlite (file) · integrity ok
      goals DB                 ~/.codex/goals_1.sqlite (file) · integrity ok
      active rollouts          160 files · 446.98 MB (avg 2.79 MB)
      archived rollouts        0 files · 0 B (avg 0 B)

Configuration
  ✓ config       loaded
      model                    gpt-5.5 · openai
      cwd                      ~/universe/vectorfl_replica
      config.toml              ~/.codex/config.toml
      config.toml parse        ok
      MCP servers              0
      feature flags            28 enabled · 0 overridden (full list with --all)
  ✓ auth         auth is configured
      auth storage mode        File
      auth file                ~/.codex/auth.json
      stored auth mode         chatgpt
      stored API key           false
      stored ChatGPT tokens    true
      stored agent identity    false
  ✓ mcp          no MCP servers configured
  ✓ sandbox      restricted fs + restricted network · approval OnRequest
      approval policy          OnRequest
      filesystem sandbox       restricted
      network sandbox          restricted
      linux helper             none
      execve wrapper helper    ~/.codex/tmp/arg0/codex-…7i/codex-execve-wrapper

Updates
  ✓ updates      update configuration is locally consistent
      startup update check     true
      update action            brew upgrade --cask codex
      version cache            ~/.codex/version.json
      cached latest version    0.133.0
      last checked at          2026-05-22 08:59 UTC
      latest version           0.133.0
      latest version status    current version is not older

Connectivity
  ✓ network      no proxy env vars
      proxy env vars           none
  ✓ websocket    connected (HTTP 101 Switching Protocols) · 15s timeout
      model provider           openai
      provider name            OpenAI
      wire API                 responses
      supports websockets      true
      proxy env vars           none
      connect timeout          15000 ms
      auth mode                chatgpt
      endpoint                 wss://chatgpt.com/backend-api/<redacted>
      DNS                      2 IPv4, 0 IPv6, first IPv4
      handshake result         HTTP 101 Switching Protocols
      reasoning header         false
      models etag present      true
      server model present     false
  ✓ reachability active provider endpoints are reachable over HTTP
      reachability mode        ChatGPT auth
      ChatGPT base URL         https://chatgpt.com/backend-api/ reachable (HTTP 404)

Background Server
  ○ app-server   not running (ephemeral mode)
      daemon state dir         ~/.codex/app-server-daemon
      settings                 ~/.codex/app-server-daemon/settings.json (missing)
      pid file                 ~/.codex/app-server-daemon/app-server.pid (missing)
      update-loop pid file     ~/.codex/app-server-daem…/app-server-updater.pid (missing)
      control socket           ~/.codex/app-server-cont…app-server-control.sock
      status                   not running
      mode                     ephemeral

─────────────────────────────────────────────────────────────
13 ok · 1 idle · 0 warn · 0 fail ok

--summary compact output           --all expand truncated lists
--json redacted report
```

### gemini_noninteractive_flags

```bash
gemini --help 2>&1 | sed -n '168,210p' || true
```

exit_code: 0

```text

```

### gemini_list_sessions_head

```bash
gemini --list-sessions 2>&1 | sed -n '1,80p' || true
```

exit_code: 0

```text
Available sessions for this project (73):
  1. 프로젝트를 Git 원격 저장소에 올리기 (28 days ago) [c77829ca-ce49-47ac-9af6-faa56eb76272]
  2. Test our space's minimum packet structure with real data. (26 days ago) [d1a45326-f68d-4959-a1e7-e266a2c9fe5c]
  3. ! (26 days ago) [0d5a2e04-aa83-41f1-9798-212a03322b6a]
  4. Analyze Gemini CLI's research process and output. (25 days ago) [d141695b-4b2d-450d-a5a5-67cc56368f93]
  5. Search external data, then run manual graph layer dry-run. (24 days ago) [28fbb9ac-03d8-42ae-8faa-32def93ae658]
  6. Closeout card for Space Skill Sandbox v0.3 (24 days ago) [245b114a-bbd6-42a7-b80b-700bf9835e1c]
  7. Test external material intake with v0.3 guide routing. (23 days ago) [43225c87-a235-4989-a2a9-2808b175eff4]
  8. cli  ! (23 days ago) [5afae751-f515-4fa1-b7f2-a864b5f36c73]
  9. User wants to execute Run 032 after verification. (23 days ago) [77b784d6-66d3-4ecd-9519-d338e0aa27f0]
  10. # Gemini Runner Smoke Packet v0 Reply with exactly one short sentence. Do not create files. Do no... (23 days ago) [b4aa4b0a-e1b4-4582-a555-af1a94da3fa0]
  11. Reply with exactly: GEMINI_SMOKE_OK (23 days ago) [407523db-fb9b-4946-a3bb-53836394c947]
  12. # Run 032 - Tool Affordance / Caller Shift Lens v0 ## Mode GEMINI / SANDBOX ONLY / LENS DRAFT / N... (23 days ago) [babb9ac6-7517-44b3-abe6-9e9f0ed2948e]
  13. Reply with exactly: GEMINI_SMOKE_OK (23 days ago) [34af0832-b5d8-4b76-a0e7-1b6f7b332056]
  14. # Gemini Write Probe Packet v0 Create exactly one file: ```text app/work/space-skill-sandbox/test... (23 days ago) [ea8e1549-7dd8-4649-9933-912c96e49505]
  15. # Run 032 Retry - Tool Affordance / Caller Shift Lens v0 Response Bundle ## Mode GEMINI / SANDBOX... (23 days ago) [fe5b61b9-630c-46b6-8e4a-9d12ab775e07]
  16. Reply with exactly: GEMINI_SMOKE_OK (23 days ago) [618c9e36-9b2a-4578-8319-6d28660bf3d9]
  17. # Run 032 - Tool Affordance / Caller Shift Lens v0 ## Mode GEMINI / SANDBOX ONLY / LENS DRAFT / N... (23 days ago) [d96c7e25-bda4-43f8-9ef3-e63f5d6ed930]
  18. # Run 032 - Tool Affordance / Caller Shift Lens v0 ## Packet Metadata - packet_id: next_gemini_ta... (23 days ago) [787b6420-412f-4652-8929-1003b9b0c2c1]
  19. Sandbox 산출물 승격 가능성 검토 (23 days ago) [0cd070d7-0812-4df7-aa04-49f4d8e1bf2e]
  20. Reply with exactly: GEMINI_SMOKE_OK (22 days ago) [499afaeb-a78e-42a5-b6c5-56161e51db75]
  21. # Package 000 Smoke Packet Reply with exactly: PACKAGE_SMOKE_OK (22 days ago) [1fe8e09f-6261-4af3-abee-b2f67bf1b6cb]
  22. # Package 000 Smoke Packet Reply with exactly: PACKAGE_SMOKE_OK (22 days ago) [e5656001-3d87-4807-8c35-0681f092cb39]
  23. # Package 000 Smoke Packet Reply with exactly: PACKAGE_SMOKE_OK (22 days ago) [65c4c2b0-89b0-476e-b340-69b7c35b0444]
  24. # Package 000 Smoke Packet Reply with exactly: PACKAGE_SMOKE_OK (22 days ago) [7bedbe6a-ec48-45c0-a155-24a0e405c58b]
  25. # Package 001 / Session 01 - Agent Harness Engineering Lens ## Purpose Read Agent Harness Enginee... (22 days ago) [a04989ce-0b2f-4873-83f7-5534bdfd9114]
  26. # Package 001 / Session 02 - Tools Live Beyond Their Maker Lens ## Purpose Read the "tools live b... (22 days ago) [f2d62bee-34a1-4e9b-9cef-e2fc673b557e]
  27. # Package 001 / Session 03 - mini-swe-agent Lens ## Purpose Read mini-swe-agent as a lens for sma... (22 days ago) [8937af7c-204a-48c5-96d7-199262e87e9f]
  28. # Package 003 - Graphify Lens with Compact Feedback ## Purpose Read Graphify as a lens for our cu... (22 days ago) [88319f40-f92c-4ec2-8e96-8b2fa664ae97]
  29. Determine if `session_artifact_collector.sh` needs manifest. (22 days ago) [c878af9c-3538-4188-9ce6-2d0e72d83656]
  30. Gemini, 공간 독해자로 문서 분석 (21 days ago) [b09f63d6-be90-40ed-a0a3-93e9b7a6a120]
  31. User wants to define a manual relay protocol. (21 days ago) [9c18702d-fbe3-4bcb-9de6-6b28d824b0b4]
  32. # run_063_inventory_revalidation ## Role Boundary - Gemini performs read-only observation and cla... (21 days ago) [9955c226-abee-4df6-8732-78e9fde19334]
  33. # run_063_inventory_revalidation ## Role Boundary - Gemini performs read-only observation and cla... (21 days ago) [40c94704-f9f6-4d6b-847c-6042cd2f2443]
  34. exit (21 days ago) [49aaea10-d270-45bc-bf22-6ee25b0b6d2a]
  35. 사용자 결정을 위한 옵션 패킷 생성 (21 days ago) [15b9da13-256d-4f99-86d1-ea16de5d10ae]
  36. cli  ! (19 days ago) [dbbe34f0-1cb1-4e24-ab95-228a35d04d2b]
  37. # Next Gemini Task Packet - Run 122 Current Position Recovery ## Mode CODEX -> GEMINI / STRUCTURE... (21 days ago) [6d36eeeb-3f8d-460f-9982-4f558d508ad5]
  38. . Gemini   .  Gemini  **,   ,   worker**.  . **Kernel + Guardrails      , ///    .**   Gemini   .... (18 days ago) [4a84f3ef-ce96-437a-9efc-b8bc10782373]
  39. .         .  **  **  .  Gemini  ?   : **Gemini   // ,          **  .  re-entry summary   ,      .... (17 days ago) [76739f1d-9483-424d-b8ff-64a625209b9d]
  40. 프로그램 단위 파이프라인 구조화 및 문서화 (17 days ago) [5c667e79-1181-4212-b852-dea24065cb06]
  41. # Gemini Space Exploration Packet - Plan from Space / Session Convergence Prevention ## Role You ... (16 days ago) [4e43af5a-1555-49df-9671-f5eea1b1766f]
  42. # Gemini Compact Crosscheck Packet - Plan from Space Anchor Stack ## Mode Do not use tools. Do no... (16 days ago) [02a3a239-1651-4bf0-8a2f-21d1e500a2e9]
  43. # Gemini Position Value Discovery Packet - Plan from Space ## Role You are doing bounded space ex... (16 days ago) [f4dbd710-7dea-42ba-92c1-c0a75664c5c2]
  44. ! (15 days ago) [28fa8853-130e-4f59-91cc-4f771790891f]
  45. # Gemini Space-Aware External Loop Test 001 - Anchor Request ## Status ```yaml status: live_test_... (15 days ago) [7a6ca3a2-d6e6-488d-898b-6e4dbecb25e7]
  46. # Gemini Space-Aware External Loop Test 001 - Execute With Anchor Packet ## Status ```yaml status... (15 days ago) [fa110db6-7790-405c-b8e6-c49638a1b5fd]
  47. # Gemini Space Loop Test 002 - QMD Attach Anchor Request ## Status ```yaml status: live_test_pack... (15 days ago) [5d4a46c0-573f-4200-aa7f-c897803ab861]
  48. # Gemini Space Loop Test 002 - QMD Attach Execute With Anchor Packet ## Status ```yaml status: li... (15 days ago) [899107d2-4f88-4d7f-b73d-52e2495d4959]
  49. Gemini 지시서 작성 및 결과 보정 (15 days ago) [733b409f-a87b-4449-9417-cd149ebcd1de]
  50. cli  ! (14 days ago) [6aea8fa2-d70c-4725-94e9-dbead53c361c]
  51. Re-read VectorFL space to improve re-entry. (13 days ago) [a3d27c1f-45d2-466e-8675-8aed0d0fa6ee]
  52. Summarize the user's primary intent or goal in this conversation in ONE sentence (max 80 characte... (9 days ago) [f287c0ad-a037-4568-b2ac-e3588f8c0491]
  53. # Gemini CLI Packet - Structure Before ChatGPT Review 2026-05-12 v0 ## 1. Role and Boundary ```te... (10 days ago) [fb755890-aa10-4249-8beb-bb8c42d9d329]
  54. # Gemini CLI Packet - Active Surface Selection-Cost Test 2026-05-12 v0 ## 1. Role and Boundary ``... (10 days ago) [f293cdde-37f2-421e-8c1f-7fc8feaa514d]
  55. # Gemini CLI Packet - Active Surface Selection-Cost Test v1 Visible Failure 2026-05-12 ## 1. Sour... (10 days ago) [1863eb6e-84a5-43ec-a9d6-8742921d4b24]
  56. # Gemini CLI Packet - Visible Failure Packet Test v2 Strict Full Package 2026-05-12 ## 1. Role an... (10 days ago) [82ecd70a-1ed7-4be8-b576-c4eaf7e83860]
  57. Reply with exactly: GEMINI_SMOKE_OK (10 days ago) [3381003d-f2bd-4e79-bfd0-5df16b93f607]
  58. Reply with exactly: GEMINI_SMOKE_OK (10 days ago) [a69e1bd3-83fb-4e3a-aaa5-5a54cef73566]
  59. Establish a Surface Language Downshift rule to prevent surface terms as structure. (9 days ago) [72361e1b-f202-48a5-a70e-9ef9f87d771d]
  60. Perform the bounded material intake observation for cycle_004_bounded_material_intake_thread_002 ... (9 days ago) [063ef479-c03a-4446-b087-3dd2099b0745]
  61. # Gemini Mode Selector Stress Test Packet v0 # 05-15 Mode-selection Probe ## 1. Status Status: GE... (7 days ago) [9fb1ff6d-5b3a-4a81-b116-a480c73635a4]
  62. Conduct stress tests and gap analysis on the VectorFL vessel framework. (6 days ago) [00ba25a0-a0aa-49be-8171-872cf71eff03]
  63. # Gemini Vessel Working Standard Fresh Check Packet v0 ## 0. Mission Verify whether the vessel wo... (6 days ago) [1ec002cc-d233-492c-b4b6-fb8a3cc12314]
  64. # Gemini Vessel Working Standard Fresh Check Packet v0 ## 0. Mission Verify whether the vessel wo... (6 days ago) [61b6bbbe-a2ed-4428-9676-adbfb59f0273]
  65. # Gemini Vessel Flow Performance Test Packet v0 ## 0. Mission Generate diverse messy examples and... (6 days ago) [9e1f4604-a99b-4e20-b074-513797d6145f]
  66. # Gemini Stage 1 Diff Audit Maturation Packet v0 ## 0. Mission Evaluate the Stage 1 local diff-au... (6 days ago) [bc3558f0-aa91-4201-b66d-ae30b25cea41]
  67. # Gemini Diff Audit Component Readiness Review Packet v0 ## 0. Mission Review the Stage 1 diff-au... (6 days ago) [0fd8dba5-adab-4d7e-9a07-ed9a56057ea6]
  68. You are running a bounded Gemini-only lite-output test for VectorFL bridge topology. STRICT SCOPE... (5 days ago) [79a300c2-548b-4715-9a7d-be549f951c6f]
  69. You are running Option 3A: a bounded combined bridge rehearsal for VectorFL tool topology. STRICT... (5 days ago) [bd19bbc7-14f7-4c1f-b81d-4c64fdc05bff]
  70. You are Gemini running S5_GEMINI_SPACE_MEDIATED_RUN for a bounded VectorFL/Hermes packet. Read th... (3 days ago) [1096d065-093a-4369-8d97-6bbd147f263e]
  71. Build a reproducible, program-interface-based local operating spine (Level 2.0). (1 day ago) [ac7f00f2-ded9-4033-99b3-d01563d85438]
  72. Generate review-prep materials for Input Localization M3 without status change. (10 hours ago) [f6f39096-c3f3-468f-90c3-b72a913ca016]
  73. Design a cross-tool relay system for Gemini, Hermes, and Codex workflows. (15 minutes ago) [4756b1d4-ebdf-45bd-8311-d861a62d3961]
```

## Recommended Invocation Pattern

Hermes should not call Codex/Gemini as free-form assistants. Use packet-bound commands only.

### Codex H4 review-only command template

```bash
codex exec --cd /Users/sungsookim/universe/vectorfl_replica   --sandbox read-only   --ask-for-approval never   "Read app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260523_h1_h2_stage1_verification/codex_h4_review_only_prompt_card.md and return review-only output in the required shape. Do not edit files."
```

If this Codex version does not accept `--cd` or `--sandbox read-only`, use the equivalent flags shown by `codex exec --help` and keep the same constraints: read-only, no file edits, no approval drift.

### Gemini H3 gap-scan command template

```bash
gemini --approval-mode plan   --prompt "Read the declared shared-space files and the Gemini personal program gap scan packet. Return broad findings only. No repo mutation. Classification labels only: READY_FOR_CONTRACT, CANDIDATE_MATERIAL, WATCH, STOP, OUT_OF_SCOPE."
```

For Gemini, prefer `--approval-mode plan` for read-only/plan behavior. Do not use `--yolo` for VectorFL work.

## Required Output Storage

For any real invocation, Hermes must save:

```text
raw_output.md
lite_output.md
receipt.md
commands_run.md
codex_recovery_or_review_return.md
```

under a task-specific subfolder of:

```text
app/work/space-skill-sandbox/relay/runs/hermes_centered/
```

## Setup State

- Codex CLI exists at `/usr/local/bin/codex`.
- Gemini CLI exists at `/usr/local/bin/gemini`.
- Hermes CLI exists at `/Users/sungsookim/.local/bin/hermes`.
- Hermes auth list shows openai-codex credential present.
- Gemini CLI auth was not proven by a model call; no Gemini model execution was performed.

## HOLD

- real Codex execution: HOLD until packet-approved
- real Gemini execution: HOLD until packet-approved
- package install: NO
- Hermes config mutation: NO
- login/auth mutation: NO
- network/model API call: NO in this setup discovery
- authority mutation: NO
- promotion: HOLD
