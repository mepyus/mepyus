# delta_society node-link visual map v1

## 1. Purpose

This document renders the current `delta_society.md` reading as a compact node-link visual.

It is a reading aid, not a promotion decision.

## 2. Mermaid graph

```mermaid
graph TD
    A[delta_society_as_ai_native_operating_company]

    subgraph Company_Frame
        B[vc_redefinition]
        C[knowledge_community]
        D[ai_native_company_hypothesis]
    end

    subgraph Operating_Structure
        E[end_to_end_ownership]
        F[dependency_decomposition]
        G[result_first_communication]
        H[modular_end_to_end_units]
    end

    subgraph Input_to_Action
        I[meeting_recording]
        J[concept_extraction]
        K[idea_seed]
        L[triage_queue]
        M[task_routing]
        N[agent_delegation]
        O[compound_result_store]
    end

    subgraph Trace_and_Truth
        P[github_ssot]
        Q[decision_trace]
        R[result_archive]
    end

    subgraph Tool_Surfaces
        S[slack_recording]
        T[claude_code]
        U[linear]
        V[compound]
        W[github]
    end

    subgraph Current_Space_Contact
        X[input_to_reading_organ]
        Y[transition_over_surface]
        Z[pre_read_eye]
    end

    subgraph Caution
        CA[promotional_framing]
        CB[one_company_specificity]
        CC[coarse_transcript_segmentation]
    end

    A --> B
    A --> C
    A --> D

    D --> E
    D --> F
    D --> G
    D --> H
    C --> H

    E --> M
    F --> M
    G --> O
    H --> N

    I --> J
    J --> K
    K --> L
    L --> M
    M --> N
    N --> O

    S --> I
    T --> J
    T --> N
    U --> L
    V --> O
    W --> P

    P --> Q
    Q --> R
    O --> R

    I --> X
    J --> X
    K --> X

    L --> Y
    M --> Y
    N --> Y
    O --> Y
    P --> Y

    CC --> Z

    CA -.caution.-> D
    CA -.caution.-> C
    CB -.caution.-> E
    CC -.caution.-> Y

    classDef center fill:#f3f0e8,stroke:#3a332b,stroke-width:2px,color:#231f1a;
    classDef support fill:#e7f4ea,stroke:#355b3d,color:#1f3324;
    classDef structure fill:#e8f0f8,stroke:#38506a,color:#1f2c38;
    classDef tool fill:#f7efe2,stroke:#72562d,color:#3e2d14;
    classDef contact fill:#f0e8f6,stroke:#5a3e6e,color:#2d1f38;
    classDef caution fill:#f8e6e6,stroke:#7a3b3b,color:#3d1f1f,stroke-dasharray: 5 5;

    class A center;
    class B,C,D structure;
    class E,F,G,H support;
    class I,J,K,L,M,N,O support;
    class P,Q,R structure;
    class S,T,U,V,W tool;
    class X,Y,Z contact;
    class CA,CB,CC caution;
```

## 3. Reading guide

- green nodes:
  - operational support chain
- blue nodes:
  - company/frame/trace structure
- tan nodes:
  - concrete tool surfaces
- purple nodes:
  - contact with current strong lines
- red dashed nodes:
  - caution / overread risk

## 4. Fast reading

- strongest support path:
  - `meeting_recording -> concept_extraction -> idea_seed -> triage_queue -> task_routing -> agent_delegation -> compound_result_store`
- strongest current-space contact:
  - `input_to_reading_organ`
  - `transition_over_surface`
- strongest caution:
  - `coarse_transcript_segmentation`
  - `promotional_framing`
  - `one_company_specificity`
