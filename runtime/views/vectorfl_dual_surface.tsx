import React, { useMemo, useState } from "react";
import { motion } from "framer-motion";
import {
  ArrowRight,
  Blocks,
  Bot,
  BrainCircuit,
  CheckCircle2,
  Command,
  FileSearch,
  Goal,
  Grip,
  Hammer,
  HeartPulse,
  LayoutDashboard,
  Link2,
  ListTree,
  MessageSquare,
  PauseCircle,
  PenSquare,
  Pencil,
  Play,
  Plus,
  Radar,
  RefreshCcw,
  Search,
  ShieldCheck,
  Sparkles,
  Ticket,
  Trash2,
  Users,
  Waypoints,
  Workflow,
  Code2,
  NotebookPen,
} from "lucide-react";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Badge } from "@/components/ui/badge";
import { Input } from "@/components/ui/input";
import { Textarea } from "@/components/ui/textarea";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle,
} from "@/components/ui/dialog";

type TeamStatus = "active" | "queued" | "waiting" | "idle";
type RoleStatus = "running" | "ready" | "waiting";
type UserGoalStatus = "draft" | "active" | "hold" | "closed";
type LineHealth = "strong" | "growing" | "thin";
type LineEventType = "born" | "strengthened" | "exported" | "refluxed";
type VectorLineStage = "ingress" | "processing" | "export" | "reflux" | "pending_validation";

type RoleKind =
  | "reference"
  | "structure"
  | "risk"
  | "search"
  | "synth"
  | "implement"
  | "validate"
  | "custom";

type TeamKind =
  | "internal"
  | "external"
  | "build"
  | "review"
  | "writing"
  | "shorts"
  | "custom";

type Role = {
  id: string;
  title: string;
  kind: RoleKind;
  purpose: string;
  goal: string;
  status: RoleStatus;
};

type Team = {
  id: string;
  name: string;
  kind: TeamKind;
  purpose: string;
  goal: string;
  status: TeamStatus;
  roles: Role[];
};

type Line = {
  id: string;
  name: string;
  purpose: string;
  health: LineHealth;
  anchors: string[];
  connectedTo: string[];
  weakPoints: string[];
  exportToUser: string[];
  refluxFromUser: string[];
  lineage: string[];
  notes: string[];
};

type LineEvent = {
  id: string;
  type: LineEventType;
  lineId: string;
  detail: string;
  time: string;
};

type TeamDraft = Team;
type RoleDraft = { teamId: string; role: Role };
type LineDraft = {
  id: string;
  name: string;
  purpose: string;
  health: LineHealth;
  anchorsText: string;
  weakPointsText: string;
  exportText: string;
  refluxText: string;
  notesText: string;
};

type UserGoalStateSlot = {
  goalId: string;
  title: string;
  purpose: string;
  scope: string;
  constraints: string[];
  expectedOutputs: string[];
  status: UserGoalStatus;
  linkedIngestIds: string[];
};

type VectorActiveLineSlot = {
  line: Line;
  currentStage: VectorLineStage;
  sourceRefs: string[];
};

const TEAM_KIND_OPTIONS: TeamKind[] = ["internal", "external", "build", "review", "writing", "shorts", "custom"];
const TEAM_STATUS_OPTIONS: TeamStatus[] = ["active", "queued", "waiting", "idle"];
const ROLE_KIND_OPTIONS: RoleKind[] = ["reference", "structure", "risk", "search", "synth", "implement", "validate", "custom"];
const ROLE_STATUS_OPTIONS: RoleStatus[] = ["running", "ready", "waiting"];
const LINE_HEALTH_OPTIONS: LineHealth[] = ["strong", "growing", "thin"];

const sidebarItems = [
  { label: "User Surface", value: "user", icon: LayoutDashboard },
  { label: "VectorFL Surface", value: "vectorfl", icon: Blocks },
  { label: "Engine Surface", value: "engine", icon: BrainCircuit },
] as const;

type SurfaceTab = (typeof sidebarItems)[number]["value"];

const teamKindMeta: Record<TeamKind, { label: string; icon: React.ComponentType<{ className?: string }> }> = {
  internal: { label: "내부 분석", icon: BrainCircuit },
  external: { label: "외부 서치", icon: Search },
  build: { label: "구현", icon: Code2 },
  review: { label: "검증", icon: ShieldCheck },
  writing: { label: "작문", icon: PenSquare },
  shorts: { label: "쇼츠", icon: Sparkles },
  custom: { label: "커스텀", icon: Bot },
};

const roleKindMeta: Record<RoleKind, { label: string; icon: React.ComponentType<{ className?: string }> }> = {
  reference: { label: "레퍼런스 탐색", icon: FileSearch },
  structure: { label: "구조 추출", icon: Grip },
  risk: { label: "리스크 판독", icon: Radar },
  search: { label: "외부 조사", icon: Search },
  synth: { label: "보강 정리", icon: Sparkles },
  implement: { label: "구현", icon: Hammer },
  validate: { label: "검토", icon: CheckCircle2 },
  custom: { label: "커스텀", icon: Bot },
};

const teamTemplates: Omit<Team, "id">[] = [
  {
    name: "내부 분석팀",
    kind: "internal",
    purpose: "내부 레퍼런스를 읽고 재사용 가능한 구조와 리스크를 라인으로 만든다",
    goal: "물류 시스템에 활용 가능한 내부 구조 후보를 확보한다",
    status: "active",
    roles: [
      {
        id: "role-seed-1",
        title: "레퍼런스 탐색 담당",
        kind: "reference",
        purpose: "관련 내부 자산과 참조 구조를 찾는다",
        goal: "탱크프로그램의 핵심 구조를 식별한다",
        status: "running",
      },
      {
        id: "role-seed-2",
        title: "구조 추출 담당",
        kind: "structure",
        purpose: "재사용 가능한 구조를 추출한다",
        goal: "구현팀에 넘길 수 있는 구조 후보를 만든다",
        status: "ready",
      },
    ],
  },
  {
    name: "외부 서치팀",
    kind: "external",
    purpose: "외부 정보로 부족 라인을 보강한다",
    goal: "공간 내부만으로 부족한 결핍을 채운다",
    status: "queued",
    roles: [
      {
        id: "role-seed-3",
        title: "외부 조사 담당",
        kind: "search",
        purpose: "도메인 외부 자료를 조사한다",
        goal: "부족 라인에 붙일 수 있는 근거를 찾는다",
        status: "waiting",
      },
    ],
  },
  {
    name: "구현팀",
    kind: "build",
    purpose: "전달된 라인과 구조 후보를 활용해 구현한다",
    goal: "실제 코드나 데이터 구조를 만든다",
    status: "waiting",
    roles: [
      {
        id: "role-seed-4",
        title: "구현 담당",
        kind: "implement",
        purpose: "입력 자산으로 기능을 구현한다",
        goal: "작동 가능한 첫 결과를 만든다",
        status: "waiting",
      },
    ],
  },
  {
    name: "검증팀",
    kind: "review",
    purpose: "구현 결과를 비교, 분석하고 공간 환류 준비를 한다",
    goal: "완료/보류와 함께 공간 자산화를 정리한다",
    status: "waiting",
    roles: [
      {
        id: "role-seed-5",
        title: "검토 담당",
        kind: "validate",
        purpose: "결과를 비교하고 검토한다",
        goal: "공간으로 환류할 가치와 보완 포인트를 판단한다",
        status: "waiting",
      },
    ],
  },
];

const initialLines: Line[] = [
  {
    id: "l-1",
    name: "탱크프로그램 구조 재사용 가능성 라인",
    purpose: "기존 탱크프로그램 내부 구조 중 물류 시스템으로 전용 가능한 연속 구조를 읽어내는 라인",
    health: "strong",
    anchors: ["tank_program_structure", "reference_module_map", "internal_usage_pattern"],
    connectedTo: ["물류 시스템 모듈 대응 가능성 라인", "구현팀 전달용 구조 요약 라인"],
    weakPoints: ["도메인 전환 시 네이밍 차이", "화면/업무 흐름 차이"],
    exportToUser: ["구조 후보 4개", "재사용 가능 모듈 후보"],
    refluxFromUser: ["구현 적용 결과", "전환 실패 사례"],
    lineage: ["request ingress", "reference scan", "structure extraction", "line strengthening", "user export"],
    notes: ["현재 가장 강한 출발 라인", "구현팀 전달 자산과 직접 연결됨"],
  },
  {
    id: "l-2",
    name: "물류 시스템 모듈 대응 가능성 라인",
    purpose: "탱크프로그램 구조를 물류 시스템의 목적과 모듈로 번역해 이어붙이는 해석 라인",
    health: "growing",
    anchors: ["logistics_requirements", "module_translation", "domain_mapping"],
    connectedTo: ["탱크프로그램 구조 재사용 가능성 라인", "외부 조사 필요 포인트 라인"],
    weakPoints: ["외부 표준 비교 부족", "업무 경계 미확정"],
    exportToUser: ["모듈 매핑 초안"],
    refluxFromUser: ["구현 중 수정된 모듈 경계"],
    lineage: ["request ingress", "domain mapping", "relation bridge", "partial export"],
    notes: ["내부 구조를 물류 도메인으로 번역하는 핵심 라인"],
  },
  {
    id: "l-3",
    name: "기존 구현 사용성 문제 예측 라인",
    purpose: "재사용 전에 발생할 가능성이 높은 구조적 문제와 사용성 저항을 먼저 읽는 라인",
    health: "growing",
    anchors: ["risk_hint", "ui_gap", "workflow_mismatch"],
    connectedTo: ["외부 조사 필요 포인트 라인"],
    weakPoints: ["정량 근거 부족"],
    exportToUser: ["리스크 2개"],
    refluxFromUser: ["실제 구현 막힘 로그"],
    lineage: ["risk reading", "line formation", "user export", "future reflux"],
    notes: ["구현 전에 미리 마찰을 보는 선행 경고 라인"],
  },
  {
    id: "l-4",
    name: "외부 조사 필요 포인트 라인",
    purpose: "공간 내부만으로는 부족한 지점을 외부 조사 주제로 드러내는 결핍 라인",
    health: "thin",
    anchors: ["gap_signal", "market_pattern", "external_spec"],
    connectedTo: ["물류 시스템 모듈 대응 가능성 라인", "기존 구현 사용성 문제 예측 라인"],
    weakPoints: ["외부 자료 미유입"],
    exportToUser: ["외부 조사 주제 4개"],
    refluxFromUser: ["외부 조사 결과"],
    lineage: ["gap detection", "external request", "waiting for reflux"],
    notes: ["얇지만 중요한 결핍 라인", "외부 서치팀과 직접 맞물림"],
  },
  {
    id: "l-5",
    name: "구현팀 전달용 구조 요약 라인",
    purpose: "구현팀이 바로 사용할 수 있게 구조 후보와 해석 결과를 조립해 넘기는 전달 라인",
    health: "strong",
    anchors: ["implementation_packet", "handoff_summary", "usable_structure"],
    connectedTo: ["탱크프로그램 구조 재사용 가능성 라인"],
    weakPoints: ["구현 후 피드백 미반영"],
    exportToUser: ["구현 입력 패킷"],
    refluxFromUser: ["구현 코드", "검증 메모"],
    lineage: ["packet build", "handoff", "implementation", "reflux"],
    notes: ["사용자면과 가장 직접적으로 맞닿는 라인"],
  },
];

const lineEvents: LineEvent[] = [
  { id: "e-1", type: "born", lineId: "l-1", detail: "탱크프로그램 구조 재사용 가능성 라인 생성", time: "09:41" },
  { id: "e-2", type: "strengthened", lineId: "l-1", detail: "유사 라인 탐색 후 strength 강화", time: "09:47" },
  { id: "e-3", type: "exported", lineId: "l-5", detail: "구현 입력 패킷 후보 사용자면 전달", time: "09:49" },
  { id: "e-4", type: "refluxed", lineId: "l-4", detail: "향후 외부 조사 결과 환류 대기 등록", time: "09:50" },
];

const userMaterialContextSeed = [
  {
    ingestId: "ingest-tank-ref-001",
    label: "탱크프로그램 레퍼런스",
    kind: "internal reference",
    status: "processing",
    summary: "물류 시스템 전용 가능성을 읽기 위한 1차 구조 재료",
  },
  {
    ingestId: "ingest-logistics-qmd-002",
    label: "물류 시스템 qmd 정리",
    kind: "space material",
    status: "queued",
    summary: "목적 선언과 내부팀 해석 범위를 묶는 보조 재료",
  },
];

const userSurfaceAttachmentNote = {
  mock: "runtime/views/vectorfl_dual_surface.tsx local mock state",
  actual: "future user surface injected state layer / viewer state user summary",
};

const vectorSurfaceAttachmentNote = {
  mock: "runtime/views/vectorfl_dual_surface.tsx lines + lineEvents local mock state",
  actual: "future VectorFlowState injected from integrated engine viewer state",
};

function createId(prefix: string) {
  return `${prefix}-${Math.random().toString(36).slice(2, 9)}`;
}

function toMultiline(values: string[]) {
  return values.join("\n");
}

function fromMultiline(value: string) {
  return value
    .split(/\n|,/)
    .map((item) => item.trim())
    .filter(Boolean);
}

function createTeamFromTemplate(template: Omit<Team, "id">, existing: Team[]): Team {
  return {
    ...template,
    id: createId("team"),
    name: `${template.name} ${existing.filter((team) => team.kind === template.kind).length + 1}`,
    roles: template.roles.map((role) => ({ ...role, id: createId("role") })),
  };
}

function createLineDraft(line: Line): LineDraft {
  return {
    id: line.id,
    name: line.name,
    purpose: line.purpose,
    health: line.health,
    anchorsText: toMultiline(line.anchors),
    weakPointsText: toMultiline(line.weakPoints),
    exportText: toMultiline(line.exportToUser),
    refluxText: toMultiline(line.refluxFromUser),
    notesText: toMultiline(line.notes),
  };
}

function applyLineDraft(line: Line, draft: LineDraft): Line {
  return {
    ...line,
    name: draft.name,
    purpose: draft.purpose,
    health: draft.health,
    anchors: fromMultiline(draft.anchorsText),
    weakPoints: fromMultiline(draft.weakPointsText),
    exportToUser: fromMultiline(draft.exportText),
    refluxFromUser: fromMultiline(draft.refluxText),
    notes: fromMultiline(draft.notesText),
  };
}

function buildTickets(teams: Team[]) {
  const buckets = {
    backlog: [] as Array<{ id: string; title: string; owner: string; meta: string }>,
    active: [] as Array<{ id: string; title: string; owner: string; meta: string }>,
    handoff: [] as Array<{ id: string; title: string; owner: string; meta: string }>,
    review: [] as Array<{ id: string; title: string; owner: string; meta: string }>,
  };

  teams.forEach((team) => {
    team.roles.forEach((role, index) => {
      const item = {
        id: `${team.id.slice(-4).toUpperCase()}-${index + 1}`,
        title: role.title,
        owner: team.name,
        meta: roleKindMeta[role.kind].label,
      };
      if (team.kind === "review") buckets.review.push(item);
      else if (role.status === "running") buckets.active.push(item);
      else if (role.status === "ready") buckets.handoff.push(item);
      else buckets.backlog.push(item);
    });
  });

  return buckets;
}

function buildTeamRelaySteps(teams: Team[]) {
  return teams.map((team, index) => {
    const primaryRole = team.roles[0];
    const nextTeam = teams[index + 1];
    return {
      id: `${team.id}-relay`,
      order: index + 1,
      team,
      primaryRole,
      input: index === 0 ? "연결 재료 + 현재 목적" : `${teams[index - 1]?.name ?? "이전 팀"} output`,
      work: primaryRole?.goal ?? team.goal,
      output: team.kind === "review" ? "accepted / hold / reflux note" : `${teamKindMeta[team.kind].label} output packet`,
      next: nextTeam ? `${nextTeam.name} handoff` : "엔진면 환류 후보",
    };
  });
}

function buildHandoffReports(teams: Team[]) {
  return teams.map((team, index) => {
    const role = team.roles[0];
    return {
      id: `${team.id}-handoff`,
      teamName: team.name,
      teamKind: team.kind,
      roleTitle: role?.title ?? "담당 미지정",
      roleKind: role?.kind ?? "custom",
      state: team.status === "active" ? "watching" : team.status === "queued" ? "waiting" : team.kind === "review" ? "hold" : "pending",
      waitingFor: team.status === "active" ? "현재 역할의 1차 보고" : index === 0 ? "목적 선언 확정" : `${teams[index - 1]?.name ?? "이전 팀"} output`,
      handoff: index < teams.length - 1 ? `${teams[index + 1]?.name}로 전달 준비` : "검증 환류를 엔진면으로 넘길 준비",
      userAttention: team.status === "active" ? "보고 도착 후 다음 팀에 넘길지 판단" : "아직 직접 실행하지 않고 대기",
    };
  });
}

function buildRelationBoard(lines: Line[]) {
  return lines.flatMap((line) => line.connectedTo.map((target) => ({ left: line.name, right: target }))).slice(0, 8);
}

function inferVectorLineStage(line: Line): VectorLineStage {
  if (line.lineage.some((step) => step.includes("waiting for reflux")) || line.refluxFromUser.length > 1) return "reflux";
  if (line.lineage.some((step) => step.includes("handoff") || step.includes("user export"))) return "export";
  if (line.health === "thin") return "pending_validation";
  if (line.lineage.some((step) => step.includes("request ingress"))) return "processing";
  return "ingress";
}

function buildVectorActiveLines(lines: Line[]): VectorActiveLineSlot[] {
  return lines.map((line) => ({
    line,
    currentStage: inferVectorLineStage(line),
    sourceRefs: line.anchors.slice(0, 3),
  }));
}

function buildGapField(lines: Line[]) {
  return lines.flatMap((line) =>
    line.weakPoints.map((point, index) => ({
      id: `${line.id}-gap-${index}`,
      title: point,
      why: line.health === "thin" ? "현재 연결이 얇아 보강 또는 검증 대기가 필요함" : "연결은 있으나 다음 처리 전 확인할 약점",
      linkedLineIds: [line.id, ...line.connectedTo.slice(0, 2)],
    }))
  );
}

function vectorStageLabel(stage: VectorLineStage) {
  return (
    {
      ingress: "ingress",
      processing: "processing",
      export: "export",
      reflux: "reflux",
      pending_validation: "pending validation",
    }[stage] || stage
  );
}

function buildVectorSurfaceSummary(lines: Line[]) {
  const strongest = lines.find((line) => line.health === "strong")?.name ?? "없음";
  const weakest = lines.find((line) => line.health === "thin")?.name ?? "없음";
  const gaps = buildGapField(lines);
  return {
    strongest,
    weakest,
    currentFocus: lines[0]?.name ?? "없음",
    nextIntervention: "결핍 라인 보강 + 구현 환류 연결",
    gapCount: gaps.length,
    bridgeCount: buildRelationBoard(lines).length,
  };
}

function statusClass(status: string) {
  return (
    {
      active: "bg-emerald-100 text-emerald-700",
      queued: "bg-amber-100 text-amber-700",
      processing: "bg-sky-100 text-sky-700",
      ingress: "bg-sky-100 text-sky-700",
      export: "bg-amber-100 text-amber-700",
      reflux: "bg-violet-100 text-violet-700",
      pending_validation: "bg-rose-100 text-rose-700",
      waiting: "bg-slate-100 text-slate-700",
      idle: "bg-slate-100 text-slate-600",
      draft: "bg-slate-100 text-slate-700",
      hold: "bg-amber-100 text-amber-700",
      closed: "bg-slate-900 text-white",
      running: "bg-emerald-100 text-emerald-700",
      ready: "bg-sky-100 text-sky-700",
      strong: "bg-emerald-100 text-emerald-700",
      growing: "bg-amber-100 text-amber-700",
      thin: "bg-rose-100 text-rose-700",
    }[status] || "bg-slate-100 text-slate-700"
  );
}

function statusLabel(status: string) {
  return (
    {
      active: "활성",
      queued: "대기",
      processing: "처리 중",
      ingress: "유입",
      export: "수출",
      reflux: "환류",
      pending_validation: "검증 대기",
      waiting: "입력 대기",
      idle: "idle",
      draft: "초안",
      hold: "보류",
      closed: "종료",
      running: "진행 중",
      ready: "준비",
      strong: "강함",
      growing: "자라는 중",
      thin: "얇음",
    }[status] || status
  );
}

function eventMeta(type: LineEventType) {
  return {
    born: { label: "born", icon: Plus, cls: "bg-sky-100 text-sky-700" },
    strengthened: { label: "strengthened", icon: Sparkles, cls: "bg-emerald-100 text-emerald-700" },
    exported: { label: "exported", icon: ArrowRight, cls: "bg-amber-100 text-amber-700" },
    refluxed: { label: "refluxed", icon: RefreshCcw, cls: "bg-violet-100 text-violet-700" },
  }[type];
}

function DarkMetric({ label, value, note }: { label: string; value: string; note: string }) {
  return (
    <div className="rounded-2xl border border-white/10 bg-white/5 p-4 backdrop-blur-sm">
      <div className="text-[11px] uppercase tracking-[0.18em] text-slate-400">{label}</div>
      <div className="mt-2 text-2xl font-semibold tracking-tight text-white">{value}</div>
      <div className="mt-1 text-sm text-slate-400">{note}</div>
    </div>
  );
}

function LightMetric({ label, value, note }: { label: string; value: string; note: string }) {
  return (
    <div className="rounded-2xl border border-slate-200 bg-white p-4">
      <div className="text-[11px] uppercase tracking-[0.18em] text-slate-500">{label}</div>
      <div className="mt-2 text-2xl font-semibold tracking-tight text-slate-900">{value}</div>
      <div className="mt-1 text-sm text-slate-600">{note}</div>
    </div>
  );
}

function TeamIcon({ kind, className = "h-4 w-4" }: { kind: TeamKind; className?: string }) {
  const Icon = teamKindMeta[kind].icon;
  return <Icon className={className} />;
}

function RoleIcon({ kind, className = "h-4 w-4" }: { kind: RoleKind; className?: string }) {
  const Icon = roleKindMeta[kind].icon;
  return <Icon className={className} />;
}

function TicketColumn({ title, items }: { title: string; items: Array<{ id: string; title: string; owner: string; meta: string }> }) {
  return (
    <div className="rounded-3xl bg-slate-50 p-3">
      <div className="mb-3 flex items-center justify-between">
        <div className="text-sm font-medium">{title}</div>
        <Badge variant="outline" className="rounded-full">{items.length}</Badge>
      </div>
      <div className="space-y-3">
        {items.map((ticket) => (
          <div key={ticket.id} className="rounded-2xl border border-slate-200 bg-white p-3 shadow-sm">
            <div className="text-[11px] uppercase tracking-[0.18em] text-slate-500">{ticket.id}</div>
            <div className="mt-1 text-sm font-medium">{ticket.title}</div>
            <div className="mt-2 text-xs text-slate-500">{ticket.owner}</div>
            <div className="mt-2 text-xs text-slate-600">{ticket.meta}</div>
          </div>
        ))}
      </div>
    </div>
  );
}

function TeamEditModal({ open, onOpenChange, draft, onChange, onSave }: {
  open: boolean;
  onOpenChange: (open: boolean) => void;
  draft: TeamDraft | null;
  onChange: (draft: TeamDraft) => void;
  onSave: () => void;
}) {
  return (
    <Dialog open={open} onOpenChange={onOpenChange}>
      <DialogContent className="max-w-2xl">
        <DialogHeader>
          <DialogTitle>팀 수정</DialogTitle>
          <DialogDescription>팀의 이름, 종류, 목적, 목표, 상태를 수정합니다.</DialogDescription>
        </DialogHeader>
        {draft && (
          <div className="grid gap-4 py-2">
            <div className="grid gap-2 sm:grid-cols-2">
              <div className="grid gap-2">
                <label className="text-sm font-medium">팀 이름</label>
                <Input value={draft.name} onChange={(e) => onChange({ ...draft, name: e.target.value })} />
              </div>
              <div className="grid gap-2">
                <label className="text-sm font-medium">팀 종류</label>
                <select className="h-10 rounded-md border border-slate-200 bg-white px-3 text-sm" value={draft.kind} onChange={(e) => onChange({ ...draft, kind: e.target.value as TeamKind })}>
                  {TEAM_KIND_OPTIONS.map((option) => <option key={option} value={option}>{teamKindMeta[option].label}</option>)}
                </select>
              </div>
            </div>
            <div className="grid gap-2">
              <label className="text-sm font-medium">팀 목적</label>
              <Textarea rows={3} value={draft.purpose} onChange={(e) => onChange({ ...draft, purpose: e.target.value })} />
            </div>
            <div className="grid gap-2">
              <label className="text-sm font-medium">팀 목표</label>
              <Textarea rows={3} value={draft.goal} onChange={(e) => onChange({ ...draft, goal: e.target.value })} />
            </div>
            <div className="grid gap-2">
              <label className="text-sm font-medium">팀 상태</label>
              <select className="h-10 rounded-md border border-slate-200 bg-white px-3 text-sm" value={draft.status} onChange={(e) => onChange({ ...draft, status: e.target.value as TeamStatus })}>
                {TEAM_STATUS_OPTIONS.map((option) => <option key={option} value={option}>{statusLabel(option)}</option>)}
              </select>
            </div>
          </div>
        )}
        <DialogFooter>
          <Button variant="outline" onClick={() => onOpenChange(false)}>닫기</Button>
          <Button onClick={onSave}>저장</Button>
        </DialogFooter>
      </DialogContent>
    </Dialog>
  );
}

function RoleEditModal({ open, onOpenChange, draft, onChange, onSave }: {
  open: boolean;
  onOpenChange: (open: boolean) => void;
  draft: RoleDraft | null;
  onChange: (draft: RoleDraft) => void;
  onSave: () => void;
}) {
  return (
    <Dialog open={open} onOpenChange={onOpenChange}>
      <DialogContent className="max-w-2xl">
        <DialogHeader>
          <DialogTitle>담당 수정</DialogTitle>
          <DialogDescription>담당의 역할, 목적, 목표를 수정하며 운용 흐름에 맞게 계속 조정합니다.</DialogDescription>
        </DialogHeader>
        {draft && (
          <div className="grid gap-4 py-2">
            <div className="grid gap-2 sm:grid-cols-2">
              <div className="grid gap-2">
                <label className="text-sm font-medium">담당 이름</label>
                <Input value={draft.role.title} onChange={(e) => onChange({ ...draft, role: { ...draft.role, title: e.target.value } })} />
              </div>
              <div className="grid gap-2">
                <label className="text-sm font-medium">역할 종류</label>
                <select className="h-10 rounded-md border border-slate-200 bg-white px-3 text-sm" value={draft.role.kind} onChange={(e) => onChange({ ...draft, role: { ...draft.role, kind: e.target.value as RoleKind } })}>
                  {ROLE_KIND_OPTIONS.map((option) => <option key={option} value={option}>{roleKindMeta[option].label}</option>)}
                </select>
              </div>
            </div>
            <div className="grid gap-2">
              <label className="text-sm font-medium">담당 목적</label>
              <Textarea rows={3} value={draft.role.purpose} onChange={(e) => onChange({ ...draft, role: { ...draft.role, purpose: e.target.value } })} />
            </div>
            <div className="grid gap-2">
              <label className="text-sm font-medium">담당 목표</label>
              <Textarea rows={3} value={draft.role.goal} onChange={(e) => onChange({ ...draft, role: { ...draft.role, goal: e.target.value } })} />
            </div>
            <div className="grid gap-2">
              <label className="text-sm font-medium">담당 상태</label>
              <select className="h-10 rounded-md border border-slate-200 bg-white px-3 text-sm" value={draft.role.status} onChange={(e) => onChange({ ...draft, role: { ...draft.role, status: e.target.value as RoleStatus } })}>
                {ROLE_STATUS_OPTIONS.map((option) => <option key={option} value={option}>{statusLabel(option)}</option>)}
              </select>
            </div>
          </div>
        )}
        <DialogFooter>
          <Button variant="outline" onClick={() => onOpenChange(false)}>닫기</Button>
          <Button onClick={onSave}>저장</Button>
        </DialogFooter>
      </DialogContent>
    </Dialog>
  );
}

function LineEditModal({ open, onOpenChange, draft, onChange, onSave }: {
  open: boolean;
  onOpenChange: (open: boolean) => void;
  draft: LineDraft | null;
  onChange: (draft: LineDraft) => void;
  onSave: () => void;
}) {
  return (
    <Dialog open={open} onOpenChange={onOpenChange}>
      <DialogContent className="max-w-3xl">
        <DialogHeader>
          <DialogTitle>라인 수정 / 주석 부착</DialogTitle>
          <DialogDescription>선택한 라인의 의미, 상태, 앵커, 약점, 수출/환류, 메모를 수정합니다.</DialogDescription>
        </DialogHeader>
        {draft && (
          <div className="grid gap-4 py-2">
            <div className="grid gap-2 sm:grid-cols-[1fr_180px]">
              <div className="grid gap-2">
                <label className="text-sm font-medium">라인 이름</label>
                <Input value={draft.name} onChange={(e) => onChange({ ...draft, name: e.target.value })} />
              </div>
              <div className="grid gap-2">
                <label className="text-sm font-medium">라인 상태</label>
                <select className="h-10 rounded-md border border-slate-200 bg-white px-3 text-sm" value={draft.health} onChange={(e) => onChange({ ...draft, health: e.target.value as LineHealth })}>
                  {LINE_HEALTH_OPTIONS.map((option) => <option key={option} value={option}>{statusLabel(option)}</option>)}
                </select>
              </div>
            </div>
            <div className="grid gap-2">
              <label className="text-sm font-medium">라인 목적</label>
              <Textarea rows={3} value={draft.purpose} onChange={(e) => onChange({ ...draft, purpose: e.target.value })} />
            </div>
            <div className="grid gap-4 sm:grid-cols-2">
              <div className="grid gap-2">
                <label className="text-sm font-medium">앵커 목록</label>
                <Textarea rows={5} value={draft.anchorsText} onChange={(e) => onChange({ ...draft, anchorsText: e.target.value })} />
              </div>
              <div className="grid gap-2">
                <label className="text-sm font-medium">약점 목록</label>
                <Textarea rows={5} value={draft.weakPointsText} onChange={(e) => onChange({ ...draft, weakPointsText: e.target.value })} />
              </div>
            </div>
            <div className="grid gap-4 sm:grid-cols-2">
              <div className="grid gap-2">
                <label className="text-sm font-medium">사용자면 수출 항목</label>
                <Textarea rows={4} value={draft.exportText} onChange={(e) => onChange({ ...draft, exportText: e.target.value })} />
              </div>
              <div className="grid gap-2">
                <label className="text-sm font-medium">예상 환류 항목</label>
                <Textarea rows={4} value={draft.refluxText} onChange={(e) => onChange({ ...draft, refluxText: e.target.value })} />
              </div>
            </div>
            <div className="grid gap-2">
              <label className="text-sm font-medium">라인 메모 / 판단 주석</label>
              <Textarea rows={4} value={draft.notesText} onChange={(e) => onChange({ ...draft, notesText: e.target.value })} />
            </div>
          </div>
        )}
        <DialogFooter>
          <Button variant="outline" onClick={() => onOpenChange(false)}>닫기</Button>
          <Button onClick={onSave}>저장</Button>
        </DialogFooter>
      </DialogContent>
    </Dialog>
  );
}

export default function VectorFLSurfacesMock() {
  const [activeSurface, setActiveSurface] = useState<SurfaceTab>("user");
  const [goal, setGoal] = useState("레퍼런스에 존재하는 탱크프로그램을 활용/참조해 물류 시스템 프로그램을 만들려고 한다");
  const [teams, setTeams] = useState<Team[]>(() => {
    const built: Team[] = [];
    teamTemplates.forEach((template) => built.push(createTeamFromTemplate(template, built)));
    return built;
  });
  const [selectedTeamId, setSelectedTeamId] = useState<string | null>(null);
  const [lines, setLines] = useState<Line[]>(initialLines);
  const [selectedLineId, setSelectedLineId] = useState<string>(initialLines[0].id);
  const [teamDraft, setTeamDraft] = useState<TeamDraft | null>(null);
  const [roleDraft, setRoleDraft] = useState<RoleDraft | null>(null);
  const [lineDraft, setLineDraft] = useState<LineDraft | null>(null);

  const selectedTeam = useMemo(() => teams.find((team) => team.id === selectedTeamId) ?? teams[0] ?? null, [teams, selectedTeamId]);
  const selectedLine = useMemo(() => lines.find((line) => line.id === selectedLineId) ?? lines[0], [lines, selectedLineId]);

  const tickets = useMemo(() => buildTickets(teams), [teams]);
  const relationBoard = useMemo(() => buildRelationBoard(lines), [lines]);
  const vectorActiveLines = useMemo(() => buildVectorActiveLines(lines), [lines]);
  const vectorGaps = useMemo(() => buildGapField(lines), [lines]);
  const vectorSummary = useMemo(() => buildVectorSurfaceSummary(lines), [lines]);
  const userGoalState: UserGoalStateSlot = useMemo(() => ({
    goalId: "goal-user-surface-001",
    title: goal,
    purpose: "외부/내부 재료를 바탕으로 물류 시스템 변주 가능성을 팀 흐름으로 조직한다",
    scope: "이번 턴은 목적 선언, 연결 재료, 팀 relay, handoff 대기 상태를 화면 슬롯으로 잠그는 단계",
    constraints: ["CLI 자동 운영 없음", "사용자면에서 엔진 직접 조작 없음", "contract는 final schema가 아님"],
    expectedOutputs: ["팀별 relay 판단", "구현팀 전달 후보", "검증 환류 후보"],
    status: "active",
    linkedIngestIds: userMaterialContextSeed.map((item) => item.ingestId),
  }), [goal]);
  const teamRelaySteps = useMemo(() => buildTeamRelaySteps(teams), [teams]);
  const handoffReports = useMemo(() => buildHandoffReports(teams), [teams]);

  const addTeam = () => {
    const template = teamTemplates[teams.length % teamTemplates.length];
    const nextTeam = createTeamFromTemplate(template, teams);
    setTeams((prev) => [...prev, nextTeam]);
    setSelectedTeamId(nextTeam.id);
  };

  const removeSelectedTeam = () => {
    if (!selectedTeam) return;
    const next = teams.filter((team) => team.id !== selectedTeam.id);
    setTeams(next);
    setSelectedTeamId(next[0]?.id ?? null);
  };

  const addRole = () => {
    if (!selectedTeam) return;
    const nextRole: Role = {
      id: createId("role"),
      title: `추가 담당 ${selectedTeam.roles.length + 1}`,
      kind: "custom",
      purpose: "필요에 따라 사용자 정의 역할을 수행한다",
      goal: "팀 흐름에서 비어 있는 부분을 메운다",
      status: "ready",
    };
    setTeams((prev) => prev.map((team) => (team.id === selectedTeam.id ? { ...team, roles: [...team.roles, nextRole] } : team)));
  };

  const removeRole = () => {
    if (!selectedTeam || selectedTeam.roles.length === 0) return;
    setTeams((prev) => prev.map((team) => (team.id === selectedTeam.id ? { ...team, roles: team.roles.slice(0, -1) } : team)));
  };

  const saveTeamDraft = () => {
    if (!teamDraft) return;
    setTeams((prev) => prev.map((team) => (team.id === teamDraft.id ? teamDraft : team)));
    setTeamDraft(null);
  };

  const saveRoleDraft = () => {
    if (!roleDraft) return;
    setTeams((prev) => prev.map((team) => (team.id === roleDraft.teamId ? { ...team, roles: team.roles.map((role) => (role.id === roleDraft.role.id ? roleDraft.role : role)) } : team)));
    setRoleDraft(null);
  };

  const saveLineDraft = () => {
    if (!lineDraft) return;
    setLines((prev) => prev.map((line) => (line.id === lineDraft.id ? applyLineDraft(line, lineDraft) : line)));
    setLineDraft(null);
  };

  return (
    <div className="min-h-screen bg-slate-950 text-slate-100">
      <div className="grid min-h-screen lg:grid-cols-[250px_1fr]">
        <aside className="border-r border-white/10 bg-slate-950/95 p-5">
          <div className="flex items-center gap-3">
            <div className="rounded-2xl bg-white/10 p-2"><Command className="h-5 w-5" /></div>
            <div>
              <div className="text-sm font-semibold tracking-wide">VECTORFL / SURFACES</div>
              <div className="text-xs text-slate-400">user / vectorfl / engine</div>
            </div>
          </div>

          <div className="mt-6 rounded-2xl border border-white/10 bg-white/5 p-4">
            <div className="text-[11px] uppercase tracking-[0.18em] text-slate-400">locked flow</div>
            <div className="mt-2 text-sm font-medium">mock first → engine later</div>
            <div className="mt-1 text-xs text-slate-400">사용자면 / 벡터플면 1차 완성 후 엔진면 정리</div>
          </div>

          <div className="mt-6 space-y-1">
            {sidebarItems.map((item) => {
              const Icon = item.icon;
              return (
                <button
                  key={item.label}
                  onClick={() => setActiveSurface(item.value)}
                  className={`flex w-full items-center gap-3 rounded-xl px-3 py-2 text-sm transition hover:bg-white/5 hover:text-white ${
                    activeSurface === item.value ? "border border-white/10 bg-white/10 text-white" : "text-slate-300"
                  }`}
                >
                  <Icon className="h-4 w-4" />
                  <span>{item.label}</span>
                </button>
              );
            })}
          </div>

          <div className="mt-6 rounded-2xl border border-emerald-500/20 bg-emerald-500/10 p-4">
            <div className="flex items-center gap-2 text-sm font-medium text-emerald-300"><HeartPulse className="h-4 w-4" />Surface split active</div>
            <div className="mt-2 text-xs leading-6 text-emerald-100/80">사용자면은 지시, 벡터플면은 표면 관찰, 엔진면은 이후 정비/제어로 분리됩니다.</div>
          </div>
        </aside>

        <main className="p-5 lg:p-7">
          <motion.div initial={{ opacity: 0, y: 8 }} animate={{ opacity: 1, y: 0 }} className="space-y-6">
            <div>
              <div className="flex flex-wrap items-center gap-2">
                <Badge className="rounded-full bg-white text-slate-950 hover:bg-white">surfaces mock</Badge>
                <Badge variant="outline" className="rounded-full border-white/20 text-slate-300">user surface / vectorfl surface / engine later</Badge>
              </div>
              <h1 className="mt-3 text-3xl font-semibold tracking-tight text-white">사용자면과 벡터플면을 다시 분리한 1차 mock</h1>
              <p className="mt-2 max-w-3xl text-sm leading-7 text-slate-400">지금 단계에서는 사용자면과 벡터플면만 다시 선명하게 잡고, 엔진면은 후속 단계에서 별도로 정리하는 흐름입니다.</p>
            </div>

            <Tabs value={activeSurface} onValueChange={(value) => setActiveSurface(value as SurfaceTab)} className="w-full">
              <TabsList className="grid h-auto w-full max-w-md grid-cols-3 rounded-2xl bg-white/5 p-1">
                <TabsTrigger value="user" className="rounded-xl py-3 data-[state=active]:bg-white data-[state=active]:text-slate-950">사용자면</TabsTrigger>
                <TabsTrigger value="vectorfl" className="rounded-xl py-3 data-[state=active]:bg-white data-[state=active]:text-slate-950">벡터플면</TabsTrigger>
                <TabsTrigger value="engine" className="rounded-xl py-3 data-[state=active]:bg-white data-[state=active]:text-slate-950">엔진면 연결</TabsTrigger>
              </TabsList>

              <TabsContent value="user" className="mt-6 space-y-6">
                <section className="rounded-[28px] border border-white/10 bg-gradient-to-br from-slate-900 to-slate-950 p-5 shadow-2xl shadow-black/20">
                  <div className="flex flex-wrap items-start justify-between gap-4">
                    <div className="flex items-center gap-3">
                      <div className="rounded-2xl bg-white/10 p-2"><Goal className="h-5 w-5" /></div>
                      <div>
                        <div className="text-sm font-medium text-white">Goal Declaration</div>
                        <div className="text-xs text-slate-400">UserGoalState slot · 목적 선언이 팀보다 먼저 읽히는 운영 선언 영역</div>
                      </div>
                    </div>
                    <span className={`rounded-full px-3 py-1 text-xs font-medium ${statusClass(userGoalState.status)}`}>{statusLabel(userGoalState.status)}</span>
                  </div>
                  <div className="mt-4 grid gap-4 xl:grid-cols-[1.15fr_0.85fr]">
                    <div className="space-y-3">
                      <Input value={goal} onChange={(e) => setGoal(e.target.value)} className="h-12 rounded-2xl border-white/10 bg-white/5 text-white placeholder:text-slate-500" />
                      <div className="grid gap-3 sm:grid-cols-2 xl:grid-cols-4">
                        <DarkMetric label="goal id" value={userGoalState.goalId} note="현재 목적 선언 후보 id" />
                        <DarkMetric label="status" value={statusLabel(userGoalState.status)} note="draft / active / hold / closed" />
                        <DarkMetric label="linked ingest" value={String(userGoalState.linkedIngestIds.length)} note="현재 목적과 연결된 재료 수" />
                        <DarkMetric label="surface mode" value="user" note="목적 선언 + 팀 운영 표면" />
                      </div>
                    </div>
                    <div className="grid gap-3 sm:grid-cols-2 xl:grid-cols-2">
                      <div className="rounded-2xl border border-white/10 bg-white/5 p-4 text-white">
                        <div className="text-[11px] uppercase tracking-[0.18em] text-slate-400">purpose</div>
                        <div className="mt-2 text-sm">{userGoalState.purpose}</div>
                      </div>
                      <div className="rounded-2xl border border-white/10 bg-white/5 p-4 text-white">
                        <div className="text-[11px] uppercase tracking-[0.18em] text-slate-400">scope</div>
                        <div className="mt-2 text-sm">{userGoalState.scope}</div>
                      </div>
                      <div className="rounded-2xl border border-white/10 bg-white/5 p-4 text-white">
                        <div className="text-[11px] uppercase tracking-[0.18em] text-slate-400">constraints</div>
                        <div className="mt-2 space-y-1 text-sm">{userGoalState.constraints.map((item) => <div key={item}>- {item}</div>)}</div>
                      </div>
                      <div className="rounded-2xl border border-white/10 bg-white/5 p-4 text-white">
                        <div className="text-[11px] uppercase tracking-[0.18em] text-slate-400">expected outputs</div>
                        <div className="mt-2 space-y-1 text-sm">{userGoalState.expectedOutputs.map((item) => <div key={item}>- {item}</div>)}</div>
                      </div>
                    </div>
                  </div>
                  <div className="mt-4 rounded-2xl border border-white/10 bg-white/5 p-4 text-xs leading-6 text-slate-300">
                    mock attachment: {userSurfaceAttachmentNote.mock}<br />
                    actual attachment candidate: {userSurfaceAttachmentNote.actual}
                  </div>
                </section>

                <section className="rounded-[28px] border border-white/10 bg-slate-900 p-5 shadow-2xl shadow-black/20">
                  <div className="flex items-center gap-3">
                    <div className="rounded-2xl bg-white/10 p-2"><Link2 className="h-5 w-5" /></div>
                    <div>
                      <div className="text-sm font-medium text-white">Material Context</div>
                      <div className="text-xs text-slate-400">UserGoalState summary · 목적이 어떤 ingest / 공간 재료 위에 있는지 먼저 보여주는 영역</div>
                    </div>
                  </div>
                  <div className="mt-4 grid gap-3 lg:grid-cols-2">
                    {userMaterialContextSeed.map((material) => (
                      <div key={material.ingestId} className="rounded-2xl border border-white/10 bg-white/5 p-4 text-white">
                        <div className="flex items-start justify-between gap-3">
                          <div>
                            <div className="text-[11px] uppercase tracking-[0.18em] text-slate-400">{material.ingestId}</div>
                            <div className="mt-2 font-medium">{material.label}</div>
                            <div className="mt-1 text-xs text-slate-400">{material.kind}</div>
                          </div>
                          <span className={`rounded-full px-3 py-1 text-xs font-medium ${statusClass(material.status)}`}>{statusLabel(material.status)}</span>
                        </div>
                        <div className="mt-3 text-sm leading-6 text-slate-300">{material.summary}</div>
                      </div>
                    ))}
                  </div>
                  <div className="mt-4 text-xs text-slate-400">linked_ingest_ids: {userGoalState.linkedIngestIds.join(", ")}</div>
                </section>

                <div className="grid gap-6 xl:grid-cols-[0.85fr_1.15fr]">
                  <Card className="rounded-[28px] border-slate-200 bg-white text-slate-900 shadow-xl shadow-black/10">
                    <CardHeader>
                        <div className="flex items-center justify-between gap-3">
                          <div className="flex items-center gap-3">
                            <div className="rounded-2xl bg-slate-900 p-2 text-white"><Users className="h-5 w-5" /></div>
                            <div>
                              <CardTitle className="text-xl">Team Relay Board</CardTitle>
                              <CardDescription>TeamFlowState.teams slot · 내부팀 → 외부서치팀 → 구현팀 → 검증팀 relay 흐름</CardDescription>
                            </div>
                          </div>
                        <div className="flex gap-2">
                          <Button size="sm" onClick={addTeam} className="rounded-xl"><Plus className="mr-2 h-4 w-4" />팀 추가</Button>
                          <Button size="sm" variant="outline" onClick={removeSelectedTeam} className="rounded-xl"><Trash2 className="mr-2 h-4 w-4" />삭제</Button>
                        </div>
                      </div>
                    </CardHeader>
                    <CardContent className="space-y-3">
                      {teamRelaySteps.map(({ team, primaryRole, input, work, output, next, order }) => (
                        <button key={team.id} onClick={() => setSelectedTeamId(team.id)} className={`w-full rounded-2xl border px-4 py-3 text-left transition ${selectedTeam?.id === team.id ? "border-slate-900 bg-slate-50" : "border-slate-200 bg-white hover:border-slate-300"}`}>
                          <div className="flex items-start justify-between gap-3">
                            <div className="flex items-start gap-3">
                              <div className="rounded-xl bg-slate-100 p-2"><TeamIcon kind={team.kind} /></div>
                              <div>
                                <div className="text-[11px] uppercase tracking-[0.18em] text-slate-500">relay {order}</div>
                                <div className="mt-1 font-medium">{team.name}</div>
                                <div className="mt-1 text-sm text-slate-600">{teamKindMeta[team.kind].label} · {primaryRole?.title ?? "담당 미지정"} · roles {team.roles.length}</div>
                              </div>
                            </div>
                            <span className={`rounded-full px-3 py-1 text-xs font-medium ${statusClass(team.status)}`}>{statusLabel(team.status)}</span>
                          </div>
                          <div className="mt-3 grid gap-2 text-xs text-slate-600">
                            <div><span className="font-medium text-slate-900">input</span> · {input}</div>
                            <div><span className="font-medium text-slate-900">work</span> · {work}</div>
                            <div><span className="font-medium text-slate-900">output</span> · {output}</div>
                            <div className="flex items-center gap-2 text-slate-500"><ArrowRight className="h-3.5 w-3.5" />{next}</div>
                          </div>
                        </button>
                      ))}
                    </CardContent>
                  </Card>

                  <div className="space-y-6">
                    <Card className="rounded-[28px] border-slate-200 bg-white text-slate-900 shadow-xl shadow-black/10">
                      <CardHeader>
                        <div className="flex items-center justify-between gap-3">
                          <div className="flex items-center gap-3">
                            <div className="rounded-2xl bg-slate-900 p-2 text-white"><Workflow className="h-5 w-5" /></div>
                            <div>
                              <CardTitle className="text-xl">Selected Relay Team Console</CardTitle>
                              <CardDescription>선택된 relay team의 role / instruction / status를 조정합니다</CardDescription>
                            </div>
                          </div>
                          <div className="flex gap-2">
                            <Button size="sm" variant="outline" onClick={() => selectedTeam && setTeamDraft({ ...selectedTeam })} className="rounded-xl"><Pencil className="mr-2 h-4 w-4" />팀 수정</Button>
                            <Button size="sm" onClick={addRole} className="rounded-xl"><Plus className="mr-2 h-4 w-4" />담당 추가</Button>
                            <Button size="sm" variant="outline" onClick={removeRole} className="rounded-xl"><Trash2 className="mr-2 h-4 w-4" />담당 삭제</Button>
                          </div>
                        </div>
                      </CardHeader>
                      <CardContent>
                        {selectedTeam ? (
                          <div className="space-y-4">
                            <div className="rounded-2xl bg-slate-50 p-4">
                              <div className="flex items-center gap-3">
                                <div className="rounded-xl bg-slate-900 p-2 text-white"><TeamIcon kind={selectedTeam.kind} /></div>
                                <div>
                                  <div className="font-medium">{selectedTeam.name}</div>
                                  <div className="text-sm text-slate-600">{selectedTeam.purpose}</div>
                                  <div className="mt-1 text-xs text-slate-500">goal: {selectedTeam.goal}</div>
                                </div>
                              </div>
                            </div>
                            <div className="grid gap-3 sm:grid-cols-2">
                              {selectedTeam.roles.map((role) => (
                                <button key={role.id} onClick={() => setRoleDraft({ teamId: selectedTeam.id, role: { ...role } })} className="rounded-2xl border border-slate-200 bg-white p-4 text-left shadow-sm transition hover:border-slate-400">
                                  <div className="flex items-start justify-between gap-3">
                                    <div className="flex items-start gap-3">
                                      <div className="rounded-xl bg-slate-100 p-2"><RoleIcon kind={role.kind} /></div>
                                      <div>
                                        <div className="font-medium">{role.title}</div>
                                        <div className="mt-1 text-sm text-slate-600">{roleKindMeta[role.kind].label}</div>
                                      </div>
                                    </div>
                                    <span className={`rounded-full px-3 py-1 text-xs font-medium ${statusClass(role.status)}`}>{statusLabel(role.status)}</span>
                                  </div>
                                  <div className="mt-3 text-sm text-slate-600 line-clamp-2">{role.goal}</div>
                                </button>
                              ))}
                            </div>
                          </div>
                        ) : (
                          <div className="rounded-2xl border border-dashed border-slate-300 p-6 text-sm text-slate-500">팀을 먼저 선택하세요.</div>
                        )}
                      </CardContent>
                    </Card>

                    <div className="grid gap-6 lg:grid-cols-[1.05fr_0.95fr]">
                      <Card className="rounded-[28px] border-slate-200 bg-white text-slate-900 shadow-xl shadow-black/10">
                        <CardHeader>
                          <div className="flex items-center gap-3">
                            <div className="rounded-2xl bg-slate-900 p-2 text-white"><Ticket className="h-5 w-5" /></div>
                            <div>
                              <CardTitle className="text-xl">Handoff / Waiting Board</CardTitle>
                              <CardDescription>TeamFlowState summary slot · backlog / active / handoff / review 상태 관찰층</CardDescription>
                            </div>
                          </div>
                        </CardHeader>
                        <CardContent>
                          <div className="grid gap-4 xl:grid-cols-4">
                            <TicketColumn title="Backlog" items={tickets.backlog} />
                            <TicketColumn title="Active" items={tickets.active} />
                            <TicketColumn title="Handoff" items={tickets.handoff} />
                            <TicketColumn title="Review" items={tickets.review} />
                          </div>
                        </CardContent>
                      </Card>

                      <Card className="rounded-[28px] border-slate-200 bg-white text-slate-900 shadow-xl shadow-black/10">
                        <CardHeader>
                          <div className="flex items-center gap-3">
                            <div className="rounded-2xl bg-slate-900 p-2 text-white"><MessageSquare className="h-5 w-5" /></div>
                            <div>
                              <CardTitle className="text-xl">Report / Waiting Center</CardTitle>
                              <CardDescription>사용자가 지금 기다리거나 검토해야 할 relay 상태</CardDescription>
                            </div>
                          </div>
                        </CardHeader>
                        <CardContent className="space-y-3">
                          {handoffReports.map((item) => (
                            <div key={item.id} className="rounded-2xl bg-slate-50 p-4">
                              <div className="flex items-center justify-between gap-3">
                                <div className="flex items-center gap-3">
                                  <div className="rounded-xl bg-slate-900 p-2 text-white"><TeamIcon kind={item.teamKind} /></div>
                                  <div className="rounded-xl bg-slate-200 p-2 text-slate-700"><RoleIcon kind={item.roleKind} /></div>
                                  <div>
                                    <div className="text-sm font-medium">{item.teamName}</div>
                                    <div className="text-xs text-slate-500">{item.roleTitle}</div>
                                  </div>
                                </div>
                                <div className="text-xs text-slate-500">{item.state}</div>
                              </div>
                              <div className="mt-3 text-sm text-slate-700">waiting: {item.waitingFor}</div>
                              <div className="mt-2 flex items-center gap-2 text-xs text-slate-500"><ArrowRight className="h-3.5 w-3.5" />{item.handoff}</div>
                              <div className="mt-2 text-xs text-slate-500">user attention: {item.userAttention}</div>
                            </div>
                          ))}
                        </CardContent>
                      </Card>
                    </div>
                  </div>
                </div>
              </TabsContent>

              <TabsContent value="vectorfl" className="mt-6 space-y-6">
                <section className="rounded-[28px] border border-white/10 bg-gradient-to-br from-slate-900 to-slate-950 p-5 shadow-2xl shadow-black/20">
                  <div className="flex items-center gap-3">
                    <div className="rounded-2xl bg-white/10 p-2"><Blocks className="h-5 w-5" /></div>
                    <div>
                      <div className="text-sm font-medium text-white">Flow Summary</div>
                      <div className="text-xs text-slate-400">VectorFlowState slot · 사용자면 작업과 엔진 처리 사이의 중간 흐름 요약</div>
                    </div>
                  </div>
                  <div className="mt-4 grid gap-4 xl:grid-cols-[1.1fr_0.9fr]">
                    <div className="grid gap-3 sm:grid-cols-2 xl:grid-cols-4">
                      <DarkMetric label="active lines" value={String(vectorActiveLines.length)} note="현재 목적과 연결된 line 후보" />
                      <DarkMetric label="strong lines" value={String(lines.filter((line) => line.health === "strong").length)} note="강하게 읽히는 중간 흐름" />
                      <DarkMetric label="current gaps" value={String(vectorSummary.gapCount)} note="보강 / 검증이 필요한 약점" />
                      <DarkMetric label="relations" value={String(vectorSummary.bridgeCount)} note="현재 연결 중인 relation 수" />
                    </div>
                    <div className="grid gap-3 sm:grid-cols-2 xl:grid-cols-2">
                      <div className="rounded-2xl border border-white/10 bg-white/5 p-4 text-white">
                        <div className="text-[11px] uppercase tracking-[0.18em] text-slate-400">strongest line</div>
                        <div className="mt-2 text-sm">{vectorSummary.strongest}</div>
                      </div>
                      <div className="rounded-2xl border border-white/10 bg-white/5 p-4 text-white">
                        <div className="text-[11px] uppercase tracking-[0.18em] text-slate-400">weakest line</div>
                        <div className="mt-2 text-sm">{vectorSummary.weakest}</div>
                      </div>
                      <div className="rounded-2xl border border-white/10 bg-white/5 p-4 text-white">
                        <div className="text-[11px] uppercase tracking-[0.18em] text-slate-400">current focus</div>
                        <div className="mt-2 text-sm">{vectorSummary.currentFocus}</div>
                      </div>
                      <div className="rounded-2xl border border-white/10 bg-white/5 p-4 text-white">
                        <div className="text-[11px] uppercase tracking-[0.18em] text-slate-400">next intervention</div>
                        <div className="mt-2 text-sm">{vectorSummary.nextIntervention}</div>
                      </div>
                    </div>
                  </div>
                  <div className="mt-4 rounded-2xl border border-white/10 bg-white/5 p-4 text-xs leading-6 text-slate-300">
                    mock attachment: {vectorSurfaceAttachmentNote.mock}<br />
                    actual attachment candidate: {vectorSurfaceAttachmentNote.actual}
                  </div>
                </section>

                <Card className="rounded-[28px] border-slate-200 bg-white text-slate-900 shadow-xl shadow-black/10">
                  <CardHeader>
                    <div className="flex items-center justify-between gap-3">
                      <div className="flex items-center gap-3">
                        <div className="rounded-2xl bg-slate-900 p-2 text-white"><ListTree className="h-5 w-5" /></div>
                        <div>
                          <CardTitle className="text-xl">Active Line Atlas</CardTitle>
                          <CardDescription>VectorFlowState.active_lines slot · 지금 움직이는 line 목록</CardDescription>
                        </div>
                      </div>
                      <Button size="sm" variant="outline" onClick={() => setLineDraft(createLineDraft(selectedLine))} className="rounded-xl"><NotebookPen className="mr-2 h-4 w-4" />라인 수정</Button>
                    </div>
                  </CardHeader>
                  <CardContent>
                    <div className="grid gap-3 lg:grid-cols-2">
                      {vectorActiveLines.map(({ line, currentStage, sourceRefs }) => (
                        <button key={line.id} onClick={() => setSelectedLineId(line.id)} className={`rounded-2xl border p-4 text-left transition ${selectedLine.id === line.id ? "border-slate-900 bg-slate-50" : "border-slate-200 bg-white hover:border-slate-300"}`}>
                          <div className="flex items-start justify-between gap-3">
                            <div>
                              <div className="text-[11px] uppercase tracking-[0.18em] text-slate-500">{line.id}</div>
                              <div className="mt-1 font-medium">{line.name}</div>
                              <div className="mt-2 text-sm text-slate-600 line-clamp-2">{line.purpose}</div>
                            </div>
                            <span className={`rounded-full px-3 py-1 text-xs font-medium ${statusClass(line.health)}`}>{statusLabel(line.health)}</span>
                          </div>
                          <div className="mt-3 grid gap-2 text-xs text-slate-600">
                            <div><span className="font-medium text-slate-900">current_stage</span> · {vectorStageLabel(currentStage)}</div>
                            <div><span className="font-medium text-slate-900">source_refs</span> · {sourceRefs.join(", ")}</div>
                            <div><span className="font-medium text-slate-900">connected_to</span> · {line.connectedTo.slice(0, 2).join(", ") || "none"}</div>
                          </div>
                        </button>
                      ))}
                    </div>
                  </CardContent>
                </Card>

                <div className="grid gap-6 xl:grid-cols-[1fr_1fr]">
                  <Card className="rounded-[28px] border-slate-200 bg-white text-slate-900 shadow-xl shadow-black/10">
                    <CardHeader>
                      <div className="flex items-center gap-3">
                        <div className="rounded-2xl bg-slate-900 p-2 text-white"><Link2 className="h-5 w-5" /></div>
                        <div>
                          <CardTitle className="text-xl">Relation / Gap Field</CardTitle>
                          <CardDescription>VectorFlowState.gaps + relation summary · 어디가 연결 중이고 어디가 비었는지</CardDescription>
                        </div>
                      </div>
                    </CardHeader>
                    <CardContent className="grid gap-4 lg:grid-cols-2">
                      <div className="space-y-3">
                        <div className="text-sm font-medium">Relation links</div>
                        {relationBoard.map((relation) => (
                          <div key={`${relation.left}-${relation.right}`} className="rounded-2xl bg-slate-50 p-4">
                            <div className="text-sm text-slate-700">{relation.left}</div>
                            <div className="my-2 flex items-center gap-2 text-xs text-slate-500"><ArrowRight className="h-3.5 w-3.5" />connected to</div>
                            <div className="text-sm text-slate-700">{relation.right}</div>
                          </div>
                        ))}
                      </div>
                      <div className="space-y-3">
                        <div className="text-sm font-medium">Current gaps</div>
                        {vectorGaps.slice(0, 8).map((gap) => (
                          <div key={gap.id} className="rounded-2xl border border-rose-100 bg-rose-50 p-4">
                            <div className="text-sm font-medium text-rose-900">{gap.title}</div>
                            <div className="mt-2 text-xs leading-5 text-rose-700">{gap.why}</div>
                            <div className="mt-2 text-xs text-rose-600">linked_line_ids: {gap.linkedLineIds.join(", ")}</div>
                          </div>
                        ))}
                      </div>
                    </CardContent>
                  </Card>

                  <Card className="rounded-[28px] border-white/10 bg-slate-900 text-slate-100 shadow-xl shadow-black/20">
                    <CardHeader>
                      <div className="flex items-center gap-3">
                        <div className="rounded-2xl bg-white/10 p-2"><RefreshCcw className="h-5 w-5" /></div>
                        <div>
                          <CardTitle className="text-xl text-white">Ingress / Reflux / Pending Trace</CardTitle>
                          <CardDescription className="text-slate-400">VectorFlowState.lineage_events + current_stage strip</CardDescription>
                        </div>
                      </div>
                    </CardHeader>
                    <CardContent className="space-y-4">
                      <div className="grid gap-3 sm:grid-cols-2">
                        {(["ingress", "processing", "export", "reflux", "pending_validation"] as VectorLineStage[]).map((stage) => (
                          <div key={stage} className="rounded-2xl border border-white/10 bg-white/5 p-4">
                            <div className="text-[11px] uppercase tracking-[0.18em] text-slate-400">{vectorStageLabel(stage)}</div>
                            <div className="mt-2 space-y-2">
                              {vectorActiveLines.filter((item) => item.currentStage === stage).map((item) => (
                                <div key={item.line.id} className="rounded-xl bg-white/5 p-3 text-sm text-slate-200">{item.line.name}</div>
                              ))}
                              {vectorActiveLines.filter((item) => item.currentStage === stage).length === 0 && (
                                <div className="rounded-xl bg-black/20 p-3 text-sm text-slate-500">empty</div>
                              )}
                            </div>
                          </div>
                        ))}
                      </div>

                      <div className="space-y-3">
                        {lineEvents.map((event) => {
                          const meta = eventMeta(event.type);
                          const Icon = meta.icon;
                          const line = lines.find((item) => item.id === event.lineId);
                          return (
                            <div key={event.id} className="rounded-2xl border border-white/10 bg-white/5 p-4">
                              <div className="flex items-center justify-between gap-3">
                                <div className="flex items-center gap-3">
                                  <div className={`rounded-xl p-2 ${meta.cls}`}><Icon className="h-4 w-4" /></div>
                                  <div>
                                    <div className="text-sm font-medium text-white">{line?.name}</div>
                                    <div className="text-xs text-slate-400">{meta.label}</div>
                                  </div>
                                </div>
                                <div className="text-xs text-slate-500">{event.time}</div>
                              </div>
                              <div className="mt-3 text-sm text-slate-300">{event.detail}</div>
                            </div>
                          );
                        })}
                      </div>
                    </CardContent>
                  </Card>
                </div>

                <div className="grid gap-6 xl:grid-cols-[0.9fr_1.1fr]">
                  <Card className="rounded-[28px] border-slate-200 bg-white text-slate-900 shadow-xl shadow-black/10">
                    <CardHeader>
                      <div className="flex items-center gap-3">
                        <div className="rounded-2xl bg-slate-900 p-2 text-white"><Waypoints className="h-5 w-5" /></div>
                        <div>
                          <CardTitle className="text-xl">Selected Line Genealogy</CardTitle>
                          <CardDescription>선택 라인 계보는 보조층으로 유지합니다</CardDescription>
                        </div>
                      </div>
                    </CardHeader>
                    <CardContent className="space-y-3">
                      {selectedLine.lineage.map((step, idx) => (
                        <div key={step} className="flex items-start gap-3 rounded-2xl bg-slate-50 p-4">
                          <div className="flex h-7 w-7 items-center justify-center rounded-full bg-slate-900 text-sm font-semibold text-white">{idx + 1}</div>
                          <div className="flex-1 text-sm text-slate-700">{step}</div>
                        </div>
                      ))}
                    </CardContent>
                  </Card>

                  <Card className="rounded-[28px] border-white/10 bg-slate-900 text-slate-100 shadow-xl shadow-black/20">
                    <CardHeader>
                      <div className="flex items-center gap-3">
                        <div className="rounded-2xl bg-white/10 p-2"><BrainCircuit className="h-5 w-5" /></div>
                        <div>
                          <CardTitle className="text-xl text-white">Selected Line Inspector</CardTitle>
                          <CardDescription className="text-slate-400">상세 판독은 중간 통로 핵심 섹션 뒤의 보조층으로 둡니다</CardDescription>
                        </div>
                      </div>
                    </CardHeader>
                    <CardContent className="space-y-4">
                      <div className="rounded-2xl border border-white/10 bg-white/5 p-4">
                        <div className="text-[11px] uppercase tracking-[0.18em] text-slate-400">selected line</div>
                        <div className="mt-2 text-lg font-semibold text-white">{selectedLine.name}</div>
                        <div className="mt-2 text-sm leading-7 text-slate-300">{selectedLine.purpose}</div>
                      </div>
                      <div className="grid gap-3 sm:grid-cols-2">
                        <LightMetric label="anchors" value={String(selectedLine.anchors.length)} note="이 라인을 붙드는 근거 점들" />
                        <LightMetric label="connections" value={String(selectedLine.connectedTo.length)} note="다른 라인과 연결된 수" />
                      </div>
                      <div className="rounded-2xl border border-white/10 bg-black/20 p-4">
                        <div className="mb-3 text-sm font-medium text-white">Line notes / judgments</div>
                        <div className="space-y-2">
                          {selectedLine.notes.map((note) => (
                            <div key={note} className="rounded-xl bg-white/5 p-3 text-sm text-slate-300">{note}</div>
                          ))}
                        </div>
                      </div>
                      <div className="grid gap-4 sm:grid-cols-2">
                        <div>
                          <div className="mb-2 text-sm font-medium text-white">Export</div>
                          <div className="space-y-2">
                            {selectedLine.exportToUser.map((item) => (
                              <div key={item} className="rounded-xl border border-white/10 bg-white/5 p-3 text-sm text-slate-200">{item}</div>
                            ))}
                          </div>
                        </div>
                        <div>
                          <div className="mb-2 text-sm font-medium text-white">Reflux</div>
                          <div className="space-y-2">
                            {selectedLine.refluxFromUser.map((item) => (
                              <div key={item} className="rounded-xl border border-white/10 bg-white/5 p-3 text-sm text-slate-200">{item}</div>
                            ))}
                          </div>
                        </div>
                      </div>
                    </CardContent>
                  </Card>
                </div>
              </TabsContent>

              <TabsContent value="engine" className="mt-6">
                <Card className="rounded-[28px] border-slate-200 bg-white text-slate-900 shadow-xl shadow-black/10">
                  <CardHeader>
                    <div className="flex items-center gap-3">
                      <div className="rounded-2xl bg-slate-900 p-2 text-white"><BrainCircuit className="h-5 w-5" /></div>
                      <div>
                        <CardTitle className="text-xl">엔진면 연결</CardTitle>
                        <CardDescription>실제 엔진면은 별도 정비/제어 surface로 분리되어 있으며, 여기서는 연결 위치만 보여줍니다</CardDescription>
                      </div>
                    </div>
                  </CardHeader>
                  <CardContent>
                    <div className="mb-3 rounded-2xl border border-slate-200 bg-slate-50 p-4">
                      <div className="text-sm font-medium text-slate-900">실제 엔진면</div>
                      <div className="mt-1 text-sm text-slate-600">공간 내부 재료 목록, 상태창, 스크립트 접근, 유지보수 판단은 Python viewer의 엔진면에서 봅니다.</div>
                      <a className="mt-3 inline-flex rounded-xl bg-slate-900 px-4 py-2 text-sm font-semibold text-white" href="http://127.0.0.1:8421/vectorfl-engine/operate">
                        실제 엔진면 열기
                      </a>
                    </div>
                    <div className="grid gap-3 md:grid-cols-2 xl:grid-cols-4">
                      <div className="rounded-2xl bg-slate-50 p-4">
                        <div className="text-[11px] uppercase tracking-[0.18em] text-slate-500">inventory</div>
                        <div className="mt-2 text-sm text-slate-700">입력 자산 / 라인 자산 / 최근 결과물 / 관련 md/json/script 목록</div>
                      </div>
                      <div className="rounded-2xl bg-slate-50 p-4">
                        <div className="text-[11px] uppercase tracking-[0.18em] text-slate-500">space status</div>
                        <div className="mt-2 text-sm text-slate-700">현재 활성 흐름 / 오류 / 경고 / 환류 대기 / 상태 점검</div>
                      </div>
                      <div className="rounded-2xl bg-slate-50 p-4">
                        <div className="text-[11px] uppercase tracking-[0.18em] text-slate-500">script access</div>
                        <div className="mt-2 text-sm text-slate-700">라인을 만든 스크립트와 기준 파일 접근</div>
                      </div>
                      <div className="rounded-2xl bg-slate-50 p-4">
                        <div className="text-[11px] uppercase tracking-[0.18em] text-slate-500">maintenance</div>
                        <div className="mt-2 text-sm text-slate-700">출력 품질, 연료 상태, 내부 수정 포인트 점검</div>
                      </div>
                    </div>
                  </CardContent>
                </Card>
              </TabsContent>
            </Tabs>
          </motion.div>
        </main>
      </div>

      <TeamEditModal open={!!teamDraft} onOpenChange={(open) => !open && setTeamDraft(null)} draft={teamDraft} onChange={setTeamDraft} onSave={saveTeamDraft} />
      <RoleEditModal open={!!roleDraft} onOpenChange={(open) => !open && setRoleDraft(null)} draft={roleDraft} onChange={setRoleDraft} onSave={saveRoleDraft} />
      <LineEditModal open={!!lineDraft} onOpenChange={(open) => !open && setLineDraft(null)} draft={lineDraft} onChange={setLineDraft} onSave={saveLineDraft} />
    </div>
  );
}
