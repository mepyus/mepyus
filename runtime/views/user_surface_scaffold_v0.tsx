type ManifestRef = {
  role: "primary" | "supporting";
  path: string;
  reason: string;
};

type PanelReadMap = {
  panel: string;
  panelClass: "operating_expression" | "anchor_expression";
  isCentralPanel?: boolean;
  reads: ManifestRef[];
};

const MANIFEST_ROOT = "runtime/manifests";

export const USER_SURFACE_CENTRAL_PANEL = "operating_flow_panel";

export const USER_SURFACE_PANEL_MANIFEST_READ_MAP: PanelReadMap[] = [
  {
    panel: "request_organization_panel",
    panelClass: "operating_expression",
    reads: [
      {
        role: "primary",
        path: `${MANIFEST_ROOT}/packet_request_axis_enrichment_001.json`,
        reason: "Request/organization starts from the user-side request packet."
      }
    ]
  },
  {
    panel: "operating_flow_panel",
    panelClass: "operating_expression",
    isCentralPanel: true,
    reads: [
      {
        role: "primary",
        path: `${MANIFEST_ROOT}/current_loop_state_axis_enrichment_001.json`,
        reason: "User surface center shows current loop position and slot state."
      }
    ]
  },
  {
    panel: "anchor_support_panel",
    panelClass: "anchor_expression",
    reads: [
      {
        role: "primary",
        path: `${MANIFEST_ROOT}/active_anchor_integrated_engine_3_surface.json`,
        reason: "Anchor support checks whether the current request respects the three-surface baseline."
      }
    ]
  },
  {
    panel: "return_decision_panel",
    panelClass: "operating_expression",
    reads: [
      {
        role: "primary",
        path: `${MANIFEST_ROOT}/packet_return_axis_enrichment_001.json`,
        reason: "Return/decision reads the reviewed return packet before follow-up distribution."
      }
    ]
  }
];

const USER_SURFACE_FLOW_STEPS = [
  { label: "request", tone: "incoming" },
  { label: "vectorfl_review", tone: "review" },
  { label: "return", tone: "material" },
  { label: "decision_or_reflux", tone: "choice" }
];

const USER_SURFACE_STYLE_TOKENS = {
  surfaceShell: "user-surface-scaffold user-surface-scaffold--visual-translation-v0 min-h-screen bg-zinc-950 p-5 text-zinc-100 sm:p-6",
  headerShell: "user-surface-header mb-6 rounded-2xl border border-white/10 bg-white/[0.03] p-5",
  layoutShell: "user-surface-layout grid gap-5 xl:grid-cols-[minmax(220px,0.85fr)_minmax(320px,1.4fr)_minmax(220px,0.8fr)]",
  leftColumn: "user-surface-column user-surface-column--left order-2 space-y-5 xl:order-1",
  centerColumn: "user-surface-column user-surface-column--center order-1 space-y-5 xl:order-2",
  rightColumn: "user-surface-column user-surface-column--right order-3 space-y-5 xl:order-3",
  cardShell: "user-surface-card rounded-2xl border bg-zinc-950/75 p-4 text-zinc-100",
  centerCardEmphasis: "border-emerald-400/45 p-5 shadow-lg shadow-emerald-950/20",
  supportCardEmphasis: "border-white/10",
  cardHeader: "user-surface-card__header flex items-start justify-between gap-3",
  identityPill: "user-surface-pill rounded-full border border-emerald-400/30 bg-emerald-400/10 px-2.5 py-1 text-[10px] font-semibold uppercase tracking-wide text-emerald-200",
  quietPill: "user-surface-pill user-surface-pill--quiet rounded-full border border-white/10 bg-white/[0.04] px-2 py-0.5 text-[10px] font-semibold uppercase text-zinc-300",
  panelClassPill: "user-surface-panel-class rounded-full border border-white/10 bg-white/[0.04] px-2.5 py-1 text-[10px] font-semibold uppercase tracking-wide text-zinc-400",
  badgeRow: "user-surface-badge-row mt-4 flex flex-wrap gap-2",
  badge: "user-surface-badge rounded-full border border-sky-400/25 bg-sky-400/10 px-2.5 py-1 text-[10px] font-semibold uppercase tracking-wide text-sky-200",
  readCard: "user-surface-read-card rounded-xl border border-white/10 bg-white/[0.03] p-3",
  codeText: "mt-3 block break-words text-[11px] leading-5 text-zinc-300",
  readReason: "mt-2 block text-xs leading-5 text-zinc-500",
  supportNote: "user-surface-support-note mt-4 rounded-xl border border-amber-400/15 bg-amber-400/[0.035] p-3 text-xs leading-5 text-zinc-500",
  supportShell: "user-surface-side-inspection rounded-2xl border border-white/10 bg-white/[0.025] p-4 text-zinc-400",
  stripShell: "user-surface-flow-strip grid gap-2 rounded-2xl border border-white/10 bg-black/20 p-3 sm:grid-cols-4",
  stripItem: "rounded-xl border border-white/10 bg-white/[0.03] px-3 py-2 text-center",
  stripIndex: "user-surface-step-index text-[10px] font-semibold uppercase tracking-wide text-zinc-600",
  stripLabel: "text-[11px] uppercase tracking-wide text-zinc-300"
};

const PANEL_VISUAL_COPY: Record<
  string,
  {
    eyebrow: string;
    title: string;
    summary: string;
    badges: string[];
    supportNote: string;
  }
> = {
  request_organization_panel: {
    eyebrow: "request frame",
    title: "Goal, scope, and material context",
    summary: "Shapes the incoming request before it moves into review or follow-up routing.",
    badges: ["goal", "scope", "material", "next surface"],
    supportNote: "Keep the request packet first; optional distribution hints stay below the shaped request."
  },
  operating_flow_panel: {
    eyebrow: "central flow",
    title: "Request / return / reflux movement",
    summary: "Keeps the current loop slot visible so the user surface reads as operating, distributing, and deciding.",
    badges: ["current slot", "active packet", "route state", "open decision"],
    supportNote: "This is the largest panel; side support can clarify, but it does not replace the flow."
  },
  anchor_support_panel: {
    eyebrow: "anchor support",
    title: "Baseline boundary check",
    summary: "Shows the active three-surface anchor as a support check for request and decision handling.",
    badges: ["anchor", "boundary", "drift watch"],
    supportNote: "Anchor copy stays criteria-like and separate from the operating packet movement."
  },
  return_decision_panel: {
    eyebrow: "return decision",
    title: "Return material and next route",
    summary: "Reads return material as decision input, with routes open for accept, recheck, reprocess, or reflux.",
    badges: ["return", "question", "recheck", "reflux"],
    supportNote: "The return is not final by default; it stays available for user decision or VectorFL recheck."
  }
};

function getPanel(panelName: string) {
  const panel = USER_SURFACE_PANEL_MANIFEST_READ_MAP.find((item) => item.panel === panelName);

  if (!panel) {
    throw new Error(`Missing user surface panel mapping: ${panelName}`);
  }

  return panel;
}

function PanelCard({ panel, emphasis = "standard" }: { panel: PanelReadMap; emphasis?: "standard" | "central" }) {
  const copy = PANEL_VISUAL_COPY[panel.panel];
  const isCentral = emphasis === "central";

  return (
    <article
      className={[
        USER_SURFACE_STYLE_TOKENS.cardShell,
        `user-surface-card--${emphasis}`,
        isCentral ? USER_SURFACE_STYLE_TOKENS.centerCardEmphasis : USER_SURFACE_STYLE_TOKENS.supportCardEmphasis
      ].join(" ")}
      data-panel={panel.panel}
      data-central={panel.isCentralPanel ? "yes" : "no"}
    >
      <div className={USER_SURFACE_STYLE_TOKENS.cardHeader}>
        <span className={USER_SURFACE_STYLE_TOKENS.identityPill}>
          {copy.eyebrow}
        </span>
        <span className={USER_SURFACE_STYLE_TOKENS.panelClassPill}>
          {panel.panelClass}
        </span>
      </div>
      <h2 className={isCentral ? "mt-3 text-xl font-semibold tracking-tight" : "mt-3 text-base font-semibold"}>
        {panel.panel}
      </h2>
      <strong className="mt-3 block text-sm text-zinc-200">{copy.title}</strong>
      <p className="mt-2 text-sm leading-6 text-zinc-400">{copy.summary}</p>
      <div className={USER_SURFACE_STYLE_TOKENS.badgeRow} aria-label={`${panel.panel} visual tokens`}>
        {copy.badges.map((badge) => (
          <span
            key={`${panel.panel}-${badge}`}
            className={USER_SURFACE_STYLE_TOKENS.badge}
          >
            {badge}
          </span>
        ))}
      </div>
      <ul className={isCentral ? "user-surface-read-list mt-4 grid gap-3 sm:grid-cols-2" : "user-surface-read-list mt-4 space-y-3"}>
        {panel.reads.map((read) => (
          <li
            key={`${panel.panel}-${read.path}`}
            className={USER_SURFACE_STYLE_TOKENS.readCard}
          >
            <span className={USER_SURFACE_STYLE_TOKENS.quietPill}>
              {read.role}
            </span>
            <code className={USER_SURFACE_STYLE_TOKENS.codeText}>{read.path}</code>
            <small className={USER_SURFACE_STYLE_TOKENS.readReason}>{read.reason}</small>
          </li>
        ))}
      </ul>
      <p className={USER_SURFACE_STYLE_TOKENS.supportNote}>
        {copy.supportNote}
      </p>
    </article>
  );
}

export function UserSurfaceScaffoldV0() {
  const requestPanel = getPanel("request_organization_panel");
  const operatingPanel = getPanel("operating_flow_panel");
  const anchorPanel = getPanel("anchor_support_panel");
  const returnPanel = getPanel("return_decision_panel");

  return (
    <section
      className={USER_SURFACE_STYLE_TOKENS.surfaceShell}
      data-surface="user_surface"
      data-central-panel={USER_SURFACE_CENTRAL_PANEL}
    >
      <header className={USER_SURFACE_STYLE_TOKENS.headerShell}>
        <div>
          <p className={USER_SURFACE_STYLE_TOKENS.identityPill}>
            User surface scaffold v0
          </p>
          <strong className="mt-3 block text-2xl font-semibold tracking-tight">Operating / distribution / decision surface</strong>
        </div>
        <p className="mt-3 max-w-3xl text-sm leading-6 text-zinc-400">
          Request, return, and reflux flow remain ahead of optional distribution support. Central panel:
          <code className="ml-1 rounded-md bg-black/25 px-1.5 py-0.5 text-zinc-200">{USER_SURFACE_CENTRAL_PANEL}</code>
        </p>
      </header>

      <div
        className={USER_SURFACE_STYLE_TOKENS.layoutShell}
        data-layout-rhythm="left-center-right"
      >
        <aside
          className={USER_SURFACE_STYLE_TOKENS.leftColumn}
          aria-label="request and anchor support"
        >
          <PanelCard panel={requestPanel} />
          <PanelCard panel={anchorPanel} />
        </aside>

        <main
          className={USER_SURFACE_STYLE_TOKENS.centerColumn}
          aria-label="central operating flow"
        >
          <PanelCard panel={operatingPanel} emphasis="central" />
          <ol
            className={USER_SURFACE_STYLE_TOKENS.stripShell}
            aria-label="request return reflux route rhythm"
          >
            {USER_SURFACE_FLOW_STEPS.map((step, index) => (
              <li
                key={step.label}
                className={USER_SURFACE_STYLE_TOKENS.stripItem}
                data-flow-tone={step.tone}
              >
                <span className={USER_SURFACE_STYLE_TOKENS.stripIndex}>
                  {index + 1}
                </span>
                <br />
                <strong className={USER_SURFACE_STYLE_TOKENS.stripLabel}>{step.label}</strong>
              </li>
            ))}
          </ol>
        </main>

        <aside
          className={USER_SURFACE_STYLE_TOKENS.rightColumn}
          aria-label="return decision support"
        >
          <PanelCard panel={returnPanel} />
          <div
            className={USER_SURFACE_STYLE_TOKENS.supportShell}
            aria-label="support inspection note"
          >
            <span className={USER_SURFACE_STYLE_TOKENS.panelClassPill}>
              support inspection
            </span>
            <strong className="mt-3 block text-sm text-zinc-300">Decision support stays secondary</strong>
            <p className="mt-2 text-xs leading-5">
              Side detail can expose a selected route, open question, or connection note while the center keeps the
              loop position visible.
            </p>
          </div>
        </aside>
      </div>
    </section>
  );
}
