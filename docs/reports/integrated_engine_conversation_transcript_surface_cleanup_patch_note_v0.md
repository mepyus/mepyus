# Integrated Engine Conversation Transcript Surface Cleanup Patch Note v0

## verdict
PASS_WITH_NOTE

## purpose
The prior MVP proved that the current UI could send a Codex turn through the existing integrated-engine CLI session API, but the screen still felt like reading returned reports inside mixed panels.

This patch cleans the page grammar first, then adds a central conversation transcript layer.

## changed implementation

- `app/ui/integrated_engine/VectorFLIntegrationShell.tsx`
  - Removed the older mixed front-surface elements:
    - lifecycle strip
    - broad activity rail
    - goal setup panel
    - VectorFL digest card row
    - legacy flow/log/x-ray front exposure
  - Reframed the page as:
    - left: current package context
    - center: conversation workbench
    - right: engine position sidebar
  - Kept support context and raw state behind details sections.

- `app/ui/integrated_engine/CliHostControlPanel.tsx`
  - Added a `ConversationTranscript` layer.
  - Adds visible conversation turns for:
    - user message
    - engine preflight
    - CLI handoff
    - Codex return
    - VectorFL postflight reread
  - Keeps packet controls, recent turns, and route marking in support/inspector sections.

## validation

- `npm run build` passed in `app/ui/integrated_engine`.
- `http://127.0.0.1:5173/` responded.
- `http://127.0.0.1:5173/api/vectorfl-engine/state` responded through the Vite proxy.

## bounded result

The main screen is now less mixed:

```text
current package context
-> conversation transcript / composer
-> engine position sidebar
```

The user no longer has to treat the main surface primarily as a returned-output reading board. A submitted message now becomes a transcript sequence:

```text
you
-> engine preflight
-> cli handoff
-> codex
-> VectorFL reread
```

## remaining limits

- This is still request/return based, not streaming PTY output.
- Conversation turns are local UI state; they are not yet persisted as a durable transcript.
- Gemini CLI is still not attached.
- Browser hand-use is still needed to judge whether the transcript now feels conversational enough.

## next valid action

Run one small browser turn from the center composer and check whether the screen now feels like a conversation rather than a report reader.
