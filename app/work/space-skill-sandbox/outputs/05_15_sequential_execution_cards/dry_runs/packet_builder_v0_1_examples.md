# Packet Builder v0.1 Examples
# Codex / Gemini / API-CLI

## 1. Status

Status:
  MATERIALIZED_FROM_SOURCE_25_WITH_WATCH

Source:
  `25.md`

Purpose:
  Materialize three Packet Builder v0.1 dry-run examples by tool mode and risk focus.

Not:
  execution
  dispatch
  credential/API use
  command execution
  file creation outside this candidate artifact
  baseline promotion

## 2. Minimal Form

target_tool:
  [tool]

tool_mode:
  execution-capable / broad-reading / API-data-transfer / browser-observation / memory-retrieval / mixed-framework / documentation-reference / unknown

task:
  [bounded work]

smallest_anchor:
  [minimum context]

allowed:
  [allowed actions/context]

forbidden:
  [forbidden actions/context]

risk_focus:
  [mode-specific risk]

WATCH:
  [drift]

HOLD:
  [boundaries]

return_format:
  [Short Return / Analysis Return / Tool Use Decision / Return Packet]

hard_stop:
  [stop condition]

post_return_route:
  Return Packet -> Maturation Queue Item -> Daily Circulation Loop

## 3. Packet A - Codex Bounded Inspection

target_tool:
  Codex

tool_mode:
  execution-capable

risk_focus:
  file / command / patch / repo-affordance drift

task:
  Inspect whether the Daily Circulation Loop v0 minimal form is usable as a lightweight daily operating surface.

user_purpose:
  Check usability without expanding it into workflow, schema, or repo structure.

smallest_anchor:
  Daily Circulation Loop v0 Minimal Use Form
  Maturation Queue Item minimal fields
  Packet Builder v0.1 tool-mode distinction

allowed:
  read provided anchor text
  identify ambiguity or missing fields
  judge whether loop is too heavy or usable
  return suggestions in chat only

forbidden:
  file creation
  file modification
  command execution
  broad repo search
  AGENTS.md / SKILL.md update
  eval creation
  workflow/schema/registry proposal as final
  baseline promotion
  current-position update
  output_manifest update

WATCH:
  Codex capability -> permission
  repo affordance -> task authority
  missing field -> schema expansion
  review result -> structural approval
  usable surface -> workflow

HOLD:
  execution
  file write
  repo mutation
  promotion
  automation

return_format:
  Short Return Packet

hard_stop:
  Stop before reading outside provided anchors, editing files, or proposing repo-wide structure.

post_return_route:
  Return Packet -> Maturation Queue Item -> Daily Circulation Loop

verdict:
  PACKET_A_CODEX_DRY_RUN_PASSED_WITH_WATCH

## 4. Packet B - Gemini Broad Reading

target_tool:
  Gemini

tool_mode:
  broad-reading

risk_focus:
  synthesis / recommendation / adoption / ontology drift

task:
  Compare the VectorFL circulation metaphor with selected external agent-system descriptions and extract only recurring risks relevant to internal maturation automation.

user_purpose:
  Improve VectorFL's ability to mature external-tool results without adopting any external framework.

smallest_anchor:
  selected external excerpts only
  VectorFL principle: external tools are carriers, not authority
  current loop: Input -> Queue Item -> Daily Circulation -> Packet Builder -> External Tool -> Return Packet -> Queue Item

allowed:
  read selected excerpts
  summarize recurring risks
  compare at risk-pattern level
  separate observation from inference
  state uncertainty
  return reusable WATCH candidates

forbidden:
  recommend adoption as final
  propose migration
  create workflow/schema/registry
  turn external terminology into VectorFL ontology
  claim final truth
  propose file edits
  create evals
  baseline promotion

WATCH:
  fluent synthesis -> truth
  recommendation -> adoption
  external framework -> VectorFL architecture
  external terminology -> ontology
  recurring risk -> policy
  dashboard/control plane -> operating surface

HOLD:
  framework adoption
  architecture migration
  memory migration
  dashboard creation
  workflow/schema/registry creation
  baseline promotion

return_format:
  Analysis Return Packet

hard_stop:
  Stop before implementation recommendation, architecture change, or external term promotion.

post_return_route:
  Analysis Return Packet -> Maturation Queue Item -> Daily Circulation Loop

verdict:
  PACKET_B_GEMINI_DRY_RUN_PASSED_WITH_WATCH

## 5. Packet C - API / CLI High-risk Review

target_tool:
  xurl-like API CLI

tool_mode:
  API-data-transfer

risk_focus:
  credential / endpoint / account / upload / retention drift

task:
  Review the tool documentation only and determine whether any future use could be bounded safely.

user_purpose:
  Understand the tool boundary without executing it, checking auth status, reading credentials, calling APIs, or touching accounts.

smallest_anchor:
  tool README or SKILL.md excerpt only

allowed:
  read documentation only
  list claimed capabilities
  identify credential/API/account/upload boundaries
  decide REFERENCE_ONLY / BOUNDED_TEST_CANDIDATE / HOLD
  propose Pre-use Packet requirements if future execution is desired

forbidden:
  install
  execute command
  auth status check
  read local credential store
  use token
  call API
  read account data
  mutate account
  send DM
  upload media
  write files
  automation

WATCH:
  small CLI -> harmless assumption
  auth status -> safe check
  credential file existence -> consent
  API capability -> permission
  account read -> harmless observation
  JSON output -> truth
  platform response -> recovered judgment

HOLD:
  command execution
  credential/token use
  API/network call
  account read/write
  upload
  local auth store access
  automation
  file write

return_format:
  Tool Use Decision Packet

hard_stop:
  Stop before auth status, credential access, API call, account read/write, or upload.

post_return_route:
  Tool Use Decision Packet -> Maturation Queue Item -> Daily Circulation Loop

verdict:
  PACKET_C_API_CLI_DRY_RUN_PASSED_WITH_WATCH

## 6. Recovered Judgment

Packet Builder v0.1 should be tool-mode aware:

- execution-capable: constrain files, commands, writes, repo affordance
- broad-reading: constrain synthesis, recommendation, adoption, ontology drift
- API-data-transfer: constrain credentials, endpoints, account access, upload, retention

`STATUS: PACKET_BUILDER_V0_1_EXAMPLES_MATERIALIZED_WITH_WATCH`
