# Integrated Engine VectorFL Packet Layer Density Cleanup Note v0

## 1. Verdict

PASS

The VectorFL packet layer was compressed into a summary-first structure. The interaction skeleton remains intact, but secondary detail is now behind expandable sections.

## 2. Why This Patch Was Needed

After the current work packet formation layer was added, the surface began to read correctly as packet-centered, but too much internal information was visible at once.

The goal of this patch was not to remove structure. It was to separate:

- always-visible operating summary
- expandable packet evidence/detail
- expandable history/deposit support
- expandable latest-return detail

## 3. What Changed

Changed file:

- `app/ui/integrated_engine/CliHostControlPanel.tsx`

Changes:

- `Bounded context refs` and `Current message to Codex` moved into `packet input details`.
- Current packet always-visible area now focuses on:
  - purpose
  - task lens
  - route candidate
  - expected return
- locks / evidence refs / guards / manual fields moved into an expandable packet detail section.
- `Send Codex Turn` remains directly after packet confirmation.
- conversation turns moved into an expandable section.
- deposit-ready queue moved into an expandable section.
- latest return now has a compact always-visible summary with session/status/task/route/marks.
- long latest return details, operator report, structured return, and deposit preview moved into an expandable detail section.

## 4. What Stayed Visible

- current packet purpose
- current packet lens
- next route candidate
- expected return shape
- packet confirmation / send controls
- latest return summary
- current marks / route badge

## 5. What Is Now Expandable

- context refs
- full message to Codex
- governing locks
- evidence bundle
- do / do-not guards
- still-manual fields
- packet-to-return continuity detail
- recent conversation turns
- deposit-ready queue
- route and mark history
- operator report
- structured return preview
- deposit candidate preview

## 6. What This Enables Later

This keeps the panel interaction-ready:

- packet can still drive CLI runs
- return can still be marked
- marked turns can still surface in User / Engine / VectorFL handoff areas
- detailed evidence remains inspectable without occupying the first screen

## 7. Watchpoints

1. Native expandable sections are intentionally simple. If they feel too plain, improve styling later without adding new behavior.
2. The panel still carries English/internal labels; this patch only reduces density.
3. Details are still present for debugging and operation; they were not removed.
4. Automatic packet generation is still not implemented.

## 8. Next Validation Step

Open VectorFL surface and check whether the first read is now:

```text
packet summary -> send -> latest return summary
```

rather than:

```text
all internal fields -> all queues -> all return artifacts
```

If the page still feels heavy, the next patch should reduce the right support column or move older support queues lower. It should not add new features.
