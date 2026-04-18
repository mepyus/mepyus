import React from "react";
import { Link2, Clock3, Sparkles, RefreshCcw, AlertTriangle, ShieldAlert, ArrowRight, FileCode, Activity } from "lucide-react";
import { Card, CardHeader, CardTitle, CardDescription, CardContent, Badge, Tabs, TabsList, TabsTrigger, TabsContent } from "./ui-components";
import { AssetNode, EngineEvent, AssetHealth, EngineEventType } from "./engine-surface.types";

function healthMeta(health: AssetHealth) {
  return {
    healthy: { label: "healthy", className: "border-emerald-500/20 bg-emerald-500/15 text-emerald-300" },
    watch: { label: "watch", className: "border-amber-500/20 bg-amber-500/15 text-amber-300" },
    stale: { label: "stale", className: "border-slate-500/20 bg-slate-500/15 text-slate-300" },
    broken: { label: "broken", className: "border-rose-500/20 bg-rose-500/15 text-rose-300" },
  }[health];
}

function deltaMeta(status?: string) {
  switch (status) {
    case "synced": return { label: "SYNCED", color: "text-emerald-400", bg: "bg-emerald-500/10" };
    case "modified": return { label: "MODIFIED", color: "text-amber-400", bg: "bg-amber-500/10" };
    case "violation": return { label: "VIOLATION", color: "text-rose-400", bg: "bg-rose-500/10" };
    default: return { label: "UNKNOWN", color: "text-slate-400", bg: "bg-slate-500/10" };
  }
}

function eventMeta(type: EngineEventType) {
  return {
    created: { label: "created", icon: Sparkles, className: "bg-emerald-500/15 text-emerald-300" },
    updated: { label: "updated", icon: RefreshCcw, className: "bg-sky-500/15 text-sky-300" },
    warning: { label: "warning", icon: AlertTriangle, className: "bg-amber-500/15 text-amber-300" },
    hold: { label: "hold", icon: ShieldAlert, className: "bg-violet-500/15 text-violet-300" },
    skipped: { label: "skipped", icon: ArrowRight, className: "bg-slate-500/15 text-slate-300" },
  }[type];
}

export function AssetInspectorPanel({ 
  asset, 
  events 
}: {
  asset: AssetNode;
  events: EngineEvent[];
}) {
  const dMeta = deltaMeta(asset.deltaStatus);

  return (
    <Card className="rounded-[24px] border-white/10 bg-black/20 text-white">
      <CardHeader>
        <div className="flex items-center justify-between">
          <div className="flex flex-col gap-1">
            <CardTitle className="text-lg">{asset.title}</CardTitle>
            <div className={`text-[10px] font-bold px-2 py-0.5 rounded ${dMeta.bg} ${dMeta.color} self-start`}>
              BASELINE: {dMeta.label}
            </div>
          </div>
          <Badge className={healthMeta(asset.health).className}>{healthMeta(asset.health).label}</Badge>
        </div>
        <CardDescription className="font-mono text-xs mt-2">{asset.path}</CardDescription>
      </CardHeader>
      <CardContent className="space-y-4">
        {/* v2: Lineage Section */}
        <div className="rounded-xl border border-white/5 bg-white/[0.02] p-4">
          <div className="flex items-center justify-between mb-3">
            <div className="text-[11px] uppercase tracking-widest text-slate-500 flex items-center gap-2">
              <Activity className="h-3 w-3" /> System Lineage
            </div>
            {asset.attentionScore && (
              <div className="text-[10px] text-orange-400 font-mono">ATTENTION: {asset.attentionScore}%</div>
            )}
          </div>
          <div className="flex items-center gap-3 p-3 rounded-lg bg-black/40 border border-white/5">
            <FileCode className="h-5 w-5 text-sky-400" />
            <div className="flex-1 overflow-hidden">
              <div className="text-[10px] text-slate-500 uppercase">Managed By Script</div>
              <div className="text-xs font-mono text-slate-300 truncate">
                {asset.scriptLink || "No automated manager linked"}
              </div>
            </div>
            {asset.scriptLink && (
              <Badge variant="outline" className="text-[9px] border-sky-500/30 text-sky-400">ACTIVE</Badge>
            )}
          </div>
        </div>

        <div className="text-sm leading-7 text-slate-300 px-1">{asset.summary}</div>
        
        <div className="grid grid-cols-2 gap-3">
          <div className="rounded-xl bg-white/5 p-3">
            <div className="text-[10px] uppercase text-slate-500">Role</div>
            <div className="mt-1 text-xs">{asset.role}</div>
          </div>
          <div className="rounded-xl bg-white/5 p-3">
            <div className="text-[10px] uppercase text-slate-500">Updated</div>
            <div className="mt-1 text-xs">{asset.updatedAt}</div>
          </div>
        </div>

        <Tabs defaultValue="warnings" className="w-full">
          <TabsList className="grid h-auto w-full grid-cols-3 rounded-2xl bg-white/[0.04] p-1">
            <TabsTrigger value="warnings" className="rounded-xl py-2">warnings</TabsTrigger>
            <TabsTrigger value="connections" className="rounded-xl py-2">links</TabsTrigger>
            <TabsTrigger value="events" className="rounded-xl py-2">trace</TabsTrigger>
          </TabsList>

          <TabsContent value="warnings" className="mt-4 space-y-2">
            {asset.warnings.length > 0 ? (
              asset.warnings.map((w) => (
                <div key={w} className="rounded-xl border border-amber-500/20 bg-amber-500/10 p-3 text-xs text-amber-100">{w}</div>
              ))
            ) : (
              <div className="text-xs text-slate-500 p-2 italic">직접 연결된 경고 없음</div>
            )}
          </TabsContent>

          <TabsContent value="connections" className="mt-4 space-y-2">
            {asset.connectedTo.map((link) => (
              <div key={link} className="flex items-center gap-2 rounded-xl border border-white/10 bg-white/5 p-3 text-xs text-slate-300">
                <Link2 className="h-3 w-3 text-slate-500" /> {link}
              </div>
            ))}
          </TabsContent>

          <TabsContent value="events" className="mt-4 space-y-2">
            {events.length > 0 ? (
              events.map((e) => {
                const meta = eventMeta(e.type);
                return (
                  <div key={e.id} className="rounded-xl border border-white/10 bg-white/5 p-3 text-xs">
                    <div className="flex justify-between text-[10px] text-slate-500 mb-1">
                      <span>{meta.label}</span>
                      <span>{e.time}</span>
                    </div>
                    <div className="font-medium text-slate-200">{e.title}</div>
                  </div>
                );
              })
            ) : (
              <div className="text-xs text-slate-500 p-2 italic">기록된 이벤트 없음</div>
            )}
          </TabsContent>
        </Tabs>
      </CardContent>
    </Card>
  );
}
