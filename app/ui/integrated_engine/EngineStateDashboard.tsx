import React, { useEffect, useMemo, useState } from "react";
import {
  Activity,
  ArrowRight,
  Braces,
  Camera,
  CircleDot,
  FileInput,
  GitBranch,
  History,
  Layers3,
  RefreshCcw,
  ShieldCheck,
  Sparkles,
} from "lucide-react";
import { cx } from "./ui-components";

type DashboardState = {
  schema_version?: string;
  current_posture?: string;
  core_sentence?: string;
  cli_host_control?: {
    latest_readable_return?: any;
    recent_readable_returns?: any[];
    deposit_ready_returns?: any[];
    package_run_events?: any[];
    package_notebooks?: any[];
    guard?: Record<string, boolean>;
  };
  session_worker_policy?: {
    primary_operator?: any;
    secondary_operator?: any;
    script_first_jobs?: string[];
    cli_worker_jobs?: string[];
    forbidden?: string[];
  };
  guard?: Record<string, boolean>;
  next_implementation_boundary?: {
    first_real_object?: string;
    first_real_actions?: string[];
    do_not_build_yet?: string[];
  };
};

type RefreshState = {
  status: "loading" | "live" | "error";
  lastUpdated: string;
  error: string;
};

function compact(value?: string, fallback = "pending", limit = 160) {
  const text = String(value || "").trim();
  if (!text) return fallback;
  return text.length > limit ? `${text.slice(0, limit - 1)}...` : text;
}

function shortId(value?: string) {
  return value ? value.replace("cli_", "") : "none";
}

function routeLabel(turn?: any) {
  const label = turn?.route_label || turn?.suggested_next_use || "";
  return label ? String(label).replace(/_/g, " ") : "unrouted";
}

function ShellCard({ className, children }: { className?: string; children: React.ReactNode }) {
  return (
    <section className={cx("rounded-[26px] border border-white/10 bg-white/[0.045] p-5 shadow-2xl shadow-black/20", className)}>
      {children}
    </section>
  );
}

function Eyebrow({ icon: Icon, label, tone = "text-cyan-300" }: { icon: any; label: string; tone?: string }) {
  return (
    <div className={cx("flex items-center gap-2 text-[10px] font-black uppercase tracking-[0.18em]", tone)}>
      <Icon className="h-3.5 w-3.5" />
      {label}
    </div>
  );
}

function Metric({ label, value, note, active }: { label: string; value: string; note?: string; active?: boolean }) {
  return (
    <div className={cx("rounded-2xl border px-4 py-3", active ? "border-cyan-300/30 bg-cyan-300/10" : "border-white/10 bg-slate-950/70")}>
      <div className="text-[9px] font-black uppercase tracking-[0.15em] text-slate-500">{label}</div>
      <div className="mt-1 text-sm font-black text-slate-100">{value}</div>
      {note ? <div className="mt-1 line-clamp-2 text-[10px] leading-4 text-slate-500">{note}</div> : null}
    </div>
  );
}

function FlowStep({
  index,
  label,
  status,
  detail,
  active,
}: {
  index: number;
  label: string;
  status: string;
  detail: string;
  active?: boolean;
}) {
  return (
    <div className="grid grid-cols-[34px_1fr] gap-3">
      <div className="flex flex-col items-center">
        <div className={cx("grid h-8 w-8 place-items-center rounded-full border text-xs font-black", active ? "border-cyan-300 bg-cyan-300 text-slate-950" : "border-white/10 bg-slate-950 text-slate-500")}>
          {index}
        </div>
        {index < 7 ? <div className="my-2 h-8 w-px bg-gradient-to-b from-white/20 to-transparent" /> : null}
      </div>
      <div className="pb-3">
        <div className="flex flex-wrap items-center justify-between gap-2">
          <div className="text-sm font-black text-slate-100">{label}</div>
          <div className={cx("rounded-full border px-2 py-0.5 text-[9px] font-bold uppercase tracking-[0.1em]", active ? "border-cyan-300/30 bg-cyan-300/10 text-cyan-100" : "border-white/10 bg-white/[0.04] text-slate-400")}>
            {status}
          </div>
        </div>
        <p className="mt-1 text-[11px] leading-5 text-slate-500">{detail}</p>
      </div>
    </div>
  );
}

function EventRow({ event }: { event: any }) {
  return (
    <div className="rounded-2xl border border-white/10 bg-slate-950/70 p-3">
      <div className="flex items-start justify-between gap-3">
        <div>
          <div className="text-xs font-black text-slate-100">{compact(event.label || event.event_type || "event", "event", 70)}</div>
          <div className="mt-1 text-[10px] uppercase tracking-[0.12em] text-slate-500">
            {event.stage || event.package_id || "runtime event"}
          </div>
        </div>
        <div className="rounded-full border border-white/10 px-2 py-0.5 text-[9px] font-bold text-slate-400">{event.status || event.confidence || "recorded"}</div>
      </div>
      <p className="mt-2 line-clamp-3 text-[10px] leading-4 text-slate-500">{compact(event.detail || event.signal, "no detail", 220)}</p>
    </div>
  );
}

function LensRail({ lenses }: { lenses: Array<{ label: string; value: string; note: string; active?: boolean }> }) {
  return (
    <div className="grid gap-3 md:grid-cols-2 xl:grid-cols-4">
      {lenses.map((lens) => (
        <div key={lens.label} className={cx("rounded-2xl border p-4", lens.active ? "border-emerald-300/30 bg-emerald-300/10" : "border-white/10 bg-slate-950/60")}>
          <div className="text-[9px] font-black uppercase tracking-[0.16em] text-slate-500">{lens.label}</div>
          <div className="mt-2 text-lg font-black text-slate-100">{lens.value}</div>
          <p className="mt-1 text-[10px] leading-4 text-slate-500">{lens.note}</p>
        </div>
      ))}
    </div>
  );
}

export default function EngineStateDashboard() {
  const [state, setState] = useState<DashboardState>({});
  const [refresh, setRefresh] = useState<RefreshState>({ status: "loading", lastUpdated: "", error: "" });

  async function refreshState() {
    try {
      const response = await fetch("/api/vectorfl-engine/state");
      const result = await response.json();
      if (!response.ok) throw new Error(result.error || "failed to read engine state");
      setState(result);
      setRefresh({ status: "live", lastUpdated: new Date().toLocaleTimeString(), error: "" });
    } catch (error: any) {
      setRefresh({ status: "error", lastUpdated: new Date().toLocaleTimeString(), error: error?.message || "failed to refresh" });
    }
  }

  useEffect(() => {
    refreshState();
    const intervalId = window.setInterval(refreshState, 5000);
    return () => window.clearInterval(intervalId);
  }, []);

  const cli = state.cli_host_control || {};
  const latest = cli.latest_readable_return || {};
  const recent = cli.recent_readable_returns || [];
  const events = cli.package_run_events || [];
  const notebooks = cli.package_notebooks || [];
  const workerPolicy = state.session_worker_policy || {};
  const hasLatest = Boolean(latest.session_id);
  const hasEvents = events.length > 0;

  const flowSteps = useMemo(
    () => [
      {
        label: "사용자 입력 / 터미널 대화",
        status: hasLatest ? "captured" : "waiting",
        detail: hasLatest ? compact(latest.purpose_text, "latest session captured", 180) : "아직 runtime/cli_sessions에 반영된 최신 대화가 없다.",
        active: true,
      },
      {
        label: "lookup / 공정 힌트",
        status: "script-suggested",
        detail: "space_boundary_lookup_packet 같은 스크립트는 source surface, 후보 자산, lens를 제안만 한다.",
        active: true,
      },
      {
        label: "VectorFL 판독",
        status: routeLabel(latest),
        detail: "최종 렌즈, route, 과승격 금지선은 Codex/VectorFL 판독에서 결정한다.",
        active: hasLatest,
      },
      {
        label: "Codex 기본 모드",
        status: "interpreter/output",
        detail: "기본은 실행자가 아니라 해석/출력 모드. 필요할 때만 bounded worker-role로 올린다.",
        active: true,
      },
      {
        label: "운동 / worker elevation",
        status: hasLatest ? latest.task_type || "reread" : "not elevated",
        detail: "bounded comparer, packet preparer, implementation worker 같은 역할 제한이 붙어야 한다.",
        active: hasLatest && latest.task_type,
      },
      {
        label: "validation return",
        status: hasLatest ? latest.status || "returned" : "pending",
        detail: hasLatest ? compact(latest.structured_return_preview, "return exists, reread needed", 180) : "결과는 final이 아니라 다시 형성층으로 돌아오는 재료다.",
        active: hasLatest,
      },
      {
        label: "공간 재투입 / 숙성",
        status: latest.route_label === "deposit_candidate" ? "candidate" : "manual judgment",
        detail: "공간에 넣을지, hold할지, residue로 남길지는 별도 판단이다. 자동 ingestion이 아니다.",
        active: hasLatest,
      },
    ],
    [hasLatest, latest]
  );

  const lensSignals = [
    {
      label: "L / camera",
      value: "visible",
      note: "이 화면은 통합엔진 조작 화면이 아니라 흐름 관측 카메라다.",
      active: true,
    },
    {
      label: "T / maturity",
      value: state.current_posture || "forming",
      note: "대부분의 반환은 final보다 PASS_WITH_NOTE / hold / reread 후보로 남는다.",
      active: true,
    },
    {
      label: "X / translation",
      value: hasLatest ? "runtime -> dashboard" : "pending",
      note: "터미널 대화가 runtime state로 번역될 때 화면에 잡힌다.",
      active: hasLatest,
    },
    {
      label: "R / residue",
      value: `${recent.length} recent`,
      note: "CLI session, event ledger, report가 다시 찾을 수 있는 흔적이 된다.",
      active: recent.length > 0,
    },
  ];

  return (
    <div className="min-h-screen bg-[#07110f] text-slate-100">
      <div className="pointer-events-none fixed inset-0 opacity-70">
        <div className="absolute inset-0 bg-[radial-gradient(circle_at_top_left,rgba(45,212,191,0.18),transparent_35%),radial-gradient(circle_at_85%_20%,rgba(251,191,36,0.12),transparent_32%),linear-gradient(135deg,#07110f,#0f172a_48%,#111827)]" />
        <div className="absolute inset-0 bg-[linear-gradient(rgba(255,255,255,0.035)_1px,transparent_1px),linear-gradient(90deg,rgba(255,255,255,0.025)_1px,transparent_1px)] bg-[size:42px_42px]" />
      </div>

      <main className="relative mx-auto max-w-[1500px] px-5 py-6">
        <header className="rounded-[32px] border border-white/10 bg-black/30 p-6 shadow-2xl backdrop-blur">
          <div className="flex flex-wrap items-start justify-between gap-5">
            <div>
              <Eyebrow icon={Activity} label="Formation-Movement Flow Dashboard" />
              <h1 className="mt-3 max-w-4xl text-4xl font-black tracking-tight text-white md:text-5xl">
                지금 재료가 어디를 지나고 있는지 보는 화면
              </h1>
              <p className="mt-3 max-w-4xl text-sm leading-6 text-slate-400">
                기존 통합엔진 UI 코드를 참조하되, 목적은 조작이 아니라 관측이다. 터미널 대화, lookup hint, Codex return, 공간 재투입 후보를 한 장에서 본다.
              </p>
            </div>
            <button
              onClick={refreshState}
              className="rounded-2xl border border-cyan-300/30 bg-cyan-300/10 px-4 py-3 text-xs font-black uppercase tracking-[0.16em] text-cyan-100"
            >
              <RefreshCcw className="mr-2 inline h-4 w-4" />
              refresh
            </button>
          </div>
          <div className="mt-5 grid gap-3 md:grid-cols-4">
            <Metric label="state source" value="/api/vectorfl-engine/state" note="5초 poll" active />
            <Metric label="latest session" value={shortId(latest.session_id)} note={routeLabel(latest)} />
            <Metric label="events" value={String(events.length)} note="package run events" />
            <Metric label="refresh" value={refresh.status} note={refresh.error || refresh.lastUpdated || "starting"} />
          </div>
        </header>

        <div className="mt-5 grid gap-5 xl:grid-cols-[1.05fr_0.95fr]">
          <ShellCard className="bg-black/35 backdrop-blur">
            <Eyebrow icon={GitBranch} label="Default Flow" tone="text-amber-300" />
            <h2 className="mt-2 text-2xl font-black">입력에서 공간 재투입까지</h2>
            <p className="mt-2 text-xs leading-5 text-slate-500">
              이 흐름은 자동 실행 경로가 아니라 현재 재료의 위치를 읽기 위한 관측선이다.
            </p>
            <div className="mt-5">
              {flowSteps.map((step, index) => (
                <FlowStep key={step.label} index={index + 1} {...step} />
              ))}
            </div>
          </ShellCard>

          <div className="space-y-5">
            <ShellCard className="bg-black/35 backdrop-blur">
              <Eyebrow icon={Camera} label="Lens / Camera Rail" tone="text-emerald-300" />
              <h2 className="mt-2 text-2xl font-black">현재 보이는 렌즈 값</h2>
              <p className="mt-2 text-xs leading-5 text-slate-500">렌즈는 확정값이 아니라 어떤 방식으로 읽고 있는지 보여주는 관측 값이다.</p>
              <div className="mt-5">
                <LensRail lenses={lensSignals} />
              </div>
            </ShellCard>

            <ShellCard className="bg-black/35 backdrop-blur">
              <Eyebrow icon={ShieldCheck} label="Guardrails" tone="text-lime-300" />
              <div className="mt-4 grid gap-3 md:grid-cols-2">
                {Object.entries({ ...(state.guard || {}), ...(cli.guard || {}) })
                  .slice(0, 8)
                  .map(([key, value]) => (
                    <Metric key={key} label={key} value={value ? "true" : "false"} />
                  ))}
              </div>
            </ShellCard>
          </div>
        </div>

        <div className="mt-5 grid gap-5 xl:grid-cols-3">
          <ShellCard className="xl:col-span-2 bg-black/35 backdrop-blur">
            <Eyebrow icon={History} label="Runtime Return Feed" tone="text-sky-300" />
            <div className="mt-4 grid gap-3 md:grid-cols-2">
              {recent.slice(0, 6).map((turn) => (
                <div key={turn.session_id} className="rounded-2xl border border-white/10 bg-slate-950/70 p-4">
                  <div className="flex items-start justify-between gap-3">
                    <div>
                      <div className="text-sm font-black text-white">{shortId(turn.session_id)}</div>
                      <div className="mt-1 text-[10px] uppercase tracking-[0.14em] text-slate-500">{turn.task_type || "turn"} · {routeLabel(turn)}</div>
                    </div>
                    <div className="rounded-full border border-white/10 px-2 py-0.5 text-[9px] font-bold text-slate-400">{turn.status || "unknown"}</div>
                  </div>
                  <p className="mt-3 line-clamp-4 text-[11px] leading-5 text-slate-400">{compact(turn.structured_return_preview || turn.purpose_text, "no preview", 360)}</p>
                </div>
              ))}
              {!recent.length ? <div className="rounded-2xl border border-white/10 bg-slate-950/70 p-4 text-xs text-slate-500">No recent CLI returns yet.</div> : null}
            </div>
          </ShellCard>

          <ShellCard className="bg-black/35 backdrop-blur">
            <Eyebrow icon={CircleDot} label="Events" tone="text-orange-300" />
            <div className="mt-4 space-y-3">
              {events.slice(0, 7).map((event, index) => (
                <EventRow key={event.event_id || index} event={event} />
              ))}
              {!events.length ? <div className="rounded-2xl border border-white/10 bg-slate-950/70 p-4 text-xs text-slate-500">No package events yet.</div> : null}
            </div>
          </ShellCard>
        </div>

        <div className="mt-5 grid gap-5 xl:grid-cols-3">
          <ShellCard className="bg-black/35 backdrop-blur">
            <Eyebrow icon={FileInput} label="Script First" tone="text-teal-300" />
            <div className="mt-4 space-y-2">
              {(workerPolicy.script_first_jobs || []).map((item) => (
                <div key={item} className="rounded-xl border border-white/10 bg-slate-950/70 px-3 py-2 text-xs text-slate-300">{item}</div>
              ))}
            </div>
          </ShellCard>
          <ShellCard className="bg-black/35 backdrop-blur">
            <Eyebrow icon={Braces} label="Codex Role" tone="text-cyan-300" />
            <div className="mt-4 space-y-3">
              <Metric label="primary" value={workerPolicy.primary_operator?.worker || "codex"} note={workerPolicy.primary_operator?.role || "interpreter/output mode by default"} active />
              <Metric label="secondary" value={workerPolicy.secondary_operator?.worker || "gemini"} note={workerPolicy.secondary_operator?.role || "cross-check when needed"} />
            </div>
          </ShellCard>
          <ShellCard className="bg-black/35 backdrop-blur">
            <Eyebrow icon={GitBranch} label="Next Boundary" tone="text-amber-300" />
            <div className="mt-4 space-y-2">
              <Metric label="first real object" value={state.next_implementation_boundary?.first_real_object || "work_packet"} />
              {(state.next_implementation_boundary?.do_not_build_yet || []).slice(0, 4).map((item) => (
                <div key={item} className="rounded-xl border border-amber-300/20 bg-amber-300/10 px-3 py-2 text-xs text-amber-100">do not: {item}</div>
              ))}
            </div>
          </ShellCard>
        </div>

        <footer className="mt-6 rounded-[24px] border border-white/10 bg-black/25 p-4 text-[11px] leading-5 text-slate-500">
          <Sparkles className="mr-2 inline h-3.5 w-3.5 text-cyan-300" />
          이 대시보드는 기존 통합엔진 화면을 대체하지 않는다. 목적은 사용자가 터미널에서 하는 작업이 공간/공정/렌즈/return loop 안에서 어디에 놓이는지 빠르게 보는 것이다.
        </footer>
      </main>
    </div>
  );
}
