# SESSION_35_EXECUTION_INSTRUCTION.md

## 1. Goal
Conduct a Space Material Activation Audit on the selected input ("구조 취약점 분석") to verify if the tool identifies the correct Material Families and routes without broad scanning.

## 2. Search First
- `SPACE_MATERIAL_ACTIVATION_MAP_V0.md` (Activation routes).
- `MATERIAL_FAMILY_INDEX_V0.md` (Available families).
- `SESSION_34_RESULTS_V0.md` (Selected input).

## 3. Required Outputs (Artifacts)
- **Activation Audit Report**: Log of triggered routes and families.
- **Drift Log**: Record of any unscoped search attempts.
- **Depth Analysis**: Depth score (Shallow/Medium/Deep) of the activation logic.
- **Evidence Pointer Check**: Validation of pointers used for the proposal.

## 4. Constraints
- **Audit, NOT Implement.**
- **No Broad Scan.**
- If broad scan is detected -> Flag as `BOUNDARY_RISK` and log.
- **Do not modify files or execute commands without user approval.**

## 5. Next Handoff
Prepare `SESSION_36_HANDOFF.md` for Limited Tool Role Run (Trial).
