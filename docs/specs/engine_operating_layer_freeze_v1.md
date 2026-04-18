# Engine Operating Layer Freeze v1

## Purpose
- Freeze the current engine stack into explicit operating layers.
- Prevent derived, surface, and experimental layers from being mistaken for authoritative core.

## Layer 1. Core Authoritative Layer

### Includes
- `engine_state_schema_v1`
- canonical operating state fields
- `engine_state_store`
- append-only `engine_state_history`
- `engine_state_latest` as derived core operating projection
- `engine_state_update_policy_v1`
- validation fixture

### Role
- define canonical state
- govern append/update provenance
- preserve authoritative history
- regenerate latest safely

### Permissions
- write only through policy-controlled state update path
- readable by all lower layers

### Forbidden
- naming-heavy interpretive promotion
- experimental top-level contamination
- surface overwrite of core state

## Layer 2. Derived Operating Layer

### Includes
- state change diff
- interpretation badge
- history compaction
- runtime evidence priority router
- state change attention queue
- attention resolution loop
- state attention memory
- update event surfaces
- compacted history surfaces

### Role
- accelerate change reading
- distribute attention
- summarize lineage without changing truth
- improve operating readability

### Permissions
- may read core
- may write only derived artifacts

### Forbidden
- direct core mutation
- raw history deletion
- treating derived summaries as canonical truth

## Layer 3. Surface Layer

### Includes
- process console
- header badge bar
- asset rail
- state panel
- history drill-down
- diff panel
- attention strip
- queue links
- memory summary
- viewer server / process console builder / render

### Role
- main operator-facing surface
- read latest + lineage + diff + attention + memory
- provide navigation into source and history

### Read Sources
- core latest/history
- derived diff/badge/queue/memory/compaction

### Forbidden
- canonical rewrite from surface interaction
- graph-first redefinition of the engine
- default exposure of experimental layer

## Layer 4. Experimental Layer

### Includes
- `experimental_namespace`
- context unit naming
- paragraph role naming
- pivot/compression naming
- business-power-shift style high-level naming
- orchestration-style high-level naming
- exploratory object hypotheses

### Role
- comparison memory
- future promotion candidate pool
- operator reading aid
- exploratory interpretation

### Permissions
- may persist independently
- may appear only in explicit inspect/debug/expand paths

### Forbidden
- canonical top-level promotion without explicit policy
- default queue/priority/memory criteria usage
- default surface exposure

## Read / Write Rules

### Core -> Derived
- allowed

### Derived -> Core
- forbidden by default
- only runtime evidence plus update policy may change core state

### Core -> Surface
- allowed

### Derived -> Surface
- allowed

### Experimental -> Surface
- restricted
- hidden by default

### Experimental -> Core
- forbidden

## Authoritative Source Hierarchy

### Level 1
- append-only history
- schema
- update policy

### Level 2
- latest derived from history

### Level 3
- diff
- badge
- attention queue
- attention memory
- compacted history

### Level 4
- UI display mapping
- presentation strings

### Level 5
- experimental namespace
- exploratory naming

## Process Console Position
- main surface of the engine
- state-first operating surface
- reads authoritative layers but is not itself authoritative
- graph/terrain/distribution views remain secondary

## Freeze Boundary

### Allowed After Freeze
- derived-layer tuning
- surface UX refinement
- experimental hypothesis expansion

### Restricted After Freeze
- canonical field changes
- update policy redesign
- authoritative schema change

### Forbidden After Freeze
- graph-first engine redefinition
- derived-as-core slippage
- experimental-to-canonical leakage
- raw history deletion
- latest direct overwrite
- policy bypass writes

## Freeze Statement
- The current engine is officially frozen as a state-first process console stack.
- This freeze marks completion of the first operating layer baseline, not completion of all future meaning work.
