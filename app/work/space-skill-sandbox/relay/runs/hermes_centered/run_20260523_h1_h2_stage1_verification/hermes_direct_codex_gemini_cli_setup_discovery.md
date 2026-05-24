# Hermes Direct Codex/Gemini CLI Setup Discovery

status: LOCAL_DISCOVERY_ONLY_WITH_HOLD

## Purpose

Track the separate setup lane for letting Hermes invoke Codex CLI and Gemini CLI directly, while preserving role boundaries.

## Commands Run

### which_hermes_codex_gemini

```bash
for c in hermes codex gemini npx npm node; do printf '%s=' "$c"; command -v "$c" || true; done
```

exit_code: 0

```text
hermes=/Users/sungsookim/.local/bin/hermes
codex=/usr/local/bin/codex
gemini=/usr/local/bin/gemini
npx=/usr/local/bin/npx
npm=/usr/local/bin/npm
node=/usr/local/bin/node
```

### hermes_version

```bash
hermes --version 2>&1 || true
```

exit_code: 0

```text
Hermes Agent v0.12.0 (2026.4.30)
Project: /Users/sungsookim/.hermes/hermes-agent
Python: 3.11.15
OpenAI SDK: 2.33.0
Update available: 1768 commits behind — run 'hermes update'
```

### codex_version

```bash
codex --version 2>&1 || true
```

exit_code: 0

```text
codex-cli 0.133.0
```

### gemini_version

```bash
gemini --version 2>&1 || true
```

exit_code: 0

```text
0.42.0
```

### codex_help_head

```bash
codex --help 2>&1 | sed -n '1,80p' || true
```

exit_code: 0

```text
Codex CLI

If no subcommand is specified, options will be forwarded to the interactive CLI.

Usage: codex [OPTIONS] [PROMPT]
       codex [OPTIONS] <COMMAND> [ARGS]

Commands:
  exec            Run Codex non-interactively [aliases: e]
  review          Run a code review non-interactively
  login           Manage login
  logout          Remove stored authentication credentials
  mcp             Manage external MCP servers for Codex
  plugin          Manage Codex plugins
  mcp-server      Start Codex as an MCP server (stdio)
  app-server      [experimental] Run the app server or related tooling
  remote-control  [experimental] Manage the app-server daemon with remote control enabled
  app             Launch the Codex desktop app (opens the app installer if missing)
  completion      Generate shell completion scripts
  update          Update Codex to the latest version
  doctor          Diagnose local Codex installation, config, auth, and runtime health
  sandbox         Run commands within a Codex-provided sandbox
  debug           Debugging tools
  apply           Apply the latest diff produced by Codex agent as a `git apply` to your local
                  working tree [aliases: a]
  resume          Resume a previous interactive session (picker by default; use --last to continue
                  the most recent)
  fork            Fork a previous interactive session (picker by default; use --last to fork the
                  most recent)
  cloud           [EXPERIMENTAL] Browse tasks from Codex Cloud and apply changes locally
  exec-server     [EXPERIMENTAL] Run the standalone exec-server service
  features        Inspect feature flags
  help            Print this message or the help of the given subcommand(s)

Arguments:
  [PROMPT]
          Optional user prompt to start the session

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

      --remote <ADDR>
          Connect the TUI to a remote app server endpoint.
          
          Accepted forms: `ws://host:port`, `wss://host:port`, `unix://`, or `unix://PATH`.

      --remote-auth-token-env <ENV_VAR>
          Name of the environment variable containing the bearer token to send to a remote app
          server websocket

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
```

### gemini_help_head

```bash
gemini --help 2>&1 | sed -n '1,80p' || true
```

exit_code: 0

```text
Usage: gemini [options] [command]

Gemini CLI - Defaults to interactive mode. Use -p/--prompt for non-interactive (headless) mode.

Commands:
  gemini mcp                   Manage MCP servers
  gemini extensions <command>  Manage Gemini CLI extensions.  [aliases: extension]
  gemini skills <command>      Manage agent skills.  [aliases: skill]
  gemini hooks <command>       Manage Gemini CLI hooks.  [aliases: hook]
  gemini gemma                 Manage local Gemma model routing
  gemini [query..]             Launch Gemini CLI  [default]

Positionals:
  query  Initial prompt. Runs in interactive mode by default; use -p/--prompt for non-interactive.

Options:
  -d, --debug                     Run in debug mode (open debug console with F12)  [boolean] [default: false]
  -m, --model                     Model  [string]
  -p, --prompt                    Run in non-interactive (headless) mode with the given prompt. Appended to input on stdin (if any).  [string]
  -i, --prompt-interactive        Execute the provided prompt and continue in interactive mode  [string]
      --skip-trust                Trust the current workspace for this session.  [boolean] [default: false]
  -w, --worktree                  Start Gemini in a new git worktree. If no name is provided, one is generated automatically.  [string]
  -s, --sandbox                   Run in sandbox?  [boolean]
  -y, --yolo                      Automatically accept all actions (aka YOLO mode, see https://www.youtube.com/watch?v=xvFZjo5PgG0 for more details)?  [boolean] [default: false]
      --approval-mode             Set the approval mode: default (prompt for approval), auto_edit (auto-approve edit tools), yolo (auto-approve all tools), plan (read-only mode)  [string] [choices: "default", "auto_edit", "yolo", "plan"]
      --policy                    Additional policy files or directories to load (comma-separated or multiple --policy)  [array]
      --admin-policy              Additional admin policy files or directories to load (comma-separated or multiple --admin-policy)  [array]
      --acp                       Starts the agent in ACP mode  [boolean]
      --experimental-acp          Starts the agent in ACP mode (deprecated, use --acp instead)  [boolean]
      --allowed-mcp-server-names  Allowed MCP server names  [array]
      --allowed-tools             [DEPRECATED: Use Policy Engine instead See https://geminicli.com/docs/core/policy-engine] Tools that are allowed to run without confirmation  [array]
  -e, --extensions                A list of extensions to use. If not provided, all extensions are used.  [array]
  -l, --list-extensions           List all available extensions and exit.  [boolean]
  -r, --resume                    Resume a previous session. Use "latest" for most recent or index number (e.g. --resume 5)  [string]
      --session-id                Start a new session with a manually provided UUID.  [string]
      --list-sessions             List available sessions for the current project and exit.  [boolean]
      --delete-session            Delete a session by index number (use --list-sessions to see available sessions).  [string]
      --include-directories       Additional directories to include in the workspace (comma-separated or multiple --include-directories)  [array]
      --screen-reader             Enable screen reader mode for accessibility.  [boolean]
  -o, --output-format             The format of the CLI output.  [string] [choices: "text", "json", "stream-json"]
      --raw-output                Disable sanitization of model output (e.g. allow ANSI escape sequences). WARNING: This can be a security risk if the model output is untrusted.  [boolean]
      --accept-raw-output-risk    Suppress the security warning when using --raw-output.  [boolean]
  -v, --version                   Show version number  [boolean]
  -h, --help                      Show help  [boolean]
```

### hermes_config_path

```bash
hermes config path 2>&1 || true
```

exit_code: 0

```text
/Users/sungsookim/.hermes/config.yaml
```

### hermes_auth_list_head

```bash
hermes auth list 2>&1 | sed -n '1,120p' || true
```

exit_code: 0

```text
openai-codex (1 credentials):
  #1  device_code          oauth   device_code ←

openrouter (1 credentials):
  #1  OPENROUTER_API_KEY   api_key env:OPENROUTER_API_KEY ←
```

## Interpretation

- Hermes may be the main execution playground, but direct Codex/Gemini CLI invocation must stay packet-bound.
- Codex CLI lane should be review-only / structural guard unless a separate implementation packet explicitly grants edits.
- Gemini CLI lane should be broad scan / asset archaeology / gap scan, not authority.
- Any direct CLI bridge must preserve raw/lite/receipt/return split and not collapse model output into truth.

## Setup TODO

1. Confirm installed CLI names and auth state.
2. If Codex CLI is missing or unauthenticated, use Hermes documented path first: `hermes login --provider openai-codex` for Hermes provider auth, and separately install/login Codex CLI only if required by the bridge packet.
3. If Gemini CLI is missing, install/select an approved Gemini CLI path only after user approves package install or existing local binary is found.
4. Create packet-bound smoke test commands:
   - Codex: review-only prompt, no repo mutation.
   - Gemini: gap-scan prompt, no repo mutation.
5. Store each invocation under Hermes-centered run folder with commands_run, raw output, lite output, receipt, and Codex recovery review.

## HOLD

- no Hermes config mutation performed here
- no package install performed here
- no login/auth mutation performed here
- no real Codex/Gemini model execution performed here
- no VectorFL authority mutation
- no promotion
