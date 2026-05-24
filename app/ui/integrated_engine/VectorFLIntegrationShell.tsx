import React, { useEffect, useState } from "react";
import { Command, GitPullRequest, ShieldCheck } from "lucide-react";
import { CliHostControlPanel } from "./CliHostControlPanel.tsx";
import packageInstance from "../../../runtime/contracts/integrated_engine_single_handler_package_instance_v0.json";
import translationProjection from "../../../runtime/contracts/integrated_engine_language_handler_translation_projection_v0.json";
import userProjection from "../../../runtime/contracts/integrated_engine_language_handler_user_projection_v0.json";
import { cx } from "./ui-components";

type CliReadableReturn = {
  session_id?: string;
  status?: string;
  purpose_text?: string;
  route_label?: string;
  marks?: string[];
  structured_return_preview?: string;
  deposit_candidate_preview?: string;
  session_path?: string;
};

type CliHostState = {
  latest_readable_return?: CliReadableReturn;
  recent_readable_returns?: CliReadableReturn[];
  deposit_ready_returns?: CliReadableReturn[];
};

type WorkPacketDraft = {
  purpose: string;
  taskLens: string;
  internalSearchStatus: string;
  evidenceSummary: string;
  evidenceLimitation: string;
  evidenceCount: number;
  evidenceKinds: string[];
  nextRouteCandidate: string;
  expectedReturnShape: string;
  manualStillNeeded: string[];
};

type PackageCard = {
  id: string;
  title: string;
  status: "active" | "queued" | "returned" | "hold";
  stage: string;
  executor: string;
  summary: string;
};

type ModalKind = "setup" | "result" | "watch" | null;

type DashboardRefreshState = {
  status: "idle" | "refreshing" | "live" | "error";
  lastUpdated: string;
  error: string;
};

const pkg: any = packageInstance;
const vectorflMeaning: any = (translationProjection as any).vectorfl_meaning;
const engineMeaning: any = (translationProjection as any).engine_meaning;
const userMeaning: any = (userProjection as any).user_meaning;

function compactText(value?: string, fallback = "not available", limit = 120) {
  const text = (value || "").trim();
  if (!text) return fallback;
  return text.length > limit ? `${text.slice(0, limit - 1)}...` : text;
}

function shortId(id?: string) {
  return id ? id.replace("cli_", "") : "none";
}

function routeLabel(turn?: CliReadableReturn) {
  if (!turn) return "no route";
  if (turn.route_label) return turn.route_label.replace(/_/g, " ");
  if (turn.marks?.length) return turn.marks.join(", ");
  return "unmarked";
}

function SmallStat({ label, value, note, active }: { label: string; value: string; note?: string; active?: boolean }) {
  return (
    <div className={cx("rounded-lg border px-3 py-2", active ? "border-cyan-300/30 bg-cyan-300/10" : "border-white/10 bg-white/[0.04]")}>
      <div className="text-[9px] font-black uppercase tracking-[0.16em] text-slate-500">{label}</div>
      <div className="mt-1 text-xs font-black text-slate-100">{value}</div>
      {note ? <div className="mt-1 line-clamp-2 text-[10px] leading-4 text-slate-500">{note}</div> : null}
    </div>
  );
}

const packageStackSeed: PackageCard[] = [
  {
    id: "pkg_internal_space_read_001",
    title: "내부 공간 구조 분석",
    status: "active",
    stage: "internal space read",
    executor: "codex",
    summary: "엔진/통합엔진/패키지 구조 기준으로 현재 공간을 읽는 작업",
  },
  {
    id: "pkg_ui_surface_adjust_002",
    title: "화면 사용성 조정",
    status: "returned",
    stage: "return review",
    executor: "codex",
    summary: "입력창/버튼/사이드바 사용성 조정 결과 확인",
  },
  {
    id: "pkg_external_lens_pool_003",
    title: "외부 렌즈 재료 읽기",
    status: "hold",
    stage: "precedent hold",
    executor: "gemini-ready",
    summary: "OpenCode / Claude Code 화면 선례는 참고만 하고 아직 자동 확장하지 않음",
  },
  {
    id: "pkg_openharness_structure_probe",
    title: "OpenHarness 구조 분석",
    status: "queued",
    stage: "source structure reread",
    executor: "codex-dry-run",
    summary: "references/git_search/openharness-main 폴더를 내부 공간 재료로 구조 분해해 읽는 검증 패키지",
  },
  {
    id: "pkg_parallel_queue_design_004",
    title: "패키지 병렬 큐 설계",
    status: "queued",
    stage: "queue draft",
    executor: "none",
    summary: "여러 패키지 병렬 전환을 위한 좌측 stack / queue shell 후보",
  },
];

const PACKAGE_STACK_STORAGE_KEY = "integrated_engine_package_stack_v0";
const SELECTED_PACKAGE_STORAGE_KEY = "integrated_engine_selected_package_v0";

function loadPackageStack() {
  if (typeof window === "undefined") return packageStackSeed;
  try {
    const parsed = JSON.parse(window.localStorage.getItem(PACKAGE_STACK_STORAGE_KEY) || "[]");
    if (Array.isArray(parsed) && parsed.length) {
      const stored = parsed as PackageCard[];
      const storedIds = new Set(stored.map((item) => item.id));
      const missingSeeds = packageStackSeed.filter((item) => !storedIds.has(item.id));
      return [...stored, ...missingSeeds];
    }
  } catch {
    return packageStackSeed;
  }
  return packageStackSeed;
}

function loadSelectedPackageId() {
  if (typeof window === "undefined") return packageStackSeed[0].id;
  return window.localStorage.getItem(SELECTED_PACKAGE_STORAGE_KEY) || packageStackSeed[0].id;
}

function PackageStack({
  packages,
  selectedId,
  onSelect,
  onCreate,
  onDelete,
  onOpenModal,
}: {
  packages: PackageCard[];
  selectedId: string;
  onSelect: (id: string) => void;
  onCreate: (title: string) => void;
  onDelete: (id: string) => void;
  onOpenModal: (kind: Exclude<ModalKind, null>, id: string) => void;
}) {
  const [draftTitle, setDraftTitle] = useState("");
  const counts = packages.reduce<Record<string, number>>((acc, item) => {
    acc[item.status] = (acc[item.status] || 0) + 1;
    return acc;
  }, {});

  return (
    <aside className="min-h-0 overflow-y-auto border-r border-slate-800 bg-slate-950 p-5">
      <div className="flex items-center gap-2 text-sm font-black">
        <Command className="h-4 w-4 text-cyan-300" />
        통합엔진
      </div>

      <section className="mt-8">
        <div className="text-[10px] font-black uppercase tracking-[0.2em] text-cyan-300">Package Stack</div>
        <h1 className="mt-2 text-xl font-black leading-tight">현재 작업 묶음</h1>
        <p className="mt-2 text-xs leading-5 text-slate-500">
          병렬 실행이 아니라, 여러 작업 패키지를 전환해 볼 수 있는 관리 껍데기다.
        </p>
      </section>

      <section className="mt-5 grid grid-cols-2 gap-2">
        <SmallStat label="active" value={String(counts.active || 0)} />
        <SmallStat label="queued" value={String(counts.queued || 0)} />
        <SmallStat label="returned" value={String(counts.returned || 0)} />
        <SmallStat label="hold" value={String(counts.hold || 0)} />
      </section>

      <section className="mt-5 rounded-xl border border-white/10 bg-white/[0.04] p-3">
        <div className="text-[10px] font-black uppercase tracking-[0.18em] text-slate-500">new package</div>
        <input
          value={draftTitle}
          onChange={(event) => setDraftTitle(event.target.value)}
          placeholder="예: 내부 공간 구조 분석"
          className="mt-2 w-full rounded-lg border border-white/10 px-3 py-2 text-xs"
          style={{ backgroundColor: "#020617", color: "#ffffff", caretColor: "#67e8f9" }}
        />
        <button
          onClick={() => {
            onCreate(draftTitle);
            setDraftTitle("");
          }}
          className="mt-2 w-full rounded-lg border border-white/25 px-3 py-2 text-xs font-black text-white"
          style={{ backgroundColor: "#020617", color: "#ffffff" }}
        >
          Add package
        </button>
        <p className="mt-2 text-[10px] leading-4 text-slate-500">
          새 패키지는 먼저 목적/업무 지시를 받고, 이후 중앙 setup에서 lens/context를 잡아 CLI에 넘긴다.
        </p>
      </section>

      <section className="mt-5 space-y-2">
        {packages.map((item) => {
          const selected = item.id === selectedId;
          return (
            <button
              key={item.id}
              onClick={() => onSelect(item.id)}
              className={cx(
                "w-full rounded-xl border p-3 text-left transition",
                selected ? "border-cyan-300/40 bg-cyan-300/10" : "border-white/10 bg-white/[0.04] hover:bg-white/[0.07]"
              )}
            >
              <div className="flex items-center justify-between gap-3">
                <span className="text-xs font-black text-slate-100">{item.title}</span>
                <span className="rounded-full border border-white/10 bg-slate-950 px-2 py-0.5 text-[9px] font-bold text-slate-300">{item.status}</span>
              </div>
              <div className="mt-2 text-[10px] font-bold uppercase tracking-[0.14em] text-slate-500">{item.stage} · {item.executor}</div>
              <p className="mt-2 line-clamp-2 text-[10px] leading-4 text-slate-500">{item.summary}</p>
              {selected ? (
                <div className="mt-3 flex flex-wrap gap-2">
                  <span className="rounded-md border border-cyan-300/25 px-2 py-1 text-[9px] font-black text-cyan-100">selected</span>
                  {(["setup", "result", "watch"] as const).map((kind) => (
                    <button
                      key={kind}
                      onClick={(event) => {
                        event.stopPropagation();
                        onOpenModal(kind, item.id);
                      }}
                      className="rounded-md border border-white/20 px-2 py-1 text-[9px] font-black text-white"
                      style={{ backgroundColor: "#020617", color: "#ffffff" }}
                    >
                      {kind}
                    </button>
                  ))}
                  <button
                    onClick={(event) => {
                      event.stopPropagation();
                      onDelete(item.id);
                    }}
                    className="rounded-md border border-white/20 px-2 py-1 text-[9px] font-black text-white"
                    style={{ backgroundColor: "#020617", color: "#ffffff" }}
                  >
                    delete
                  </button>
                </div>
              ) : null}
            </button>
          );
        })}
      </section>

      <details className="mt-6 border-t border-white/10 pt-4">
        <summary className="cursor-pointer text-[10px] font-black uppercase tracking-[0.18em] text-slate-500">stack boundary</summary>
        <p className="mt-3 text-xs leading-5 text-slate-500">
          이 stack은 아직 실제 병렬 runner가 아니다. 선택된 패키지 하나만 중앙 workbench에서 깊게 본다.
        </p>
      </details>
    </aside>
  );
}

function PackageModal({
  kind,
  pkg,
  latestTurn,
  workPacketDraft,
  onClose,
}: {
  kind: ModalKind;
  pkg?: PackageCard;
  latestTurn?: CliReadableReturn;
  workPacketDraft?: WorkPacketDraft;
  onClose: () => void;
}) {
  if (!kind || !pkg) return null;

  const title =
    kind === "setup"
      ? "Package Setup"
      : kind === "result"
        ? "Package Result"
        : "Line / Axis Watch";

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/70 p-5">
      <section className="max-h-[86vh] w-full max-w-3xl overflow-y-auto rounded-2xl border border-white/15 bg-slate-950 p-5 text-slate-100 shadow-2xl">
        <div className="flex items-start justify-between gap-4 border-b border-white/10 pb-4">
          <div>
            <div className="text-[10px] font-black uppercase tracking-[0.2em] text-cyan-300">{title}</div>
            <h2 className="mt-2 text-2xl font-black">{pkg.title}</h2>
            <p className="mt-2 text-xs leading-5 text-slate-500">{pkg.id} · {pkg.status} · {pkg.stage}</p>
          </div>
          <button
            onClick={onClose}
            className="rounded-lg border border-white/25 px-3 py-2 text-xs font-black text-white"
            style={{ backgroundColor: "#020617", color: "#ffffff" }}
          >
            Close
          </button>
        </div>

        {kind === "setup" ? (
          <div className="mt-5 grid gap-3 md:grid-cols-2">
            <SmallStat label="package vessel" value={pkg.title} note="목적어를 바꾸면 다시 쓸 수 있는 처리 그릇. 지금은 이 패키지의 목적/범위/근거를 담음" active />
            <SmallStat label="inner line / axis" value="purpose-shaped" note={pkg.summary} />
            <SmallStat label="executor candidate" value={pkg.executor} note="CLI 실행자는 여기서 후보일 뿐이며 자동 실행 권한을 뜻하지 않음" />
            <SmallStat label="initial route" value={pkg.stage} note="신규 패키지는 목적/범위/context refs를 잡은 뒤 실행 가능" />
            <SmallStat label="context refs" value={workPacketDraft?.evidenceCount ? `${workPacketDraft.evidenceCount} refs` : "not attached"} note={workPacketDraft?.evidenceSummary || "중앙 engine setup에서 spec/context refs를 지정해야 함"} />
            <SmallStat label="line / axis watch" value="manual watch" note="반응 라인/축을 볼 수는 있지만 자동 감지는 아직 아님" />
            <SmallStat label="digestion guard" value="read-only / no promotion" note="소화/흡수/재투입 언어는 공정 해석이며 자동화, canonical ingestion, promotion을 열지 않음" />
          </div>
        ) : null}

        {kind === "result" ? (
          <div className="mt-5 space-y-3">
            <div className="grid gap-3 md:grid-cols-3">
              <SmallStat label="session" value={shortId(latestTurn?.session_id)} />
              <SmallStat label="status" value={latestTurn?.status || "none"} />
              <SmallStat label="route" value={routeLabel(latestTurn)} />
            </div>
            <section className="rounded-xl border border-white/10 bg-white/[0.04] p-4">
              <div className="text-[10px] font-black uppercase tracking-[0.16em] text-slate-500">return preview</div>
              <p className="mt-3 max-h-80 overflow-auto whitespace-pre-wrap text-xs leading-5 text-slate-300">
                {compactText(latestTurn?.structured_return_preview || latestTurn?.purpose_text, "아직 반환 없음", 4000)}
              </p>
            </section>
            <SmallStat label="not enough for" value="final approval" note="이 모달은 결과 확인용이며 redeposit, promotion, canonical decision은 별도 판단 필요" />
          </div>
        ) : null}

        {kind === "watch" ? (
          <div className="mt-5 grid gap-3 md:grid-cols-2">
            <SmallStat label="line reaction" value={workPacketDraft?.evidenceCount ? "visible / weak" : "pending"} note="다른 패키지 실행 중 건드린 라인이 있는지 보는 수동 감시 슬롯" active />
            <SmallStat label="axis reaction" value={workPacketDraft?.taskLens ? "lens-linked / weak" : "pending"} note="축 후보는 아직 반응 신호일 뿐 검증 결과가 아님" />
            <SmallStat label="digestion signal" value={latestTurn?.session_id ? "return material present" : "not yet"} note="처리 결과가 생기면 그대로 승인하지 않고 흡수/재투입 후보로 재독해함" />
            <SmallStat label="internal exploration trigger" value="manual only" note="새 반응이 보여도 내부 탐색팀 자동 실행은 아직 하지 않음" />
            <SmallStat label="redeposit route" value="blocked until review" note="분석/정리/재투입은 결과 확인 후 별도 패키지로 열어야 함" />
            <SmallStat label="what this is not" value="not automation" note="이 watch는 반응 기록용이다. 실제 내부팀 실행, 라인 승격, 축 확정은 하지 않음" />
          </div>
        ) : null}
      </section>
    </div>
  );
}

function StructureReadingSlot({
  latestTurn,
  workPacketDraft,
}: {
  latestTurn?: CliReadableReturn;
  workPacketDraft?: WorkPacketDraft;
}) {
  const hasEvidence = Boolean(workPacketDraft?.evidenceCount);
  const hasReturn = Boolean(latestTurn?.session_id);
  const route = routeLabel(latestTurn);
  const lineHint = hasEvidence ? "inferred" : "pending";
  const axisHint = hasEvidence && workPacketDraft?.taskLens ? "weak" : "pending";
  const precedent = hasEvidence ? "not checked here" : "pending";
  const boundary = latestTurn?.status === "failed" ? "hold" : "read-only / no promotion";
  const packageState = hasReturn ? "returned package" : workPacketDraft ? "draft packet" : "not formed";
  const digestionState = hasReturn ? "reread for absorption" : workPacketDraft ? "vessel forming" : "waiting";

  const rows = [
    {
      label: "vessel",
      value: workPacketDraft ? "formed" : "waiting",
      note: workPacketDraft ? "패키지는 목적어를 담는 그릇으로 먼저 형성됨" : "목적/범위/근거가 아직 그릇으로 묶이지 않음",
    },
    {
      label: "line hint",
      value: lineHint,
      note: hasEvidence ? "현재 지시와 근거에서 작업 흐름 후보만 약하게 읽힘" : "지시가 아직 내부 근거와 연결되지 않음",
    },
    {
      label: "axis hint",
      value: axisHint,
      note: hasEvidence ? `${workPacketDraft?.taskLens || "lens"} 렌즈 기준의 약한 축 신호` : "axis 판단 전",
    },
    {
      label: "precedent",
      value: precedent,
      note: "이 화면 슬롯은 선례 채굴 완료를 뜻하지 않음. 필요 시 별도 내부 선례 읽기로 보냄",
    },
    {
      label: "boundary",
      value: boundary,
      note: "승격, 자동화, canonical ingestion은 여전히 열지 않음",
    },
    {
      label: "package state",
      value: packageState,
      note: hasReturn ? `route: ${route}` : "CLI 반환 전에는 결과 패키지 아님",
    },
    {
      label: "digestion",
      value: digestionState,
      note: hasReturn ? "처리 결과를 바로 승인하지 않고 내부 변화/새 재료/재투입 후보로 다시 읽음" : "아직 소화 결과가 아니라 실행 전 또는 형성 중 상태",
    },
  ];

  return (
    <section className="mt-4 rounded-xl border border-white/10 bg-white/[0.04] p-4">
      <div className="text-[9px] font-black uppercase tracking-[0.16em] text-cyan-300">Structure Reading</div>
      <p className="mt-2 text-[10px] leading-4 text-slate-500">
        패키지를 그릇으로 보고, 그 안의 라인/축 후보와 처리 후 재투입 후보를 약하게 읽는다. 자동 판단이나 승격은 아니다.
      </p>
      <div className="mt-3 space-y-2">
        {rows.map((row) => (
          <div key={row.label} className="rounded-lg border border-white/10 bg-slate-950 px-3 py-2">
            <div className="flex items-center justify-between gap-3">
              <span className="text-[9px] font-black uppercase tracking-[0.14em] text-slate-500">{row.label}</span>
              <span className="rounded-full border border-white/10 bg-white/[0.05] px-2 py-0.5 text-[9px] font-bold text-slate-200">{row.value}</span>
            </div>
            <p className="mt-1 line-clamp-2 text-[10px] leading-4 text-slate-500">{row.note}</p>
          </div>
        ))}
      </div>
    </section>
  );
}

function EnginePositionSidebar({
  latestTurn,
  workPacketDraft,
  onLoadLatest,
}: {
  latestTurn?: CliReadableReturn;
  workPacketDraft?: WorkPacketDraft;
  onLoadLatest: () => void;
}) {
  const steps = [
    {
      label: "지시 수신",
      status: workPacketDraft ? "captured" : "waiting",
      detail: workPacketDraft?.purpose || "사용자 지시 입력 대기",
    },
    {
      label: "내부 공간 읽기",
      status: workPacketDraft ? workPacketDraft.internalSearchStatus : "not formed",
      detail: workPacketDraft?.evidenceSummary || "엔진/통합엔진/패키지 구조를 읽기 전",
    },
    {
      label: "패키지 형성 / CLI 실행",
      status: latestTurn?.session_id ? "returned" : "ready",
      detail: latestTurn?.session_id ? `${shortId(latestTurn.session_id)} · ${latestTurn.status || "unknown"}` : "엔진 공정 wrapper를 붙여 Codex CLI 전송 가능",
    },
    {
      label: "반환 재독해",
      status: latestTurn?.session_id ? routeLabel(latestTurn) : "pending",
      detail: compactText(latestTurn?.structured_return_preview || latestTurn?.purpose_text, "CLI 출력이 패키지/route/다음 행동으로 아직 재독해되지 않음", 120),
    },
  ];

  return (
    <aside className="min-h-0 overflow-y-auto border-l border-slate-800 bg-slate-950 p-5 text-slate-100">
      <div>
        <div className="text-[10px] font-black uppercase tracking-[0.2em] text-cyan-300">Engine position</div>
        <h2 className="mt-2 text-xl font-black">현재 위치</h2>
        <p className="mt-2 text-xs leading-5 text-slate-400">CLI 로그가 아니라, 지시가 그릇 형성, 라인/축 읽기, 처리, 재투입 후보 중 어디를 흐르는지 보여준다.</p>
      </div>

      <section className="mt-5 rounded-xl border border-white/10 bg-white/[0.04] p-4">
        <div className="text-[9px] font-black uppercase tracking-[0.16em] text-slate-500">process</div>
        <div className="mt-3 space-y-3">
          {steps.map((step, index) => (
            <div key={step.label} className="grid grid-cols-[24px_1fr] gap-3">
              <div className="flex flex-col items-center">
                <span className={cx("grid h-6 w-6 place-items-center rounded-full text-[10px] font-black", step.status !== "pending" && step.status !== "waiting" && step.status !== "not formed" ? "bg-cyan-300 text-slate-950" : "bg-white/10 text-slate-500")}>
                  {index + 1}
                </span>
                {index < steps.length - 1 ? <span className="mt-1 h-8 w-px bg-white/10" /> : null}
              </div>
              <div>
                <div className="flex items-center justify-between gap-2">
                  <span className="text-xs font-black text-slate-100">{step.label}</span>
                  <span className="rounded-full bg-white/[0.06] px-2 py-0.5 text-[9px] font-bold text-slate-400">{step.status}</span>
                </div>
                <p className="mt-1 line-clamp-2 text-[10px] leading-4 text-slate-500">{step.detail}</p>
              </div>
            </div>
          ))}
        </div>
      </section>

      <section className="mt-4 space-y-2">
        <SmallStat label="engine" value="소화 / 처리" note={engineMeaning.engine_meaning_summary} />
        <SmallStat label="integrated engine" value="라인·축 / 경계 / route 판정" note={vectorflMeaning.vectorfl_state_reason} />
        <SmallStat label="package" value="그릇 / 결과물 / 재투입 후보" note={userMeaning.user_next_action_reason} />
      </section>

      <StructureReadingSlot latestTurn={latestTurn} workPacketDraft={workPacketDraft} />

      <section className="mt-4 rounded-xl border border-white/10 bg-white/[0.04] p-4">
        <div className="text-[9px] font-black uppercase tracking-[0.16em] text-slate-500">latest return</div>
        <div className="mt-2 text-xs font-bold text-slate-100">{shortId(latestTurn?.session_id)} · {latestTurn?.status || "none"}</div>
        <div className="mt-1 text-[10px] text-slate-500">{routeLabel(latestTurn)}</div>
        <p className="mt-3 max-h-44 overflow-auto whitespace-pre-wrap text-[10px] leading-5 text-slate-400">
          {compactText(latestTurn?.structured_return_preview || latestTurn?.purpose_text, "아직 반환 없음", 520)}
        </p>
      </section>

      <button
        onClick={onLoadLatest}
        className="mt-4 w-full rounded-lg border border-white/25 px-3 py-2 text-xs font-black text-white"
        style={{ backgroundColor: "#020617", color: "#ffffff" }}
      >
        <GitPullRequest className="mr-1 inline h-3.5 w-3.5" />
        latest return to VectorFL
      </button>

      <details className="mt-5 border-t border-white/10 pt-4">
        <summary className="cursor-pointer text-[10px] font-black uppercase tracking-[0.18em] text-slate-500">inspector: raw state boundary</summary>
        <div className="mt-3 space-y-2">
          <SmallStat label="not done" value="no automation" note={engineMeaning.engine_not_done_summary} />
          <SmallStat label="uncertainty" value="human validation needed" note={engineMeaning.engine_uncertainty_notes || "브라우저 사용감 검증은 아직 사람 손검증 대상입니다."} />
        </div>
      </details>

      <div className="mt-4 flex items-start gap-2 rounded-xl border border-amber-300/20 bg-amber-300/10 p-3 text-[10px] leading-4 text-amber-100">
        <ShieldCheck className="mt-0.5 h-3.5 w-3.5 flex-none" />
        CLI is executor. Integrated Engine remains interpreter, governor, memory layer. No automation or second handler.
      </div>
    </aside>
  );
}

export default function VectorFLIntegrationShell() {
  const [cliHostState, setCliHostState] = useState<CliHostState>({});
  const [workPacketDraft, setWorkPacketDraft] = useState<WorkPacketDraft | undefined>();
  const [externalFollowupTurn, setExternalFollowupTurn] = useState<CliReadableReturn | undefined>();
  const [packages, setPackages] = useState<PackageCard[]>(() => loadPackageStack());
  const [selectedPackageId, setSelectedPackageId] = useState(() => loadSelectedPackageId());
  const [modal, setModal] = useState<{ kind: ModalKind; packageId: string }>({ kind: null, packageId: "" });
  const [dashboardRefresh, setDashboardRefresh] = useState<DashboardRefreshState>({
    status: "idle",
    lastUpdated: "",
    error: "",
  });

  async function refreshDashboardState(silent = false) {
    if (!silent) {
      setDashboardRefresh((current) => ({ ...current, status: "refreshing", error: "" }));
    }
    try {
      const response = await fetch("/api/vectorfl-engine/state");
      const result = await response.json();
      if (!response.ok) throw new Error(result.error || "failed to refresh engine state");
      setCliHostState(result.cli_host_control || {});
      setDashboardRefresh({
        status: "live",
        lastUpdated: new Date().toLocaleTimeString(),
        error: "",
      });
    } catch (error: any) {
      setDashboardRefresh({
        status: "error",
        lastUpdated: new Date().toLocaleTimeString(),
        error: error?.message || "failed to refresh",
      });
    }
  }

  useEffect(() => {
    refreshDashboardState(true);
    const intervalId = window.setInterval(() => refreshDashboardState(true), 5000);
    return () => window.clearInterval(intervalId);
  }, []);

  const latestTurn = cliHostState.latest_readable_return || cliHostState.recent_readable_returns?.[0];
  const selectedPackage = packages.find((item) => item.id === selectedPackageId) || packages[0] || packageStackSeed[0];
  const modalPackage = packages.find((item) => item.id === modal.packageId) || selectedPackage;

  useEffect(() => {
    if (typeof window === "undefined") return;
    window.localStorage.setItem(PACKAGE_STACK_STORAGE_KEY, JSON.stringify(packages));
  }, [packages]);

  useEffect(() => {
    if (typeof window === "undefined") return;
    window.localStorage.setItem(SELECTED_PACKAGE_STORAGE_KEY, selectedPackageId);
  }, [selectedPackageId]);

  function createPackage(title: string) {
    const cleaned = title.trim();
    if (!cleaned) return;
    const id = `pkg_${Date.now().toString(36)}`;
    const newPackage: PackageCard = {
      id,
      title: cleaned,
      status: "queued",
      stage: "purpose intake",
      executor: "codex-ready",
      summary: "신규 패키지. 중앙 setup에서 목적/렌즈/근거를 잡은 뒤 CLI 실행으로 보낼 수 있음",
    };
    setPackages((current) => [newPackage, ...current]);
    setSelectedPackageId(id);
  }

  function deletePackage(id: string) {
    setPackages((current) => {
      if (current.length <= 1) return current;
      const next = current.filter((item) => item.id !== id);
      if (selectedPackageId === id) setSelectedPackageId(next[0]?.id || packageStackSeed[0].id);
      return next;
    });
  }

  return (
    <div className="h-screen overflow-hidden bg-slate-950 text-slate-100">
      <div className="grid h-full grid-cols-1 lg:grid-cols-[280px_minmax(0,1fr)_360px]">
        <PackageStack
          packages={packages}
          selectedId={selectedPackageId}
          onSelect={setSelectedPackageId}
          onCreate={createPackage}
          onDelete={deletePackage}
          onOpenModal={(kind, id) => setModal({ kind, packageId: id })}
        />

        <main className="min-h-0 overflow-y-auto bg-slate-900 p-5">
          <div className="mx-auto max-w-5xl">
            <header className="mb-4 rounded-xl border border-white/10 bg-white/[0.04] p-4">
              <div className="flex flex-wrap items-start justify-between gap-3">
                <div>
                  <div className="text-[10px] font-black uppercase tracking-[0.22em] text-cyan-300">Active Package Workbench</div>
                  <div className="mt-1 text-[10px] font-bold uppercase tracking-[0.16em] text-slate-500">
                    terminal conversation mirror / runtime poll
                  </div>
                </div>
                <button
                  onClick={() => refreshDashboardState(false)}
                  className="rounded-lg border border-cyan-300/30 bg-cyan-300/10 px-3 py-2 text-[10px] font-black uppercase tracking-[0.14em] text-cyan-100"
                >
                  {dashboardRefresh.status === "refreshing" ? "refreshing" : "refresh now"}
                </button>
              </div>
              <h2 className="mt-2 text-2xl font-black tracking-tight">{selectedPackage.title}</h2>
              <p className="mt-2 max-w-3xl text-sm leading-6 text-slate-400">
                {selectedPackage.summary} 선택된 패키지 하나를 그릇으로 보고, 내부 라인/축 후보를 읽은 뒤 처리 결과를 재투입 가능한 재료로 다시 읽는다.
              </p>
              <div className="mt-3 rounded-lg border border-white/10 bg-slate-950 px-3 py-2 text-[10px] leading-4 text-slate-400">
                <span className="font-black uppercase tracking-[0.16em] text-cyan-300">live source</span>
                <span className="ml-2">
                  `/api/vectorfl-engine/state`를 5초마다 읽어 `runtime/cli_sessions`, package run events, latest return을 화면에 반영한다.
                </span>
                <span className="ml-2 text-slate-500">
                  status={dashboardRefresh.status}
                  {dashboardRefresh.lastUpdated ? ` · last=${dashboardRefresh.lastUpdated}` : ""}
                  {dashboardRefresh.error ? ` · error=${dashboardRefresh.error}` : ""}
                </span>
                <div className="mt-1 text-slate-500">
                  Shell auto-refreshes runtime state every 5s. Control panel refreshes on load/manual/action and owns run/mark controls.
                </div>
              </div>
              <div className="mt-3 grid gap-2 md:grid-cols-3">
                <SmallStat label="stage" value={selectedPackage.stage} />
                <SmallStat label="executor" value={selectedPackage.executor} />
                <SmallStat label="status" value={selectedPackage.status} active />
              </div>
            </header>

            <CliHostControlPanel
              activeSurface="vectorfl"
              onSurfaceChange={() => {}}
              onCliStateChange={setCliHostState}
              onPacketDraftChange={setWorkPacketDraft}
              externalFollowupTurn={externalFollowupTurn}
              activePackage={selectedPackage}
            />
          </div>
        </main>

        <EnginePositionSidebar
          latestTurn={latestTurn}
          workPacketDraft={workPacketDraft}
          onLoadLatest={() => setExternalFollowupTurn(latestTurn)}
        />
      </div>
      <PackageModal
        kind={modal.kind}
        pkg={modalPackage}
        latestTurn={latestTurn}
        workPacketDraft={workPacketDraft}
        onClose={() => setModal({ kind: null, packageId: "" })}
      />
    </div>
  );
}
