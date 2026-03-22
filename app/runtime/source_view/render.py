from __future__ import annotations

from typing import Dict, Optional
import json


def render_source_fragment_html(data: Optional[Dict[str, object]] = None, api_path: str = "/api/source") -> str:
    payload_block = (
        f'<script id="source-data" type="application/json">{json.dumps(data, ensure_ascii=False)}</script>'
        if data is not None
        else ""
    )
    bootstrap = (
        "const embedded = document.getElementById('source-data');\n"
        "const data = embedded ? JSON.parse(embedded.textContent) : await (await fetch('"
        + api_path +
        "')).json();"
    )
    return """<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Source Fragment View</title>
  <style>
    body { margin: 0; font-family: Georgia, serif; background: #f7f1e8; color: #1f2937; }
    .page { max-width: 1200px; margin: 0 auto; padding: 24px; }
    .source { background: #fffaf3; border: 1px solid #d8ccb9; border-radius: 16px; padding: 16px; margin-bottom: 18px; }
    .source.target { border-color: #8b5e34; box-shadow: 0 10px 20px rgba(73,52,33,0.08); }
    .meta { color: #6b7280; font-size: 14px; margin-bottom: 12px; }
    .summary-strip { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 12px; margin-bottom: 18px; }
    .summary-card { background: #fffaf3; border: 1px solid #d8ccb9; border-radius: 14px; padding: 12px; }
    .summary-card h3 { margin: 0 0 8px; font-size: 13px; color: #6d4c2f; text-transform: uppercase; letter-spacing: 0.04em; }
    .return-bar { display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 14px; }
    .return-link { display: inline-block; padding: 8px 12px; border-radius: 999px; border: 1px solid #d8ccb9; background: #fff8ef; color: #6d4c2f; text-decoration: none; font-size: 12px; }
    pre { white-space: pre-wrap; word-break: break-word; background: #fff; padding: 12px; border-radius: 12px; border: 1px solid #e5dccd; }
    .fragment { border-top: 1px solid #eadfce; padding-top: 10px; margin-top: 10px; }
    .fragment.target { border: 1px solid #8b5e34; border-radius: 12px; padding: 10px; background: #fffdf8; }
    .chips { display: flex; gap: 8px; flex-wrap: wrap; margin: 8px 0; }
    .chip { background: #efe4d2; border-radius: 999px; padding: 4px 8px; font-size: 12px; }
    .status { background: #fffaf3; border: 1px solid #d8ccb9; border-radius: 14px; padding: 10px 12px; margin-bottom: 16px; color: #6d4c2f; }
  </style>
</head>
<body>
  <div id="app"></div>
  """ + payload_block + """
  <script>
    (async () => {
      """ + bootstrap + """
      const app = document.getElementById("app");
      const page = document.createElement("div");
      page.className = "page";
      const params = new URLSearchParams(window.location.search);
      const requestedFragmentId = params.get("fragment_id");
      const requestedSourceRef = params.get("source_ref");
      const requestedFrom = params.get("from");
      const requestedReturnHref = params.get("return_href");
      const requestedReturnLabel = params.get("return_label");
      const originRoute = params.get("origin_route");
      const originLocalSpaceId = params.get("origin_local_space_id");
      const originRegionLabel = params.get("origin_region_label");
      const originBridgeId = params.get("origin_bridge_id");
      const originSourceRef = params.get("origin_source_ref");
      const originFragmentId = params.get("origin_fragment_id");
      const originDustId = params.get("origin_dust_id");
      const status = document.createElement("div");
      status.className = "status";
      status.style.display = "none";
      page.appendChild(status);
      const returnBar = document.createElement("div");
      returnBar.className = "return-bar";
      const addReturnLink = (href, label) => {
        const link = document.createElement("a");
        link.className = "return-link";
        link.href = href;
        link.textContent = label;
        returnBar.appendChild(link);
      };
      if (requestedReturnHref) {
        addReturnLink(requestedReturnHref, requestedReturnLabel || "Back");
      } else if (requestedFrom === "atlas") {
        addReturnLink("/atlas", "Back to Atlas");
      } else if (requestedFrom === "operator") {
        addReturnLink("/", "Back to Operator");
      } else {
        addReturnLink("/", "Operator");
        addReturnLink("/atlas", "Atlas");
      }
      page.appendChild(returnBar);
      const contextBar = document.createElement("div");
      contextBar.className = "chips";
      contextBar.style.marginBottom = "14px";
      const pushContextChip = (label, value) => {
        if (!value) return;
        const chip = document.createElement("span");
        chip.className = "chip";
        chip.textContent = `${label}: ${value}`;
        contextBar.appendChild(chip);
      };
      pushContextChip("origin", originRoute || requestedFrom);
      pushContextChip("region", originRegionLabel);
      pushContextChip("local_space", originLocalSpaceId);
      pushContextChip("bridge", originBridgeId);
      pushContextChip("source_ref", originSourceRef);
      pushContextChip("fragment", originFragmentId);
      pushContextChip("dust", originDustId);
      if (contextBar.childElementCount) page.appendChild(contextBar);
      const summary = document.createElement("div");
      summary.className = "meta";
      summary.textContent = `sources ${data.summary.source_count} / fragments ${data.summary.fragment_count}`;
      page.appendChild(summary);
      let matchedFragment = false;
      let matchedSource = false;
      let focusedSummary = null;
      const buildFragmentCompactSummary = (fragment) => {
        const promotion = fragment.canonical_promotion || { available: false, items: [] };
        const dropped = fragment.dropped_weak_anchor_state || { available: false, items: [] };
        const disagreement = fragment.observer_disagreement || { available: false, items: [] };
        const lineage = fragment.ingest_lineage || {};
        const lineageItems = [
          lineage.ingest_batch_id || "",
          lineage.ingest_session_id || "",
          lineage.ingest_input_path || "",
          ...((lineage.provenance_steps || []).slice(0, 2))
        ].filter(Boolean).slice(0, 3);
        return {
          canonical_promotion: {
            state: promotion.available ? (promotion.items && promotion.items.length ? "present" : "none") : "not_available_yet",
            items: (promotion.items || []).slice(0, 3),
          },
          dropped_weak: {
            state: dropped.available === false ? "not_available_yet" : ((dropped.items || []).length ? "present" : "none"),
            items: (dropped.items || []).slice(0, 3),
          },
          observer_disagreement: {
            state: disagreement.available ? ((disagreement.items || []).length ? "present" : "none") : "not_available_yet",
            items: (disagreement.items || []).slice(0, 3).map((item) => item.summary || String(item)),
          },
          ingest_lineage: {
            state: lineageItems.length ? "present" : "not_available_yet",
            items: lineageItems,
          },
        };
      };
      if (requestedFragmentId) {
        for (const source of (data.sources || [])) {
          const foundFragment = (source.fragments || []).find((fragment) => fragment.fragment_id === requestedFragmentId);
          if (foundFragment) {
            focusedSummary = buildFragmentCompactSummary(foundFragment);
            break;
          }
        }
      }
      if (!focusedSummary && requestedSourceRef) {
        const found = (data.sources || []).find((source) => source.source_path === requestedSourceRef);
        if (found && found.compact_summary) {
          focusedSummary = found.compact_summary;
        }
      }
      const compactSummary = focusedSummary || data.compact_summary || {};
      const summaryStrip = document.createElement("div");
      summaryStrip.className = "summary-strip";
      const renderSummaryCard = (title, payload, formatter) => {
        const card = document.createElement("div");
        card.className = "summary-card";
        const heading = document.createElement("h3");
        heading.textContent = title;
        card.appendChild(heading);
        const chips = document.createElement("div");
        chips.className = "chips";
        const state = (payload && payload.state) || "not_available_yet";
        if (state === "not_available_yet") {
          const chip = document.createElement("span");
          chip.className = "chip";
          chip.textContent = "not available yet";
          chips.appendChild(chip);
        } else if (state === "none") {
          const chip = document.createElement("span");
          chip.className = "chip";
          chip.textContent = "none";
          chips.appendChild(chip);
        } else {
          (payload.items || []).slice(0, 3).forEach((item) => {
            const chip = document.createElement("span");
            chip.className = "chip";
            chip.textContent = formatter(item);
            chips.appendChild(chip);
          });
          if ((payload.overflow_count || 0) > 0) {
            const chip = document.createElement("span");
            chip.className = "chip";
            chip.textContent = `+${payload.overflow_count} more`;
            chips.appendChild(chip);
          }
          if (!chips.childElementCount) {
            const chip = document.createElement("span");
            chip.className = "chip";
            chip.textContent = "present";
            chips.appendChild(chip);
          }
        }
        card.appendChild(chips);
        return card;
      };
      summaryStrip.appendChild(
        renderSummaryCard("Canonical Promotion", compactSummary.canonical_promotion || {}, (item) => `${item.anchor_type}:${item.display_label}`)
      );
      summaryStrip.appendChild(
        renderSummaryCard("Dropped Weak", compactSummary.dropped_weak || {}, (item) => String(item))
      );
      summaryStrip.appendChild(
        renderSummaryCard("Observer Disagreement", compactSummary.observer_disagreement || {}, (item) => String(item))
      );
      summaryStrip.appendChild(
        renderSummaryCard("Ingest Lineage", compactSummary.ingest_lineage || {}, (item) => String(item))
      );
      page.appendChild(summaryStrip);
      data.sources.forEach((source) => {
        const section = document.createElement("section");
        section.className = "source";
        const isTargetSource = requestedSourceRef && source.source_path === requestedSourceRef;
        if (isTargetSource) {
          section.classList.add("target");
          matchedSource = true;
        }
        const title = document.createElement("h2");
        title.textContent = source.source_path || "(unknown source)";
        section.appendChild(title);
        const meta = document.createElement("div");
        meta.className = "meta";
        meta.textContent = `fragments ${source.fragment_count}`;
        section.appendChild(meta);
        const sourceText = document.createElement("pre");
        sourceText.textContent = source.source_text || "(source text unavailable)";
        section.appendChild(sourceText);
        source.fragments.forEach((fragment) => {
          const card = document.createElement("div");
          card.className = "fragment";
          if (requestedFragmentId && fragment.fragment_id === requestedFragmentId) {
            card.classList.add("target");
            matchedFragment = true;
          }
          const head = document.createElement("strong");
          head.textContent = fragment.fragment_id;
          card.appendChild(head);
          const chips = document.createElement("div");
          chips.className = "chips";
          [fragment.scene, fragment.flow, fragment.time, fragment.unit_scale].filter(Boolean).forEach((value) => {
            const chip = document.createElement("span");
            chip.className = "chip";
            chip.textContent = value;
            chips.appendChild(chip);
          });
          [fragment.metadata && fragment.metadata.ingest_batch_id, fragment.metadata && fragment.metadata.ingest_session_id].filter(Boolean).forEach((value) => {
            const chip = document.createElement("span");
            chip.className = "chip";
            chip.textContent = value;
            chips.appendChild(chip);
          });
          card.appendChild(chips);
          if (fragment.anchors && fragment.anchors.length) {
            const anchorRow = document.createElement("div");
            anchorRow.className = "chips";
            fragment.anchors.forEach((anchor) => {
              const chip = document.createElement("span");
              chip.className = "chip";
              chip.textContent = `${anchor.anchor_type}:${anchor.key}`;
              chip.title = `${anchor.label || anchor.value} | origin=${anchor.origin} | confidence=${anchor.confidence}`;
              anchorRow.appendChild(chip);
            });
            card.appendChild(anchorRow);
          }
          if (fragment.canonical_promotion && fragment.canonical_promotion.available) {
            const promoHead = document.createElement("div");
            promoHead.className = "meta";
            promoHead.textContent = `canonical promotion ${fragment.canonical_promotion.count}`;
            card.appendChild(promoHead);
            const promoRow = document.createElement("div");
            promoRow.className = "chips";
            (fragment.canonical_promotion.items || []).forEach((item) => {
              const chip = document.createElement("span");
              chip.className = "chip";
              chip.textContent = `${item.anchor_type}:${item.display_label}`;
              chip.title = `${item.canonical_key} | origin=${item.origin} | confidence=${item.confidence}`;
              promoRow.appendChild(chip);
            });
            card.appendChild(promoRow);
          }
          if (fragment.dropped_weak_anchor_state) {
            const droppedHead = document.createElement("div");
            droppedHead.className = "meta";
            droppedHead.textContent = "dropped weak anchors";
            card.appendChild(droppedHead);
            const droppedRow = document.createElement("div");
            droppedRow.className = "chips";
            if (fragment.dropped_weak_anchor_state.available === false) {
              const chip = document.createElement("span");
              chip.className = "chip";
              chip.textContent = "not available yet";
              droppedRow.appendChild(chip);
            } else if ((fragment.dropped_weak_anchor_state.items || []).length) {
              (fragment.dropped_weak_anchor_state.items || []).forEach((value) => {
                const chip = document.createElement("span");
                chip.className = "chip";
                chip.textContent = value;
                droppedRow.appendChild(chip);
              });
            } else {
              const chip = document.createElement("span");
              chip.className = "chip";
              chip.textContent = "none";
              droppedRow.appendChild(chip);
            }
            card.appendChild(droppedRow);
          }
          if (fragment.measurement_summary && fragment.measurement_summary.count) {
            const msrRow = document.createElement("div");
            msrRow.className = "chips";
            fragment.measurement_summary.types.forEach((value) => {
              const chip = document.createElement("span");
              chip.className = "chip";
              chip.textContent = `measurement:${value}`;
              msrRow.appendChild(chip);
            });
            card.appendChild(msrRow);
          }
          if (fragment.measurement_summary && fragment.measurement_summary.anchor_history && fragment.measurement_summary.anchor_history.version_count) {
            const hist = fragment.measurement_summary.anchor_history;
            const histRow = document.createElement("div");
            histRow.className = "chips";
            [
              `anchor_versions:${hist.version_count}`,
              hist.latest_batch_id ? `latest:${hist.latest_batch_id}` : '',
              hist.previous_batch_id ? `previous:${hist.previous_batch_id}` : '',
            ].filter(Boolean).forEach((value) => {
              const chip = document.createElement("span");
              chip.className = "chip";
              chip.textContent = value;
              histRow.appendChild(chip);
            });
            card.appendChild(histRow);
            if ((hist.added_keys && hist.added_keys.length) || (hist.removed_keys && hist.removed_keys.length)) {
              const deltaRow = document.createElement("div");
              deltaRow.className = "chips";
              (hist.added_keys || []).forEach((value) => {
                const chip = document.createElement("span");
                chip.className = "chip";
                chip.textContent = `added:${value}`;
                deltaRow.appendChild(chip);
              });
              (hist.removed_keys || []).forEach((value) => {
                const chip = document.createElement("span");
                chip.className = "chip";
                chip.textContent = `removed:${value}`;
                deltaRow.appendChild(chip);
              });
              card.appendChild(deltaRow);
            }
          }
          if (fragment.measurement_summary && fragment.measurement_summary.observer_summary && fragment.measurement_summary.observer_summary.count) {
            const observer = fragment.measurement_summary.observer_summary;
            const obsRow = document.createElement("div");
            obsRow.className = "chips";
            [
              `observer:${observer.count}`,
              observer.revision_count ? `revision:${observer.revision_count}` : '',
              observer.deferred_count ? `deferred:${observer.deferred_count}` : '',
              observer.rejected_count ? `rejected:${observer.rejected_count}` : '',
              observer.accepted_count ? `accepted:${observer.accepted_count}` : '',
            ].filter(Boolean).forEach((value) => {
              const chip = document.createElement("span");
              chip.className = "chip";
              chip.textContent = value;
              obsRow.appendChild(chip);
            });
            card.appendChild(obsRow);
            (observer.records || []).forEach((record) => {
              const meta = document.createElement("div");
              meta.className = "meta";
              meta.textContent = `${record.measurement_type} | ${record.column_key} | ${record.evidence_text}`;
              card.appendChild(meta);
            });
          }
          if (fragment.observer_disagreement && fragment.observer_disagreement.available) {
            const disagreementHead = document.createElement("div");
            disagreementHead.className = "meta";
            disagreementHead.textContent = "observer disagreement";
            card.appendChild(disagreementHead);
            const disagreementRow = document.createElement("div");
            disagreementRow.className = "chips";
            const merged = fragment.observer_disagreement.merged || {};
            const mergedChip = document.createElement("span");
            mergedChip.className = "chip";
            mergedChip.textContent = `merged:${merged.scene || '-'} / ${merged.role || '-'}`;
            disagreementRow.appendChild(mergedChip);
            (fragment.observer_disagreement.items || []).forEach((item) => {
              const chip = document.createElement("span");
              chip.className = "chip";
              chip.textContent = item.summary;
              disagreementRow.appendChild(chip);
            });
            if (!(fragment.observer_disagreement.items || []).length) {
              const chip = document.createElement("span");
              chip.className = "chip";
              chip.textContent = "no explicit disagreement";
              disagreementRow.appendChild(chip);
            }
            card.appendChild(disagreementRow);
          }
          if (fragment.ingest_lineage) {
            const lineageHead = document.createElement("div");
            lineageHead.className = "meta";
            lineageHead.textContent = "ingest lineage";
            card.appendChild(lineageHead);
            const lineageRow = document.createElement("div");
            lineageRow.className = "chips";
            [
              fragment.ingest_lineage.ingest_batch_id ? `batch:${fragment.ingest_lineage.ingest_batch_id}` : '',
              fragment.ingest_lineage.ingest_session_id ? `session:${fragment.ingest_lineage.ingest_session_id}` : '',
              fragment.ingest_lineage.ingest_input_path ? `input:${fragment.ingest_lineage.ingest_input_path}` : '',
            ].filter(Boolean).forEach((value) => {
              const chip = document.createElement("span");
              chip.className = "chip";
              chip.textContent = value;
              lineageRow.appendChild(chip);
            });
            (fragment.ingest_lineage.provenance_steps || []).forEach((value) => {
              const chip = document.createElement("span");
              chip.className = "chip";
              chip.textContent = `step:${value}`;
              lineageRow.appendChild(chip);
            });
            card.appendChild(lineageRow);
          }
          if (fragment.provenance_log && fragment.provenance_log.length) {
            const provRow = document.createElement("div");
            provRow.className = "chips";
            fragment.provenance_log.forEach((entry) => {
              const chip = document.createElement("span");
              chip.className = "chip";
              chip.textContent = `step:${entry.step}`;
              chip.title = entry.note || "";
              provRow.appendChild(chip);
            });
            card.appendChild(provRow);
          }
          if (fragment.related_cross_source && fragment.related_cross_source.length) {
            const relatedHead = document.createElement("div");
            relatedHead.className = "meta";
            relatedHead.textContent = `cross-source related ${fragment.related_cross_source.length}`;
            card.appendChild(relatedHead);
            fragment.related_cross_source.forEach((rel) => {
              const relRow = document.createElement("div");
              relRow.className = "chips";
              [
                rel.fragment_id,
                rel.source_path,
                rel.scene,
                rel.flow,
                `shared:${rel.shared_anchor_count}`,
                rel.family_match_count ? `family:${rel.family_match_count}` : '',
                rel.observer_relation && rel.observer_relation.relation_status ? `observer:${rel.observer_relation.relation_status}` : '',
              ].filter(Boolean).forEach((value) => {
                const chip = document.createElement("span");
                chip.className = "chip";
                chip.textContent = value;
                relRow.appendChild(chip);
              });
              (rel.shared_anchor_keys || []).slice(0, 4).forEach((value) => {
                const chip = document.createElement("span");
                chip.className = "chip";
                chip.textContent = `anchor:${value}`;
                relRow.appendChild(chip);
              });
              (rel.shared_anchor_families || []).slice(0, 3).forEach((value) => {
                const chip = document.createElement("span");
                chip.className = "chip";
                chip.textContent = `family:${value}`;
                relRow.appendChild(chip);
              });
              if (rel.observer_relation && rel.observer_relation.reason) {
                const meta = document.createElement("div");
                meta.className = "meta";
                meta.textContent = rel.observer_relation.reason;
                card.appendChild(meta);
              }
              card.appendChild(relRow);
            });
          }
          if (fragment.related_same_source && fragment.related_same_source.length) {
            const relatedHead = document.createElement("div");
            relatedHead.className = "meta";
            relatedHead.textContent = `same-source related ${fragment.related_same_source.length}`;
            card.appendChild(relatedHead);
            fragment.related_same_source.forEach((rel) => {
              const relRow = document.createElement("div");
              relRow.className = "chips";
              [
                rel.fragment_id,
                rel.scene,
                rel.flow,
                `shared:${rel.shared_anchor_count}`,
                rel.family_match_count ? `family:${rel.family_match_count}` : '',
                rel.observer_relation && rel.observer_relation.relation_status ? `observer:${rel.observer_relation.relation_status}` : '',
              ].filter(Boolean).forEach((value) => {
                const chip = document.createElement("span");
                chip.className = "chip";
                chip.textContent = value;
                relRow.appendChild(chip);
              });
              (rel.shared_anchor_keys || []).slice(0, 4).forEach((value) => {
                const chip = document.createElement("span");
                chip.className = "chip";
                chip.textContent = `anchor:${value}`;
                relRow.appendChild(chip);
              });
              card.appendChild(relRow);
            });
          }
          const body = document.createElement("pre");
          body.textContent = fragment.raw_text;
          card.appendChild(body);
          section.appendChild(card);
        });
        page.appendChild(section);
      });
      if (requestedFragmentId) {
        status.style.display = "block";
        if (matchedFragment) {
          status.textContent = `fragment selected: ${requestedFragmentId}`;
        } else {
          status.textContent = `requested fragment not found: ${requestedFragmentId}`;
        }
      } else if (requestedSourceRef) {
        status.style.display = "block";
        if (matchedSource) {
          status.textContent = `source selected: ${requestedSourceRef}`;
        } else {
          status.textContent = `source_ref matched 없음: ${requestedSourceRef}`;
        }
      }
      app.appendChild(page);
      const target = document.querySelector('.fragment.target, .source.target');
      if (target) {
        target.scrollIntoView({ block: 'center' });
      }
    })();
  </script>
</body>
</html>
"""
