import React from "react";

export type TeamStatus = "active" | "queued" | "waiting" | "idle";
export type RoleStatus = "running" | "ready" | "waiting";

export type RoleKind =
  | "reference"
  | "structure"
  | "risk"
  | "search"
  | "synth"
  | "implement"
  | "validate"
  | "custom";

export type TeamKind =
  | "internal"
  | "external"
  | "build"
  | "review"
  | "writing"
  | "shorts"
  | "custom";

export type Role = {
  id: string;
  title: string;
  kind: RoleKind;
  purpose: string;
  goal: string;
  status: RoleStatus;
};

export type Team = {
  id: string;
  name: string;
  kind: TeamKind;
  purpose: string;
  goal: string;
  status: TeamStatus;
  roles: Role[];
};

export type BoardStat = {
  label: string;
  value: string;
  note: string;
};

export type AuditLog = {
  id: string;
  teamName: string;
  teamKind: TeamKind;
  roleTitle: string;
  roleKind: RoleKind;
  body: string;
  next: string;
  time: string;
};

export type TicketItem = {
  id: string;
  title: string;
  role: string;
  team: string;
};
