import React from "react";
import { Blocks, Activity } from "lucide-react";
import { Card, CardHeader, CardTitle, CardDescription, CardContent } from "./ui-components";

export function FlowSummaryPanel({ stats, summary }: { stats: { label: string; value: string; note: string }[]; summary: any }) {
  return (
    <section className="rounded-[28px] border border-amber-500/20 bg-gradient-to-br from-amber-900/10 to-slate-900 p-6 shadow-2xl">
      <div className="flex items-center gap-3 mb-6">
        <div className="rounded-2xl bg-amber-500/20 p-2.5 border border-amber-500/30">
          <Blocks className="h-6 w-6 text-amber-400" />
        </div>
        <div>
          <div className="text-[10px] uppercase tracking-[0.2em] text-amber-400/80 font-bold">Interpretation / Mediation Layer</div>
          <h2 className="text-xl font-bold text-white tracking-tight">VectorFL Surface: Work Packet Mediation</h2>
        </div>
      </div>
      <div className="grid gap-6 xl:grid-cols-[1fr_1fr]">
        <div className="grid grid-cols-2 gap-3">
          {stats.map((item) => (
            <div key={item.label} className="rounded-2xl border border-white/5 bg-white/[0.02] p-4">
              <div className="text-[9px] uppercase tracking-wider text-slate-500 font-bold mb-1">{item.label}</div>
              <div className="text-lg font-mono font-bold text-white">{item.value}</div>
              <div className="text-[9px] text-slate-600 mt-1">{item.note}</div>
            </div>
          ))}
        </div>
        <div className="grid grid-cols-2 gap-3">
          {[
            { label: "Strongest Line", val: summary.strongest },
            { label: "Weakest Line", val: summary.weakest },
            { label: "Current Focus", val: summary.currentFocus },
            { label: "Next Intervention", val: summary.nextIntervention }
          ].map(box => (
            <div key={box.label} className="rounded-2xl border border-white/5 bg-white/[0.03] p-4">
              <div className="text-[9px] uppercase tracking-widest text-amber-400/60 font-black mb-1">{box.label}</div>
              <div className="text-xs text-slate-300 font-medium leading-5 truncate" title={box.val}>{box.val}</div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
