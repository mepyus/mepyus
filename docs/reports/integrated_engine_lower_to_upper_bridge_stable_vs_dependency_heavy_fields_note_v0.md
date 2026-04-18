# Integrated Engine Lower To Upper Bridge Stable Vs Dependency Heavy Fields Note v0

## 1. Verdict

PASS_WITH_NOTE

Across two bridge examples, lower bundles consistently carry evidence and trace upward. They do not carry packet purpose, action authority, or next route.

## 2. Stable Lower-Derived Field Families

These fields consistently survive upward when the lower bundle is grounded:

| field family | examples | stability |
| --- | --- | --- |
| source identity | source path, doc id, doc ref, input id | stable |
| artifact path | generated file path, manifest path, receipt path | stable |
| run identity | run id, generated timestamp, receipt run identity | stable |
| formation trace | processing trace, receipt events, generated file list | stable |
| object-local structure | split mode/unit ids or route labels/ticket id | stable within bundle type |
| evidence object list | source manifest/split/trace or label/receipt/ticket | stable |

## 3. Bundle-Type-Specific Stable Fields

### Source Bundle

- split mode
- unit count
- sample unit evidence
- detected profile
- processing stage

### Routing Bundle

- docrole
- runmode
- priority
- processing profile
- execution_linkable
- ticket id
- receipt final status

## 4. Structurally Dependency-Heavy Upper Fields

These fields required upper context in both examples:

- current purpose
- scope boundary
- authority boundary
- selected lens set
- allowed actions
- forbidden actions
- expected output shape
- next route candidate
- why this path was chosen

This dependency appears structural, not incidental.

## 5. Why The Dependency Is Structural

Lower-input outputs are formed to preserve and expose input material. They do not know:

- what current supervisory question is being asked
- which upper surface will use the result
- what action is allowed
- what is forbidden
- what final output shape is required
- whether this attempt should stop, hold, or route forward

Those are upper/input packet responsibilities.

## 6. Stable Bridge Pattern Emerging

The emerging pattern is:

```text
lower bundle supplies evidence / trace / local structure
upper context supplies purpose / action / authority / route
bridge packet must preserve the origin of each field
```

This is a stable supervisory pattern, not a runtime implementation.

## 7. Phase 3 Validation

- Evidence-led check: passed. Stable fields are derived from two bridge examples.
- Dependency preservation check: passed. Upper-added fields are not reclassified as lower-derived.
- No automation check: passed. Pattern is supervisory, not runtime.

