import React from "react";
import { Users, Plus, Trash2, BrainCircuit, Search, Code2, ShieldCheck, PenSquare, Sparkles } from "lucide-react";
import { Card, CardHeader, CardTitle, CardDescription, CardContent, Button } from "./ui-components";
import { Team, TeamKind, TeamStatus } from "./user-surface.types";

const teamKindMeta: Record<TeamKind, { label: string; icon: React.ComponentType<{ className?: string }> }> = {
  internal: { label: "내부 분석", icon: BrainCircuit },
  external: { label: "외부 서치", icon: Search },
  build: { label: "구현", icon: Code2 },
  review: { label: "검증", icon: ShieldCheck },
  writing: { label: "작문", icon: PenSquare },
  shorts: { label: "쇼츠", icon: Sparkles },
  custom: { label: "기타", icon: Users }
};

function statusClass(status: TeamStatus) {
  switch (status) {
    case "active": return "bg-emerald-500/20 text-emerald-400 border border-emerald-500/30";
    case "queued": return "bg-amber-500/20 text-amber-400 border border-amber-500/30";
    case "waiting": return "bg-slate-800 text-slate-400 border border-slate-700";
    default: return "bg-slate-900 text-slate-500";
  }
}

export function TeamRoutingPanel({ 
  teams, 
  selectedId, 
  onSelect, 
  onAdd, 
  onRemove 
}: {
  teams: Team[];
  selectedId: string | null;
  onSelect: (id: string) => void;
  onAdd: () => void;
  onRemove: () => void;
}) {
  return (
    <Card className="rounded-[28px] border-white/10 bg-[#0d0d12] text-slate-100 shadow-2xl">
      <CardHeader className="border-b border-white/5 pb-6">
        <div className="flex items-center justify-between gap-3">
          <div className="flex items-center gap-3">
            <div className="rounded-2xl bg-indigo-500/10 p-2.5 border border-indigo-500/20"><Users className="h-5 w-5 text-indigo-400" /></div>
            <div>
              <CardTitle className="text-lg font-bold text-white tracking-tight">Team Routing Board</CardTitle>
              <CardDescription className="text-[11px] text-slate-500 uppercase tracking-wider">Dynamic Path Management</CardDescription>
            </div>
          </div>
          <div className="flex gap-2">
            <Button size="sm" onClick={onAdd} className="rounded-xl bg-indigo-600 hover:bg-indigo-500"><Plus className="mr-2 h-4 w-4" />팀 추가</Button>
            <Button size="sm" variant="outline" onClick={onRemove} className="rounded-xl border-white/10 hover:bg-white/5 text-slate-400"><Trash2 className="mr-2 h-4 w-4" /></Button>
          </div>
        </div>
      </CardHeader>
      <CardContent className="space-y-3 pt-6">
        {teams.map((team) => {
          const isActive = selectedId === team.id;
          const Icon = teamKindMeta[team.kind].icon;
          return (
            <button 
              key={team.id} 
              onClick={() => onSelect(team.id)} 
              className={`group w-full rounded-2xl border p-4 text-left transition-all duration-300 relative overflow-hidden ${
                isActive 
                  ? "border-indigo-500/40 bg-indigo-500/10 shadow-[0_0_20px_rgba(99,102,241,0.1)]" 
                  : "border-white/5 bg-white/[0.02] hover:bg-white/[0.05]"
              }`}
            >
              <div className="flex items-start justify-between gap-3 relative z-10">
                <div className="flex items-start gap-3">
                  <div className={`rounded-xl p-2 border transition-colors ${isActive ? "bg-indigo-500/20 border-indigo-500/30" : "bg-white/5 border-white/5 group-hover:border-white/10"}`}>
                    <Icon className={`h-4 w-4 ${isActive ? "text-indigo-400" : "text-slate-500"}`} />
                  </div>
                  <div>
                    <div className={`font-bold text-sm ${isActive ? "text-white" : "text-slate-300"}`}>{team.name}</div>
                    <div className="mt-1 text-[10px] uppercase tracking-widest text-slate-500 font-bold">
                      {teamKindMeta[team.kind].label} <span className="mx-1 opacity-30">|</span> roles {team.roles.length}
                    </div>
                  </div>
                </div>
                <span className={`rounded-full px-2.5 py-0.5 text-[9px] font-black uppercase tracking-tighter ${statusClass(team.status)}`}>
                  {team.status}
                </span>
              </div>
            </button>
          );
        })}
      </CardContent>
    </Card>
  );
}
