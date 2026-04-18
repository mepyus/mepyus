import React from "react";
import { MessageSquare, ArrowRight, BrainCircuit, Search, Code2, ShieldCheck, PenSquare, Sparkles, Users } from "lucide-react";
import { Card, CardHeader, CardTitle, CardDescription, CardContent } from "./ui-components";
import { AuditLog, TeamKind, RoleKind } from "./user-surface.types";

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

export function OperationLogPanel({ logs }: { logs: AuditLog[] }) {
  return (
    <Card className="rounded-[28px] border-white/10 bg-[#0d0d12] text-slate-100 shadow-2xl">
      <CardHeader className="border-b border-white/5 pb-6">
        <div className="flex items-center gap-3">
          <div className="rounded-2xl bg-indigo-500/10 p-2.5 border border-indigo-500/20"><MessageSquare className="h-5 w-5 text-indigo-400" /></div>
          <div>
            <CardTitle className="text-lg font-bold text-white tracking-tight">Report / Log Center</CardTitle>
            <CardDescription className="text-[11px] text-slate-500 uppercase tracking-wider">Live Operation Feed</CardDescription>
          </div>
        </div>
      </CardHeader>
      <CardContent className="space-y-3 pt-6">
        {logs.map((item) => {
          const TeamIcon = teamKindMeta[item.teamKind].icon;
          const RoleIcon = roleKindMeta[item.roleKind].icon;
          return (
            <div key={item.id} className="rounded-2xl border border-white/5 bg-white/[0.03] p-5 hover:bg-white/[0.05] transition-colors">
              <div className="flex items-center justify-between gap-3 mb-4">
                <div className="flex items-center gap-3">
                  <div className="flex -space-x-2">
                    <div className="rounded-xl bg-slate-900 border border-white/10 p-2 text-indigo-400 z-10 shadow-lg"><TeamIcon className="h-4 w-4" /></div>
                    <div className="rounded-xl bg-white/5 border border-white/10 p-2 text-slate-400 z-0"><RoleIcon className="h-4 w-4" /></div>
                  </div>
                  <div>
                    <div className="text-sm font-bold text-white">{item.teamName}</div>
                    <div className="text-[10px] text-slate-500 uppercase tracking-tight font-black">{item.roleTitle}</div>
                  </div>
                </div>
                <div className="text-[10px] text-slate-600 font-mono">{item.time}</div>
              </div>
              <div className="text-xs text-slate-300 leading-6 border-l-2 border-indigo-500/20 pl-4 py-1 mb-3">{item.body}</div>
              <div className="mt-2 flex items-center gap-2 text-[10px] font-bold text-indigo-400/70 bg-indigo-500/5 px-3 py-1.5 rounded-lg border border-indigo-500/10">
                <ArrowRight className="h-3 w-3" /> NEXT: {item.next}
              </div>
            </div>
          );
        })}
      </CardContent>
    </Card>
  );
}
