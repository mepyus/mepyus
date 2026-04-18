# VectorFL Dual Surface App

## role

This is the current React/Vite program shell for the VectorFL user surface and VectorFL surface.

It is not the Python engine surface.

Current split:

- User surface: direct operating / assignment / team-role setup surface.
- VectorFL surface: line, relation, gap, genealogy, export, and reflux reading surface.
- Engine surface: Python viewer surface at `/vectorfl-engine/operate`.

## entrypoints

Source entry:

- `src/main.tsx`

Current imported surface source:

- `../vectorfl_dual_surface.tsx`

Runtime URL in local development:

- `http://127.0.0.1:5174/`

Engine surface URL:

- `http://127.0.0.1:8421/vectorfl-engine/operate`

## commands

Run dev server:

```bash
npm run dev
```

Build:

```bash
npm run build
```

Preview built app:

```bash
npm run preview
```

## dependency boundary

This app currently reuses the existing dependency tree through:

- `node_modules -> ../../../references/WashTank/node_modules`

This was chosen to avoid a fresh install during the current stabilization pass.

Do not assume this is the final dependency strategy. When this app becomes a stable program package, replace the symlink dependency with a normal package install or workspace-level package manager decision.

## design boundary

Tailwind v4 is now part of the Vite pipeline:

- `vite.config.ts` uses `@tailwindcss/vite`
- `src/styles.css` imports `tailwindcss`
- `src/styles.css` also defines the current Paperclip-aligned VectorFL token overrides

Do not rebuild a large hand-written Tailwind clone in `src/styles.css`.

Use `src/styles.css` for:

- global font/background
- design token overrides
- minimal local support for the temporary UI wrappers

Use Tailwind classes in TSX for layout and component styling.

## UI wrapper boundary

The local files in `src/components/ui/` are temporary shadcn-style compatibility wrappers.

They exist because the imported TSX surface expects:

- `@/components/ui/card`
- `@/components/ui/button`
- `@/components/ui/badge`
- `@/components/ui/input`
- `@/components/ui/textarea`
- `@/components/ui/tabs`
- `@/components/ui/dialog`

Keep these wrappers thin. They should not override the imported surface so strongly that the original design language disappears.

## generated output boundary

`dist/` is generated build output and is ignored by this app.

Do not edit `dist/` directly.

If a static runtime surface is needed later, create a deliberate export/copy step rather than manually changing generated files.

## current limitations

- The main surface source still lives at `runtime/views/vectorfl_dual_surface.tsx`, one level above the Vite app.
- The app is still a local program shell, not a fully packaged frontend workspace.
- The engine surface remains Python-rendered.
- Real operating execution still belongs to the engine runtime and latest manifests, not this app alone.

## next hardening candidates

1. Decide whether `vectorfl_dual_surface.tsx` should move into `src/` after the surface stabilizes.
2. Replace the temporary `node_modules` symlink with a normal dependency strategy.
3. Split user and VectorFL surface data into explicit view models only after the UI role boundary is stable.
4. Add a small smoke test or Playwright-style check only after the main page shape stops changing daily.
