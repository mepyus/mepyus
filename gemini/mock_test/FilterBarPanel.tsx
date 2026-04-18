import React from "react";
import { Filter, SortAsc, LayoutGrid, CheckCircle2 } from "lucide-react";
import { Card, CardContent, Input, Badge } from "./ui-components";
import { AssetKind, AssetHealth } from "./engine-surface.types";

export function FilterBarPanel({
  search, onSearchChange,
  kindFilter, onKindChange,
  healthFilter, onHealthChange,
  sortBy, onSortChange
}: {
  search: string; onSearchChange: (val: string) => void;
  kindFilter: string; onKindChange: (val: any) => void;
  healthFilter: string; onHealthChange: (val: any) => void;
  sortBy: string; onSortChange: (val: any) => void;
}) {
  const kinds: (AssetKind | "all")[] = ["all", "scripts", "docs", "inputs", "runtime"];
  const healths: (AssetHealth | "all")[] = ["all", "healthy", "watch", "broken"];

  return (
    <Card className="rounded-[24px] border-white/10 bg-black/20 text-white mb-5">
      <CardContent className="p-4">
        <div className="flex flex-col xl:flex-row gap-4 items-start xl:items-center">
          
          {/* Search */}
          <div className="relative w-full xl:w-64">
            <Input 
              value={search} 
              onChange={(e: any) => onSearchChange(e.target.value)} 
              placeholder="Search assets..." 
              className="pl-3 h-10 rounded-xl bg-white/5 border-white/10"
            />
          </div>

          <div className="h-6 w-[1px] bg-white/10 hidden xl:block" />

          {/* Kind Filters */}
          <div className="flex items-center gap-2 overflow-x-auto pb-2 xl:pb-0">
            <div className="text-[10px] uppercase tracking-wider text-slate-500 font-bold mr-1">Kind:</div>
            {kinds.map(k => (
              <button key={k} onClick={() => onKindChange(k)}>
                <Badge 
                  variant={kindFilter === k ? "default" : "outline"}
                  className={`rounded-lg px-3 py-1 cursor-pointer transition-all ${
                    kindFilter === k ? "bg-blue-600 text-white" : "border-white/10 text-slate-400 hover:text-slate-200"
                  }`}
                >
                  {k}
                </Badge>
              </button>
            ))}
          </div>

          <div className="h-6 w-[1px] bg-white/10 hidden xl:block" />

          {/* Health Filters */}
          <div className="flex items-center gap-2 overflow-x-auto pb-2 xl:pb-0">
            <div className="text-[10px] uppercase tracking-wider text-slate-500 font-bold mr-1">Health:</div>
            {healths.map(h => (
              <button key={h} onClick={() => onHealthChange(h)}>
                <Badge 
                  variant={healthFilter === h ? "default" : "outline"}
                  className={`rounded-lg px-3 py-1 cursor-pointer transition-all ${
                    healthFilter === h ? "bg-zinc-200 text-black" : "border-white/10 text-slate-400 hover:text-slate-200"
                  }`}
                >
                  {h}
                </Badge>
              </button>
            ))}
          </div>

          <div className="h-6 w-[1px] bg-white/10 hidden xl:block" />

          {/* Sorting */}
          <div className="flex items-center gap-2">
            <SortAsc className="h-4 w-4 text-slate-500" />
            <select 
              value={sortBy} 
              onChange={(e) => onSortChange(e.target.value)}
              className="bg-transparent text-xs text-slate-300 focus:outline-none cursor-pointer"
            >
              <option value="default">Default Sort</option>
              <option value="attention">Attention High</option>
              <option value="updated">Recently Updated</option>
            </select>
          </div>

        </div>
      </CardContent>
    </Card>
  );
}
