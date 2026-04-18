# structured_doc_routing_header_template_v1

## 1. Minimal Template

```md
[[DOCROLE:directive]]
[[RUNMODE:ingest_then_execute]]
[[PRIORITY:high]]
```

## 2. Korean Alias Template

```md
[[DOCROLE:지시서]]
[[RUNMODE:입력후실행]]
[[PRIORITY:높음]]
```

## 3. Common Patterns

### Declaration
```md
[[DOCROLE:declaration]]
[[RUNMODE:ingest_only]]
[[PRIORITY:normal]]
```

### Baseline
```md
[[DOCROLE:baseline]]
[[RUNMODE:ingest_only]]
[[PRIORITY:high]]
```

### Directive
```md
[[DOCROLE:directive]]
[[RUNMODE:ingest_then_execute]]
[[PRIORITY:high]]
```

### Summary
```md
[[DOCROLE:summary]]
[[RUNMODE:ingest_only]]
[[PRIORITY:normal]]
```

### Memo
```md
[[DOCROLE:memo]]
[[RUNMODE:ingest_only]]
[[PRIORITY:low]]
```

### Philosophical Interpretation
```md
[[DOCROLE:philosophical_interpretation]]
[[RUNMODE:ingest_only]]
[[PRIORITY:normal]]
```

## 4. Notes
- If `RUNMODE` is omitted, the system should treat it as `ingest_only`.
- Users do not need to memorize canonical English values.
- Codex should normalize aliases before registry or event writes.
