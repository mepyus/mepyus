type ManifestRef = {
  role: "primary" | "supporting";
  path: string;
  reason: string;
};

type PanelReadMap = {
  panel: string;
  panelClass: "anchor_expression" | "maturation_expression" | "operating_expression";
  isCentralPanel?: boolean;
  reads: ManifestRef[];
};

const MANIFEST_ROOT = "runtime/manifests";

export const VECTORFL_SURFACE_CENTRAL_PANEL = "maturation_canvas_panel";

export const VECTORFL_SURFACE_PANEL_MANIFEST_READ_MAP: PanelReadMap[] = [
  {
    panel: "anchor_context_panel",
    panelClass: "anchor_expression",
    reads: [
      {
        role: "primary",
        path: `${MANIFEST_ROOT}/active_anchor_integrated_engine_3_surface.json`,
        reason: "Anchor/context reads the active three-surface baseline before mediation."
      }
    ]
  },
  {
    panel: "maturation_canvas_panel",
    panelClass: "maturation_expression",
    isCentralPanel: true,
    reads: [
      {
        role: "primary",
        path: `${MANIFEST_ROOT}/maturation_object_axis_candidate_001.json`,
        reason: "VectorFL center reads the axis candidate as the primary maturation object."
      },
      {
        role: "supporting",
        path: `${MANIFEST_ROOT}/packet_reflux_axis_pattern_001.json`,
        reason: "Reflux packet explains how this axis candidate returned to maturation space."
      },
      {
        role: "supporting",
        path: `${MANIFEST_ROOT}/packet_return_axis_enrichment_001.json`,
        reason: "Return packet provides the engine-side result that contributed to this maturation object."
      }
    ]
  },
  {
    panel: "validation_mediation_panel",
    panelClass: "operating_expression",
    reads: [
      {
        role: "primary",
        path: `${MANIFEST_ROOT}/packet_request_axis_enrichment_001.json`,
        reason: "Validation/mediation checks the original request purpose, directionality, and validation points."
      },
      {
        role: "primary",
        path: `${MANIFEST_ROOT}/packet_return_axis_enrichment_001.json`,
        reason: "Validation/mediation checks the returned result before user decision or reflux."
      }
    ]
  },
  {
    panel: "routing_reflux_panel",
    panelClass: "operating_expression",
    reads: [
      {
        role: "primary",
        path: `${MANIFEST_ROOT}/packet_return_axis_enrichment_001.json`,
        reason: "Routing/reflux reads return status before deciding next route."
      },
      {
        role: "primary",
        path: `${MANIFEST_ROOT}/packet_reflux_axis_pattern_001.json`,
        reason: "Routing/reflux reads reflux target and maturation value."
      }
    ]
  },
  {
    panel: "evidence_history_panel",
    panelClass: "operating_expression",
    reads: [
      {
        role: "primary",
        path: `${MANIFEST_ROOT}/panel_connection_record_axis_enrichment_001.json`,
        reason: "Evidence/history reads the panel connection record that created the current review path."
      }
    ]
  }
];

const VECTORFL_SUPPORT_SELECTION_ITEMS = [
  { label: "axis candidate", objectClass: "maturation support" },
  { label: "linked object", objectClass: "maturation support" },
  { label: "open edge", objectClass: "maturation support" }
];

const VECTORFL_CENTER_FIELD_GROUPS = [
  "origin refs",
  "current position",
  "maturity stage",
  "linked objects",
  "open edges",
  "evidence density"
];

const VECTORFL_SURFACE_STYLE_TOKENS = {
  surfaceShell: "vectorfl-surface-scaffold vectorfl-surface-scaffold--visual-translation-v0 min-h-screen bg-zinc-950 p-5 text-zinc-100 sm:p-6",
  headerShell: "vectorfl-surface-header mb-6 rounded-2xl border border-white/10 bg-white/[0.03] p-5",
  layoutShell: "vectorfl-surface-layout grid gap-5 xl:grid-cols-[minmax(220px,0.78fr)_minmax(340px,1.45fr)_minmax(240px,0.85fr)]",
  leftColumn: "vectorfl-surface-column vectorfl-surface-column--left order-2 space-y-5 xl:order-1",
  centerColumn: "vectorfl-surface-column vectorfl-surface-column--center order-1 space-y-5 xl:order-2",
  rightColumn: "vectorfl-surface-column vectorfl-surface-column--right order-3 space-y-4 xl:order-3",
  cardShell: "vectorfl-surface-card rounded-2xl border bg-zinc-950/75 p-4 text-zinc-100",
  centerCardEmphasis: "border-emerald-400/45 p-5 shadow-lg shadow-emerald-950/20",
  supportCardEmphasis: "border-white/10",
  cardHeader: "vectorfl-surface-card__header flex items-start justify-between gap-3",
  identityPill: "vectorfl-surface-pill rounded-full border border-emerald-400/30 bg-emerald-400/10 px-2.5 py-1 text-[10px] font-semibold uppercase tracking-wide text-emerald-200",
  quietPill: "vectorfl-surface-pill vectorfl-surface-pill--quiet rounded-full border border-white/10 bg-white/[0.04] px-2 py-0.5 text-[10px] font-semibold uppercase text-zinc-300",
  objectToken: "vectorfl-surface-object-token rounded-full border border-white/10 bg-white/[0.04] px-2.5 py-1 text-[10px] font-semibold uppercase tracking-wide text-zinc-400",
  badgeRow: "vectorfl-surface-badge-row mt-4 flex flex-wrap gap-2",
  badge: "vectorfl-surface-badge rounded-full border border-sky-400/25 bg-sky-400/10 px-2.5 py-1 text-[10px] font-semibold uppercase tracking-wide text-sky-200",
  readCard: "vectorfl-surface-read-card rounded-xl border border-white/10 bg-white/[0.03] p-3",
  codeText: "mt-3 block break-words text-[11px] leading-5 text-zinc-300",
  readReason: "mt-2 block text-xs leading-5 text-zinc-500",
  supportNote: "vectorfl-surface-support-note mt-4 rounded-xl border border-amber-400/15 bg-amber-400/[0.035] p-3 text-xs leading-5 text-zinc-500",
  supportShell: "rounded-2xl border border-white/10 bg-white/[0.025] p-4 text-zinc-400",
  supportItem: "rounded-xl border border-white/10 bg-black/15 px-3 py-2",
  fieldGrid: "vectorfl-surface-field-grid grid gap-2 rounded-2xl border border-white/10 bg-black/20 p-3 sm:grid-cols-3",
  fieldToken: "vectorfl-surface-field-token rounded-xl border border-white/10 bg-white/[0.03] px-3 py-2 text-center text-[11px] font-semibold uppercase tracking-wide text-zinc-300"
};

const PANEL_VISUAL_COPY: Record<
  string,
  {
    eyebrow: string;
    objectClass: "anchor criteria" | "maturation body" | "operating route";
    title: string;
    summary: string;
    badges: string[];
    supportNote: string;
  }
> = {
  anchor_context_panel: {
    eyebrow: "anchor context",
    objectClass: "anchor criteria",
    title: "Baseline criteria before mediation",
    summary: "Keeps anchor refs and comparison boundaries separate from the maturation object body.",
    badges: ["anchor ref", "boundary", "drift risk"],
    supportNote: "Anchor material stays criteria-like; it does not become line content or route movement."
  },
  maturation_canvas_panel: {
    eyebrow: "central maturation",
    objectClass: "maturation body",
    title: "Axis candidate body reading",
    summary: "Reads the maturation object itself: origin, current position, maturity, linked objects, and open edges.",
    badges: ["maturity stage", "evidence density", "linked object", "open edge"],
    supportNote: "This is the largest panel; support selection can point to it, but cannot replace it."
  },
  validation_mediation_panel: {
    eyebrow: "validation mediation",
    objectClass: "operating route",
    title: "Request and return review",
    summary: "Compares operating packets before user decision, recheck, reprocess, or reflux routing.",
    badges: ["request", "return", "hold", "recheck"],
    supportNote: "Mediation can hold or route material, but it does not execute engine work."
  },
  routing_reflux_panel: {
    eyebrow: "routing reflux",
    objectClass: "operating route",
    title: "Return-to-reflux preservation route",
    summary: "Keeps reflux reason and maturation value visible without treating reflux as completion.",
    badges: ["reflux", "target zone", "preserve trace"],
    supportNote: "Reflux remains a route back into maturation space, not the maturation body itself."
  },
  evidence_history_panel: {
    eyebrow: "evidence history",
    objectClass: "operating route",
    title: "Connection record trace",
    summary: "Shows circulation evidence through selected connection records and lineage-style rows.",
    badges: ["source", "emitted state", "target panel"],
    supportNote: "History is a compact trace aid, not a live event feed or full manifest dump."
  }
};

function getPanel(panelName: string) {
  const panel = VECTORFL_SURFACE_PANEL_MANIFEST_READ_MAP.find((item) => item.panel === panelName);

  if (!panel) {
    throw new Error(`Missing VectorFL surface panel mapping: ${panelName}`);
  }

  return panel;
}

function PanelCard({ panel, emphasis = "standard" }: { panel: PanelReadMap; emphasis?: "standard" | "central" }) {
  const copy = PANEL_VISUAL_COPY[panel.panel];
  const isCentral = emphasis === "central";

  return (
    <article
      className={[
        VECTORFL_SURFACE_STYLE_TOKENS.cardShell,
        `vectorfl-surface-card--${emphasis}`,
        isCentral ? VECTORFL_SURFACE_STYLE_TOKENS.centerCardEmphasis : VECTORFL_SURFACE_STYLE_TOKENS.supportCardEmphasis
      ].join(" ")}
      data-panel={panel.panel}
      data-central={panel.isCentralPanel ? "yes" : "no"}
      data-object-class={copy.objectClass}
    >
      <div className={VECTORFL_SURFACE_STYLE_TOKENS.cardHeader}>
        <span className={VECTORFL_SURFACE_STYLE_TOKENS.identityPill}>
          {copy.eyebrow}
        </span>
        <span className={VECTORFL_SURFACE_STYLE_TOKENS.objectToken}>
          {copy.objectClass}
        </span>
      </div>
      <h2 className={isCentral ? "mt-3 text-xl font-semibold tracking-tight" : "mt-3 text-base font-semibold"}>
        {panel.panel}
      </h2>
      <strong className="mt-3 block text-sm text-zinc-200">{copy.title}</strong>
      <p className="mt-2 text-sm leading-6 text-zinc-400">{copy.summary}</p>
      <div className={VECTORFL_SURFACE_STYLE_TOKENS.badgeRow} aria-label={`${panel.panel} visual tokens`}>
        {copy.badges.map((badge) => (
          <span
            key={`${panel.panel}-${badge}`}
            className={VECTORFL_SURFACE_STYLE_TOKENS.badge}
          >
            {badge}
          </span>
        ))}
      </div>
      <ul className={isCentral ? "vectorfl-surface-read-list mt-4 grid gap-3 sm:grid-cols-2" : "vectorfl-surface-read-list mt-4 space-y-3"}>
        {panel.reads.map((read) => (
          <li
            key={`${panel.panel}-${read.path}`}
            className={VECTORFL_SURFACE_STYLE_TOKENS.readCard}
          >
            <span className={VECTORFL_SURFACE_STYLE_TOKENS.quietPill}>
              {read.role}
            </span>
            <code className={VECTORFL_SURFACE_STYLE_TOKENS.codeText}>{read.path}</code>
            <small className={VECTORFL_SURFACE_STYLE_TOKENS.readReason}>{read.reason}</small>
          </li>
        ))}
      </ul>
      <p className={VECTORFL_SURFACE_STYLE_TOKENS.supportNote}>
        {copy.supportNote}
      </p>
    </article>
  );
}

export function VectorFLSurfaceScaffoldV0() {
  const anchorPanel = getPanel("anchor_context_panel");
  const maturationPanel = getPanel("maturation_canvas_panel");
  const validationPanel = getPanel("validation_mediation_panel");
  const refluxPanel = getPanel("routing_reflux_panel");
  const evidencePanel = getPanel("evidence_history_panel");

  return (
    <section
      className={VECTORFL_SURFACE_STYLE_TOKENS.surfaceShell}
      data-surface="vectorfl_surface"
      data-central-panel={VECTORFL_SURFACE_CENTRAL_PANEL}
    >
      <header className={VECTORFL_SURFACE_STYLE_TOKENS.headerShell}>
        <div>
          <p className={VECTORFL_SURFACE_STYLE_TOKENS.identityPill}>
            VectorFL surface scaffold v0
          </p>
          <strong className="mt-3 block text-2xl font-semibold tracking-tight">
            Mediation / validation / maturation surface
          </strong>
        </div>
        <p className="mt-3 max-w-3xl text-sm leading-6 text-zinc-400">
          The center reads the maturation object body. Line and axis selection stay support-only. Central panel:
          <code className="ml-1 rounded-md bg-black/25 px-1.5 py-0.5 text-zinc-200">{VECTORFL_SURFACE_CENTRAL_PANEL}</code>
        </p>
      </header>

      <div
        className={VECTORFL_SURFACE_STYLE_TOKENS.layoutShell}
        data-layout-rhythm="left-center-right"
      >
        <aside
          className={VECTORFL_SURFACE_STYLE_TOKENS.leftColumn}
          aria-label="anchor and support selection"
        >
          <PanelCard panel={anchorPanel} />
          <div
            className={`vectorfl-surface-support-selection ${VECTORFL_SURFACE_STYLE_TOKENS.supportShell}`}
            aria-label="line axis support selection"
          >
            <span className={VECTORFL_SURFACE_STYLE_TOKENS.objectToken}>
              support selection
            </span>
            <strong className="mt-3 block text-sm text-zinc-300">Line / axis selector stays smaller than the canvas</strong>
            <ul className="mt-3 space-y-2">
              {VECTORFL_SUPPORT_SELECTION_ITEMS.map((item) => (
                <li key={item.label} className={VECTORFL_SURFACE_STYLE_TOKENS.supportItem}>
                  <span className="block text-xs font-semibold uppercase tracking-wide text-zinc-300">{item.label}</span>
                  <small className="mt-1 block text-[11px] text-zinc-600">{item.objectClass}</small>
                </li>
              ))}
            </ul>
          </div>
        </aside>

        <main
          className={VECTORFL_SURFACE_STYLE_TOKENS.centerColumn}
          aria-label="central maturation canvas"
        >
          <PanelCard panel={maturationPanel} emphasis="central" />
          <div
            className={VECTORFL_SURFACE_STYLE_TOKENS.fieldGrid}
            aria-label="maturation body field groups"
          >
            {VECTORFL_CENTER_FIELD_GROUPS.map((field) => (
              <span
                key={field}
                className={VECTORFL_SURFACE_STYLE_TOKENS.fieldToken}
              >
                {field}
              </span>
            ))}
          </div>
        </main>

        <aside
          className={VECTORFL_SURFACE_STYLE_TOKENS.rightColumn}
          aria-label="validation reflux evidence support"
        >
          <PanelCard panel={validationPanel} />
          <PanelCard panel={refluxPanel} />
          <PanelCard panel={evidencePanel} />
          <div
            className={`vectorfl-surface-side-inspection ${VECTORFL_SURFACE_STYLE_TOKENS.supportShell}`}
            aria-label="maturation support inspection"
          >
            <span className={VECTORFL_SURFACE_STYLE_TOKENS.objectToken}>
              side inspection
            </span>
            <strong className="mt-3 block text-sm text-zinc-300">Selected support stays typed</strong>
            <p className="mt-2 text-xs leading-5">
              Side detail can clarify an anchor criterion, open edge, route, or evidence row while keeping those object
              classes visually separate.
            </p>
          </div>
        </aside>
      </div>
    </section>
  );
}
