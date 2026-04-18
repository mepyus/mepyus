import React from "react";

export type AssetKind = "inputs" | "docs" | "scripts" | "runtime" | "manifests" | "views";
export type AssetHealth = "healthy" | "watch" | "stale" | "broken";
export type EngineEventType = "created" | "updated" | "warning" | "hold" | "skipped";
export type RecommendationPriority = "now" | "next" | "later";
export type WatchSeverity = "high" | "medium" | "low";
export type WatchStatus = "open" | "watching" | "hold" | "resolved";

export type AssetNode = {
  id: string;
  kind: AssetKind;
  title: string;
  path: string;
  health: AssetHealth;
  role: string;
  updatedAt: string;
  summary: string;
  connectedTo: string[];
  warnings: string[];
  children?: AssetNode[];
  // v2 확장 필드
  attentionScore?: number; // 0-100 (AI의 읽기/쓰기 집중도)
  scriptLink?: string;     // 해당 자산을 관리하는 스크립트 경로
  deltaStatus?: "synced" | "modified" | "violation"; // 기준선 정합성 상태
};

export type EngineEvent = {
  id: string;
  type: EngineEventType;
  title: string;
  detail: string;
  time: string;
  assetId?: string;
};

export type Recommendation = {
  id: string;
  title: string;
  body: string;
  priority: RecommendationPriority;
};

export type Watchpoint = {
  id: string;
  title: string;
  severity: WatchSeverity;
  status: WatchStatus;
  assetId: string;
  why: string;
  nextAction: string;
};

export type BridgeItem = {
  id: string;
  direction: "from_user" | "from_vectorfl" | "back_out";
  title: string;
  body: string;
  payload: string[];
};

export type SummaryStats = {
  inventory: number;
  watchCount: number;
  warningEvents: number;
  holds: number;
};

export type EngineIngestSlot = {
    ingestId: string;
    sourceLabel: string;
    sourcePath: string;
    sourceType: string;
    status: string;
    linkedGoalIds: string[];
    mockAttachmentPoint: string;
    actualAttachmentPoint: string;
};

export type EnginePipelineSlot = {
    pipelineId: string;
    currentStep: string;
    status: string;
    steps: { stepId: string; name: string; status: string; note: string }[];
    mockAttachmentPoint: string;
    actualAttachmentPoint: string;
};

export type ValidationReturnPacket = {
    packetId: string;
    summary: string;
    acceptedRefs: string[];
    holdRefs: string[];
    reasoningNotes: string[];
    nextReingestRequested: boolean;
    status: string;
    mockAttachmentPoint: string;
    actualAttachmentPoint: string;
};
