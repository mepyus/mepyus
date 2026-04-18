import React, { useState } from "react";
import { Terminal, Play } from "lucide-react";
import { Card, CardHeader, CardTitle, CardContent, Input, Button } from "./ui-components";

export function OperationConsolePanel({ onCommand }: { onCommand: (cmd: string) => void }) {
  const [cmd, setCmd] = useState("");
  return (
    <Card className="rounded-[28px] border-slate-800 bg-[#0d0d12] shadow-2xl">
      <CardHeader className="pb-3 border-b border-white/5">
        <CardTitle className="text-slate-400 text-xs flex items-center gap-2 uppercase tracking-widest">
            <Terminal className="h-4 w-4"/> Optional Tool Layer Console
        </CardTitle>
      </CardHeader>
      <CardContent className="pt-6 space-y-4">
        <div className="flex gap-2">
          <Input 
            value={cmd} onChange={(e: any) => setCmd(e.target.value)} 
            placeholder="CLI / Tool Command..." 
            className="font-mono text-xs bg-black/50 border-white/5"
          />
          <Button onClick={() => { onCommand(cmd); setCmd(""); }} className="rounded-xl bg-slate-700 hover:bg-slate-600 w-16">
            <Play className="h-4 w-4" />
          </Button>
        </div>
        <div className="text-[9px] text-slate-600 font-mono italic">not body skeleton. optional tool layer. use only after line shaping.</div>
      </CardContent>
    </Card>
  );
}
