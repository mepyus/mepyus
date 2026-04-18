import React, { useMemo, useState } from "react";
import { motion } from "framer-motion";
import { Blocks, Command, LayoutDashboard, BrainCircuit, ListTree, FileSearch, Terminal, Play } from "lucide-react";
import { Card, CardHeader, CardTitle, CardDescription, CardContent, Input, Button, Tabs, TabsContent } from "./ui-components";

import VectorFLEngineSurfaceMock from "./vectorfl_engine_surface_mock";
import { initialTeamsSeed, auditLogsSeed, boardStatsSeed, userSurfaceMetaSeed } from "./user-surface.seed";
import { useUserSurfaceState } from "./useUserSurfaceState";
import { CommandHeaderPanel } from "./CommandHeaderPanel.tsx";
import { TeamRoutingPanel } from "./TeamRoutingPanel.tsx";
import { RoleConfigurationPanel } from "./RoleConfigurationPanel.tsx";
import { ExecutionRoutePanel } from "./ExecutionRoutePanel.tsx";
import { OperationLogPanel } from "./OperationLogPanel.tsx";
import { FlowSummaryPanel } from "./FlowSummaryPanel.tsx";
import { OperationConsolePanel } from "./OperationConsolePanel.tsx";

import jangLines from "./jang_lines.json";
import vectorMeta from "./vectorfl_meta.json";

export default function VectorFLSurfacesMock() {
  const [activeSurface, setActiveSurface] = useState<"user" | "vectorfl" | "engine">("user");
  const [goal, setGoal] = useState(userSurfaceMetaSeed.initialGoal);
  const { teams, selectedTeam, selectedTeamId, setSelectedTeamId } = useUserSurfaceState(initialTeamsSeed);
  const [lines] = useState<any[]>(jangLines as any);
  const [selectedLineId, setSelectedLineId] = useState<string>(lines[0]?.id || "");
  const selectedLine = useMemo(() => lines.find((l: any) => l.id === selectedLineId) || lines[0], [selectedLineId]);

  return (
    <div className="min-h-screen bg-[#050507] text-slate-100">
      <div className="grid min-h-screen lg:grid-cols-[240px_1fr]">
        <aside className="border-r border-white/5 bg-[#09090b] p-6">
          <div className="flex items-center gap-3 px-2 mb-8"><Command className="h-5 w-5 text-slate-400"/><span className="text-sm font-bold">VECTORFL Shell</span></div>
          <nav className="space-y-2">
            {[ {id: "user", label: "User Surface"}, {id: "vectorfl", label: "VectorFL Surface"}, {id: "engine", label: "Engine Surface"} ].map(tab => (
              <button key={tab.id} onClick={() => setActiveSurface(tab.id as any)} className={`w-full p-3 rounded-xl text-sm ${activeSurface === tab.id ? "bg-white/10" : "text-slate-500"}`}>{tab.label}</button>
            ))}
          </nav>
        </aside>
        <main className="p-8">
            <Tabs value={activeSurface}>
              <TabsContent value="user" className="space-y-8">
                <CommandHeaderPanel goal={goal} onGoalChange={setGoal} stats={boardStatsSeed} infoBoxes={userSurfaceMetaSeed.infoBoxes} />
	                <div className="grid gap-6 xl:grid-cols-[1fr_1fr]">
                    <div className="xl:col-span-2 text-[10px] font-black uppercase tracking-[0.3em] text-slate-500 italic">Operating extension, not body skeleton</div>
	                  <TeamRoutingPanel teams={teams} selectedId={selectedTeamId} onSelect={setSelectedTeamId} onAdd={() => {}} onRemove={() => {}} />
	                  <RoleConfigurationPanel team={selectedTeam} onEditTeam={() => {}} onAddRole={() => {}} onEditRole={() => {}} />
                </div>
                <ExecutionRoutePanel teams={teams} />
                <OperationLogPanel logs={auditLogsSeed} />
              </TabsContent>
              <TabsContent value="vectorfl" className="space-y-8">
                <FlowSummaryPanel stats={vectorMeta.stats} summary={vectorMeta.summary} />
                <div className="grid gap-6 xl:grid-cols-[1fr_0.8fr]">
                  <Card className="rounded-[28px] border-amber-500/10 bg-[#0d0d12]">
                     <CardHeader><CardTitle className="text-amber-400">Line Atlas</CardTitle></CardHeader>
                     <CardContent className="grid gap-4 lg:grid-cols-2">
                        {lines.map((line: any) => (
                           <button key={line.id} onClick={() => setSelectedLineId(line.id)} className={`p-4 rounded-xl border ${selectedLine?.id === line.id ? "border-amber-500 bg-amber-500/10" : "border-white/5 bg-white/[0.02]"}`}>
                             <div className="font-bold text-slate-300">{line.name}</div>
                             <div className="text-xs text-slate-500 mt-2">"{line.purpose}"</div>
                           </button>
                        ))}
                     </CardContent>
                  </Card>
                  <div className="space-y-6">
                    <Card className="rounded-[28px] border-amber-500/10 bg-[#0d0d12] p-6">
                      <CardTitle className="text-amber-400 text-sm mb-4">Inspection: {selectedLine?.name}</CardTitle>
	                      {selectedLine ? (
	                         <div className="space-y-4 text-xs text-slate-300">
	                           <p>Health: <span className="text-slate-500 italic">(Mock readability label)</span> {selectedLine.health}</p>
                             <p className="text-slate-500 italic">Purpose: {selectedLine.purpose}</p>
                             <div className="pt-4 border-t border-white/5"><div className="font-bold mb-2">ConnectedTo</div>{selectedLine.connectedTo.map((c: string) => <div key={c} className="text-slate-500">● {c}</div>)}</div>
                             <div className="pt-4 border-t border-white/5"><div className="font-bold mb-2">WeakPoints</div>{selectedLine.weakPoints.map((w: string) => <div key={w} className="text-rose-500/70">! {w}</div>)}</div>
	                         </div>
                      ) : <div className="text-slate-600 italic">라인을 선택하세요</div>}
                    </Card>
                    <div className="rounded-[28px] border-amber-500/20 bg-[#0d0d12] p-6 shadow-2xl relative">
                      <div className="flex items-center gap-2 mb-2">
                        <span className="text-[9px] font-black uppercase tracking-widest text-slate-500">Optional Tool Layer</span>
                        <span className="text-[9px] text-slate-600 italic">"Line shaping 이후 사용"</span>
                      </div>
                      <OperationConsolePanel onCommand={(cmd) => console.log("OpHub:", cmd)} />
                    </div>
                  </div>
                </div>
              </TabsContent>
              <TabsContent value="engine">
                <VectorFLEngineSurfaceMock />
              </TabsContent>
            </Tabs>
        </main>
      </div>
    </div>
  );
}
