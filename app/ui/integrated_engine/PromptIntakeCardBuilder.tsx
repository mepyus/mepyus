import React, { useState } from "react";
import { Check, Clipboard, FileText, ShieldAlert } from "lucide-react";
import { Button } from "./ui-components";

const PLACEMENT_LABELS = [
  "RETURN_TO_SPACE_VALUE",
  "RETURN_TO_SPACE_VALUE_WITH_WATCH",
  "WATCH",
  "NEEDS_ONE_MORE_NEIGHBOR",
  "BOUNDED_IMPLEMENTATION_PREP",
  "HOLD",
  "RAW_TRACE",
] as const;

type PlacementLabel = (typeof PLACEMENT_LABELS)[number];

const PLACEMENT_HUMAN_LABELS: Record<PlacementLabel, string> = {
  RETURN_TO_SPACE_VALUE: "쓸 수 있는 판단",
  RETURN_TO_SPACE_VALUE_WITH_WATCH: "쓸 수 있지만 조심해서 써야 하는 판단",
  WATCH: "유용해 보이지만 아직 승격 불가",
  NEEDS_ONE_MORE_NEIGHBOR: "근거 하나 더 필요",
  BOUNDED_IMPLEMENTATION_PREP: "좁은 구현 준비 가능",
  HOLD: "보류 / 진행하지 않음",
  RAW_TRACE: "기록만 보관",
};

const textareaClassName =
  "mt-2 min-h-[82px] w-full rounded-xl border border-white/10 bg-slate-900/80 p-3 text-sm leading-6 normal-case tracking-normal text-slate-100 outline-none placeholder:text-slate-500 focus:border-cyan-300/50 focus:ring-1 focus:ring-cyan-300/40";

function valueOrPlaceholder(value: string, placeholder: string) {
  const clean = value.trim();
  return clean || placeholder;
}

function buildMarkdown({
  purpose,
  material,
  notRead,
  recoveredJudgment,
  placement,
  watch,
  nextAction,
}: {
  purpose: string;
  material: string;
  notRead: string;
  recoveredJudgment: string;
  placement: PlacementLabel;
  watch: string;
  nextAction: string;
}) {
  return [
    "# VectorFL Live Task Intake Card",
    "",
    "## Purpose",
    valueOrPlaceholder(purpose, "TBD: user purpose / decision to make."),
    "",
    "## Material / Request",
    valueOrPlaceholder(material, "TBD: material, prompt, or result being read."),
    "",
    "## Not Read",
    valueOrPlaceholder(notRead, "TBD: logs, raw traces, or unrelated files intentionally not read."),
    "",
    "## Recovered Judgment",
    valueOrPlaceholder(recoveredJudgment, "TBD: reusable judgment or missing evidence."),
    "",
    "## Placement",
    placement,
    "",
    "## Watch",
    valueOrPlaceholder(watch, "TBD: caution, evidence risk, or unsafe promotion risk."),
    "",
    "## Next Action",
    valueOrPlaceholder(nextAction, "TBD: one concrete next step."),
  ].join("\n");
}

export function PromptIntakeCardBuilder() {
  const [purpose, setPurpose] = useState("");
  const [material, setMaterial] = useState("");
  const [notRead, setNotRead] = useState("");
  const [recoveredJudgment, setRecoveredJudgment] = useState("");
  const [watch, setWatch] = useState("");
  const [nextAction, setNextAction] = useState("");
  const [placement, setPlacement] = useState<PlacementLabel>("RETURN_TO_SPACE_VALUE_WITH_WATCH");
  const [copyStatus, setCopyStatus] = useState<"idle" | "copied" | "failed">("idle");

  const markdown = buildMarkdown({ purpose, material, notRead, recoveredJudgment, placement, watch, nextAction });

  async function copyMarkdown() {
    try {
      if (!navigator.clipboard?.writeText) {
        throw new Error("Clipboard API unavailable");
      }
      await navigator.clipboard.writeText(markdown);
      setCopyStatus("copied");
    } catch {
      setCopyStatus("failed");
    }
  }

  return (
    <section className="rounded-[28px] border border-cyan-300/15 bg-slate-950 p-5 text-slate-100 shadow-2xl">
      <header className="flex flex-wrap items-start justify-between gap-3 border-b border-white/10 pb-4">
        <div>
          <div className="flex items-center gap-2 text-[10px] font-black uppercase tracking-[0.18em] text-cyan-300">
            <FileText className="h-4 w-4" />
            Prompt Intake Card Builder
          </div>
          <p className="mt-2 max-w-2xl text-xs leading-5 text-slate-500">
            Build a small VectorFL Live Task markdown card before routing, execution, or recovery.
          </p>
        </div>
        <Button
          onClick={copyMarkdown}
          className="rounded-lg border border-cyan-300/30 bg-cyan-300/10 px-3 py-2 text-[10px] font-black uppercase tracking-[0.14em] text-cyan-100 hover:bg-cyan-300/15"
        >
          {copyStatus === "copied" ? <Check className="mr-2 inline h-4 w-4" /> : <Clipboard className="mr-2 inline h-4 w-4" />}
          {copyStatus === "copied" ? "Copied" : "Copy"}
        </Button>
      </header>

      <div className="mt-5 grid gap-4 lg:grid-cols-[minmax(0,0.95fr)_minmax(0,1.05fr)]">
        <div className="space-y-3">
          <label className="block text-[10px] font-black uppercase tracking-[0.18em] text-slate-500">
            User Prompt
            <textarea
              value={purpose}
              onChange={(event) => setPurpose(event.target.value)}
              className={textareaClassName}
              placeholder="What judgment or decision should this task support?"
            />
          </label>

          <label className="block text-[10px] font-black uppercase tracking-[0.18em] text-slate-500">
            Material / Request
            <textarea
              value={material}
              onChange={(event) => setMaterial(event.target.value)}
              className={textareaClassName}
              placeholder="What material, prompt, or result is being read?"
            />
          </label>

          <label className="block text-[10px] font-black uppercase tracking-[0.18em] text-slate-500">
            Not Read / Out of Scope
            <textarea
              value={notRead}
              onChange={(event) => setNotRead(event.target.value)}
              className={textareaClassName}
              placeholder="What logs, traces, or files were intentionally excluded?"
            />
          </label>

          <label className="block text-[10px] font-black uppercase tracking-[0.18em] text-slate-500">
            Recovered Judgment
            <textarea
              value={recoveredJudgment}
              onChange={(event) => setRecoveredJudgment(event.target.value)}
              className={textareaClassName}
              placeholder="What usable judgment, pointer, or missing evidence was recovered?"
            />
          </label>

          <label className="block text-[10px] font-black uppercase tracking-[0.18em] text-slate-500">
            Watch / Caution
            <textarea
              value={watch}
              onChange={(event) => setWatch(event.target.value)}
              className={textareaClassName}
              placeholder="What should not be promoted, assumed, or overread?"
            />
          </label>

          <label className="block text-[10px] font-black uppercase tracking-[0.18em] text-slate-500">
            Next Action
            <textarea
              value={nextAction}
              onChange={(event) => setNextAction(event.target.value)}
              className={textareaClassName}
              placeholder="What is the next concrete step?"
            />
          </label>

          <label className="block text-[10px] font-black uppercase tracking-[0.18em] text-slate-500">
            Placement
            <select
              value={placement}
              onChange={(event) => setPlacement(event.target.value as PlacementLabel)}
              className="mt-2 w-full rounded-xl border border-white/10 bg-black/30 px-3 py-3 font-mono text-xs text-slate-100 outline-none focus:ring-1 focus:ring-cyan-300"
            >
              {PLACEMENT_LABELS.map((label) => (
                <option key={label} value={label}>
                  {label} = {PLACEMENT_HUMAN_LABELS[label]}
                </option>
              ))}
            </select>
          </label>

          {copyStatus === "failed" ? (
            <div className="flex items-start gap-2 rounded-xl border border-amber-300/20 bg-amber-300/10 p-3 text-xs leading-5 text-amber-100">
              <ShieldAlert className="mt-0.5 h-4 w-4 shrink-0" />
              Clipboard copy failed. Select the preview text and copy manually.
            </div>
          ) : null}
        </div>

        <div className="min-h-0 rounded-2xl border border-white/10 bg-black/30 p-4">
          <div className="mb-3 flex items-center justify-between gap-3">
            <div className="text-[10px] font-black uppercase tracking-[0.18em] text-cyan-300">Markdown Preview</div>
            <div className="rounded-full border border-white/10 bg-white/[0.04] px-2 py-0.5 text-[9px] font-bold text-slate-400">
              live update
            </div>
          </div>
          <pre className="max-h-[620px] overflow-auto whitespace-pre-wrap rounded-xl border border-white/10 bg-slate-950 p-5 font-mono text-xs leading-6 text-slate-300">
            {markdown}
          </pre>
        </div>
      </div>
    </section>
  );
}

export default PromptIntakeCardBuilder;
