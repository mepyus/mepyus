import React from "react";
import { Clock3, Sparkles, RefreshCcw, AlertTriangle, ShieldAlert, ArrowRight, Search } from "lucide-react";
import { Card, CardHeader, CardTitle, CardDescription, CardContent, Button } from "./ui-components";
import { EngineEvent, EngineEventType } from "./engine-surface.types";

function eventMeta(type: EngineEventType) {
  return {
    created: { label: "created", icon: Sparkles, className: "bg-emerald-500/15 text-emerald-300" },
    updated: { label: "updated", icon: RefreshCcw, className: "bg-sky-500/15 text-sky-300" },
    warning: { label: "warning", icon: AlertTriangle, className: "bg-amber-500/15 text-amber-300" },
    hold: { label: "hold", icon: ShieldAlert, className: "bg-violet-500/15 text-violet-300" },
    skipped: { label: "skipped", icon: ArrowRight, className: "bg-slate-500/15 text-slate-300" },
  }[type];
}

export function EventConsolePanel({ 
  events 
}: {
  events: EngineEvent[];
}) {
  return (
    <Card className="rounded-[24px] border-white/10 bg-black/20 text-white overflow-hidden">
      <CardHeader>
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-3">
            <Clock3 className="h-5 w-5 text-slate-300" />
            <CardTitle className="text-lg">Event Console</CardTitle>
          </div>
          <div className="flex gap-2">
            <Button variant="outline" size="sm" className="h-8 rounded-xl border-white/5 bg-white/5 text-[10px] uppercase tracking-wider">
              <Search className="mr-2 h-3 w-3" /> search
            </Button>
          </div>
        </div>
      </CardHeader>
      <CardContent className="max-h-[800px] overflow-auto space-y-3">
        {events.map((event) => {
          const meta = eventMeta(event.type);
          const Icon = meta.icon;
          return (
            <div key={event.id} className="rounded-xl border border-white/10 bg-white/5 p-4 transition hover:bg-white/[0.07]">
              <div className="flex justify-between items-start mb-2">
                <div className="flex items-center gap-2">
                  <div className={`p-1.5 rounded-lg ${meta.className}`}>
                    <Icon className="h-3.5 w-3.5" />
                  </div>
                  <div>
                    <div className="text-xs font-semibold text-slate-200">{event.title}</div>
                    <div className="text-[10px] text-slate-500 uppercase tracking-tighter">{meta.label}</div>
                  </div>
                </div>
                <div className="text-[10px] text-slate-500 font-mono">{event.time}</div>
              </div>
              <div className="text-xs text-slate-400 leading-5">{event.detail}</div>
            </div>
          );
        })}
      </CardContent>
    </Card>
  );
}
