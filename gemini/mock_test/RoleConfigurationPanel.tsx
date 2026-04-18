import React from "react";
import { Workflow, Pencil, Plus, BrainCircuit, Search, Code2, ShieldCheck, PenSquare, Sparkles, Users } from "lucide-react";
import { Card, CardHeader, CardTitle, CardContent, Button, Badge } from "./ui-components";
import { Team, Role, RoleKind, RoleStatus, TeamKind } from "./user-surface.types";

const teamKindMeta: Record<TeamKind, { label: string; icon: React.ComponentType<{ className?: string }> }> = {
  internal: { label: "내부 분석", icon: BrainCircuit },
  external: { label: "외부 서치", icon: Search },
  build: { label: "구현", icon: Code2 },
  review: { label: "검증", icon: ShieldCheck },
  writing: { label: "작문", icon: PenSquare },
  shorts: { label: "쇼츠", icon: Sparkles },
  custom: { label: "기타", icon: Users }
};

const roleKindMeta: Record<RoleKind, { label: string; icon: React.ComponentType<{ className?: string }> }> = {
  reference: { label: "레퍼런스 읽기", icon: Search },
  structure: { label: "구조 추출", icon: BrainCircuit },
  risk: { label: "리스크 탐색", icon: ShieldCheck },
  search: { label: "외부 서치", icon: Search },
  synth: { label: "종합 해석", icon: Sparkles },
  implement: { label: "실제 구현", icon: Code2 },
  validate: { label: "검증/환류", icon: ShieldCheck },
  custom: { label: "사용자 정의", icon: Users }
};

function statusClass(status: RoleStatus) {
  switch (status) {
    case "running": return "bg-sky-500/20 text-sky-400 border border-sky-500/30";
    case "ready": return "bg-emerald-500/20 text-emerald-400 border border-emerald-500/30";
    case "waiting": return "bg-slate-800 text-slate-400 border border-slate-700";
    default: return "bg-slate-900 text-slate-500";
  }
}

export function RoleConfigurationPanel({ 
  team, 
  onEditTeam, 
  onAddRole, 
  onEditRole 
}: {
  team: Team | null;
  onEditTeam: () => void;
  onAddRole: () => void;
  onEditRole: (role: Role) => void;
}) {
  if (!team) return (
    <Card className="rounded-[28px] border-white/10 bg-[#0d0d12] p-12 text-center h-full flex flex-col justify-center">
        <Users className="h-10 w-10 text-slate-700 mx-auto mb-4 opacity-20" />
        <div className="text-sm text-slate-600 font-medium">Select a team to configure roles</div>
    </Card>
  );

  return (
    <Card className="rounded-[28px] border-white/10 bg-[#0d0d12] text-slate-100 shadow-2xl">
      <CardHeader className="border-b border-white/5 pb-6">
        <div className="flex items-center justify-between gap-3">
          <div className="flex items-center gap-3">
            <div className="rounded-2xl bg-indigo-500/10 p-2.5 border border-indigo-500/20"><Workflow className="h-5 w-5 text-indigo-400" /></div>
            <div>
              <CardTitle className="text-lg font-bold text-white tracking-tight">Team Console: {team.name}</CardTitle>
            </div>
          </div>
          <div className="flex gap-2">
            <Button size="sm" variant="outline" onClick={onEditTeam} className="rounded-xl border-white/10 text-slate-400"><Pencil className="mr-2 h-4 w-4" />수정</Button>
            <Button size="sm" onClick={onAddRole} className="rounded-xl bg-indigo-600 hover:bg-indigo-500"><Plus className="mr-2 h-4 w-4" />추가</Button>
          </div>
        </div>
      </CardHeader>
      <CardContent className="pt-6">
        <div className="grid gap-4 sm:grid-cols-2">
          {team.roles.map((role) => {
            const RoleIcon = roleKindMeta[role.kind].icon;
            return (
              <div key={role.id} className="group rounded-2xl border border-white/5 bg-white/[0.02] p-5 relative overflow-hidden transition-all hover:bg-white/[0.05]">
                <div className="flex items-start justify-between gap-3 mb-4">
                  <div className="flex items-center gap-3">
                    <RoleIcon className="h-4 w-4 text-indigo-400" />
                    <div className="font-bold text-sm text-slate-200">{role.title}</div>
                  </div>
                  <Badge className={statusClass(role.status)}>{role.status}</Badge>
                </div>
                
                {/* Extension slot / optional tool layer */}
                <div className="mt-4 p-3 bg-black/40 rounded-xl border border-white/5">
                  <div className="text-[8px] uppercase tracking-widest text-slate-500 mb-2 font-bold">Extension slot / optional tool layer</div>
                  <div className="grid grid-cols-2 gap-2">
                     {/* ... selectors ... */}
                  </div>
                </div>

                <div className="mt-4 text-[10px] text-slate-500 italic">"{role.goal}"</div>
                <button onClick={() => onEditRole(role)} className="w-full mt-3 text-[10px] text-slate-600 hover:text-indigo-400 uppercase tracking-widest font-bold underline decoration-dotted">Edit Role Config</button>
              </div>
            );
          })}
        </div>
      </CardContent>
    </Card>
  );
}
