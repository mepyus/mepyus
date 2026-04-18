import React, { useEffect, useMemo, useState } from "react";
import { RefreshCcw, Play, GitPullRequest, MessageSquare, Radio } from "lucide-react";
import { Badge, Button, Textarea } from "./ui-components";

type CliReadableReturn = {
  session_id?: string;
  backend_kind?: string;
  task_type?: string;
  status?: string;
  purpose_text?: string;
  suggested_next_use?: string;
  route_label?: string;
  marks?: string[];
  mark_history?: Array<{ mark: string; marked_at: string; source?: string }>;
  structured_return_preview?: string;
  deposit_candidate_preview?: string;
  operator_report_preview?: string;
  session_path?: string;
  structured_return_path?: string;
  deposit_candidate_path?: string;
  operator_report_path?: string;
  started_at?: string;
  ended_at?: string;
};

type CliHostState = {
  latest_readable_return?: CliReadableReturn;
  recent_readable_returns?: CliReadableReturn[];
  deposit_ready_returns?: CliReadableReturn[];
  package_run_events?: RuntimePackageRunEvent[];
  package_notebooks?: PackageNotebook[];
  spine_contracts?: SpineContracts;
};

type WorkPacketDraft = {
  purpose: string;
  taskLens: string;
  internalSearchStatus: string;
  evidenceSummary: string;
  evidenceLimitation: string;
  evidenceCount: number;
  evidenceKinds: string[];
  nextRouteCandidate: string;
  expectedReturnShape: string;
  manualStillNeeded: string[];
};

type SurfaceId = "user" | "vectorfl" | "engine";

type SessionEvent = {
  id: string;
  packageId?: string;
  sessionId?: string;
  label: string;
  detail: string;
  status: string;
  eventType?: "instruction" | "preflight" | "handoff" | "return" | "route_mark" | "package" | "structure_signal" | "digestion" | "error" | "refresh" | "template" | "followup";
  signal?: string;
  confidence?: "weak" | "usable" | "strong" | "unknown";
  receiver?: "current_package" | "setup_control" | "result_modal" | "watch_modal" | "package_stack" | "engine_memory" | "none";
  suggestedAction?: "record_only" | "open_result" | "open_watch" | "queue_review" | "manual_trigger" | "hold";
};

type RuntimePackageRunEvent = {
  event_id?: string;
  event_type?: string;
  package_id?: string;
  package_title?: string;
  session_id?: string;
  stage?: string;
  label?: string;
  detail?: string;
  signal?: string;
  confidence?: "weak" | "usable" | "strong" | "unknown";
  receiver?: string;
  suggested_action?: string;
  status?: string;
  created_at?: string;
};

type PackageNotebookRun = {
  session_id?: string;
  status?: string;
  task_type?: string;
  purpose_text?: string;
  result_summary?: string;
  answer?: string;
  findings?: string[];
  files_artifacts?: string[];
  next_continue_hint?: string;
  open_questions?: string[];
  risks_or_limits?: string[];
  source_refs?: string[];
  suggested_next_use?: string;
  route_label?: string;
  started_at?: string;
  ended_at?: string;
  event_count?: number;
  artifacts?: {
    session_path?: string;
    structured_return_path?: string;
    deposit_candidate_path?: string;
    operator_report_path?: string;
  };
  bounded_context_refs?: string[];
};

type PackageNotebook = {
  package_id: string;
  package_title: string;
  package_summary?: string;
  latest_stage?: string;
  latest_executor?: string;
  runs: PackageNotebookRun[];
  run_count: number;
  latest_run?: PackageNotebookRun;
};

type SpineContracts = {
  packages?: Array<{
    id: string;
    title: string;
    goal: string;
    scope: string;
    stage: string;
    status: string;
    route_label: string;
    active_worker: string;
    context_refs: string[];
    artifact_refs: string[];
    prior_run_ids: string[];
    notebook_id: string;
  }>;
  handoff_packets?: Array<{ packet_id: string; package_id: string; worker_role: string }>;
  run_records?: Array<{ run_id: string; package_id: string; input_packet_id: string }>;
  notebooks?: Array<{ notebook_id: string; package_id: string; latest_run_id: string; run_count: number }>;
  worker_profiles?: Array<{ worker_id: string; type: string; supported_task_types: string[] }>;
};

type ConversationTurn = {
  id: string;
  role: "user" | "engine" | "codex" | "vectorfl" | "system";
  label: string;
  body: string;
  meta?: string;
};

type CliHostControlPanelProps = {
  activeSurface?: SurfaceId;
  onSurfaceChange?: (surface: SurfaceId) => void;
  onCliStateChange?: (state: CliHostState) => void;
  onPacketDraftChange?: (draft: WorkPacketDraft) => void;
  externalFollowupTurn?: CliReadableReturn & { source_surface?: string; handoff_reason?: string };
  activePackage?: {
    id: string;
    title: string;
    status: string;
    stage: string;
    executor: string;
    summary: string;
  };
};

const DEFAULT_PURPOSE = "VectorFL면에서 Codex와 한 턴 대화하며 다음 운용 판단을 작게 검증한다.";
const DEFAULT_CONTEXT = "docs/reports/integrated_engine_ui_stable_folder_migration_note_v0.md";
const DEFAULT_PAYLOAD =
  "내부 공간의 구조를 분석해서 가져와. 엔진/통합엔진/패키지 구조 기준으로 무엇을 읽었는지, 현재 어디를 흐르는지, 결과물을 어떻게 보면 되는지 한국어로 짧게 반환해줘. 파일은 수정하지 않는다.";

const CONVERSATION_RETURN_CONTRACT =
  "Return format for this VectorFL CLI conversation turn:\n" +
  "1. Korean operating summary\n" +
  "2. Surface reading: user / VectorFL / engine\n" +
  "3. Route suggestion: reread_target / validation_target / implementation_return / deposit_candidate / hold\n" +
  "4. What must not be inferred\n" +
  "5. Suggested next use\n" +
  "Do not modify files. Do not promote, ingest, or canonicalize anything.";

const SURFACE_TEMPLATES: Record<SurfaceId, { taskType: string; purpose: string; prompt: string }> = {
  user: {
    taskType: "reread",
    purpose: "User Surface 관점에서 현재 목적/제약/결정 포인트를 점검한다.",
    prompt:
      "Read the bounded context from the User Surface angle. Return: current purpose, active constraints, decision point, and what should not be promoted yet. Do not modify files.",
  },
  vectorfl: {
    taskType: "reread",
    purpose: "VectorFL Surface 관점에서 현재 해석/중재/되읽기 지점을 점검한다.",
    prompt:
      "Read the bounded context from the VectorFL Surface angle. Return: what needs reread, what needs mediation, whether CLI remains on-top, and the next safe mark. Do not modify files.",
  },
  engine: {
    taskType: "validate",
    purpose: "Engine Surface 관점에서 현재 처리/반환/기록 후보를 검증한다.",
    prompt:
      "Read the bounded context from the Engine Surface angle. Return: processing status, return material, validation risk, and whether this should be marked for deposit or reread. Do not modify files.",
  },
};

const SESSION_DRAFT_STORAGE_KEY = "vectorfl_integrated_engine_cli_session_strip_draft_v0";

function loadSessionDraft() {
  if (typeof window === "undefined") return {};
  try {
    return JSON.parse(window.sessionStorage.getItem(SESSION_DRAFT_STORAGE_KEY) || "{}") || {};
  } catch {
    return {};
  }
}

function compact(value?: string, fallback = "pending") {
  const text = String(value || "").trim();
  return text || fallback;
}

function shortId(id?: string) {
  return id ? id.replace("cli_", "") : "none";
}

function markLabel(mark: string) {
  return mark.replace(/_/g, " ");
}

function routeLabel(route?: string) {
  switch (route) {
    case "user_assignment_candidate":
      return "user assignment candidate";
    case "engine_request_candidate":
      return "engine request candidate";
    case "validation_target":
      return "validation target";
    case "deposit_candidate":
      return "deposit candidate";
    case "hold":
      return "hold";
    case "vectorfl_reread":
      return "VectorFL reread";
    default:
      return "unrouted";
  }
}

function routeTone(route?: string) {
  switch (route) {
    case "user_assignment_candidate":
      return "border-emerald-500/20 bg-emerald-500/10 text-emerald-200";
    case "engine_request_candidate":
      return "border-violet-500/20 bg-violet-500/10 text-violet-200";
    case "validation_target":
      return "border-sky-500/20 bg-sky-500/10 text-sky-200";
    case "deposit_candidate":
      return "border-amber-500/20 bg-amber-500/10 text-amber-200";
    case "hold":
      return "border-slate-500/20 bg-slate-500/10 text-slate-300";
    case "vectorfl_reread":
      return "border-cyan-500/20 bg-cyan-500/10 text-cyan-200";
    default:
      return "border-white/10 bg-white/[0.04] text-slate-400";
  }
}

function mergeRefs(current: string, refs: string[]) {
  const lines = current
    .split(/\r?\n/)
    .map((line) => line.trim())
    .filter(Boolean);
  refs.forEach((ref) => {
    if (ref && !lines.includes(ref)) lines.push(ref);
  });
  return lines.join("\n");
}

function formatTime(value?: string) {
  if (!value) return "time pending";
  const parsed = Date.parse(value);
  if (Number.isNaN(parsed)) return value;
  return new Date(parsed).toLocaleString();
}

function splitRefs(value: string) {
  return value
    .split(/\r?\n/)
    .map((line) => line.trim())
    .filter(Boolean);
}

function inferPackageContextRefs(activePackage?: CliHostControlPanelProps["activePackage"]) {
  const text = `${activePackage?.id || ""} ${activePackage?.title || ""} ${activePackage?.summary || ""}`.toLowerCase();
  if (text.includes("openharness")) return "references/git_search/openharness-main";
  if (text.includes("외부 렌즈") || text.includes("external lens") || text.includes("lens pool")) return "gemini/external_analysis";
  if (text.includes("화면") || text.includes("surface") || text.includes("ui")) {
    return [
      "app/ui/integrated_engine/VectorFLIntegrationShell.tsx",
      "app/ui/integrated_engine/CliHostControlPanel.tsx",
      "docs/reports/integrated_engine_package_vessel_digestion_surface_snapshot_v0.md",
    ].join("\n");
  }
  return "";
}

function inferGoverningLocks(refs: string[]) {
  const locks: Array<{ label: string; source: string; status: "provided" | "inferred" }> = [];
  refs.forEach((ref) => {
    if (ref.includes("body_packet_memory_lock")) {
      locks.push({ label: "body / packet / memory lock", source: ref, status: "provided" });
    } else if (ref.includes("work_packet_generation_gap")) {
      locks.push({ label: "work packet generation gap", source: ref, status: "provided" });
    } else if (ref.includes("surface_language") || ref.includes("panel_application_backlog")) {
      locks.push({ label: "surface language / panel application", source: ref, status: "provided" });
    } else if (ref.includes("folder_status")) {
      locks.push({ label: "current folder operating status", source: ref, status: "provided" });
    } else if (ref.includes("integrated_engine_20260417")) {
      locks.push({ label: "2026-04-17 operating lock", source: ref, status: "provided" });
    }
  });
  if (!locks.length) {
    locks.push({ label: "fixed 3-surface body + CLI on-top boundary", source: "conversation contract", status: "inferred" });
  }
  return locks.slice(0, 4);
}

function evidenceKind(ref: string) {
  if (ref.includes("body_packet_memory_lock") || ref.includes("working_") || ref.includes("protocol") || ref.includes("interface")) return "governing lock";
  if (ref.includes("folder_status") || ref.includes("current_use_state") || ref.includes("closeout")) return "current state";
  if (ref.includes("surface_language") || ref.includes("language") || ref.includes("translation")) return "language / mapping";
  if (ref.includes("runtime/cli_sessions")) return "prior CLI turn";
  if (ref.includes("runtime/") || ref.includes("manifest")) return "runtime artifact";
  if (ref.includes("VectorFLIntegrationShell") || ref.includes("CliHostControlPanel") || ref.includes("app/ui")) return "screen/code evidence";
  return "source ref";
}

function inferEvidenceBundle(refs: string[], prompt: string) {
  const promptText = prompt.toLowerCase();
  const hasRefs = refs.length > 0;
  const requested = promptText.includes("read") || promptText.includes("reread") || promptText.includes("읽") || promptText.includes("검토");
  const searchState = !hasRefs
    ? "missing evidence"
    : refs.length < 2
      ? "thin evidence"
      : requested
        ? "completed"
        : "skipped";
  const searchBadge = searchState === "completed"
    ? "provided"
    : searchState === "thin evidence"
      ? "inferred"
      : searchState === "missing evidence"
        ? "missing"
        : "inferred";
  const items = refs.map((ref) => {
    const kind = evidenceKind(ref);
    return {
      ref,
      kind,
      source: "user provided",
      reason: kind === "governing lock"
        ? "packet boundary and body rule"
        : kind === "current state"
          ? "current operating posture"
          : kind === "language / mapping"
            ? "surface language and translation evidence"
            : kind === "prior CLI turn"
              ? "prior return / trace material"
              : kind === "screen/code evidence"
                ? "current UI structure evidence"
                : "bounded context material",
    };
  });
  const summary = hasRefs
    ? `${items.length} attached refs: ${Array.from(new Set(items.map((item) => item.kind))).join(", ")}`
    : "no evidence refs attached";
  const weakNote = !hasRefs
    ? "Evidence bundle is missing; packet would rely on prompt memory only."
    : refs.length < 2
      ? "Evidence bundle is thin; only one ref is attached."
      : "Evidence bundle is usable for a bounded reread, but not an exhaustive search.";
  return {
    searchState,
    searchBadge,
    items,
    summary,
    weakNote,
    requested: requested ? "requested by prompt" : "not explicitly requested",
  };
}

function inferExpectedReturnShape(taskType: string, prompt: string) {
  const text = prompt.toLowerCase();
  if (text.includes("3") && (text.includes("point") || text.includes("가지"))) return "3-point focused return";
  if (text.includes("conflict") || text.includes("충돌")) return "short conflict check";
  if (text.includes("route") || text.includes("mark")) return "route judgment";
  if (text.includes("summary") || text.includes("요약")) return "structured summary";
  if (taskType === "validate") return "validation finding";
  if (taskType === "inspect") return "inspection summary";
  if (taskType === "reread") return "reread judgment";
  return "bounded operating summary";
}

function inferRouteCandidate(taskType: string, prompt: string) {
  const text = prompt.toLowerCase();
  if (text.includes("deposit")) return "deposit_candidate";
  if (text.includes("engine request") || text.includes("implementation")) return "engine_request_candidate";
  if (text.includes("user assignment") || text.includes("사용자")) return "user_assignment_candidate";
  if (text.includes("hold") || text.includes("보류")) return "hold";
  if (taskType === "validate") return "validation_target";
  return "vectorfl_reread";
}

function inferGuards(prompt: string) {
  const text = prompt.toLowerCase();
  const guards = [
    { label: "read-only", status: text.includes("do not modify") || text.includes("파일은 수정하지") ? "guard-active" : "inferred" },
    { label: "no promotion", status: text.includes("promote") || text.includes("승격") ? "guard-active" : "inferred" },
    { label: "no ingestion", status: text.includes("ingest") || text.includes("보관") ? "guard-active" : "inferred" },
    { label: "no canonicalization", status: text.includes("canonical") || text.includes("확정") ? "guard-active" : "inferred" },
  ];
  return guards as Array<{ label: string; status: string }>;
}

function statusTone(status: string) {
  switch (status) {
    case "provided":
      return "border-emerald-500/20 bg-emerald-500/10 text-emerald-200";
    case "inferred":
      return "border-cyan-500/20 bg-cyan-500/10 text-cyan-200";
    case "missing":
      return "border-rose-500/20 bg-rose-500/10 text-rose-200";
    case "guard-active":
      return "border-amber-500/20 bg-amber-500/10 text-amber-200";
    default:
      return "border-white/10 bg-white/[0.04] text-slate-400";
  }
}

function PacketStatus({ status }: { status: string }) {
  return <Badge className={statusTone(status)}>{status}</Badge>;
}

function timestampId() {
  return `${Date.now()}_${Math.random().toString(16).slice(2, 7)}`;
}

function mapRuntimePackageEvent(event: RuntimePackageRunEvent): SessionEvent {
  const eventTypeMap: Record<string, SessionEvent["eventType"]> = {
    package_intake: "preflight",
    context_bundle: "structure_signal",
    source_structure_scan: "structure_signal",
    cli_handoff: "handoff",
    cli_return: "return",
    vectorfl_reread: "digestion",
    route_mark: "route_mark",
  };
  const receiver = String(event.receiver || "").includes("watch")
    ? "watch_modal"
    : String(event.receiver || "").includes("result")
      ? "result_modal"
      : String(event.receiver || "").includes("setup")
        ? "setup_control"
        : String(event.receiver || "").includes("engine")
          ? "engine_memory"
          : "current_package";
  const action = String(event.suggested_action || "").includes("watch")
    ? "open_watch"
    : String(event.suggested_action || "").includes("result")
      ? "open_result"
      : String(event.suggested_action || "").includes("hold")
        ? "hold"
        : "record_only";
  return {
    id: event.event_id || timestampId(),
    packageId: event.package_id,
    sessionId: event.session_id,
    label: event.label || event.event_type || "package event",
    detail: event.detail || event.stage || "runtime package event",
    status: event.status || "recorded",
    eventType: eventTypeMap[String(event.event_type || "")] || "digestion",
    signal: event.signal,
    confidence: event.confidence || "unknown",
    receiver: receiver as SessionEvent["receiver"],
    suggestedAction: action as SessionEvent["suggestedAction"],
  };
}

function eventTypeLabel(eventType?: SessionEvent["eventType"]) {
  switch (eventType) {
    case "instruction":
      return "input";
    case "preflight":
      return "vessel";
    case "handoff":
      return "digest";
    case "return":
      return "return";
    case "route_mark":
      return "route";
    case "structure_signal":
      return "line/axis";
    case "digestion":
      return "redeposit";
    default:
      return eventType || "event";
  }
}

function eventStepLabel(event: SessionEvent, index: number) {
  return `${index + 1}. ${eventTypeLabel(event.eventType)}`;
}

function SessionActivityRail({
  currentEvents,
  historyEvents,
  activePackageId,
  currentSessionId,
}: {
  currentEvents: SessionEvent[];
  historyEvents: SessionEvent[];
  activePackageId?: string;
  currentSessionId?: string;
}) {
  return (
    <div className="border-t border-white/10 bg-slate-950/80 px-4 py-3">
      <div className="mb-2 flex flex-wrap items-center justify-between gap-2">
        <div className="flex items-center gap-2 text-[10px] font-black uppercase tracking-[0.2em] text-cyan-300">
          <Radio className="h-3.5 w-3.5 text-cyan-300" />
          Current run event rail
        </div>
        <div className="text-[10px] font-bold text-slate-500">
          {activePackageId || "no package"} · {currentSessionId || "no runtime session yet"}
        </div>
      </div>
      {currentEvents.length ? (
        <div className="flex gap-2 overflow-x-auto pb-1">
          {currentEvents.map((event, index) => (
            <div key={event.id} className="min-w-[220px] rounded-lg border border-white/10 bg-white/[0.04] px-3 py-2">
              <div className="flex items-center justify-between gap-2">
                <span className="text-[9px] font-black uppercase tracking-[0.12em] text-cyan-200">{eventStepLabel(event, index)}</span>
                <span className="h-1.5 w-1.5 rounded-full bg-cyan-300" />
              </div>
              <div className="mt-1 line-clamp-1 text-xs font-black text-slate-100">{event.label}</div>
              <div className="mt-1 line-clamp-2 text-[10px] leading-4 text-slate-400">{event.detail}</div>
              <div className="mt-2 flex flex-wrap gap-1">
                <span className="rounded-full border border-white/10 bg-slate-950 px-2 py-0.5 text-[9px] font-bold text-slate-300">{event.status}</span>
                {event.confidence ? (
                  <span className="rounded-full border border-white/10 bg-slate-950 px-2 py-0.5 text-[9px] font-bold text-slate-300">{event.confidence}</span>
                ) : null}
                {event.receiver ? (
                  <span className="rounded-full border border-white/10 bg-slate-950 px-2 py-0.5 text-[9px] font-bold text-slate-300">{event.receiver}</span>
                ) : null}
                {event.suggestedAction ? (
                  <span className="rounded-full border border-cyan-300/20 bg-cyan-300/10 px-2 py-0.5 text-[9px] font-bold text-cyan-100">{event.suggestedAction}</span>
                ) : null}
              </div>
              {event.signal ? <div className="mt-1 line-clamp-1 text-[10px] text-slate-500">signal: {event.signal}</div> : null}
            </div>
          ))}
        </div>
      ) : (
        <div className="rounded-lg border border-white/10 bg-white/[0.04] px-3 py-3 text-xs text-slate-400">
          아직 선택 패키지의 runtime run이 없다. Send to Codex를 누르면 package_intake부터 vectorfl_reread까지 현재 실행 경로가 여기에 생긴다.
        </div>
      )}
      {historyEvents.length ? (
        <details className="mt-3 rounded-lg border border-white/10 bg-black/20 px-3 py-2">
          <summary className="cursor-pointer text-[10px] font-black uppercase tracking-[0.18em] text-slate-500">
            previous records for this package ({historyEvents.length})
          </summary>
          <div className="mt-2 grid gap-2 md:grid-cols-2">
            {historyEvents.slice(0, 6).map((event) => (
              <div key={event.id} className="rounded-lg border border-white/10 bg-slate-950 px-3 py-2">
                <div className="flex items-center justify-between gap-2">
                  <span className="text-[9px] font-black uppercase tracking-[0.12em] text-slate-500">{eventTypeLabel(event.eventType)}</span>
                  <span className="font-mono text-[9px] text-slate-600">{event.sessionId?.replace("cli_", "") || "local"}</span>
                </div>
                <div className="mt-1 line-clamp-1 text-xs font-black text-slate-200">{event.label}</div>
                <div className="mt-1 line-clamp-1 text-[10px] text-slate-500">{event.detail}</div>
              </div>
            ))}
          </div>
        </details>
      ) : null}
    </div>
  );
}

function ConversationTranscript({ turns }: { turns: ConversationTurn[] }) {
  return (
    <div className="space-y-3">
      {turns.map((turn) => {
        const isUser = turn.role === "user";
        const tone =
          turn.role === "user"
            ? "ml-auto border-cyan-300/30 bg-cyan-300/10"
            : turn.role === "codex"
              ? "border-emerald-300/20 bg-emerald-300/10"
              : turn.role === "vectorfl"
                ? "border-violet-300/20 bg-violet-300/10"
                : "border-white/10 bg-white/[0.04]";
        return (
          <article key={turn.id} className={`max-w-[86%] rounded-xl border px-4 py-3 ${tone}`}>
            <div className="mb-1 flex items-center justify-between gap-3">
              <span className="text-[10px] font-black uppercase tracking-[0.16em] text-slate-500">{turn.label}</span>
              {turn.meta ? <span className="font-mono text-[9px] text-slate-600">{turn.meta}</span> : null}
            </div>
            <p className={`whitespace-pre-wrap text-sm leading-6 ${isUser ? "text-cyan-50" : "text-slate-200"}`}>{turn.body}</p>
          </article>
        );
      })}
    </div>
  );
}

function PackageNotebookPanel({
  notebook,
  activePackage,
  onContinueRun,
}: {
  notebook?: PackageNotebook;
  activePackage?: CliHostControlPanelProps["activePackage"];
  onContinueRun: (run: PackageNotebookRun) => void;
}) {
  const runs = notebook?.runs || [];
  const latestRun = notebook?.latest_run || runs[0];
  return (
    <section className="mb-4 rounded-xl border border-white/10 bg-white/[0.04] p-4">
      <div className="flex flex-wrap items-start justify-between gap-3">
        <div>
          <div className="text-[10px] font-black uppercase tracking-[0.2em] text-cyan-300">Package Notebook</div>
          <h3 className="mt-1 text-lg font-black text-slate-100">{notebook?.package_title || activePackage?.title || "선택 패키지"}</h3>
          <p className="mt-1 max-w-3xl text-xs leading-5 text-slate-500">
            이 패키지의 이전 실행을 붙잡고 계속 작업한다. 결과/산출물/맥락은 여기에 누적되고, 다음 지시는 아래 입력창에서 이어간다.
          </p>
        </div>
        <div className="flex flex-wrap gap-2">
          <Badge className="border-cyan-500/20 bg-cyan-500/10 text-cyan-100">{runs.length} runs</Badge>
          <Badge className="border-white/10 bg-slate-950 text-slate-300">{notebook?.latest_stage || activePackage?.stage || "not started"}</Badge>
        </div>
      </div>

      <div className="mt-3 grid gap-2 md:grid-cols-3">
        <div className="rounded-lg border border-white/10 bg-slate-950 px-3 py-2">
          <div className="text-[9px] font-black uppercase tracking-[0.16em] text-slate-500">goal</div>
          <div className="mt-1 line-clamp-2 text-xs font-bold text-slate-200">{notebook?.package_summary || activePackage?.summary || "goal not set"}</div>
        </div>
        <div className="rounded-lg border border-white/10 bg-slate-950 px-3 py-2">
          <div className="text-[9px] font-black uppercase tracking-[0.16em] text-slate-500">status / route</div>
          <div className="mt-1 text-xs font-bold text-slate-200">{latestRun?.status || activePackage?.status || "not started"} · {routeLabel(latestRun?.route_label)}</div>
        </div>
        <div className="rounded-lg border border-white/10 bg-slate-950 px-3 py-2">
          <div className="text-[9px] font-black uppercase tracking-[0.16em] text-slate-500">continue target</div>
          <div className="mt-1 font-mono text-[10px] text-slate-300">{latestRun?.session_id?.replace("cli_", "") || "first run"}</div>
        </div>
      </div>

      {latestRun ? (
        <div className="mt-4 grid gap-3 lg:grid-cols-[1.2fr_0.8fr]">
          <article className="rounded-xl border border-white/10 bg-slate-950 p-4">
            <div className="flex flex-wrap items-center justify-between gap-2">
              <div className="text-[10px] font-black uppercase tracking-[0.18em] text-slate-500">latest package result</div>
              <Badge className={routeTone(latestRun.route_label)}>{routeLabel(latestRun.route_label)}</Badge>
            </div>
            <p className="mt-3 max-h-36 overflow-auto whitespace-pre-wrap text-sm leading-6 text-slate-100">
              {latestRun.answer || latestRun.result_summary || "latest run has no readable answer yet"}
            </p>
            <div className="mt-4 border-t border-white/10 pt-3">
              <div className="text-[10px] font-black uppercase tracking-[0.18em] text-slate-500">findings</div>
              <ul className="mt-2 space-y-1">
                {(latestRun.findings || []).slice(0, 5).map((finding) => (
                  <li key={finding} className="text-xs leading-5 text-slate-300">- {finding}</li>
                ))}
                {latestRun.findings?.length ? null : <li className="text-xs text-slate-500">no structured findings extracted</li>}
              </ul>
            </div>
            {latestRun.next_continue_hint ? (
              <div className="mt-3 rounded-lg border border-cyan-300/20 bg-cyan-300/10 px-3 py-2 text-xs leading-5 text-cyan-50">
                next: {latestRun.next_continue_hint}
              </div>
            ) : null}
            <div className="mt-3 flex flex-wrap gap-2">
              <button
                onClick={() => onContinueRun(latestRun)}
                className="rounded-lg border border-white/25 px-3 py-2 text-xs font-black text-white"
                style={{ backgroundColor: "#020617", color: "#ffffff" }}
              >
                Continue this package
              </button>
              <span className="self-center font-mono text-[10px] text-slate-500">{latestRun.session_id?.replace("cli_", "")}</span>
            </div>
          </article>

          <aside className="space-y-3">
            <div className="rounded-xl border border-white/10 bg-slate-950 p-3">
              <div className="text-[10px] font-black uppercase tracking-[0.18em] text-slate-500">files / artifacts</div>
              <div className="mt-2 space-y-1">
                {(latestRun.files_artifacts || Object.values(latestRun.artifacts || {}).filter(Boolean)).slice(0, 7).map((value) => (
                  <div key={value} className="truncate font-mono text-[10px] text-slate-400">{value}</div>
                ))}
                {(latestRun.files_artifacts?.length || Object.values(latestRun.artifacts || {}).filter(Boolean).length) ? null : <div className="text-xs text-slate-500">no artifact refs extracted</div>}
              </div>
            </div>
            <div className="rounded-xl border border-white/10 bg-slate-950 p-3">
              <div className="text-[10px] font-black uppercase tracking-[0.18em] text-slate-500">open / limits</div>
              <div className="mt-2 space-y-1">
                {[...(latestRun.open_questions || []), ...(latestRun.risks_or_limits || [])].slice(0, 5).map((item) => (
                  <div key={item} className="text-[10px] leading-4 text-slate-400">- {item}</div>
                ))}
                {(latestRun.open_questions?.length || latestRun.risks_or_limits?.length) ? null : <div className="text-xs text-slate-500">no explicit blockers extracted</div>}
              </div>
            </div>
          </aside>
        </div>
      ) : (
        <div className="mt-4 rounded-xl border border-white/10 bg-slate-950 p-4 text-sm leading-6 text-slate-400">
          아직 이 패키지 안에 실행 기록이 없다. 목적과 context refs를 확인한 뒤 Send to Codex로 첫 run을 만들면 여기에 누적된다.
        </div>
      )}

      {runs.length > 1 ? (
        <details className="mt-3 rounded-xl border border-white/10 bg-black/20 p-3">
          <summary className="cursor-pointer text-[10px] font-black uppercase tracking-[0.18em] text-slate-500">previous package runs</summary>
          <div className="mt-3 space-y-2">
            {runs.slice(1, 6).map((run) => (
              <button
                key={run.session_id}
                onClick={() => onContinueRun(run)}
                className="w-full rounded-lg border border-white/10 bg-slate-950 p-3 text-left"
              >
                <div className="flex flex-wrap items-center justify-between gap-2">
                  <span className="font-mono text-[10px] text-slate-400">{run.session_id?.replace("cli_", "")}</span>
                  <span className="text-[10px] font-bold text-slate-500">{run.status} · {run.event_count || 0} events</span>
                </div>
                <div className="mt-1 line-clamp-2 text-xs leading-5 text-slate-300">{run.answer || run.result_summary || run.purpose_text}</div>
              </button>
            ))}
          </div>
        </details>
      ) : null}
    </section>
  );
}

export function CliHostControlPanel({ activeSurface = "vectorfl", onSurfaceChange, onCliStateChange, onPacketDraftChange, externalFollowupTurn, activePackage }: CliHostControlPanelProps) {
  const initialDraft = useMemo(() => loadSessionDraft(), []);
  const [taskType, setTaskType] = useState(initialDraft.taskType || "summarize");
  const [purpose, setPurpose] = useState(initialDraft.purpose || DEFAULT_PURPOSE);
  const [contextRefs, setContextRefs] = useState(initialDraft.contextRefs || DEFAULT_CONTEXT);
  const [promptPayload, setPromptPayload] = useState(initialDraft.promptPayload || DEFAULT_PAYLOAD);
  const [latest, setLatest] = useState<CliReadableReturn>({});
  const [recentTurns, setRecentTurns] = useState<CliReadableReturn[]>([]);
  const [depositReadyTurns, setDepositReadyTurns] = useState<CliReadableReturn[]>([]);
  const [packageNotebooks, setPackageNotebooks] = useState<PackageNotebook[]>([]);
  const [status, setStatus] = useState("ready");
  const [isRunning, setIsRunning] = useState(false);
  const [conversationTurns, setConversationTurns] = useState<ConversationTurn[]>([
    {
      id: "welcome",
      role: "system",
      label: "integrated engine",
      body: "여기에 지시를 쓰면 통합엔진이 먼저 내부 공간을 읽고, 목적/경계/패키지를 잡은 뒤, Codex CLI 실행 결과를 다시 대화 턴과 결과 패키지로 반환합니다.",
      meta: "ready",
    },
  ]);
  const [sessionEvents, setSessionEvents] = useState<SessionEvent[]>([
    {
      id: "boot",
      packageId: "local",
      label: "conversation surface ready",
      detail: "사용자 입력을 통합엔진 packet으로 감싸 CLI에 보낼 준비 상태입니다.",
      status: "ready",
      eventType: "instruction",
      receiver: "current_package",
      confidence: "usable",
      suggestedAction: "record_only",
    },
  ]);
  const [runtimeEvents, setRuntimeEvents] = useState<SessionEvent[]>([]);

  const marks = useMemo(() => latest.marks || [], [latest.marks]);
  const turnCount = useMemo(() => recentTurns.length, [recentTurns.length]);
  const currentPacket = useMemo(() => {
    const refs = splitRefs(contextRefs);
    const evidenceBundle = inferEvidenceBundle(refs, promptPayload);
    const expectedReturnShape = inferExpectedReturnShape(taskType, promptPayload);
    const nextRouteCandidate = inferRouteCandidate(taskType, promptPayload);
    return {
      purpose: compact(purpose, "missing purpose"),
      purposeStatus: purpose.trim() ? "provided" : "missing",
      refs,
      evidenceStatus: evidenceBundle.searchBadge,
      evidenceBundle,
      locks: inferGoverningLocks(refs),
      taskLens: taskType || "unspecified",
      taskLensStatus: taskType ? "provided" : "missing",
      guards: inferGuards(`${promptPayload}\n${CONVERSATION_RETURN_CONTRACT}`),
      expectedReturnShape,
      expectedReturnStatus: expectedReturnShape ? "inferred" : "missing",
      nextRouteCandidate,
      routeStatus: nextRouteCandidate ? "inferred" : "missing",
      internalSearchStatus: evidenceBundle.searchState,
      internalSearchBadge: evidenceBundle.searchBadge,
      manualStillNeeded: [
        !refs.length ? "evidence/source refs" : "",
        "final route approval",
        "promotion/deposit decision",
      ].filter(Boolean),
    };
  }, [contextRefs, promptPayload, purpose, taskType]);
  const latestSessionEvent = latest.session_id
    ? `${compact(latest.status, "unknown")} / ${routeLabel(latest.route_label)} / ${compact(latest.session_id, "session")}`
    : status;
  const activeRuntimeOnlyEvents = useMemo(() => {
    return activePackage?.id
      ? runtimeEvents.filter((event) => event.packageId === activePackage.id)
      : runtimeEvents;
  }, [activePackage?.id, runtimeEvents]);
  const currentRuntimeSessionId = activeRuntimeOnlyEvents.find((event) => event.sessionId)?.sessionId;
  const currentRunEvents = useMemo(() => {
    if (!currentRuntimeSessionId) return [];
    return activeRuntimeOnlyEvents
      .filter((event) => event.sessionId === currentRuntimeSessionId)
      .slice()
      .reverse();
  }, [activeRuntimeOnlyEvents, currentRuntimeSessionId]);
  const historyRunEvents = useMemo(() => {
    if (!currentRuntimeSessionId) return activeRuntimeOnlyEvents.slice(0, 8);
    return activeRuntimeOnlyEvents.filter((event) => event.sessionId !== currentRuntimeSessionId).slice(0, 12);
  }, [activeRuntimeOnlyEvents, currentRuntimeSessionId]);
  const latestSourceProfileEvent = useMemo(() => {
    return currentRunEvents.find((event) => event.eventType === "structure_signal" && event.label.toLowerCase().includes("source profiled"));
  }, [currentRunEvents]);
  const activeNotebook = useMemo(() => {
    return packageNotebooks.find((notebook) => notebook.package_id === activePackage?.id);
  }, [activePackage?.id, packageNotebooks]);

  function pushSessionEvent(label: string, detail: string, eventStatus = "event", extra: Partial<SessionEvent> = {}) {
    setSessionEvents((current) => [{ id: timestampId(), packageId: activePackage?.id || "local", label, detail, status: eventStatus, ...extra }, ...current].slice(0, 12));
  }

  function pushConversationTurn(turn: Omit<ConversationTurn, "id">) {
    setConversationTurns((current) => [...current, { id: timestampId(), ...turn }].slice(-12));
  }

  async function refreshLatest() {
    setStatus("refreshing latest return...");
    pushSessionEvent("refresh latest return", "runtime/cli_sessions index를 다시 읽어 최신 반환을 표면에 반영합니다.", "refresh", {
      eventType: "refresh",
      receiver: "result_modal",
      suggestedAction: "record_only",
    });
    try {
      const response = await fetch("/api/vectorfl-engine/state");
      const result = await response.json();
      if (!response.ok) throw new Error(result.error || "failed to refresh engine state");
      const cli = (result.cli_host_control || {}) as CliHostState;
      setLatest(cli.latest_readable_return || {});
      setRecentTurns(cli.recent_readable_returns || []);
      setDepositReadyTurns(cli.deposit_ready_returns || []);
      setPackageNotebooks(cli.package_notebooks || []);
      if (cli.package_run_events?.length) {
        setRuntimeEvents(cli.package_run_events.map(mapRuntimePackageEvent));
      }
      onCliStateChange?.(cli);
      setStatus("latest return refreshed");
      pushSessionEvent("latest return refreshed", `${cli.latest_readable_return?.session_id || "no session"} 반환 상태를 다시 읽었습니다.`, "returned", {
        eventType: "return",
        receiver: "result_modal",
        confidence: cli.latest_readable_return?.session_id ? "usable" : "unknown",
        suggestedAction: cli.latest_readable_return?.session_id ? "open_result" : "record_only",
      });
    } catch (error: any) {
      setStatus(`error: ${error.message}`);
      pushSessionEvent("refresh failed", error.message, "error", { eventType: "error", suggestedAction: "hold" });
    }
  }

  function focusSurface(surface: SurfaceId) {
    const template = SURFACE_TEMPLATES[surface];
    onSurfaceChange?.(surface);
    setTaskType(template.taskType);
    setPurpose(template.purpose);
    setPromptPayload(template.prompt);
    setStatus(`focused ${surface} surface template`);
    pushSessionEvent(`loaded ${surface} template`, "surface별 질문으로 입력 초안을 전환했습니다.", "template", {
      eventType: "template",
      receiver: "setup_control",
      suggestedAction: "record_only",
    });
  }

  function buildConversationPrompt() {
    return (
      "You are operating as a Codex turn inside the integrated-engine VectorFL surface.\n" +
      "The CLI is an on-top tool layer, not a fourth surface.\n" +
      "The fixed surface split is: user = purpose/assignment/decision, VectorFL = interpretation/reread/mediation, engine = processing/return/deposit material.\n\n" +
      "Current work packet visible in the VectorFL surface:\n" +
      `- purpose: ${currentPacket.purpose}\n` +
      `- task lens: ${currentPacket.taskLens}\n` +
      `- internal search gate: ${currentPacket.evidenceBundle.searchState} (${currentPacket.evidenceBundle.requested})\n` +
      `- evidence bundle summary: ${currentPacket.evidenceBundle.summary}\n` +
      `- evidence limitation: ${currentPacket.evidenceBundle.weakNote}\n` +
      `- active locks: ${currentPacket.locks.map((lock) => `${lock.label} (${lock.status})`).join("; ")}\n` +
      `- evidence refs: ${currentPacket.refs.length ? currentPacket.refs.join("; ") : "none / unspecified"}\n` +
      `- guards: ${currentPacket.guards.map((guard) => `${guard.label} (${guard.status})`).join("; ")}\n` +
      `- expected return shape: ${currentPacket.expectedReturnShape}\n` +
      `- next route candidate: ${currentPacket.nextRouteCandidate}\n` +
      `- internal search usage: ${currentPacket.internalSearchStatus}\n\n` +
      "Current user-facing purpose:\n" +
      purpose.trim() +
      "\n\nCurrent message to Codex:\n" +
      promptPayload.trim() +
      "\n\n" +
      CONVERSATION_RETURN_CONTRACT
    );
  }

  function continueFromTurn(turn: CliReadableReturn = latest) {
    const refs = [turn.session_path, turn.structured_return_path, turn.deposit_candidate_path].filter(Boolean) as string[];
    if (!turn.session_id || !refs.length) {
      setStatus("no selected turn artifact path to continue from");
      return;
    }
    setTaskType("reread");
    setPurpose(`Continue from Codex turn ${turn.session_id} inside the VectorFL surface.`);
    setContextRefs((current) => mergeRefs(current, refs));
    setPromptPayload(
      "Continue from the selected Codex turn as a bounded operating conversation. Return: what remains valid, what needs reread or validation, and the next smallest safe action. Do not modify files."
    );
    setStatus(`loaded ${turn.session_id} as follow-up context`);
    pushSessionEvent("follow-up context loaded", `${turn.session_id} 반환물을 다음 입력 refs에 붙였습니다.`, "follow-up", {
      eventType: "followup",
      receiver: "setup_control",
      confidence: "usable",
      suggestedAction: "record_only",
    });
  }

  function continueFromNotebookRun(run: PackageNotebookRun) {
    const refs = [
      run.artifacts?.session_path,
      run.artifacts?.structured_return_path,
      run.artifacts?.deposit_candidate_path,
      ...(run.bounded_context_refs || []),
    ].filter(Boolean) as string[];
    if (!run.session_id || !refs.length) {
      setStatus("no package run artifact path to continue from");
      return;
    }
    setTaskType("reread");
    setPurpose(`Continue package ${activePackage?.title || "selected package"} from ${run.session_id}.`);
    setContextRefs((current) => mergeRefs(current, refs));
    setPromptPayload(
      `이 패키지의 이전 실행 ${run.session_id}에서 계속한다.\n` +
      "이전 결과를 다시 읽고, 남은 판단/다음 실행/산출물 후보를 정리해줘. 파일은 수정하지 않는다."
    );
    setStatus(`loaded package run ${run.session_id} as follow-up context`);
    pushSessionEvent("package run loaded", `${run.session_id} artifacts were attached to setup refs.`, "follow-up", {
      eventType: "followup",
      receiver: "setup_control",
      confidence: "usable",
      suggestedAction: "record_only",
    });
  }

  async function runSession() {
    setIsRunning(true);
    setStatus("sending Codex conversation turn...");
    pushConversationTurn({
      role: "user",
      label: "you",
      body: promptPayload.trim() || "(empty message)",
      meta: currentPacket.taskLens,
    });
    pushConversationTurn({
      role: "engine",
      label: "engine preflight",
      body:
        `목적: ${currentPacket.purpose}\n` +
        `내부 읽기: ${currentPacket.evidenceBundle.summary}\n` +
        `공정 위치: 지시 수신 → 내부 공간 읽기 → 패키지 형성\n` +
        `예상 route: ${routeLabel(currentPacket.nextRouteCandidate)}`,
      meta: currentPacket.internalSearchStatus,
    });
    pushSessionEvent("preflight packet formed", `${currentPacket.taskLens} · ${currentPacket.evidenceBundle.summary} · route=${currentPacket.nextRouteCandidate}`, "preflight", {
      eventType: "preflight",
      signal: "목적어를 담는 그릇이 형성됨",
      receiver: "setup_control",
      confidence: currentPacket.evidenceBundle.items.length ? "usable" : "weak",
      suggestedAction: "record_only",
    });
    try {
      pushConversationTurn({
        role: "engine",
        label: "cli handoff",
        body: "Codex CLI에 직접 원문만 넘기지 않고, 엔진/통합엔진/패키지 기준의 context wrapper를 붙여 실행합니다.",
        meta: "handoff",
      });
      pushSessionEvent("handoff to Codex CLI", "통합엔진 packet/context wrapper를 붙여 Codex 세션 API로 보냅니다.", "handoff", {
        eventType: "handoff",
        signal: "그릇 안의 목적/라인/축 후보를 CLI 처리로 넘김",
        receiver: "current_package",
        confidence: "usable",
        suggestedAction: "record_only",
      });
      const response = await fetch("/api/vectorfl-engine/actions/cli-session/run", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          backend_kind: "codex",
          task_type: taskType,
          requested_by_surface: "vectorfl_surface",
          requested_by_page: "app/ui/integrated_engine",
          purpose_text: purpose,
          bounded_context_refs: contextRefs,
          prompt_payload: buildConversationPrompt(),
          active_package: activePackage || {},
          timeout_seconds: 90,
        }),
      });
      const result = await response.json();
      if (!response.ok) throw new Error(result.error || result.detail || "failed to run session");
      const session = result.session || {};
      setLatest({
        session_id: session.session_id,
        backend_kind: session.backend_kind,
        task_type: session.task_type,
        status: session.status,
        purpose_text: session.purpose_text,
        suggested_next_use: result.structured_return?.suggested_next_use || session.suggested_next_use || "",
        route_label: result.structured_return?.suggested_next_use === "deposit_candidate"
          ? "deposit_candidate"
          : result.structured_return?.suggested_next_use === "implementation_return" || result.structured_return?.suggested_next_use === "validation_target"
            ? "engine_request_candidate"
            : "vectorfl_reread",
        marks: session.marks || [],
        mark_history: session.mark_history || [],
        structured_return_preview: result.structured_return?.result_summary || session.result_summary || "",
        deposit_candidate_preview: result.deposit_candidate_preview || "",
        operator_report_preview: session.operator_report_preview || "",
        session_path: result.session_path || session.session_path || "",
        structured_return_path: session.structured_return_path || "",
        deposit_candidate_path: session.deposit_candidate_path || "",
        operator_report_path: session.operator_report_path || "",
      });
      await refreshLatest();
      setStatus(`${result.ok ? "turn returned" : "turn failed"} -> ${result.session_path || session.session_id}`);
      const returnSummary = result.structured_return?.result_summary || session.result_summary || "Codex returned without a readable summary.";
      const nextUse = result.structured_return?.suggested_next_use || session.suggested_next_use || "route pending";
      pushConversationTurn({
        role: "codex",
        label: "codex",
        body: returnSummary,
        meta: session.session_id || "returned",
      });
      pushConversationTurn({
        role: "vectorfl",
        label: "VectorFL reread",
        body:
          `반환 판정: ${nextUse}\n` +
          `결과 읽기: CLI 출력물을 그대로 두지 않고 패키지/route/다음 행동으로 다시 읽습니다.\n` +
          `다음 후보 route: ${routeLabel(nextUse === "deposit_candidate" ? "deposit_candidate" : nextUse === "validation_target" ? "engine_request_candidate" : "vectorfl_reread")}`,
        meta: "postflight",
      });
      pushSessionEvent("return package received", `${session.session_id || "session"} · ${result.structured_return?.suggested_next_use || "route pending"}`, result.ok ? "returned" : "failed", {
        eventType: "return",
        signal: "CLI 출력이 결과 패키지로 돌아옴",
        receiver: "result_modal",
        confidence: result.ok ? "usable" : "weak",
        suggestedAction: result.ok ? "open_result" : "hold",
      });
      if (Array.isArray(result.package_run_events) && result.package_run_events.length) {
        setRuntimeEvents(result.package_run_events.map(mapRuntimePackageEvent));
      }
      pushSessionEvent("digestion reread needed", "반환물은 그대로 승인하지 않고 라인/축 반응, route, 재투입 후보로 다시 읽어야 합니다.", "reread", {
        eventType: "digestion",
        signal: "처리 결과를 흡수/재투입 후보로 재독해",
        receiver: "watch_modal",
        confidence: "weak",
        suggestedAction: "open_watch",
      });
    } catch (error: any) {
      setStatus(`error: ${error.message}`);
      pushConversationTurn({
        role: "engine",
        label: "handoff failed",
        body: error.message,
        meta: "error",
      });
      pushSessionEvent("Codex handoff failed", error.message, "error", { eventType: "error", suggestedAction: "hold" });
    } finally {
      setIsRunning(false);
    }
  }

  async function markLatest(mark: string) {
    const sessionId = latest.session_id;
    if (!sessionId) {
      setStatus("no latest session to mark");
      return;
    }
    setStatus(`marking ${mark}...`);
    pushSessionEvent("route mark requested", `${sessionId} -> ${mark}`, "mark", {
      eventType: "route_mark",
      receiver: "current_package",
      suggestedAction: mark === "hold" ? "hold" : "record_only",
    });
    try {
      const response = await fetch("/api/vectorfl-engine/actions/cli-session/mark", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ session_id: sessionId, mark }),
      });
      const result = await response.json();
      if (!response.ok) throw new Error(result.error || result.detail || "failed to mark session");
      const session = result.session || {};
      setLatest((prev) => ({
        ...prev,
        marks: session.marks || [],
        mark_history: session.mark_history || [],
        route_label: session.marks?.includes("user_assignment_candidate")
          ? "user_assignment_candidate"
          : session.marks?.includes("engine_request_candidate") || session.marks?.includes("implementation_return") || session.marks?.includes("validation_target")
            ? "engine_request_candidate"
            : session.marks?.includes("deposit_candidate")
              ? "deposit_candidate"
              : session.marks?.includes("hold")
                ? "hold"
                : prev.route_label,
      }));
      setStatus(`marked ${mark}`);
      pushSessionEvent("route mark recorded", `${sessionId} now carries ${mark}`, "marked", {
        eventType: "route_mark",
        receiver: "engine_memory",
        confidence: "usable",
        suggestedAction: "record_only",
      });
    } catch (error: any) {
      setStatus(`error: ${error.message}`);
      pushSessionEvent("route mark failed", error.message, "error", { eventType: "error", suggestedAction: "hold" });
    }
  }

  useEffect(() => {
    refreshLatest();
  }, []);

  useEffect(() => {
    onPacketDraftChange?.({
      purpose: currentPacket.purpose,
      taskLens: currentPacket.taskLens,
      internalSearchStatus: currentPacket.internalSearchStatus,
      evidenceSummary: currentPacket.evidenceBundle.summary,
      evidenceLimitation: currentPacket.evidenceBundle.weakNote,
      evidenceCount: currentPacket.evidenceBundle.items.length,
      evidenceKinds: Array.from(new Set(currentPacket.evidenceBundle.items.map((item) => item.kind))),
      nextRouteCandidate: currentPacket.nextRouteCandidate,
      expectedReturnShape: currentPacket.expectedReturnShape,
      manualStillNeeded: currentPacket.manualStillNeeded,
    });
  }, [currentPacket, onPacketDraftChange]);

  useEffect(() => {
    if (typeof window === "undefined") return;
    window.sessionStorage.setItem(
      SESSION_DRAFT_STORAGE_KEY,
      JSON.stringify({ taskType, purpose, contextRefs, promptPayload })
    );
  }, [taskType, purpose, contextRefs, promptPayload]);

  useEffect(() => {
    if (!externalFollowupTurn?.session_id) return;
    setLatest(externalFollowupTurn);
    continueFromTurn(externalFollowupTurn);
    setStatus(`loaded ${externalFollowupTurn.session_id} from ${externalFollowupTurn.source_surface || "surface"} handoff`);
  }, [externalFollowupTurn?.session_id, externalFollowupTurn?.handoff_reason]);

  useEffect(() => {
    if (!activePackage?.id) return;
    const nextPurpose = `${activePackage.title}: ${activePackage.summary}`;
    const nextPrompt =
      `${activePackage.title} 작업을 시작한다.\n` +
      `현재 stage는 ${activePackage.stage}, executor 후보는 ${activePackage.executor}다.\n` +
      "엔진/통합엔진/패키지 구조 기준으로 먼저 내부 공간을 읽고, 무엇을 실행해야 하는지 짧게 정리해줘. 파일은 수정하지 않는다.";
    setPurpose(nextPurpose);
    const inferredRefs = inferPackageContextRefs(activePackage);
    if (inferredRefs) setContextRefs(inferredRefs);
    setPromptPayload(nextPrompt);
    setStatus(`loaded package ${activePackage.id}`);
    pushConversationTurn({
      role: "system",
      label: "package selected",
      body: `${activePackage.title}\n${activePackage.summary}`,
      meta: activePackage.status,
    });
    pushSessionEvent("package selected", `${activePackage.id} -> ${activePackage.stage}`, "package", {
      eventType: "package",
      signal: "작업 그릇 전환",
      receiver: "current_package",
      confidence: "usable",
      suggestedAction: "record_only",
    });
  }, [activePackage?.id]);

  return (
    <section className="overflow-hidden rounded-2xl border border-slate-800 bg-slate-950 text-slate-100 shadow-sm">
      <div className="border-b border-white/10 px-4 py-3">
        <div className="flex flex-wrap items-center justify-between gap-3">
          <div>
            <div className="flex items-center gap-2 text-[10px] font-black uppercase tracking-[0.18em] text-cyan-300">
            <GitPullRequest className="h-4 w-4" />
              Integrated Engine chat
            </div>
            <div className="mt-1 text-sm font-bold text-slate-100">대화하듯 지시하면 내부 공간 읽기, 패키지 형성, CLI 실행, 반환 재독해가 한 흐름으로 보입니다.</div>
            {activePackage ? (
              <div className="mt-2 font-mono text-[10px] text-slate-500">
                active package: {activePackage.id} / {activePackage.stage} / {activePackage.executor}
              </div>
            ) : null}
          </div>
          <div className="flex flex-wrap gap-2">
            <Badge className="border-cyan-500/20 bg-cyan-500/10 text-cyan-200">{turnCount} turns</Badge>
            <Badge className={routeTone(latest.route_label)}>{routeLabel(latest.route_label)}</Badge>
            <Badge className="border-white/10 bg-white/[0.04] text-slate-300">{compact(latest.status, "ready")}</Badge>
          </div>
        </div>
      </div>

      <div className="px-4 py-4">
        <PackageNotebookPanel
          notebook={activeNotebook}
          activePackage={activePackage}
          onContinueRun={continueFromNotebookRun}
        />

        <div className="mb-4 max-h-[420px] overflow-y-auto rounded-xl border border-white/10 bg-black/20 p-4">
          <ConversationTranscript turns={conversationTurns} />
        </div>

        <label className="block text-[10px] font-black uppercase tracking-[0.18em] text-slate-500">
        message to integrated engine
        <Textarea
          value={promptPayload}
          onChange={(event: any) => setPromptPayload(event.target.value)}
          placeholder="예: 내부 공간의 구조를 분석해서 가져와"
          className="mt-2 min-h-[180px] w-full resize-y rounded-xl border-white/10 bg-black/30 p-4 text-base leading-7 normal-case tracking-normal text-slate-100 placeholder:text-slate-600 focus:ring-cyan-400"
          style={{
            backgroundColor: "#020617",
            color: "#f8fafc",
            caretColor: "#67e8f9",
          }}
        />
      </label>

      <div className="mt-3 flex flex-wrap items-center gap-2">
        <Button
          onClick={runSession}
          disabled={isRunning}
          className="rounded-lg border border-white/25 px-4 py-2 font-black text-white disabled:opacity-50"
          style={{ backgroundColor: "#020617", color: "#ffffff" }}
        >
          <Play className="mr-2 inline h-4 w-4" />
          {isRunning ? "Running..." : "Send to Codex"}
        </Button>
        <Button
          onClick={refreshLatest}
          className="rounded-lg border border-white/25 px-4 py-2 font-black text-white"
          style={{ backgroundColor: "#020617", color: "#ffffff" }}
        >
          <RefreshCcw className="mr-2 inline h-4 w-4" />
          Refresh
        </Button>
        <Button
          onClick={() => continueFromTurn()}
          className="rounded-lg border border-white/25 px-4 py-2 font-black text-white"
          style={{ backgroundColor: "#020617", color: "#ffffff" }}
        >
          <MessageSquare className="mr-2 inline h-4 w-4" />
          Continue latest
        </Button>
        <Button
          onClick={() => markLatest("hold")}
          className="rounded-lg border border-white/25 px-4 py-2 font-black text-white"
          style={{ backgroundColor: "#020617", color: "#ffffff" }}
        >
          Stop / hold
        </Button>
        <span className="font-mono text-[10px] text-slate-500">{latestSessionEvent}</span>
      </div>

      <div className="mt-4 grid gap-3 lg:grid-cols-[1fr_0.75fr]">
        <section className="rounded-xl border border-white/10 bg-white/[0.04] p-4">
          <div className="mb-2 flex flex-wrap items-center justify-between gap-2">
            <div className="text-[10px] font-black uppercase tracking-[0.18em] text-slate-500">latest return</div>
            <div className="flex flex-wrap gap-1">
              {marks.length ? marks.map((mark) => <Badge key={mark} className="border-white/10 bg-white/[0.06] text-slate-300">{markLabel(mark)}</Badge>) : <Badge className="border-white/10 bg-white/[0.06] text-slate-400">unmarked</Badge>}
            </div>
          </div>
          <div className="text-xs font-bold text-slate-200">{shortId(latest.session_id)} · {compact(latest.status, "none")}</div>
          <p className="mt-2 max-h-36 overflow-auto whitespace-pre-wrap text-xs leading-5 text-slate-400">
            {compact(latest.structured_return_preview || latest.purpose_text, "아직 반환 없음")}
          </p>
        </section>

        <section className="rounded-xl border border-white/10 bg-white/[0.04] p-4">
          <div className="text-[10px] font-black uppercase tracking-[0.18em] text-slate-500">packet digest</div>
          <div className="mt-3 space-y-2">
            <div className="flex items-center justify-between gap-3 text-xs">
              <span className="text-slate-500">active events</span>
              <span className="font-bold text-cyan-100">{activeRuntimeOnlyEvents.length} runtime</span>
            </div>
            <div className="flex items-center justify-between gap-3 text-xs">
              <span className="text-slate-500">source profile</span>
              <span className="max-w-[58%] truncate text-right font-bold text-slate-200">{latestSourceProfileEvent?.detail || "not profiled yet"}</span>
            </div>
            <div className="flex items-center justify-between gap-3 text-xs">
              <span className="text-slate-500">lens</span>
              <span className="font-bold text-slate-200">{currentPacket.taskLens}</span>
            </div>
            <div className="flex items-center justify-between gap-3 text-xs">
              <span className="text-slate-500">evidence</span>
              <span className="font-bold text-slate-200">{currentPacket.evidenceBundle.searchBadge}</span>
            </div>
            <div className="flex items-center justify-between gap-3 text-xs">
              <span className="text-slate-500">route</span>
              <span className="font-bold text-slate-200">{routeLabel(currentPacket.nextRouteCandidate)}</span>
            </div>
            <div className="flex items-center justify-between gap-3 text-xs">
              <span className="text-slate-500">return shape</span>
              <span className="font-bold text-slate-200">{currentPacket.expectedReturnShape}</span>
            </div>
          </div>
        </section>
      </div>
      </div>

      <SessionActivityRail
        currentEvents={currentRunEvents.length ? currentRunEvents : sessionEvents.slice(0, 4).reverse()}
        historyEvents={historyRunEvents}
        activePackageId={activePackage?.id}
        currentSessionId={currentRuntimeSessionId}
      />

      <details className="border-t border-white/10 bg-slate-900/60 px-4 py-3">
        <summary className="cursor-pointer text-[10px] font-black uppercase tracking-[0.18em] text-slate-500">support: engine setup / package controls</summary>
        <p className="mt-3 max-w-3xl text-[10px] leading-4 text-slate-500">
          이 영역은 Claude Code의 CLAUDE.md / spec.md / context refs처럼, 새 패키지가 시작될 때 CLI가 먼저 읽을 목적, 렌즈, 내부 근거를 잡는 셋업면이다.
          전면 대화는 단순하게 두고, 실행 전 엔진 wrapper는 여기서 조정한다.
        </p>
        <div className="mt-4 grid gap-3 lg:grid-cols-[150px_1fr]">
          <label className="space-y-2 text-[10px] font-black uppercase tracking-[0.18em] text-slate-500">
            reading lens
            <select
              value={taskType}
              onChange={(event) => setTaskType(event.target.value)}
              className="w-full rounded-lg border border-white/10 bg-slate-950 px-3 py-2 text-xs normal-case tracking-normal text-slate-100"
              style={{
                backgroundColor: "#020617",
                color: "#f8fafc",
              }}
            >
              <option value="summarize">summarize</option>
              <option value="inspect">inspect</option>
              <option value="reread">reread</option>
              <option value="validate">validate</option>
            </select>
          </label>
          <label className="space-y-2 text-[10px] font-black uppercase tracking-[0.18em] text-slate-500">
            package purpose / instruction
            <Textarea
              value={purpose}
              onChange={(event: any) => setPurpose(event.target.value)}
              className="min-h-[72px] w-full rounded-lg border-white/10 bg-slate-950 text-xs normal-case tracking-normal text-slate-100"
              style={{
                backgroundColor: "#020617",
                color: "#f8fafc",
                caretColor: "#67e8f9",
              }}
            />
          </label>
        </div>
        <label className="mt-3 block space-y-2 text-[10px] font-black uppercase tracking-[0.18em] text-slate-500">
          engine context refs / spec inputs
          <Textarea
            value={contextRefs}
            onChange={(event: any) => setContextRefs(event.target.value)}
            className="min-h-[72px] w-full rounded-lg border-white/10 bg-slate-950 font-mono text-xs normal-case tracking-normal text-slate-100"
            style={{
              backgroundColor: "#020617",
              color: "#f8fafc",
              caretColor: "#67e8f9",
            }}
          />
        </label>
        <div className="mt-3 flex flex-wrap gap-2">
          {(["user", "vectorfl", "engine"] as SurfaceId[]).map((surface) => (
            <Button
              key={surface}
              onClick={() => focusSurface(surface)}
              className="rounded-lg border border-white/25 px-3 py-2 text-xs font-black text-white"
              style={{ backgroundColor: "#020617", color: "#ffffff" }}
            >
              {surface} template
            </Button>
          ))}
        </div>
      </details>

      <details className="border-t border-white/10 bg-slate-900/60 px-4 py-3">
        <summary className="cursor-pointer text-[10px] font-black uppercase tracking-[0.18em] text-slate-500">inspector: recent turns and route marks</summary>
        <div className="mt-3 grid gap-2 lg:grid-cols-2">
          {recentTurns.length ? recentTurns.slice(0, 6).map((turn) => (
            <button
              key={turn.session_id}
              onClick={() => {
                setLatest(turn);
                continueFromTurn(turn);
              }}
              className="rounded-lg border border-white/10 bg-white/[0.04] p-3 text-left hover:bg-white/[0.08]"
            >
              <div className="flex items-center justify-between gap-2">
                <span className="font-mono text-[10px] text-slate-500">{shortId(turn.session_id)}</span>
                <span className="text-[10px] text-slate-500">{turn.status || "unknown"}</span>
              </div>
              <div className="mt-2 line-clamp-2 text-xs leading-5 text-slate-300">{compact(turn.purpose_text, "no purpose")}</div>
            </button>
          )) : <div className="text-xs text-slate-500">No recent CLI turns yet.</div>}
        </div>
        <div className="mt-3 flex flex-wrap gap-2">
          <Button onClick={() => markLatest("reread_target")} className="rounded-lg border border-white/25 font-black text-white" style={{ backgroundColor: "#020617", color: "#ffffff" }}>reread</Button>
          <Button onClick={() => markLatest("user_assignment_candidate")} className="rounded-lg border border-white/25 font-black text-white" style={{ backgroundColor: "#020617", color: "#ffffff" }}>user assignment</Button>
          <Button onClick={() => markLatest("engine_request_candidate")} className="rounded-lg border border-white/25 font-black text-white" style={{ backgroundColor: "#020617", color: "#ffffff" }}>engine request</Button>
          <Button onClick={() => markLatest("validation_target")} className="rounded-lg border border-white/25 font-black text-white" style={{ backgroundColor: "#020617", color: "#ffffff" }}>validation</Button>
          <Button onClick={() => markLatest("deposit_candidate")} className="rounded-lg border border-white/25 font-black text-white" style={{ backgroundColor: "#020617", color: "#ffffff" }}>deposit</Button>
        </div>
      </details>

      <div className="border-t border-white/10 px-4 py-2 text-[9px] font-mono italic text-slate-500">
        Uses existing runtime/cli_sessions and integrated-engine API. No package 2, no background registry, no new surface.
      </div>
    </section>
  );
}
