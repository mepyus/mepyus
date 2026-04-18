import React, { useMemo } from "react";
import { motion } from "framer-motion";
import {
  AlertTriangle,
  CheckCircle2,
  Clock,
  Database,
  Eye,
  FileInput,
  GitBranch,
  PauseCircle,
  RefreshCcw,
  ShieldAlert,
  Layers3,
  ArrowRight,
  FolderTree,
  ListTree,
  FileSearch,
  Command,
  HeartPulse,
} from "lucide-react";
import { 
  Card, CardHeader, CardTitle, CardContent, CardDescription,
  Badge,
  Input,
  cx
} from "./ui-components";

// Types & Seeds
import { 
  AssetNode,
  EngineIngestSlot, 
  EnginePipelineSlot, 
  ValidationReturnPacket 
} from "./engine-surface.types";
import { 
  assetTreeSeed, 
  engineEventsSeed, 
  recommendationsSeed, 
  watchpointsSeed, 
  bridgeItemsSeed,
  ingestSlotSeed,
  pipelineSlotSeed,
  validationReturnSlotSeed,
  engineStatusSeed,
  workMemorySeed
} from "./engine-surface.seed";

// Panels
import { AssetInventoryPanel } from "./AssetInventoryPanel";
import { AssetInspectorPanel } from "./AssetInspectorPanel";
import { WatchpointRegistryPanel } from "./WatchpointRegistryPanel";
import { EventConsolePanel } from "./EventConsolePanel";
import { SupervisorQueuePanel } from "./SupervisorQueuePanel";
import { BridgePanel } from "./BridgePanel";
import { SpaceHealthPanel } from "./SpaceHealthPanel.tsx";
import { FilterBarPanel } from "./FilterBarPanel.tsx";

// Hooks
import { useEngineSurfaceMockState } from "./useEngineSurfaceMockState";
import { useEngineSurfaceMockFilters } from "./useEngineSurfaceMockFilters";

// Sub-components
function StatusPill({ status }: { status: string }) {
  const statusTone: Record<string, string> = {
    queued: "border-slate-500/30 bg-slate-500/10 text-slate-200",
    processing: "border-sky-400/40 bg-sky-500/10 text-sky-200",
    done: "border-emerald-400/40 bg-emerald-500/10 text-emerald-200",
    failed: "border-red-400/40 bg-red-500/10 text-red-200",
    hold: "border-amber-400/40 bg-amber-500/10 text-amber-200",
    ready_for_review: "border-violet-400/40 bg-violet-500/10 text-violet-200",
  };
  return (
    <span className={`rounded-full border px-2.5 py-0.5 text-[10px] font-bold uppercase tracking-tighter shadow-sm transition-all ${statusTone[status] || statusTone.queued} ${status === "processing" ? "animate-pulse ring-2 ring-sky-500/20" : ""}`}>
      {status}
    </span>
  );
}

function SlotAttachmentNote({ mock, actual }: { mock: string; actual: string }) {
  return (
    <div className="mt-4 rounded-xl border border-white/5 bg-black/40 p-3 font-mono text-[9px] leading-5 text-slate-500">
      <div className="flex items-center gap-2 truncate"><span className="text-slate-600 font-bold uppercase tracking-widest text-[8px]">Mock:</span> {mock}</div>
      <div className="flex items-center gap-2 truncate"><span className="text-slate-600 font-bold uppercase tracking-widest text-[8px]">Actual:</span> {actual}</div>
    </div>
  );
}

function PipelineConnector() {
  return (
    <div className="flex justify-center py-2">
      <div className="h-8 w-[1px] bg-gradient-to-b from-white/10 via-white/20 to-white/10 relative">
        <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 h-1.5 w-1.5 rounded-full bg-white/20 blur-[1px]" />
      </div>
    </div>
  );
}

function IngestEntryPanel({ ingest }: { ingest: EngineIngestSlot }) {
  return (
    <section className="rounded-[28px] border border-sky-500/20 bg-gradient-to-br from-sky-500/[0.08] to-transparent p-6 shadow-2xl transition-all hover:border-sky-500/30">
      <div className="flex flex-wrap items-start justify-between gap-4">
        <div className="flex items-start gap-4">
          <div className="rounded-2xl bg-sky-500/10 p-3 border border-sky-500/20 shadow-lg shadow-sky-900/20 text-sky-400">
            <FileInput className="h-6 w-6" />
          </div>
          <div>
            <div className="flex items-center gap-2">
              <div className="text-[10px] uppercase tracking-[0.2em] text-sky-400/80 font-bold">Slot 01 / EngineIngestState</div>
              <Badge variant="outline" className="text-[8px] border-sky-500/30 text-sky-500/70 h-4">MOCK ATTACHMENT CANDIDATE</Badge>
            </div>
            <h2 className="mt-1 text-2xl font-bold tracking-tight text-white">외부 자료 입력 상태</h2>
            <p className="mt-1 text-xs text-slate-400 italic">"무슨 자료가 공간 재료로 들어왔는가?"</p>
          </div>
        </div>
        <StatusPill status={ingest.status} />
      </div>
      <div className="mt-6 grid gap-4 lg:grid-cols-4">
        <ConsoleStat label="source_label" value={ingest.sourceLabel} note="외부 자료 이름" icon={FileInput} />
        <ConsoleStat label="source_type" value={ingest.sourceType} note="입력 데이터 종류" icon={Database} />
        <ConsoleStat label="linked_goal_ids" value={String(ingest.linkedGoalIds.length)} note={ingest.linkedGoalIds.join(", ")} icon={GitBranch} />
        <ConsoleStat label="source_path" value="VERIFIED" note={ingest.sourcePath} icon={CheckCircle2} />
      </div>
      <SlotAttachmentNote mock={ingest.mockAttachmentPoint} actual={ingest.actualAttachmentPoint} />
    </section>
  );
}

function PipelineStatusPanel({ pipeline }: { pipeline: EnginePipelineSlot }) {
  return (
    <section className="rounded-[28px] border border-emerald-500/20 bg-gradient-to-br from-emerald-500/[0.05] to-transparent p-6 shadow-2xl transition-all hover:border-emerald-500/30">
      <div className="flex flex-wrap items-start justify-between gap-4">
        <div className="flex items-start gap-4">
          <div className="rounded-2xl bg-emerald-500/10 p-3 border border-emerald-500/20 shadow-lg shadow-emerald-900/20 text-emerald-400">
            <GitBranch className="h-6 w-6" />
          </div>
          <div>
            <div className="flex items-center gap-2">
              <div className="text-[10px] uppercase tracking-[0.2em] text-emerald-400/80 font-bold">Slot 02 / EnginePipelineState</div>
              <Badge variant="outline" className="text-[8px] border-emerald-500/30 text-emerald-500/70 h-4">MOCK ATTACHMENT CANDIDATE</Badge>
            </div>
            <h2 className="mt-1 text-2xl font-bold tracking-tight text-white">엔진 파이프라인 단계</h2>
            <p className="mt-1 text-xs text-slate-400 italic">"그 자료가 현재 어디까지 처리되었는가?"</p>
          </div>
        </div>
        <StatusPill status={pipeline.status} />
      </div>
      <div className="mt-6 grid gap-3 sm:grid-cols-2 lg:grid-cols-4">
        {pipeline.steps.map((step) => {
          const isActive = step.status === "processing";
          const isDone = step.status === "done";
          return (
            <div key={step.stepId} className={`rounded-2xl border transition-all duration-500 p-4 ${
              isActive ? "border-emerald-500/40 bg-emerald-500/10 shadow-lg shadow-emerald-900/10 scale-[1.02]" : "border-white/5 bg-white/[0.02]"
            }`}>
              <div className="flex items-center justify-between gap-2 mb-3">
                <div className={`text-[9px] uppercase tracking-widest font-bold ${isActive ? "text-emerald-400" : "text-slate-600"}`}>{step.stepId}</div>
                <div className={`h-1.5 w-1.5 rounded-full ${isActive ? "bg-emerald-400 animate-ping" : isDone ? "bg-emerald-600" : "bg-slate-800"}`} />
              </div>
              <div className={`text-sm font-bold ${isActive ? "text-white" : "text-slate-400"}`}>{step.name}</div>
              <div className="mt-2 text-[10px] leading-4 text-slate-500">{step.note}</div>
            </div>
          );
        })}
      </div>
      <SlotAttachmentNote mock={pipeline.mockAttachmentPoint} actual={pipeline.actualAttachmentPoint} />
    </section>
  );
}

function ValidationReturnPanel({ packet }: { packet: ValidationReturnPacket }) {
  return (
    <section className="rounded-[28px] border border-violet-500/20 bg-gradient-to-br from-violet-500/[0.08] to-transparent p-6 shadow-2xl transition-all hover:border-violet-500/30">
      <div className="flex flex-wrap items-start justify-between gap-4">
        <div className="flex items-start gap-4">
          <div className="rounded-2xl bg-violet-500/10 p-3 border border-violet-500/20 shadow-lg shadow-violet-900/20 text-violet-400">
            <RefreshCcw className="h-6 w-6" />
          </div>
          <div>
            <div className="flex items-center gap-2">
              <div className="text-[10px] uppercase tracking-[0.2em] text-violet-400/80 font-bold">Slot 03 / ValidationReturnPacket</div>
              <Badge variant="outline" className="text-[8px] border-violet-500/30 text-violet-500/70 h-4">OPERATING VIEW CANDIDATE</Badge>
            </div>
            <h2 className="mt-1 text-2xl font-bold tracking-tight text-white">검증 환류 및 피드백</h2>
            <p className="mt-1 text-xs text-slate-400 italic">"검증 뒤 다시 공간에 넣을 return / trace-memory 재료는 무엇인가?"</p>
          </div>
        </div>
        <StatusPill status={packet.status} />
      </div>
      <div className="mt-6 grid gap-4 lg:grid-cols-3">
        <div className="rounded-2xl border border-emerald-500/20 bg-emerald-500/[0.03] p-5 shadow-inner">
          <div className="flex items-center gap-2 text-[10px] font-bold uppercase tracking-widest text-emerald-400 mb-4 italic">
            <CheckCircle2 className="h-3 w-3" /> accepted_refs
          </div>
          <div className="space-y-2">
            {packet.acceptedRefs.map((ref) => (
              <div key={ref} className="rounded-xl bg-black/40 border border-white/5 p-3 font-mono text-[10px] text-slate-300 transition-colors hover:bg-black/60">
                {ref}
              </div>
            ))}
          </div>
        </div>
        <div className="rounded-2xl border border-amber-500/20 bg-amber-500/[0.03] p-5 shadow-inner">
          <div className="flex items-center gap-2 text-[10px] font-bold uppercase tracking-widest text-amber-400 mb-4 italic">
            <PauseCircle className="h-3 w-3" /> hold_refs
          </div>
          <div className="space-y-2">
            {packet.holdRefs.map((ref) => (
              <div key={ref} className="rounded-xl bg-black/40 border border-white/5 p-3 font-mono text-[10px] text-slate-300 transition-colors hover:bg-black/60">
                {ref}
              </div>
            ))}
          </div>
        </div>
        <div className="rounded-2xl border border-white/5 bg-white/[0.03] p-5 shadow-inner">
          <div className="flex items-center gap-2 text-[10px] font-bold uppercase tracking-widest text-slate-400 mb-4 italic">
            <ShieldAlert className="h-3 w-3" /> reasoning_notes
          </div>
          <div className="space-y-2">
            {packet.reasoningNotes.map((note) => (
              <div key={note} className="rounded-xl bg-black/40 border border-white/5 p-3 text-[11px] leading-5 text-slate-400 transition-colors hover:bg-black/60">
                {note}
              </div>
            ))}
          </div>
        </div>
      </div>
      <div className="mt-5 flex items-center justify-between rounded-2xl border border-white/5 bg-black/20 p-4">
        <div className="flex items-center gap-3">
          <div className="text-[10px] uppercase tracking-[0.2em] text-slate-500 font-bold">next_reingest_requested</div>
          <div className={`px-3 py-1 rounded-lg text-xs font-bold ${packet.nextReingestRequested ? "bg-emerald-500/20 text-emerald-400 border border-emerald-500/30" : "bg-slate-800 text-slate-500"}`}>
            {packet.nextReingestRequested ? "YES / RE-INGEST QUEUED" : "NO / COMPLETED"}
          </div>
        </div>
        <div className="text-[10px] font-mono text-slate-600 font-bold">Packet ID: {packet.packetId}</div>
      </div>
      <div className="mt-4 grid gap-2 sm:grid-cols-2">
        <div className="rounded-xl border border-white/5 bg-black/20 px-3 py-2 text-[10px] uppercase tracking-widest text-slate-500">
          report return != product completion
        </div>
        <div className="rounded-xl border border-white/5 bg-black/20 px-3 py-2 text-[10px] uppercase tracking-widest text-slate-500">
          return artifact != chat-only note
        </div>
      </div>
      <SlotAttachmentNote mock={packet.mockAttachmentPoint} actual={packet.actualAttachmentPoint} />
    </section>
  );
}

function WorkMemoryRecordPanel({ memory }: { memory: any }) {
  return (
    <Card className="rounded-[24px] border-white/10 bg-black/20 text-white">
      <CardHeader className="pb-3 border-b border-white/5">
        <div className="flex items-center gap-3">
          <Layers3 className="h-5 w-5 text-slate-300" />
          <div>
            <CardTitle className="text-lg">Work Memory Record</CardTitle>
            <div className="mt-1 text-[9px] uppercase tracking-widest text-slate-600">return includes trace-memory</div>
          </div>
        </div>
      </CardHeader>
      <CardContent className="pt-6 space-y-4">
        <div className="space-y-2">
          <div className="text-[10px] uppercase tracking-widest text-emerald-500 font-black">이번 턴의 판단</div>
          <div className="rounded-xl bg-white/[0.03] border border-white/5 p-4 text-xs text-slate-300 leading-6">
            {memory?.decision || "판단 기록 없음"}
          </div>
        </div>
        <div className="space-y-2">
          <div className="text-[10px] uppercase tracking-widest text-amber-500 font-black">Hold 이유</div>
          <div className="rounded-xl bg-white/[0.03] border border-white/5 p-4 text-xs text-slate-400 italic">
            {memory?.holdReason || "보류 사유 없음"}
          </div>
        </div>
        <div className="pt-2">
          <div className="text-[10px] uppercase tracking-widest text-sky-500 font-black mb-2">다음 작업 방향</div>
          <div className="flex items-center gap-2 text-xs text-slate-200 bg-sky-500/5 p-3 rounded-xl border border-sky-500/10">
            <ArrowRight className="h-3.5 w-3.5 text-sky-400" /> {memory?.nextDirection || "방향 설정 대기 중"}
          </div>
        </div>
      </CardContent>
    </Card>
  );
}

function ConsoleStat({ label, value, note, icon: Icon }: any) {
  return (
    <div className="rounded-2xl border border-white/10 bg-white/[0.03] p-4">
      <div className="flex items-center justify-between gap-3">
        <div className="text-[11px] uppercase tracking-[0.18em] text-slate-500">{label}</div>
        <Icon className="h-4 w-4 text-slate-400" />
      </div>
      <div className="mt-3 text-2xl font-semibold tracking-tight text-white">{value}</div>
      <div className="mt-1 text-sm leading-6 text-slate-400">{note}</div>
    </div>
  );
}

// Flat asset list for state management
function flattenAssets(nodes: AssetNode[]): AssetNode[] {
  return nodes.flatMap((node) => [node, ...(node.children ? flattenAssets(node.children) : [])]);
}

export default function VectorFLEngineSurfaceMock() {
  const allAssets = useMemo(() => flattenAssets(assetTreeSeed), []);
  const { selectedAssetId, setSelectedAssetId, selectedAsset, selectedEvents, stats } = useEngineSurfaceMockState(allAssets, engineEventsSeed);
  const { search, setSearch, filteredTree } = useEngineSurfaceMockFilters(assetTreeSeed);
  const highPriorityRecommendations = recommendationsSeed.filter(r => r.priority === "now");

  return (
    <div className="text-white">
      <div className="space-y-10">
        <motion.div initial={{ opacity: 1, y: 0 }} animate={{ opacity: 1, y: 0 }} className="space-y-10">
          
          <section className="px-2">
            <div className="flex flex-wrap items-center justify-between gap-4">
              <div>
                <div className="flex items-center gap-2 mb-3">
                  <Badge className="rounded-full bg-emerald-500 text-black hover:bg-emerald-400 font-black px-3">ENGINE / CONTROL ROOM</Badge>
                  <Badge variant="outline" className="rounded-full border-white/10 text-slate-500 text-[10px] uppercase tracking-widest">Mock view draft</Badge>
                </div>
                <h1 className="text-3xl font-bold tracking-tight text-white">공간 엔진 컨트롤면</h1>
                <p className="mt-2 text-sm text-slate-400 italic">"ingest / process / validate / trace-memory / return 흐름을 읽는 엔진면 mock입니다."</p>
                <p className="mt-2 text-[10px] font-mono text-slate-600">latest completed != current truth without freshness gate. This mock is a view draft, not runtime truth.</p>
              </div>
              <div className="grid grid-cols-2 gap-4">
                <div className="rounded-2xl border border-white/5 bg-white/[0.02] p-4 text-center min-w-[120px]">
                  <div className="text-[10px] text-slate-500 uppercase font-bold mb-1">Active Slot</div>
                  <div className="text-lg font-mono font-bold text-emerald-400">{engineStatusSeed.activeSlotCount}</div>
                </div>
                <div className="rounded-2xl border border-white/5 bg-white/[0.02] p-4 text-center min-w-[120px]">
                  <div className="text-[10px] text-slate-500 uppercase font-bold mb-1">System Load</div>
                  <div className="text-lg font-mono font-bold text-sky-400">{engineStatusSeed.systemLoad}</div>
                </div>
              </div>
            </div>
          </section>

          <section className="space-y-0">
            <div className="flex items-center gap-3 px-2 mb-6">
              <span className="text-[10px] font-black uppercase tracking-[0.4em] text-emerald-500/70 italic">Primary Control Pipeline</span>
              <div className="h-[1px] flex-1 bg-gradient-to-r from-emerald-500/20 to-transparent" />
            </div>
            <IngestEntryPanel ingest={ingestSlotSeed} />
            <PipelineConnector />
            <PipelineStatusPanel pipeline={pipelineSlotSeed} />
            <PipelineConnector />
            <ValidationReturnPanel packet={validationReturnSlotSeed} />
          </section>

          <SpaceHealthPanel syncRate={engineStatusSeed.syncRate} maturationLevel={engineStatusSeed.maturationLevel} activeViolations={stats.warningEvents} />

          <section className="space-y-6 pt-4">
            <div className="flex items-center justify-between border-b border-white/5 pb-4 px-2">
              <div>
                <div className="text-[10px] uppercase tracking-[0.2em] text-slate-500 font-bold">Secondary Monitoring Layer</div>
                <h2 className="mt-1 text-xl font-bold text-slate-200">Asset / Watch / Trace Audit</h2>
              </div>
              <Badge variant="outline" className="rounded-lg border-white/5 text-slate-600 text-[10px]">Passive Observation</Badge>
            </div>
            <FilterBarPanel search={search} onSearchChange={setSearch} kindFilter={"all"} onKindChange={() => {}} healthFilter={"all"} onHealthChange={() => {}} sortBy={"default"} onSortChange={() => {}} />
            <div className="grid gap-6 xl:grid-cols-[280px_1fr_320px] 2xl:grid-cols-[320px_1fr_360px]">
              <AssetInventoryPanel assets={filteredTree} selectedId={selectedAssetId} onSelect={setSelectedAssetId} search={search} onSearchChange={setSearch} />
              <div className="space-y-6">
                <AssetInspectorPanel asset={selectedAsset} events={selectedEvents} />
                <WatchpointRegistryPanel watchpoints={watchpointsSeed} />
              </div>
              <div className="space-y-6">
                <WorkMemoryRecordPanel memory={workMemorySeed} />
                <EventConsolePanel events={engineEventsSeed} />
                <SupervisorQueuePanel recommendations={highPriorityRecommendations} />
                <BridgePanel items={bridgeItemsSeed} />
              </div>
            </div>
          </section>
          <div className="px-2 text-[10px] font-mono italic text-slate-600">
            Runtime truth requires latest manifests and freshness gate. Mock evidence must not be treated as current truth.
          </div>
        </motion.div>
      </div>
    </div>
  );
}
