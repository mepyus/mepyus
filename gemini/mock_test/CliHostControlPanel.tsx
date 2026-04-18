import React, { useEffect, useMemo, useState } from "react";
import { RefreshCcw, Play, BadgeCheck, Archive, Eye, GitPullRequest } from "lucide-react";
import { Badge, Button, Card, CardContent, CardHeader, CardTitle, Textarea } from "./ui-components";

type CliReadableReturn = {
  session_id?: string;
  backend_kind?: string;
  task_type?: string;
  status?: string;
  purpose_text?: string;
  marks?: string[];
  mark_history?: Array<{ mark: string; marked_at: string; source?: string }>;
  structured_return_preview?: string;
  deposit_candidate_preview?: string;
};

type CliHostState = {
  latest_readable_return?: CliReadableReturn;
};

const DEFAULT_PURPOSE = "Gemini mock 본문에서 CLI on-top path를 작게 검증한다.";
const DEFAULT_CONTEXT = "docs/reports/integrated_engine_cli_on_top_package1_1_closeout_note_v0.md";
const DEFAULT_PAYLOAD =
  "Read the bounded context. Return three short bullets: useful now, deferred, and whether CLI remains on-top. Do not modify files.";

function compact(value?: string, fallback = "pending") {
  const text = String(value || "").trim();
  return text || fallback;
}

function markLabel(mark: string) {
  return mark.replace(/_/g, " ");
}

export function CliHostControlPanel() {
  const [taskType, setTaskType] = useState("summarize");
  const [purpose, setPurpose] = useState(DEFAULT_PURPOSE);
  const [contextRefs, setContextRefs] = useState(DEFAULT_CONTEXT);
  const [promptPayload, setPromptPayload] = useState(DEFAULT_PAYLOAD);
  const [latest, setLatest] = useState<CliReadableReturn>({});
  const [status, setStatus] = useState("ready");
  const [isRunning, setIsRunning] = useState(false);

  const marks = useMemo(() => latest.marks || [], [latest.marks]);

  async function refreshLatest() {
    setStatus("refreshing latest return...");
    try {
      const response = await fetch("/api/vectorfl-engine/state");
      const result = await response.json();
      if (!response.ok) throw new Error(result.error || "failed to refresh engine state");
      const cli = (result.cli_host_control || {}) as CliHostState;
      setLatest(cli.latest_readable_return || {});
      setStatus("latest return refreshed");
    } catch (error: any) {
      setStatus(`error: ${error.message}`);
    }
  }

  async function runSession() {
    setIsRunning(true);
    setStatus("running Codex read-only session...");
    try {
      const response = await fetch("/api/vectorfl-engine/actions/cli-session/run", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          backend_kind: "codex",
          task_type: taskType,
          requested_by_surface: "vectorfl_surface",
          requested_by_page: "gemini/mock_test",
          purpose_text: purpose,
          bounded_context_refs: contextRefs,
          prompt_payload: promptPayload,
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
        marks: session.marks || [],
        mark_history: session.mark_history || [],
        structured_return_preview: result.structured_return?.result_summary || session.result_summary || "",
        deposit_candidate_preview: result.deposit_candidate_preview || "",
      });
      setStatus(`${result.ok ? "done" : "failed"} -> ${result.session_path || session.session_id}`);
    } catch (error: any) {
      setStatus(`error: ${error.message}`);
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
      }));
      setStatus(`marked ${mark}`);
    } catch (error: any) {
      setStatus(`error: ${error.message}`);
    }
  }

  useEffect(() => {
    refreshLatest();
  }, []);

  return (
    <Card className="rounded-[28px] border-cyan-500/10 bg-[#0d0d12] shadow-2xl">
      <CardHeader className="pb-3 border-b border-white/5">
        <div className="flex items-start justify-between gap-4">
          <div>
            <CardTitle className="text-cyan-300 text-xs flex items-center gap-2 uppercase tracking-widest">
              <GitPullRequest className="h-4 w-4" />
              CLI Host / Control Layer
            </CardTitle>
            <div className="mt-2 text-[10px] text-slate-500">
              Gemini mock 본문에서 쓰는 실제 Codex on-top path. 새 surface가 아니라 VectorFL support tool layer.
            </div>
          </div>
          <Badge className="bg-cyan-500/10 text-cyan-300 border border-cyan-500/20">on-top</Badge>
        </div>
      </CardHeader>
      <CardContent className="pt-5 space-y-5">
        <div className="grid gap-3 xl:grid-cols-[180px_1fr]">
          <label className="space-y-2 text-[10px] uppercase tracking-[0.2em] text-slate-500 font-black">
            Task
            <select
              value={taskType}
              onChange={(event) => setTaskType(event.target.value)}
              className="w-full rounded-xl border border-white/10 bg-black/40 px-3 py-2 text-xs normal-case tracking-normal text-slate-200"
            >
              <option value="summarize">summarize</option>
              <option value="inspect">inspect</option>
              <option value="reread">reread</option>
              <option value="validate">validate</option>
            </select>
          </label>
          <label className="space-y-2 text-[10px] uppercase tracking-[0.2em] text-slate-500 font-black">
            Purpose
            <Textarea
              value={purpose}
              onChange={(event: any) => setPurpose(event.target.value)}
              className="min-h-[72px] w-full text-xs normal-case tracking-normal text-slate-200"
            />
          </label>
        </div>

        <div className="grid gap-3 xl:grid-cols-2">
          <label className="space-y-2 text-[10px] uppercase tracking-[0.2em] text-slate-500 font-black">
            Bounded context refs
            <Textarea
              value={contextRefs}
              onChange={(event: any) => setContextRefs(event.target.value)}
              className="min-h-[94px] w-full font-mono text-xs normal-case tracking-normal text-slate-200"
            />
          </label>
          <label className="space-y-2 text-[10px] uppercase tracking-[0.2em] text-slate-500 font-black">
            Prompt payload
            <Textarea
              value={promptPayload}
              onChange={(event: any) => setPromptPayload(event.target.value)}
              className="min-h-[94px] w-full text-xs normal-case tracking-normal text-slate-200"
            />
          </label>
        </div>

        <div className="flex flex-wrap items-center gap-2">
          <Button onClick={runSession} disabled={isRunning} className="rounded-xl bg-cyan-600 text-white hover:bg-cyan-500 disabled:opacity-50">
            <Play className="mr-2 inline h-4 w-4" />
            Run Codex
          </Button>
          <Button onClick={refreshLatest} className="rounded-xl border border-white/10 bg-white/[0.03] text-slate-300 hover:bg-white/[0.06]">
            <RefreshCcw className="mr-2 inline h-4 w-4" />
            Refresh
          </Button>
          <span className="font-mono text-[10px] text-cyan-300">{status}</span>
        </div>

        <div className="grid gap-3 xl:grid-cols-4">
          <div className="rounded-2xl border border-white/5 bg-black/20 p-3">
            <div className="text-[9px] uppercase tracking-[0.2em] text-slate-500">session</div>
            <div className="mt-2 break-all font-mono text-xs text-slate-300">{compact(latest.session_id, "none")}</div>
          </div>
          <div className="rounded-2xl border border-white/5 bg-black/20 p-3">
            <div className="text-[9px] uppercase tracking-[0.2em] text-slate-500">backend / task</div>
            <div className="mt-2 text-xs text-slate-300">{compact(latest.backend_kind, "none")} / {compact(latest.task_type, "none")}</div>
          </div>
          <div className="rounded-2xl border border-white/5 bg-black/20 p-3">
            <div className="text-[9px] uppercase tracking-[0.2em] text-slate-500">status</div>
            <div className="mt-2 text-xs text-slate-300">{compact(latest.status, "none")}</div>
          </div>
          <div className="rounded-2xl border border-white/5 bg-black/20 p-3">
            <div className="text-[9px] uppercase tracking-[0.2em] text-slate-500">marks</div>
            <div className="mt-2 flex flex-wrap gap-1">
              {marks.length ? marks.map((mark) => <Badge key={mark} className="bg-white/5 text-slate-300">{markLabel(mark)}</Badge>) : <span className="text-xs text-slate-600">none</span>}
            </div>
          </div>
        </div>

        <div className="grid gap-3 xl:grid-cols-[1fr_1fr]">
          <div className="rounded-2xl border border-white/5 bg-black/20 p-4">
            <div className="text-[9px] uppercase tracking-[0.2em] text-slate-500">current engine route</div>
            <p className="mt-2 text-xs leading-6 text-slate-300">
              Latest CLI return can be marked back into reread, implementation return, validation, or deposit-candidate flow from here.
            </p>
          </div>
          <div className="rounded-2xl border border-white/5 bg-black/20 p-4">
            <div className="text-[9px] uppercase tracking-[0.2em] text-slate-500">mark history</div>
            <div className="mt-2 space-y-1">
              {latest.mark_history?.length ? (
                latest.mark_history.slice(-4).map((entry, index) => (
                  <div key={`${entry.mark}-${entry.marked_at}-${index}`} className="flex items-center justify-between gap-3 rounded-xl bg-white/[0.03] px-3 py-2 text-[10px] text-slate-400">
                    <span>{markLabel(entry.mark)}</span>
                    <span className="font-mono text-slate-600">{entry.marked_at || "marked"}</span>
                  </div>
                ))
              ) : (
                <span className="text-xs text-slate-600">no mark history yet</span>
              )}
            </div>
          </div>
        </div>

        <div className="rounded-2xl border border-white/5 bg-black/20 p-4">
          <div className="text-[9px] uppercase tracking-[0.2em] text-slate-500">latest purpose</div>
          <p className="mt-2 text-xs leading-6 text-slate-300">{compact(latest.purpose_text, "no latest purpose")}</p>
        </div>

        <div className="grid gap-3 xl:grid-cols-2">
          <div className="rounded-2xl border border-cyan-500/10 bg-cyan-500/[0.03] p-4">
            <div className="mb-2 flex items-center gap-2 text-[9px] uppercase tracking-[0.2em] text-cyan-300">
              <Eye className="h-3.5 w-3.5" /> structured return preview
            </div>
            <pre className="max-h-72 overflow-auto whitespace-pre-wrap break-words text-xs leading-6 text-slate-300">{compact(latest.structured_return_preview, "no structured return yet")}</pre>
          </div>
          <div className="rounded-2xl border border-emerald-500/10 bg-emerald-500/[0.03] p-4">
            <div className="mb-2 flex items-center gap-2 text-[9px] uppercase tracking-[0.2em] text-emerald-300">
              <Archive className="h-3.5 w-3.5" /> deposit candidate preview
            </div>
            <pre className="max-h-72 overflow-auto whitespace-pre-wrap break-words text-xs leading-6 text-slate-300">{compact(latest.deposit_candidate_preview, "no deposit candidate yet")}</pre>
          </div>
        </div>

        <div className="flex flex-wrap gap-2">
          <Button onClick={() => markLatest("reread_target")} className="rounded-xl bg-white/[0.04] text-slate-300 hover:bg-white/[0.07]">reread</Button>
          <Button onClick={() => markLatest("implementation_return")} className="rounded-xl bg-white/[0.04] text-slate-300 hover:bg-white/[0.07]">implementation</Button>
          <Button onClick={() => markLatest("validation_target")} className="rounded-xl bg-white/[0.04] text-slate-300 hover:bg-white/[0.07]">
            <BadgeCheck className="mr-2 inline h-4 w-4" /> validation
          </Button>
          <Button onClick={() => markLatest("deposit_candidate")} className="rounded-xl bg-white/[0.04] text-slate-300 hover:bg-white/[0.07]">deposit</Button>
        </div>

        <div className="text-[9px] text-slate-600 font-mono italic">
          Uses existing runtime/cli_sessions and integrated-engine API. No package 2, no background registry, no new surface.
        </div>
      </CardContent>
    </Card>
  );
}
