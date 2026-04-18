import React from "react";
import { Goal } from "lucide-react";
import { Input } from "./ui-components";
import { BoardStat } from "./user-surface.types";

export function CommandHeaderPanel({ 
  goal, 
  onGoalChange, 
  stats,
  infoBoxes
}: { 
  goal: string; 
  onGoalChange: (val: string) => void; 
  stats: any[];
  infoBoxes: { label: string; val: string }[];
}) {
  return (
    <section className="rounded-[28px] border border-indigo-500/20 bg-gradient-to-br from-indigo-900/10 to-slate-950 p-6 shadow-2xl">
      <div className="flex items-center gap-3 mb-6">
        <Goal className="h-5 w-5 text-indigo-400" />
        <div className="text-sm font-bold text-white uppercase tracking-wider">Goal & Scope</div>
      </div>
      <Input 
        value={goal} 
        onChange={(e: any) => onGoalChange(e.target.value)} 
        className="h-14 mb-6 text-lg font-medium bg-black/40 border-white/10" 
      />
      <div className="grid gap-4 sm:grid-cols-2">
        {infoBoxes.map((box: any) => (
          <div key={box.label} className="rounded-2xl border border-white/5 bg-white/[0.03] p-4 transition-colors hover:border-indigo-500/20">
            <div className="text-[9px] uppercase tracking-widest text-indigo-400/60 font-black mb-1">{box.label}</div>
            <div className="text-xs text-slate-300 font-medium leading-5">{box.val}</div>
          </div>
        ))}
      </div>
    </section>
  );
}
