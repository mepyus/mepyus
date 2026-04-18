# delta_society node-link concept map v1

## 1. center node

- `delta_society_as_ai_native_operating_company`
  - read as:
    - VC redefinition
    - knowledge/community operating layer
    - agent-mediated work system

## 2. node list

### A. company frame nodes

- `vc_redefinition`
- `knowledge_community`
- `ai_native_company_hypothesis`

### B. operating structure nodes

- `end_to_end_ownership`
- `dependency_decomposition`
- `result_first_communication`
- `modular_end_to_end_units`

### C. input-to-action nodes

- `meeting_recording`
- `concept_extraction`
- `idea_seed`
- `triage_queue`
- `task_routing`
- `agent_delegation`
- `compound_result_store`

### D. trace / truth surface nodes

- `github_ssot`
- `decision_trace`
- `result_archive`

### E. tool surface nodes

- `slack_recording`
- `claude_code`
- `linear`
- `compound`
- `github`

### F. current space contact nodes

- `input_to_reading_organ`
- `transition_over_surface`
- `pre_read_eye`

### G. caution nodes

- `promotional_framing`
- `one_company_specificity`
- `coarse_transcript_segmentation`

## 3. link map

### center to company frame

- `delta_society_as_ai_native_operating_company -> vc_redefinition`
- `delta_society_as_ai_native_operating_company -> knowledge_community`
- `delta_society_as_ai_native_operating_company -> ai_native_company_hypothesis`

### company frame to operating structure

- `ai_native_company_hypothesis -> end_to_end_ownership`
- `ai_native_company_hypothesis -> dependency_decomposition`
- `ai_native_company_hypothesis -> result_first_communication`
- `ai_native_company_hypothesis -> modular_end_to_end_units`
- `knowledge_community -> modular_end_to_end_units`

### operating structure to input/action chain

- `end_to_end_ownership -> task_routing`
- `dependency_decomposition -> task_routing`
- `result_first_communication -> compound_result_store`
- `modular_end_to_end_units -> agent_delegation`

### input/action chain internal links

- `meeting_recording -> concept_extraction`
- `concept_extraction -> idea_seed`
- `idea_seed -> triage_queue`
- `triage_queue -> task_routing`
- `task_routing -> agent_delegation`
- `agent_delegation -> compound_result_store`

### tool surface links

- `slack_recording -> meeting_recording`
- `claude_code -> concept_extraction`
- `claude_code -> agent_delegation`
- `linear -> triage_queue`
- `compound -> compound_result_store`
- `github -> github_ssot`

### truth / trace links

- `github_ssot -> decision_trace`
- `decision_trace -> result_archive`
- `compound_result_store -> result_archive`

### current space contact links

- `meeting_recording -> input_to_reading_organ`
- `concept_extraction -> input_to_reading_organ`
- `triage_queue -> transition_over_surface`
- `task_routing -> transition_over_surface`
- `compound_result_store -> transition_over_surface`
- `coarse_transcript_segmentation -> pre_read_eye`

### caution links

- `promotional_framing -> ai_native_company_hypothesis`
- `one_company_specificity -> end_to_end_ownership`
- `coarse_transcript_segmentation -> transition_over_surface`
- `promotional_framing -> knowledge_community`

## 4. strongest current reads

### `input_to_reading_organ`

- strongest incoming links:
  - `meeting_recording`
  - `concept_extraction`
  - `idea_seed`
- reading:
  - raw external material is directly turned into next-stage thinking and task material

### `transition_over_surface`

- strongest incoming links:
  - `triage_queue`
  - `task_routing`
  - `agent_delegation`
  - `compound_result_store`
  - `github_ssot`
- reading:
  - the case makes surface transition explicit and operational

### `pre_read_eye`

- strongest incoming links:
  - `coarse_transcript_segmentation`
- reading:
  - this is less a support node than a reading-entry requirement for this transcript

## 5. what not to overread

- `ai_native_company_hypothesis` is still a strong company-level claim, not a locked core rule
- `end_to_end_ownership` is a valid external operating signal, but still one-company specific
- `knowledge_community` is meaningful, but not yet a direct core line
- current map is a reading map, not a promotion map
