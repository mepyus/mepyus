import { useState, useMemo } from "react";
import { Team, Role, TeamKind, RoleKind } from "./user-surface.types";

export function useUserSurfaceState(initialTeams: Team[]) {
  const [teams, setTeams] = useState<Team[]>(initialTeams);
  const [selectedTeamId, setSelectedTeamId] = useState<string | null>(initialTeams[0]?.id || null);
  
  const selectedTeam = useMemo(() => 
    teams.find((t) => t.id === selectedTeamId) || teams[0] || null, 
    [teams, selectedTeamId]
  );

  const createId = (prefix: string) => `${prefix}-${Math.random().toString(36).slice(2, 9)}`;

  const addTeam = (kind: TeamKind = "internal") => {
    const newTeam: Team = {
      id: createId("team"),
      name: "New Team",
      kind,
      purpose: "Define team purpose here",
      goal: "Define team goal here",
      status: "queued",
      roles: []
    };
    setTeams([...teams, newTeam]);
    setSelectedTeamId(newTeam.id);
  };

  const removeTeam = (id: string) => {
    const filtered = teams.filter(t => t.id !== id);
    setTeams(filtered);
    if (selectedTeamId === id) setSelectedTeamId(filtered[0]?.id || null);
  };

  const addRole = (teamId: string) => {
    const newRole: Role = {
      id: createId("role"),
      title: "New Role",
      kind: "custom",
      purpose: "Define role purpose",
      goal: "Define role goal",
      status: "ready"
    };
    setTeams(teams.map(t => t.id === teamId ? { ...t, roles: [...t.roles, newRole] } : t));
  };

  const removeRole = (teamId: string, roleId: string) => {
    setTeams(teams.map(t => t.id === teamId ? { ...t, roles: t.roles.filter(r => r.id !== roleId) } : t));
  };

  const updateTeam = (updatedTeam: Team) => {
    setTeams(teams.map(t => t.id === updatedTeam.id ? updatedTeam : t));
  };

  return {
    teams,
    selectedTeam,
    selectedTeamId,
    setSelectedTeamId,
    addTeam,
    removeTeam,
    addRole,
    removeRole,
    updateTeam
  };
}
