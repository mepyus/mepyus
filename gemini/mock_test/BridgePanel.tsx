import React from "react";
import { Link2 } from "lucide-react";
import { Card, CardHeader, CardTitle, CardContent, Badge } from "./ui-components";
import { BridgeItem } from "./engine-surface.types";

function bridgeMeta(direction: BridgeItem["direction"]) {
  return {
    from_user: { label: "from user surface", className: "border-sky-500/20 bg-sky-500/10 text-sky-100" },
    from_vectorfl: { label: "from vectorfl surface", className: "border-amber-500/20 bg-amber-500/10 text-amber-100" },
    back_out: { label: "back to surfaces", className: "border-emerald-500/20 bg-emerald-500/10 text-emerald-100" },
  }[direction];
}

export function BridgePanel({ 
  items 
}: {
  items: BridgeItem[];
}) {
  return (
    <Card className="rounded-[24px] border-white/10 bg-black/20 text-white">
      <CardHeader className="pb-3">
        <div className="flex items-center gap-3">
          <Link2 className="h-5 w-5 text-slate-300" />
          <CardTitle className="text-lg text-white">Surface Bridge Rules</CardTitle>
        </div>
      </CardHeader>
      <CardContent className="space-y-3">
        {items.map((item) => (
          <div key={item.id} className="rounded-xl border border-white/10 bg-white/5 p-4">
            <div className="flex items-center justify-between mb-2">
              <div className="text-sm font-medium text-slate-200">{item.title}</div>
              <Badge className={bridgeMeta(item.direction).className}>{bridgeMeta(item.direction).label}</Badge>
            </div>
            <div className="text-xs text-slate-400 leading-5 mb-3">{item.body}</div>
            <div className="flex flex-wrap gap-1.5">
              {item.payload.map((p) => (
                <span key={p} className="px-2 py-0.5 rounded-full bg-white/5 border border-white/10 text-[10px] text-slate-500">
                  {p}
                </span>
              ))}
            </div>
          </div>
        ))}
      </CardContent>
    </Card>
  );
}
