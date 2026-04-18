import { Team, AuditLog, BoardStat } from "./user-surface.types";

export const initialTeamsSeed: Team[] = [
  {
    id: "t-ref-analysis",
    name: "분석팀",
    kind: "internal",
    purpose: "Raw 자산 해석 및 라인 후보 발굴",
    goal: "구조 후보 생성",
    status: "active",
    roles: [
      { id: "r-ana-1", title: "구조 해석", kind: "structure", purpose: "구조 식별", goal: "추상화 레이어", status: "running" }
    ]
  }
];

export const auditLogsSeed: AuditLog[] = [];
export const boardStatsSeed: BoardStat[] = [
  { label: "Goal State", value: "active", note: "현재 목적 선언 상태" },
  { label: "Scope Guard", value: "draft", note: "범위 기준 정렬 중" },
  { label: "Material Context", value: "2", note: "연결된 재료 문맥" },
  { label: "Next Reading", value: "VectorFL", note: "중간 판독면으로 전달" }
];

export const userSurfaceMetaSeed = {
  initialGoal: "레퍼런스 탱크프로그램 활용 물류 시스템 전환",
  infoBoxes: [
    { label: "Surface Role", val: "목적 / 범위 / 재료 문맥을 세우는 시작면" },
    { label: "Material Context", val: "현재 읽을 재료와 연결 범위를 먼저 드러냄" },
    { label: "User Outcome", val: "지금 무엇을 왜 어디까지 할지 확정" },
    { label: "Next Surface", val: "VectorFL 중간 형성체 판독으로 전달" }
  ]
};
