import React from "react";
import { FolderTree, Search, Database, BookOpen, FileCode2, Terminal, FileJson, Blocks, Flame, AlertCircle } from "lucide-react";
import { Card, CardHeader, CardTitle, CardContent, Input } from "./ui-components";
import { AssetNode, AssetKind, AssetHealth } from "./engine-surface.types";

function healthMeta(health: AssetHealth) {
  return {
    healthy: { dot: "bg-emerald-400" },
    watch: { dot: "bg-amber-400" },
    stale: { dot: "bg-slate-400" },
    broken: { dot: "bg-rose-400" },
  }[health];
}

function kindMeta(kind: AssetKind) {
  return {
    inputs: { label: "inputs", icon: Database },
    docs: { label: "docs", icon: BookOpen },
    scripts: { label: "scripts", icon: FileCode2 },
    runtime: { label: "runtime", icon: Terminal },
    manifests: { label: "manifests", icon: FileJson },
    views: { label: "views", icon: Blocks },
  }[kind];
}

function AssetListItem({ asset, selected, onSelect, indent = false }: {
  asset: AssetNode;
  selected: boolean;
  onSelect: (id: string) => void;
  indent?: boolean;
}) {
  const meta = healthMeta(asset.health);
  const Icon = kindMeta(asset.kind).icon;
  
  // v2: 어텐션 기반 히트맵 정교화
  const attention = asset.attentionScore || 0;
  const isHot = attention > 70;
  const isWarm = attention > 30 && attention <= 70;
  const isViolation = asset.deltaStatus === "violation";

  return (
    <button
      onClick={() => onSelect(asset.id)}
      className={`group w-full rounded-2xl border p-3 text-left transition-all duration-300 relative overflow-hidden ${
        selected 
          ? "border-blue-500/40 bg-blue-500/10 shadow-[0_0_20px_rgba(59,130,246,0.1)]" 
          : isHot 
            ? "border-orange-500/20 bg-orange-500/[0.03]" 
            : "border-transparent hover:bg-white/[0.03]"
      }`}
    >
      {/* Hot Heatmap Glow */}
      {isHot && !selected && (
        <div className="absolute inset-0 bg-gradient-to-r from-orange-500/[0.05] to-transparent pointer-events-none animate-pulse" />
      )}
      
      <div className={`flex items-center gap-3 relative z-10 ${indent ? "ml-6" : ""}`}>
        <div className={`h-1.5 w-1.5 rounded-full shadow-sm ${meta.dot} ${isViolation ? "animate-ping" : ""}`} />
        <Icon className={`h-4 w-4 transition-colors ${selected ? "text-blue-400" : isHot ? "text-orange-400" : "text-slate-500"}`} />
        
        <div className="flex-1 overflow-hidden">
          <div className="flex items-center gap-2">
            <div className={`truncate text-sm font-semibold tracking-tight ${selected ? "text-white" : isHot ? "text-orange-100" : "text-slate-300"}`}>
              {asset.title}
            </div>
            {isHot && <Flame className="h-3 w-3 text-orange-500 fill-orange-500" />}
            {isViolation && <div className="px-1.5 py-0.5 rounded-md bg-rose-500 text-[8px] font-black text-white uppercase tracking-tighter">Violation</div>}
          </div>
          <div className="flex items-center gap-2 mt-0.5">
            <div className="truncate text-[10px] text-slate-500 font-mono opacity-70">{asset.path}</div>
            {attention > 0 && (
              <div className={`text-[9px] font-bold ${isHot ? "text-orange-500/70" : "text-slate-600"}`}>
                {attention}%
              </div>
            )}
          </div>
        </div>
      </div>
    </button>
  );
}

export function AssetInventoryPanel({ 
  assets, 
  selectedId, 
  onSelect, 
  search, 
  onSearchChange 
}: {
  assets: AssetNode[];
  selectedId: string;
  onSelect: (id: string) => void;
  search: string;
  onSearchChange: (val: string) => void;
}) {
  return (
    <Card className="rounded-[24px] border-white/10 bg-black/20 text-white">
      <CardHeader className="pb-3">
        <div className="flex items-center gap-3">
          <FolderTree className="h-5 w-5 text-slate-300" />
          <CardTitle className="text-lg text-white">Inventory Tree</CardTitle>
        </div>
        <Input 
          value={search} 
          onChange={(e: any) => onSearchChange(e.target.value)} 
          placeholder="검색..." 
          className="mt-2" 
        />
      </CardHeader>
      <CardContent className="max-h-[600px] overflow-auto space-y-1">
        {assets.map((asset) => (
          <div key={asset.id}>
            <AssetListItem 
              asset={asset} 
              selected={selectedId === asset.id} 
              onSelect={onSelect} 
            />
            {asset.children?.map((child) => (
              <AssetListItem 
                key={child.id} 
                asset={child} 
                selected={selectedId === child.id} 
                onSelect={onSelect} 
                indent 
              />
            ))}
          </div>
        ))}
      </CardContent>
    </Card>
  );
}
