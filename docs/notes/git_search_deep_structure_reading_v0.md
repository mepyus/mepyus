# Git Search Deep Structure Reading v0

## Purpose

This note does not extract features first.
It records how the reference folders are spatially organized, how files are shaped, and where the connection lines actually run.

The goal is to preserve a structure-first reading surface before any direct translation into our repo.

## Reading Method

The useful order is:

1. Read the folder as a space.
2. Read the dominant file forms inside that space.
3. Read the connection lines between files and subspaces.
4. Only after that, translate the structure into our own layered spaces.

This matters because reading code too early at the file-logic level tends to collapse the repo into local implementation details before its structural roles are visible.

## Repo Clusters

### `everything-claude-code-main`

This repo is not just a Claude extension bundle.
It is a multi-surface operating bundle.

At the folder level, the main clue is that it duplicates operating surfaces across harnesses:

- `.claude`
- `.codex`
- `.cursor`
- `.kiro`
- `.opencode`
- `agents`
- `commands`
- `contexts`
- `hooks`
- `manifests`
- `rules`
- `scripts`
- `skills`

This means the repo is designed around portable operating surfaces rather than a single runtime core.

#### Dominant file forms

- Markdown command surfaces in `commands/`
- Markdown skill surfaces in `skills/*/SKILL.md`
- JSON hook declarations in `hooks/hooks.json`
- JS CLI entrypoints in `scripts/*.js`
- JS library modules in `scripts/lib/**`
- SQLite state-store modules in `scripts/lib/state-store/**`

#### Structural center

The structural center is not one runtime file.
It is the relation between:

- `scripts/ecc.js`
- `scripts/session-inspect.js`
- `scripts/sessions-cli.js`
- `scripts/lib/session-adapters/registry.js`
- `scripts/lib/session-manager.js`
- `scripts/lib/orchestration-session.js`
- `scripts/lib/observer-sessions.js`
- `scripts/lib/state-store/index.js`

#### Connection lines

The main line is:

`ecc.js` -> subcommand scripts -> lib modules -> state store / adapters / orchestration snapshots

That means the repo behaves like a command-routed operating shell, not a monolithic app server.

The secondary line is:

`session-inspect.js` -> adapter registry -> canonical snapshot

This is important because the repo does not treat one session format as canonical.
It treats canonical inspection as an adapter product.

The third line is:

`orchestration-session.js` -> worker status/task/handoff markdown + tmux panes -> unified snapshot

This is especially valuable as a reference because it reconstructs one operational view from several low-level surfaces instead of assuming one source of truth file.

The fourth line is:

`observer-sessions.js` -> project root resolution -> project-scoped observer lease files

This shows a scoped-memory pattern:
not global state first, but project-scoped operating state.

#### What this repo structurally teaches

- A repo can be organized around operating surfaces rather than one core runtime.
- Adapters can be the canonical inspection surface.
- Operational state can be reconstructed from several files instead of stored in one perfect object.
- Skill, hook, command, and session layers can coexist without becoming the same thing.

### `openclaw-main`

This repo reads very differently.
It is not a multi-surface operating bundle.
It is a product/control-plane/runtime system with strong internal decomposition.

At the folder level, the important spaces are:

- `src/gateway`
- `src/routing`
- `src/sessions`
- `src/security`

The naming already shows that the repo wants explicit subdomain boundaries, not one giant assistant runtime.

#### Dominant file forms

- TypeScript runtime modules
- TypeScript tests paired closely with runtime files
- Focused utility files with narrow names
- Event and policy files split away from transport files

#### Structural center

The structural center is not one CLI script.
It is the separation between:

- ingress and serving in `src/gateway`
- route resolution in `src/routing`
- session identity and lifecycle in `src/sessions`
- audit/policy enforcement in `src/security`

`gateway` is large, but it is not a blob.
It is an assembly surface sitting above smaller specialized domains.

#### Connection lines

The route line:

`routing/resolve-route.ts` -> bindings + session-key helpers + normalized identity -> resolved route

This file shows that routing is treated as its own logic domain, not as a side effect inside server code.

The session identity line:

`routing/session-key.ts` -> normalized agent/account/peer forms -> stable session keys

This is important because it means session identity is formalized before runtime behavior attaches to it.

The session event line:

`sessions/session-lifecycle-events.ts`
`sessions/transcript-events.ts`

These are tiny files, but structurally they matter a lot.
They define event channels as first-class spaces instead of burying them in storage code.

The audit line:

`security/audit.ts` -> config + gateway auth + fs permissions + tool policy + deep/nondeep audit modules

This shows a control-plane style audit aggregator.
Security is not one check.
It is a report-building subsystem with severity, remediation, and optional deep probing.

The composition line:

`gateway/server-chat.ts` -> config + heartbeat visibility + session row loaders + lifecycle persistence + session utils

This is where upstream subsystems meet, but the file still imports them as modules rather than re-owning their logic.

#### What this repo structurally teaches

- Domain boundaries can be made visible through folder structure alone.
- Session identity, routing, security, and gateway serving should not collapse into one layer.
- Event surfaces can be tiny files but still represent important architectural seams.
- A control-plane audit layer can aggregate multiple lower-level checks without replacing them.

### `claw-code-main`

This repo is closer to a runtime substrate.

Its meaningful spaces are:

- `src/`
- `rust/crates/runtime/src/`
- `tests/`

The Python layer gives a thin operating surface, but the deeper runtime logic sits in Rust.

#### Dominant file forms

- Thin Python wrappers and CLIs
- Rust runtime/session/permissions/hooks/compact modules
- Tests attached to porting/runtime behavior

#### Connection lines

The main line is:

Python entry -> runtime wrapper -> Rust session/conversation loop

The important sub-lines are:

- `session.rs` for structured session blocks
- `conversation.rs` for turn/tool iteration
- `hooks.rs` for runtime hook execution
- `permissions.rs` for allow/deny/escalation separation
- `compact.rs` for continuation summary

#### What this repo structurally teaches

- Internal runtime substrate can stay coherent when session, hook, permission, and compaction are separate modules.
- A thin outer layer can still front a strong inner runtime layer.
- Continuation and fallback reasons deserve explicit modules.

### `claude-code-main`

This repo is much more extension-oriented.

Its meaningful spaces are:

- `plugins/`
- `.claude/`
- `.claude-plugin/`
- `examples/`
- `scripts/`

#### Dominant file forms

- Plugin readmes
- Hook declarations
- Hook scripts
- Rule-engine Python modules
- Small example validators

#### Connection lines

The important line is:

host stop/hook event -> hook script -> repeat/block/warn behavior

This means the repo is structurally about host interception, not internal runtime ownership.

#### What this repo structurally teaches

- External orchestration can sit on top of an existing assistant runtime.
- Small validators and hook rules can be useful even when they are not part of core logic.
- Loop behavior can be imposed from outside the core.

### `ralph-main`

This repo is small, but structurally sharp.

Its meaningful spaces are:

- root shell scripts
- skill surface
- progress memory artifacts

#### Connection lines

task prompt -> fresh run -> progress artifact -> next fresh run

This repo is useful as a minimal repetition discipline reference.

At the folder level, the core space is tiny:

- `ralph.sh`
- `prompt.md` / `CLAUDE.md`
- `prd.json.example`
- `skills/prd/`
- `skills/ralph/`

There is also a `flowchart/` folder, but structurally that is explanation and visualization space rather than loop core.

#### Dominant file forms

- One bash loop script
- One prompt template per tool surface
- One JSON task artifact
- One append-only progress artifact
- Small skill folders

#### Structural center

The structural center is not a runtime module graph.
It is the very small chain:

`ralph.sh` -> prompt surface -> fresh tool run -> `prd.json` + `progress.txt` update -> next fresh run

#### What this repo structurally teaches

- A repetition system can stay coherent with almost no internal architecture if the artifacts are explicit.
- The memory boundary can be externalized into files instead of held in process.
- A loop can be defined more by disciplined artifacts than by a complex runtime.

### `autoresearch-master`

This repo is also small, but its structure is disciplined.

The key spatial trait is that the editable surface and the evaluation surface are intentionally narrowed.

#### Connection lines

program contract -> one change lane -> fixed evaluation -> keep/discard decision

This makes it more of an experiment-discipline reference than a runtime reference.

At the folder level, this repo is intentionally narrow:

- `program.md`
- `prepare.py`
- `train.py`
- `analysis.ipynb`

The important thing is not module richness.
It is the deliberate restriction of the editable and evaluable surfaces.

#### Dominant file forms

- One contract file
- One data-prep script
- One training script
- One analysis notebook

#### Structural center

The center is:

`program.md` -> constrained mutation surface -> fixed training/eval pipeline -> result inspection

#### What this repo structurally teaches

- Narrowness itself can be an architectural asset.
- Experiment loops get clearer when the editable surface is intentionally small.
- A repo can function as a discipline machine without needing many subsystems.

### Additional Reading: `claw-code-main`

One more structural point is worth making explicit.

At the folder level, `claw-code-main` is not just `src/`.
It is a two-story system:

- broad Python operating surface under `src/`
- deeper Rust substrate under `rust/crates/*`

The Rust side is already decomposed by runtime concerns:

- `api`
- `claw-cli`
- `commands`
- `compat-harness`
- `lsp`
- `plugins`
- `runtime`
- `server`
- `tools`

This means the repo is not merely a port.
It is a layered runtime project with a thin outer operating layer and a stronger inner systems layer.

#### Dominant file forms

- Python wrappers and entrypoints
- Rust crates with narrow concerns
- tests alongside both layers

#### Structural center

The connection line is:

Python surface -> runtime wrapper / query layer -> Rust runtime crates

So even when the Python side looks broad, the structural truth of the repo is still in the crate split.

#### What this repo structurally teaches

- A repo can preserve a broad operator-facing surface while moving real invariants into a substrate layer.
- Crate boundaries can reveal the actual architectural center better than top-level CLI files.
- Thin wrappers and deep substrate can coexist without being the same design layer.

## Cross-Repo Structural Contrast

### Bundle space vs product space

`everything-claude-code-main` is a bundle space.
It gathers many operating surfaces and lets commands, hooks, skills, and session tools coexist.

`openclaw-main` is a product space.
It decomposes one product/control-plane runtime into explicit internal domains.

### Adapter-first inspection vs domain-first decomposition

`everything-claude-code-main` tends to solve heterogeneity with adapters.

`openclaw-main` tends to solve complexity with domain boundaries.

### Script-routed shell vs module-routed runtime

`everything-claude-code-main` is script-routed:

CLI -> script -> library -> state/inspection surface

`openclaw-main` is module-routed:

domain module -> composed gateway/runtime behavior

### External operating layer vs internal runtime substrate

`claude-code-main` and much of `everything-claude-code-main` show how to build an operating layer around a host.

`claw-code-main` and `openclaw-main` show how to keep the internal runtime/core domains explicit.

## Why This Matters For Us

Before deciding what to import, we should decide what kind of structure we are reading:

- operating bundle
- runtime substrate
- control-plane decomposition
- external orchestration layer
- bounded experiment loop

If we skip that step, we tend to copy a function shape from the wrong spatial layer.

## Import-Reading Guidance

When a reference looks useful, the first questions should be:

1. Is this space an engine, a control plane, a hook layer, or an experiment lane?
2. Is the useful thing here a file, or the relation between files?
3. Is the canonical unit a runtime object, an adapter snapshot, a state artifact, or a report?
4. Does the repo solve complexity by decomposition, by adapters, by orchestration scripts, or by loop discipline?

Only after those are answered should we translate it into our own spaces.

## Immediate High-Value Structural References

- `everything-claude-code-main/scripts/ecc.js`
- `everything-claude-code-main/scripts/session-inspect.js`
- `everything-claude-code-main/scripts/lib/orchestration-session.js`
- `everything-claude-code-main/scripts/lib/observer-sessions.js`
- `everything-claude-code-main/scripts/lib/state-store/index.js`
- `openclaw-main/src/routing/resolve-route.ts`
- `openclaw-main/src/routing/session-key.ts`
- `openclaw-main/src/sessions/session-lifecycle-events.ts`
- `openclaw-main/src/sessions/transcript-events.ts`
- `openclaw-main/src/security/audit.ts`
- `openclaw-main/src/gateway/server-chat.ts`

These are useful not because they match our code directly, but because they make the repo's structural seams visible.
