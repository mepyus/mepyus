import React from "react";
import { ListChecks } from "lucide-react";
import { Card, CardHeader, CardTitle, CardContent, Badge } from "./ui-components";
import { Recommendation, RecommendationPriority } from "./engine-surface.types";

function priorityMeta(priority: RecommendationPriority) {
  return {
    now: { label: "now", className: "border-rose-500/20 bg-rose-500/15 text-rose-300" },
    next: { label: "next", className: "border-sky-500/20 bg-sky-500/15 text-sky-300" },
    later: { label: "later", className: "border-slate-500/20 bg-slate-500/15 text-slate-300" },
  }[priority];
}

export function SupervisorQueuePanel({ 
  recommendations 
}: {
  recommendations: Recommendation[];
}) {
  return (
    <Card className="rounded-[24px] border-white/10 bg-black/20 text-white">
      <CardHeader className="pb-3">
        <div className="flex items-center gap-3">
          <ListChecks className="h-5 w-5 text-slate-300" />
          <CardTitle className="text-lg text-white">Supervisor Queue</CardTitle>
        </div>
      </CardHeader>
      <CardContent className="space-y-3">
        {recommendations.map((item) => {
          const meta = priorityMeta(item.priority);
          return (
            <div key={item.id} className="rounded-xl border border-white/10 bg-white/5 p-4">
              <div className="flex items-center justify-between">
                <div className="text-sm font-medium text-white">{item.title}</div>
                <Badge className={meta.className}>{meta.label}</Badge>
              </div>
              <div className="mt-2 text-xs text-slate-400 leading-5">{item.body}</div>
            </div>
          );
        })}
      </CardContent>
    </Card>
  );
}
