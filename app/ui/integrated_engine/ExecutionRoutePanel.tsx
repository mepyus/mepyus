import React from "react";
import { Ticket } from "lucide-react";
import { Card, CardHeader, CardTitle, CardDescription, CardContent } from "./ui-components";
import { Team } from "./user-surface.types";

type CliRouteReturn = {
  session_id?: string;
  task_type?: string;
  purpose_text?: string;
  marks?: string[];
  status?: string;
};

function cliTicketStage(turn: CliRouteReturn) {
  const marks = turn.marks || [];
  if (marks.includes("validation_target")) return "review";
  if (marks.includes("deposit_candidate")) return "review";
  if (marks.includes("implementation_return")) return "handoff";
  if (marks.includes("reread_target")) return "backlog";
  return "backlog";
}

function cliTicketRole(turn: CliRouteReturn) {
  const marks = turn.marks || [];
  if (marks.includes("deposit_candidate")) return "deposit review";
  if (marks.includes("validation_target")) return "validation";
  if (marks.includes("implementation_return")) return "implementation return";
  if (marks.includes("reread_target")) return "reread";
  return turn.task_type || "cli return";
}

function cliTickets(cliReturns: CliRouteReturn[]) {
  return cliReturns
    .filter((turn) => turn.session_id)
    .map((turn) => ({
      id: `cli-${turn.session_id}`,
      title: turn.purpose_text || "CLI return needs user routing",
      role: cliTicketRole(turn),
      team: `Codex CLI / ${turn.status || "unknown"}`,
      stage: cliTicketStage(turn),
    }));
}

function TicketColumn({ title, items }: { title: string; items: any[] }) {
  return (
    <div className="space-y-3">
      <div className="flex items-center justify-between px-1">
        <div className="text-[10px] font-black uppercase tracking-[0.2em] text-slate-500">{title}</div>
        <div className="text-[10px] font-mono text-slate-600">{items.length}</div>
      </div>
      <div className="space-y-2">
        {items.map((item) => (
          <div key={item.id} className="rounded-xl border border-white/5 bg-white/[0.02] p-3 shadow-sm hover:border-indigo-500/30 transition-colors">
            <div className="text-[10px] text-indigo-400 font-bold mb-1 uppercase tracking-tighter">{item.role}</div>
            <div className="text-xs font-medium text-slate-200 line-clamp-2">{item.title}</div>
            <div className="mt-2 text-[9px] text-slate-600 font-mono italic">{item.team}</div>
          </div>
        ))}
        {items.length === 0 && (
          <div className="rounded-xl border border-dashed border-white/5 p-4 text-[10px] text-slate-700 text-center italic">Empty</div>
        )}
      </div>
    </div>
  );
}

export function ExecutionRoutePanel({ teams, cliReturns = [] }: { teams: Team[]; cliReturns?: CliRouteReturn[] }) {
  const routedCliTickets = cliTickets(cliReturns);
  // Derive tickets from teams and roles
  const tickets = {
    backlog: teams.filter(t => t.status === "idle" || t.status === "waiting").flatMap(t => t.roles.map(r => ({ id: r.id, title: r.goal, role: r.title, team: t.name }))).concat(routedCliTickets.filter(t => t.stage === "backlog")),
    active: teams.filter(t => t.status === "active").flatMap(t => t.roles.filter(r => r.status === "running").map(r => ({ id: r.id, title: r.goal, role: r.title, team: t.name }))),
    handoff: teams.filter(t => t.status === "active").flatMap(t => t.roles.filter(r => r.status === "ready").map(r => ({ id: r.id, title: r.goal, role: r.title, team: t.name }))).concat(routedCliTickets.filter(t => t.stage === "handoff")),
    review: teams.filter(t => t.status === "queued").flatMap(t => t.roles.map(r => ({ id: r.id, title: r.goal, role: r.title, team: t.name }))).concat(routedCliTickets.filter(t => t.stage === "review"))
  };

  return (
    <Card className="rounded-[28px] border-white/10 bg-[#0d0d12] text-slate-100 shadow-2xl">
      <CardHeader className="border-b border-white/5 pb-6">
        <div className="flex items-center gap-3">
          <div className="rounded-2xl bg-indigo-500/10 p-2.5 border border-indigo-500/20"><Ticket className="h-5 w-5 text-indigo-400" /></div>
          <div>
            <CardTitle className="text-lg font-bold text-white tracking-tight">Execution Route Board</CardTitle>
            <CardDescription className="text-[11px] text-slate-500 uppercase tracking-wider">Dynamic Ticket Lifecycle / CLI returns are routed as candidates only</CardDescription>
          </div>
        </div>
      </CardHeader>
      <CardContent className="pt-6">
        <div className="grid gap-4 xl:grid-cols-4">
          <TicketColumn title="Backlog" items={tickets.backlog} />
          <TicketColumn title="Active" items={tickets.active} />
          <TicketColumn title="Handoff" items={tickets.handoff} />
          <TicketColumn title="Review" items={tickets.review} />
        </div>
      </CardContent>
    </Card>
  );
}
