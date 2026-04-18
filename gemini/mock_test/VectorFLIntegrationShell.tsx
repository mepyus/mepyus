import React, { useState } from "react";
import { motion } from "framer-motion";
import { Command, LayoutDashboard, Blocks, BrainCircuit, ArrowRight } from "lucide-react";
import { 
  Tabs, TabsContent, 
  Card, CardHeader, CardTitle, CardDescription, CardContent 
} from "./ui-components";

// Surfaces
import VectorFLEngineSurfaceMock from "./vectorfl_engine_surface_mock";
import { CommandHeaderPanel } from "./CommandHeaderPanel.tsx";
import { TeamRoutingPanel } from "./TeamRoutingPanel.tsx";
import { RoleConfigurationPanel } from "./RoleConfigurationPanel.tsx";
import { ExecutionRoutePanel } from "./ExecutionRoutePanel.tsx";
import { OperationLogPanel } from "./OperationLogPanel.tsx";
import { FlowSummaryPanel } from "./FlowSummaryPanel.tsx";
import { CliHostControlPanel } from "./CliHostControlPanel.tsx";

// Seeds & Data
import { initialTeamsSeed, auditLogsSeed, boardStatsSeed, userSurfaceMetaSeed } from "./user-surface.seed";
import { useUserSurfaceState } from "./useUserSurfaceState";
import vectorMeta from "./vectorfl_meta.json";
import jangLines from "./jang_lines.json";

export default function VectorFLIntegrationShell() {
  const [active, setActive] = useState<"user" | "vectorfl" | "engine">("vectorfl");
  const [goal, setGoal] = useState(userSurfaceMetaSeed.initialGoal);
  const { teams, selectedTeam, selectedTeamId, setSelectedTeamId } = useUserSurfaceState(initialTeamsSeed);
  const [selectedLineId, setSelectedLineId] = useState<string>(jangLines[0]?.id || "");
  const selectedLine = jangLines.find((l: any) => l.id === selectedLineId) || jangLines[0];

  return (
    <div className="min-h-screen bg-[#050507] text-slate-100 selection:bg-indigo-500/30">
      <div className="grid min-h-screen lg:grid-cols-[240px_1fr]">
        <aside className="border-r border-white/5 bg-[#09090b] p-6">
          <div className="flex items-center gap-3 px-2 mb-8"><Command className="h-5 w-5 text-slate-400"/><span className="text-sm font-bold tracking-tighter">VECTORFL Shell</span></div>
          <nav className="space-y-2">
            {[ {id: "user", label: "User Surface"}, {id: "vectorfl", label: "VectorFL Surface"}, {id: "engine", label: "Engine Surface"} ].map(tab => (
              <button key={tab.id} onClick={() => setActive(tab.id as any)} className={`w-full p-3 rounded-xl text-sm transition ${active === tab.id ? "bg-white/10 text-white" : "text-slate-500 hover:text-slate-300"}`}>{tab.label}</button>
            ))}
          </nav>
        </aside>

        <main className="p-8 overflow-y-auto">
          {/* Orientation Band */}
          <div className="mb-8 flex items-center justify-center gap-2 py-3 px-6 rounded-2xl bg-white/[0.03] border border-white/5 text-[9px] uppercase tracking-[0.2em] text-slate-500 font-bold">
            <span>Goal/Scope/Material</span> <ArrowRight className="h-3 w-3" /> 
            <span>Line Reading</span> <ArrowRight className="h-3 w-3" /> 
            <span>Engine Processing</span> <ArrowRight className="h-3 w-3" /> 
            <span>Return Artifact</span>
          </div>

          <motion.div key={active} initial={{ opacity: 0, y: 10 }} animate={{ opacity: 1, y: 0 }}>
            <Tabs value={active}>
              {/* User Surface */}
              <TabsContent value="user" className="space-y-8">
                <CommandHeaderPanel goal={goal} onGoalChange={setGoal} stats={boardStatsSeed} infoBoxes={userSurfaceMetaSeed.infoBoxes} />
                <section className="pt-8 border-t border-white/5 space-y-4">
                  <div className="px-2 text-[10px] font-black uppercase tracking-[0.3em] text-slate-500 italic">Operating extension / not body skeleton</div>
                  <div className="grid gap-6 xl:grid-cols-[1fr_1fr]">
                    <TeamRoutingPanel teams={teams} selectedId={selectedTeamId} onSelect={setSelectedTeamId} onAdd={() => {}} onRemove={() => {}} />
                    <RoleConfigurationPanel team={selectedTeam} onEditTeam={() => {}} onAddRole={() => {}} onEditRole={() => {}} />
                  </div>
                  <ExecutionRoutePanel teams={teams} />
                  <OperationLogPanel logs={auditLogsSeed} />
                </section>
                <div className="text-[10px] text-slate-600 font-mono italic">This mock is a view draft, not runtime truth. Runtime truth requires latest manifests and freshness gate.</div>
              </TabsContent>

              {/* VectorFL Surface */}
              <TabsContent value="vectorfl" className="space-y-8">
                <FlowSummaryPanel stats={vectorMeta.stats} summary={vectorMeta.summary} />
                <div className="grid gap-6 xl:grid-cols-[300px_1fr]">
                  <Card className="rounded-[28px] border-amber-500/10 bg-[#0d0d12] h-[600px] overflow-y-auto">
                    <CardHeader><CardTitle className="text-amber-400">Line Atlas</CardTitle></CardHeader>
                    <CardContent className="space-y-3">
                        {jangLines.map((line: any) => (
                           <button key={line.id} onClick={() => setSelectedLineId(line.id)} className={`w-full p-4 rounded-xl border text-left transition ${selectedLine?.id === line.id ? "border-amber-500 bg-amber-500/10" : "border-white/5 bg-white/[0.02]"}`}>
                             <div className="font-bold text-slate-300">{line.name}</div>
                             <div className="text-[10px] text-slate-500 mt-2 italic">"{line.purpose}"</div>
                           </button>
                        ))}
                    </CardContent>
                  </Card>
                  <div className="space-y-6">
                    <CliHostControlPanel />
                    <Card className="rounded-[28px] border-amber-500/10 bg-[#0d0d12] p-6 shadow-2xl">
                        <CardTitle className="text-amber-400 text-sm mb-4">Inspection: {selectedLine?.name}</CardTitle>
                        {selectedLine ? (
                            <div className="space-y-4 text-xs text-slate-300">
                                <p>Health: <span className="text-slate-500 italic">(Mock readability label)</span> {selectedLine.health}</p>
                                <div className="pt-4 border-t border-white/5"><div className="font-bold mb-2">ConnectedTo</div>{selectedLine.connectedTo.map((c: string) => <div key={c} className="text-slate-500">● {c}</div>)}</div>
                            </div>
                        ) : <div className="text-slate-600 italic">라인을 선택하세요</div>}
                    </Card>
                  </div>
                </div>
                <div className="text-[10px] text-slate-600 font-mono italic">This mock is a view draft, not runtime truth.</div>
              </TabsContent>

              {/* Engine Surface */}
              <TabsContent value="engine">
                <VectorFLEngineSurfaceMock />
              </TabsContent>
            </Tabs>
          </motion.div>
        </main>
      </div>
    </div>
  );
}
