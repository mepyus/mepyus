# Integrated Engine Opencode-Like CLI Surface MVP Patch Note v0

## verdict
PASS_WITH_NOTE

## purpose
This patch moves the current integrated-engine screen toward an opencode-like operating surface:

- one main conversation workbench
- direct Codex CLI handoff through the existing integrated-engine API
- visible engine-position log
- right-side process sidebar
- deep details kept in inspector/support sections

This is not a full CLI automation layer, not a Gemini adapter, not multi-handler orchestration, and not upper/lower unification.

## changed implementation

- `app/ui/integrated_engine/CliHostControlPanel.tsx`
  - Reframed the panel as a dark live composer.
  - Added a local `engine position log` rail.
  - Records visible events for refresh, preflight packet formation, CLI handoff, return receipt, follow-up loading, and route marking.
  - Keeps packet controls and recent turns available, but demoted to support/inspector details.

- `app/ui/integrated_engine/VectorFLIntegrationShell.tsx`
  - Added a right-side `EnginePositionSidebar`.
  - Shows the current flow as `input -> preflight -> cli handoff -> postflight`.
  - Keeps legacy flow/log/x-ray material inside inspector details.
  - Preserves the one-handler package and existing CLI/session API.

## execution checklist

1. Read current integrated-engine UI and CLI-host implementation.
2. Confirm existing backend route:
   - `/api/vectorfl-engine/state`
   - `/api/vectorfl-engine/actions/cli-session/run`
   - `/api/vectorfl-engine/actions/cli-session/mark`
3. Patch the current UI only.
4. Preserve the existing Vite proxy to `http://127.0.0.1:8421`.
5. Build the UI.
6. Check active dev/API endpoints.

## validation result

- `npm run build` in `app/ui/integrated_engine` passed.
- `http://127.0.0.1:8421/api/vectorfl-engine/state` responded.
- `http://127.0.0.1:5173/` responded.
- `http://127.0.0.1:5173/api/vectorfl-engine/state` responded through the Vite proxy.

## bounded result

The screen is now closer to:

```text
main conversation workbench
+ engine position sidebar
+ compact event/activity rail
+ support/inspector detail
```

instead of:

```text
many parallel verification panels
```

## remaining limits

- The UI still uses the existing Codex backend path only.
- Gemini CLI is not attached yet.
- The CLI run is still request/return based, not full streaming PTY.
- The engine position log is currently local UI state plus latest return state, not a persisted event stream.
- Human browser testing is still needed to judge actual feel.

## next valid action

Open the current app and run one small browser-based Codex turn from the main composer. Verify whether:

- the input feels like the front door,
- the engine position log visibly changes,
- the right sidebar helps locate the current process stage,
- latest return can be loaded back into VectorFL without feeling like a panel maze.
