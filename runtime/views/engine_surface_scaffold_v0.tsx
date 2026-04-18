type ManifestRef = {
  role: "primary" | "supporting";
  path: string;
  reason: string;
};

type PanelReadMap = {
  panel: string;
  panelClass: "operating_expression";
  isCentralPanel?: boolean;
  reads: ManifestRef[];
};

const MANIFEST_ROOT = "runtime/manifests";

export const ENGINE_SURFACE_CENTRAL_PANEL = "execution_state_panel";

export const ENGINE_SURFACE_PANEL_MANIFEST_READ_MAP: PanelReadMap[] = [
  {
    panel: "work_input_panel",
    panelClass: "operating_expression",
    reads: [
      {
        role: "primary",
        path: `${MANIFEST_ROOT}/packet_request_axis_enrichment_001.json`,
        reason: "Work input reads the VectorFL-shaped request packet, not raw user intent."
      }
    ]
  },
  {
    panel: "execution_state_panel",
    panelClass: "operating_expression",
    isCentralPanel: true,
    reads: [
      {
        role: "primary",
        path: `${MANIFEST_ROOT}/current_loop_state_axis_enrichment_001.json`,
        reason: "Engine center shows current loop slot and processing state."
      }
    ]
  },
  {
    panel: "result_return_panel",
    panelClass: "operating_expression",
    reads: [
      {
        role: "primary",
        path: `${MANIFEST_ROOT}/packet_return_axis_enrichment_001.json`,
        reason: "Result/return drafts the return packet for VectorFL validation."
      }
    ]
  },
  {
    panel: "execution_history_panel",
    panelClass: "operating_expression",
    reads: [
      {
        role: "primary",
        path: `${MANIFEST_ROOT}/panel_connection_record_engine_return_to_vectorfl_validation_001.json`,
        reason: "Execution history reads the engine return to VectorFL validation record as the minimal route trace."
      }
    ]
  }
];

const PANEL_VISUAL_COPY: Record<
  string,
  {
    badge: string;
    question: string;
    visualRole: string;
    supportNote: string;
  }
> = {
  work_input_panel: {
    badge: "shaped input",
    question: "What request is ready for engine processing?",
    visualRole: "Slot card for VectorFL-shaped work input.",
    supportNote: "Reads shaped request material only; source details stay within the mapped manifest note."
  },
  execution_state_panel: {
    badge: "central slot",
    question: "Where is engine processing now?",
    visualRole: "Central execution-state card for current slot and loop position.",
    supportNote: "Shows processing position only; return meaning is validated outside this panel."
  },
  result_return_panel: {
    badge: "return draft",
    question: "What return material is being prepared?",
    visualRole: "Return-material card for VectorFL validation or follow-up route.",
    supportNote: "Return material is not product completion."
  },
  execution_history_panel: {
    badge: "route trace",
    question: "Which route trace explains this return?",
    visualRole: "Compact trace card for panel connection / execution history.",
    supportNote: "History support only; keeps route trace separate from command or decision surfaces."
  }
};

const ENGINE_SURFACE_STYLE_TOKENS = {
  surfaceShell: "min-h-screen bg-zinc-950 p-5 text-zinc-100 sm:p-6",
  headerShell: "mb-6 rounded-2xl border border-white/10 bg-white/[0.03] p-5",
  layoutShell: "grid gap-5 xl:grid-cols-[minmax(220px,0.8fr)_minmax(320px,1.35fr)_minmax(240px,0.9fr)]",
  leftColumn: "order-2 space-y-5 xl:order-1",
  centerColumn: "order-1 space-y-5 xl:order-2",
  rightColumn: "order-3 space-y-4 xl:order-3",
  cardShell: "rounded-2xl border bg-zinc-950/75 p-4 text-zinc-100",
  centerCardEmphasis: "border-emerald-400/45 p-5 shadow-lg shadow-emerald-950/20",
  supportCardEmphasis: "border-white/10",
  cardHeader: "flex items-start justify-between gap-3",
  identityText: "text-[10px] font-semibold uppercase tracking-[0.18em] text-zinc-500",
  identityPill: "rounded-full border border-emerald-400/40 bg-emerald-400/10 px-3 py-1 text-xs font-semibold uppercase tracking-wide text-emerald-200",
  classPillBase: "rounded-full border px-2.5 py-1 text-[10px] font-semibold uppercase tracking-wide",
  classPillCentral: "border-emerald-400/40 bg-emerald-400/10 text-emerald-200",
  classPillSupport: "border-white/10 bg-white/[0.04] text-zinc-400",
  questionBox: "mt-4 rounded-xl border border-white/10 bg-black/20 p-3",
  readCard: "rounded-xl border border-white/10 bg-white/[0.03] p-3",
  readPill: "rounded-full border border-sky-400/30 bg-sky-400/10 px-2 py-0.5 text-[10px] font-semibold uppercase text-sky-200",
  codeText: "mt-3 block break-words text-[11px] leading-5 text-zinc-300",
  readReason: "mt-2 text-xs leading-5 text-zinc-500",
  supportNote: "mt-4 rounded-xl border border-amber-400/15 bg-amber-400/[0.035] p-3",
  supportLabel: "text-[10px] font-semibold uppercase tracking-[0.16em] text-amber-300/70",
  supportText: "mt-1 text-xs leading-5 text-zinc-500",
  stripShell: "rounded-2xl border border-white/10 bg-black/20 p-4",
  stripItem: "rounded-xl border border-white/10 bg-white/[0.03] px-3 py-2 text-center text-[11px] uppercase tracking-wide text-zinc-400"
};

function getPanel(panelId: string) {
  return ENGINE_SURFACE_PANEL_MANIFEST_READ_MAP.find((panel) => panel.panel === panelId);
}

function PanelCard({ panel, emphasis = "support" }: { panel: PanelReadMap; emphasis?: "central" | "support" }) {
  const copy = PANEL_VISUAL_COPY[panel.panel];
  const isCentral = emphasis === "central";

  return (
    <article
      key={panel.panel}
      data-panel={panel.panel}
      data-central={panel.isCentralPanel ? "yes" : "no"}
      className={[
        ENGINE_SURFACE_STYLE_TOKENS.cardShell,
        isCentral ? ENGINE_SURFACE_STYLE_TOKENS.centerCardEmphasis : ENGINE_SURFACE_STYLE_TOKENS.supportCardEmphasis
      ].join(" ")}
    >
      <div className={ENGINE_SURFACE_STYLE_TOKENS.cardHeader}>
        <div>
          <div className={ENGINE_SURFACE_STYLE_TOKENS.identityText}>
            {copy.badge}
          </div>
          <h2 className={isCentral ? "mt-1 text-xl font-semibold" : "mt-1 text-base font-semibold"}>
            {panel.panel}
          </h2>
        </div>
        <span
          className={[
            ENGINE_SURFACE_STYLE_TOKENS.classPillBase,
            isCentral ? ENGINE_SURFACE_STYLE_TOKENS.classPillCentral : ENGINE_SURFACE_STYLE_TOKENS.classPillSupport
          ].join(" ")}
        >
          {panel.panelClass}
        </span>
      </div>

      <div className={ENGINE_SURFACE_STYLE_TOKENS.questionBox}>
        <div className={ENGINE_SURFACE_STYLE_TOKENS.identityText}>
          Panel question
        </div>
        <p className="mt-1 text-sm leading-6 text-zinc-300">{copy.question}</p>
      </div>

      <div className={isCentral ? "mt-4 grid gap-3 sm:grid-cols-2" : "mt-4 space-y-3"}>
        {panel.reads.map((read) => (
          <div key={`${panel.panel}-${read.path}`} className={ENGINE_SURFACE_STYLE_TOKENS.readCard}>
            <div className="flex items-center justify-between gap-2">
              <span className={ENGINE_SURFACE_STYLE_TOKENS.readPill}>
                {read.role}
              </span>
              <span className="text-[10px] uppercase tracking-wide text-zinc-600">manifest read</span>
            </div>
            <code className={ENGINE_SURFACE_STYLE_TOKENS.codeText}>{read.path}</code>
            <p className={ENGINE_SURFACE_STYLE_TOKENS.readReason}>{read.reason}</p>
          </div>
        ))}
      </div>

      <div className={ENGINE_SURFACE_STYLE_TOKENS.supportNote}>
        <div className={ENGINE_SURFACE_STYLE_TOKENS.supportLabel}>
          Support boundary
        </div>
        <p className={ENGINE_SURFACE_STYLE_TOKENS.supportText}>{copy.supportNote}</p>
      </div>

      <div className="mt-3 text-[10px] uppercase tracking-[0.16em] text-zinc-600">{copy.visualRole}</div>
    </article>
  );
}

export function EngineSurfaceScaffoldV0() {
  const workInputPanel = getPanel("work_input_panel");
  const executionStatePanel = getPanel("execution_state_panel");
  const resultReturnPanel = getPanel("result_return_panel");
  const executionHistoryPanel = getPanel("execution_history_panel");

  return (
    <section
      data-surface="engine_surface"
      data-central-panel={ENGINE_SURFACE_CENTRAL_PANEL}
      className={ENGINE_SURFACE_STYLE_TOKENS.surfaceShell}
    >
      <header className={ENGINE_SURFACE_STYLE_TOKENS.headerShell}>
        <div className="flex flex-wrap items-start justify-between gap-4">
          <div>
            <p className="text-[11px] font-semibold uppercase tracking-[0.24em] text-zinc-500">
              Engine surface scaffold v0
            </p>
            <h1 className="mt-2 text-2xl font-semibold tracking-tight">Processing / execution / return-draft surface</h1>
            <p className="mt-2 max-w-3xl text-sm leading-6 text-zinc-400">
              This scaffold keeps the existing manifest read mapping while applying a bounded visual rhythm for shaped input,
              current execution state, return material, and route trace.
            </p>
          </div>
          <span className={ENGINE_SURFACE_STYLE_TOKENS.identityPill}>
            Central panel: {ENGINE_SURFACE_CENTRAL_PANEL}
          </span>
        </div>
      </header>

      <div className={ENGINE_SURFACE_STYLE_TOKENS.layoutShell}>
        <div className={ENGINE_SURFACE_STYLE_TOKENS.leftColumn}>{workInputPanel && <PanelCard panel={workInputPanel} />}</div>

        <div className={ENGINE_SURFACE_STYLE_TOKENS.centerColumn}>
          {executionStatePanel && <PanelCard panel={executionStatePanel} emphasis="central" />}
          <div className={ENGINE_SURFACE_STYLE_TOKENS.stripShell}>
            <div className={ENGINE_SURFACE_STYLE_TOKENS.identityText}>
              Visual slot rhythm
            </div>
            <div className="mt-3 grid gap-2 sm:grid-cols-4">
              {["input", "processing", "return", "trace"].map((step) => (
                <div key={step} className={ENGINE_SURFACE_STYLE_TOKENS.stripItem}>
                  {step}
                </div>
              ))}
            </div>
            <p className={ENGINE_SURFACE_STYLE_TOKENS.supportText}>
              These markers are visual only. They do not add runtime automation or alter manifest reads.
            </p>
          </div>
        </div>

        <div className={ENGINE_SURFACE_STYLE_TOKENS.rightColumn}>
          {resultReturnPanel && <PanelCard panel={resultReturnPanel} />}
          {executionHistoryPanel && <PanelCard panel={executionHistoryPanel} />}
        </div>
      </div>
    </section>
  );
}
