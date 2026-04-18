import React from "react";
import { ShieldCheck, Activity, TrendingUp, AlertTriangle } from "lucide-react";
import { Card, CardHeader, CardTitle, CardContent, Badge } from "./ui-components";

export function SpaceHealthPanel({ 
  syncRate, 
  maturationLevel, 
  activeViolations 
}: {
  syncRate: number; // 0-100
  maturationLevel: number; // 0-100
  activeViolations: number;
}) {
  return (
    <Card className="rounded-[28px] border-white/10 bg-gradient-to-br from-zinc-900 to-black text-white shadow-2xl">
      <CardHeader className="pb-2">
        <div className="flex items-center gap-3">
          <ShieldCheck className="h-5 w-5 text-emerald-400" />
          <CardTitle className="text-lg">Space Health & Maturation</CardTitle>
        </div>
      </CardHeader>
      <CardContent>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 py-2">
          
          {/* Baseline Sync Rate */}
          <div className="space-y-3">
            <div className="flex justify-between text-[11px] uppercase tracking-wider text-slate-500">
              <span>Baseline Sync</span>
              <span className="text-emerald-400 font-mono">{syncRate}%</span>
            </div>
            <div className="h-1.5 w-full bg-white/5 rounded-full overflow-hidden">
              <div 
                className="h-full bg-emerald-500 transition-all duration-1000" 
                style={{ width: `${syncRate}%` }} 
              />
            </div>
            <p className="text-[10px] text-slate-400 leading-4">리포지토리 자산과 현재 working lexicon 기준선 간의 mock 정렬도입니다.</p>
          </div>

          {/* Maturation Progress */}
          <div className="space-y-3">
            <div className="flex justify-between text-[11px] uppercase tracking-wider text-slate-500">
              <span>Line Maturation</span>
              <span className="text-sky-400 font-mono">{maturationLevel}%</span>
            </div>
            <div className="h-1.5 w-full bg-white/5 rounded-full overflow-hidden">
              <div 
                className="h-full bg-sky-500 transition-all duration-1000" 
                style={{ width: `${maturationLevel}%` }} 
              />
            </div>
            <p className="text-[10px] text-slate-400 leading-4">현재 공간 내 '라인'들이 임계점을 넘어 데이터로 응결된 정도입니다.</p>
          </div>

          {/* Active Risks */}
          <div className="flex flex-col justify-center items-center bg-white/[0.03] rounded-2xl p-4 border border-white/5">
            <div className="flex items-center gap-2 mb-1">
              <AlertTriangle className={`h-4 w-4 ${activeViolations > 0 ? "text-rose-500 animate-bounce" : "text-slate-500"}`} />
              <span className="text-[11px] uppercase tracking-widest text-slate-400">Active Risks</span>
            </div>
            <div className={`text-3xl font-bold font-mono ${activeViolations > 0 ? "text-rose-500" : "text-slate-200"}`}>
              {activeViolations}
            </div>
            <Badge variant="outline" className={`mt-2 text-[9px] ${activeViolations > 0 ? "border-rose-500/30 text-rose-400" : "border-slate-700 text-slate-500"}`}>
              {activeViolations > 0 ? "INTERVENTION REQUIRED" : "STABLE STATE"}
            </Badge>
          </div>

        </div>
      </CardContent>
    </Card>
  );
}
