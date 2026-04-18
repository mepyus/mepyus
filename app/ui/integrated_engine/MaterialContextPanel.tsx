import React from "react";
import { Database, FileText, Info } from "lucide-react";
import { Card, CardHeader, CardTitle, CardContent } from "./ui-components";

export function MaterialContextPanel({ stats }: { stats: { label: string; value: string; note: string }[] }) {
  return (
    <Card className="rounded-[28px] border border-white/5 bg-gradient-to-br from-indigo-900/10 to-slate-900 p-6 shadow-2xl">
      <CardHeader className="pb-4">
        <div className="flex items-center gap-3">
          <Database className="h-5 w-5 text-indigo-400" />
          <CardTitle className="text-lg font-bold text-white tracking-tight">Material Context</CardTitle>
        </div>
      </CardHeader>
      <CardContent>
        <div className="grid grid-cols-2 gap-4">
          {stats.map((item) => (
            <div key={item.label} className="rounded-2xl border border-white/5 bg-white/[0.02] p-4 transition-all hover:bg-white/[0.05]">
              <div className="text-[9px] uppercase tracking-wider text-slate-500 font-bold mb-1">{item.label}</div>
              <div className="text-lg font-mono font-bold text-white">{item.value}</div>
              <div className="text-[9px] text-slate-600 mt-1">{item.note}</div>
            </div>
          ))}
        </div>
      </CardContent>
    </Card>
  );
}
