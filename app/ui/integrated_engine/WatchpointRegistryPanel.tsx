import React from "react";
import { Wrench } from "lucide-react";
import { Card, CardHeader, CardTitle, CardContent, Badge } from "./ui-components";
import { Watchpoint, WatchSeverity, WatchStatus } from "./engine-surface.types";

function severityMeta(severity: WatchSeverity) {
  return {
    high: { label: "high", className: "border-rose-500/20 bg-rose-500/15 text-rose-300" },
    medium: { label: "medium", className: "border-amber-500/20 bg-amber-500/15 text-amber-300" },
    low: { label: "low", className: "border-slate-500/20 bg-slate-500/15 text-slate-300" },
  }[severity];
}

function watchStatusMeta(status: WatchStatus) {
  return {
    open: { label: "open", className: "border-rose-500/20 bg-rose-500/15 text-rose-300" },
    watching: { label: "watching", className: "border-sky-500/20 bg-sky-500/15 text-sky-300" },
    hold: { label: "hold", className: "border-violet-500/20 bg-violet-500/15 text-violet-300" },
    resolved: { label: "resolved", className: "border-emerald-500/20 bg-emerald-500/15 text-emerald-300" },
  }[status];
}

export function WatchpointRegistryPanel({ 
  watchpoints 
}: {
  watchpoints: Watchpoint[];
}) {
  return (
    <Card className="rounded-[24px] border-white/10 bg-black/20 text-white">
      <CardHeader className="pb-3">
        <div className="flex items-center gap-3">
          <Wrench className="h-5 w-5 text-slate-300" />
          <CardTitle className="text-lg text-white">Watchpoint Registry</CardTitle>
        </div>
      </CardHeader>
      <CardContent className="space-y-3">
        {watchpoints.map((wp) => (
          <div key={wp.id} className="rounded-xl border border-white/10 bg-white/5 p-4">
            <div className="flex items-center justify-between mb-2">
              <div className="text-sm font-medium text-slate-200">{wp.title}</div>
              <div className="flex gap-2">
                <Badge className={severityMeta(wp.severity).className}>{severityMeta(wp.severity).label}</Badge>
                <Badge className={watchStatusMeta(wp.status).className}>{watchStatusMeta(wp.status).label}</Badge>
              </div>
            </div>
            <div className="text-xs text-slate-400 leading-5">{wp.why}</div>
            <div className="mt-3 text-[10px] uppercase tracking-wider text-slate-500 font-semibold border-t border-white/5 pt-2">
              Next Action: <span className="text-sky-400">{wp.nextAction}</span>
            </div>
          </div>
        ))}
      </CardContent>
    </Card>
  );
}
