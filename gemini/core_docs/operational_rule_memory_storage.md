# Operational Rule: Memory and Record Storage

## Purpose
This document records a critical operational rule regarding how Gemini CLI (myself) should handle information that needs to be remembered or recorded within the `vectorfl_replica` project.

## Rule
- **Any content that needs to be remembered or recorded during the ongoing process MUST be stored in the `gemini` folder.**
- **Gemini CLI MUST NOT use its internal memory (`save_memory` tool) for project-specific persistent storage.**
- **All instances requiring memory or recording SHALL result in the creation of a new file or modification of an existing relevant file within the `gemini` folder.**

## Rationale
This rule aligns with the project's principles of:
- **Single Source of Truth (SSOT):** Centralizing all operational knowledge within designated project artifacts.
- **Auditability and Transparency:** Ensuring that all remembered information is externalized and visible within the project's file system.
- **Role Definition:** Reinforcing Gemini's role as an analytical and reporting tool that interacts with the filesystem, rather than maintaining internal, opaque state for project context.

## Implications for Gemini CLI
- When a user provides a new instruction or piece of information that would typically be saved to memory, it will instead be documented in the `gemini` folder.
- When generating reports or analyses, if there are findings or observations that should persist beyond the immediate session, they will be recorded as files in the `gemini` folder.
- The `gemini` folder will serve as the primary external memory and knowledge base for Gemini's operation within this project.
