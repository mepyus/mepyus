# SESSION_29_EXECUTION_INSTRUCTION.md

## 1. Goal
Execute the Real Input Activation step for one actual task/input. Verify that the external tool uses the `Space Material Activation Map` to retrieve only relevant `Material Families` without triggering a broad scan.

## 2. Search First
- `SPACE_MATERIAL_ACTIVATION_MAP_V0` (Routes).
- `MATERIAL_FAMILY_INDEX_V0` (Available families).
- `TOOL_READABLE_SURFACE_V0` (Entry rules).

## 3. Required Outputs (Artifacts)
- **Input/Trigger Mapping**: Map the user purpose to an activation trigger.
- **Activation Result**: List of activated Material Families and evidence pointers used.
- **Drift Log**: Record any attempt to scan outside the identified activation scope.
- **Context Bundle Draft**: The resulting bounded package for the tool.

## 4. Constraints
- **Search-First, Scoped-Search ONLY.**
- **NO Broad Scan.**
- **Log all issues** (don't stop unless Hard Boundary violation).
- **Do not modify files or execute commands without user approval.**

## 5. Next Handoff
Prepare `SESSION_30_HANDOFF.md` for Limited Tool Role Run.
