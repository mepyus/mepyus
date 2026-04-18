from __future__ import annotations

from typing import Dict, Optional
import json


def render_process_console_view_html(data: Optional[Dict[str, object]] = None, api_path: str = "/api/process-console") -> str:
    payload_block = (
        f'<script id="process-console-data" type="application/json">{json.dumps(data, ensure_ascii=False)}</script>'
        if data is not None
        else ""
    )
    bootstrap = (
        "const embedded = document.getElementById('process-console-data');\n"
        "const data = embedded ? JSON.parse(embedded.textContent) : await (await fetch('"
        + api_path +
        "')).json();"
    )
    return """<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Process Console</title>
  <style>
    body { margin: 0; font-family: Georgia, serif; background: #f5f1e8; color: #1f2937; }
    .page { display: grid; grid-template-columns: 280px 1fr 320px; gap: 16px; max-width: 1440px; margin: 0 auto; padding: 20px; }
    .top { grid-column: 1 / -1; background: #fffaf2; border: 1px solid #d7cab7; border-radius: 18px; padding: 16px; }
    .topbar { display: flex; gap: 10px; flex-wrap: wrap; margin-bottom: 12px; }
    .nav { display: inline-block; padding: 7px 12px; border-radius: 999px; border: 1px solid #d7cab7; text-decoration: none; color: #6c4d2f; background: #fff; }
    .badge-row, .chip-row { display: flex; gap: 8px; flex-wrap: wrap; }
    .badge, .chip { border-radius: 999px; padding: 5px 9px; font-size: 12px; background: #efe5d3; color: #5b422a; }
    .panel { background: #fffaf2; border: 1px solid #d7cab7; border-radius: 18px; padding: 14px; min-height: 280px; }
    .asset-card { padding: 10px; border-radius: 14px; border: 1px solid #e5dac8; background: #fff; margin-bottom: 10px; }
    .asset-card a { color: inherit; text-decoration: none; }
    .meta { color: #6b7280; font-size: 13px; }
    .section { margin-bottom: 14px; }
    .field { padding: 8px 0; border-top: 1px solid #efe5d3; }
    .field:first-child { border-top: 0; }
    .small { font-size: 13px; color: #6b7280; }
    .timeline-item { padding: 10px; border: 1px solid #e5dac8; border-radius: 12px; background: #fff; margin-bottom: 10px; }
    .diff-row { padding: 8px 0; border-top: 1px solid #efe5d3; }
    .diff-row:first-child { border-top: 0; }
    details { margin-top: 8px; }
    summary { cursor: pointer; color: #6c4d2f; }
    pre { white-space: pre-wrap; word-break: break-word; background: #fff; border: 1px solid #e5dac8; border-radius: 12px; padding: 10px; }
    .empty { color: #8b7355; font-style: italic; }
  </style>
</head>
<body>
  <div id="app"></div>
  """ + payload_block + """
  <script>
    (async () => {
      """ + bootstrap + """
      const app = document.getElementById('app');
      const page = document.createElement('div');
      page.className = 'page';

      const top = document.createElement('div');
      top.className = 'top';
      const topbar = document.createElement('div');
      topbar.className = 'topbar';
      [['/','graph'], ['/process-console','process-console'], ['/source','source'], ['/measurements','measurements']].forEach(([href, label]) => {
        const link = document.createElement('a');
        link.className = 'nav';
        link.href = href;
        link.textContent = label;
        topbar.appendChild(link);
      });
      top.appendChild(topbar);
      const title = document.createElement('div');
      title.innerHTML = `<strong>${data.header.asset_name || 'no_canonical_state_yet'}</strong> <span class="small">${data.header.source_type || ''}</span>`;
      top.appendChild(title);
      const badgeRow = document.createElement('div');
      badgeRow.className = 'badge-row';
      (data.header.badges || []).forEach((badge) => {
        const el = document.createElement('span');
        el.className = 'badge';
        el.textContent = `${badge.key}: ${badge.label}`;
        badgeRow.appendChild(el);
      });
      if (!(data.header.badges || []).length) {
        const empty = document.createElement('div');
        empty.className = 'empty';
        empty.textContent = 'no_canonical_state_yet';
        badgeRow.appendChild(empty);
      }
      top.appendChild(badgeRow);

      const attention = data.attention_queue || {};
      const attentionSection = document.createElement('div');
      attentionSection.className = 'section';
      attentionSection.innerHTML = `<h4>attention queue</h4><div class="meta">active=${(attention.counts || {}).active || 0} / resolved=${(attention.counts || {}).resolved || 0} / background=${(attention.counts || {}).background_summaries || 0}</div>`;
      const selectedAttention = attention.selected_asset_attention || null;
      if (selectedAttention) {
        const selectedCard = document.createElement('div');
        selectedCard.className = 'asset-card';
        if (selectedAttention.kind === 'active_item') {
          selectedCard.innerHTML = `<strong>selected asset attention</strong><div class="meta">${selectedAttention.queue_status || 'new'} / ${selectedAttention.priority_level || 'n/a'} / ${selectedAttention.attention_reason || 'n/a'}</div><div class="meta">${selectedAttention.diff_class || 'n/a'} / ${(selectedAttention.changed_fields || []).join(', ') || 'provenance_only'}</div>`;
        } else {
          const title = selectedAttention.kind === 'resolved_item' ? 'selected asset resolved attention' : 'selected asset background summary';
          selectedCard.innerHTML = `<strong>${title}</strong><div class="meta">${selectedAttention.summary || selectedAttention.resolution_reason || 'background_summary'}</div><div class="meta">${selectedAttention.queue_status || 'resolved'} / ${selectedAttention.priority_level || 'background'} / ${selectedAttention.attention_reason || 'n/a'}</div>`;
        }
        attentionSection.appendChild(selectedCard);
      }

      const attentionItems = document.createElement('div');
      attentionItems.className = 'chip-row';
      (attention.top_items || []).forEach((item) => {
        const link = document.createElement('a');
        link.className = 'nav';
        link.href = item.process_console_href || `/process-console?asset_id=${encodeURIComponent(item.asset_id)}`;
        link.textContent = `${item.asset_name}: ${item.priority_level}`;
        attentionItems.appendChild(link);
      });
      if (!(attention.top_items || []).length) {
        const empty = document.createElement('div');
        empty.className = 'empty';
        empty.textContent = 'no_high_attention_items';
        attentionItems.appendChild(empty);
      }
      attentionSection.appendChild(attentionItems);

      const backgroundItems = document.createElement('div');
      backgroundItems.className = 'small';
      const backgroundCount = ((attention.background_summaries || []).length || 0);
      backgroundItems.textContent = `background summaries: ${backgroundCount}`;
      attentionSection.appendChild(backgroundItems);

      const attentionMemory = attention.selected_asset_memory || null;
      const memorySection = document.createElement('div');
      memorySection.className = 'section';
      memorySection.innerHTML = '<h4>attention memory</h4>';
      if (attentionMemory) {
        const card = document.createElement('div');
        card.className = 'asset-card';
        card.innerHTML = `<strong>${attentionMemory.attention_pattern_summary || 'insufficient_attention_history'}</strong><div class="meta">total=${attentionMemory.total_attention_events || 0} / reopened=${attentionMemory.reopened_attention_count || 0} / suppressed=${attentionMemory.suppressed_attention_count || 0}</div><div class="meta">provenance density=${attentionMemory.provenance_only_repeat_density || 0} / dominant shift=${(attentionMemory.dominant_shift_types || []).join(', ') || 'n/a'}</div>`;
        memorySection.appendChild(card);
      } else {
        const empty = document.createElement('div');
        empty.className = 'empty';
        empty.textContent = 'insufficient_attention_history';
        memorySection.appendChild(empty);
      }
      attentionSection.appendChild(memorySection);
      top.appendChild(attentionSection);
      page.appendChild(top);

      const rail = document.createElement('div');
      rail.className = 'panel';
      rail.innerHTML = '<h3>Asset Rail</h3>';
      (data.asset_rail || []).forEach((card) => {
        const box = document.createElement('div');
        box.className = 'asset-card';
        box.innerHTML = `<a href="/process-console?asset_id=${encodeURIComponent(card.asset_id)}"><strong>${card.asset_name}</strong><div class="meta">${card.packet_texture_label} / ${card.maturation_state_label}</div><div class="meta">${card.traceability_status_label} / ${card.emergence_status_label}</div></a>`;
        rail.appendChild(box);
      });
      page.appendChild(rail);

      const center = document.createElement('div');
      center.className = 'panel';
      center.innerHTML = '<h3>State Panel</h3>';
      if (data.state_panel.state === 'state_unavailable') {
        const empty = document.createElement('div');
        empty.className = 'empty';
        empty.textContent = 'no_canonical_state_yet';
        center.appendChild(empty);
      } else {
        (data.state_panel.canonical_fields || []).forEach((field) => {
          const row = document.createElement('div');
          row.className = 'field';
          row.innerHTML = `<strong>${field.key}</strong><div class="meta">${field.label}</div>`;
          center.appendChild(row);
        });
        const notes = document.createElement('div');
        notes.className = 'section';
        notes.innerHTML = `<h4>state notes</h4><pre>${data.state_panel.state_notes || ''}</pre>`;
        center.appendChild(notes);
        const evidence = document.createElement('div');
        evidence.className = 'section';
        evidence.innerHTML = '<h4>evidence refs</h4>';
        const evidenceList = document.createElement('div');
        evidenceList.className = 'chip-row';
        (data.state_panel.evidence_refs || []).forEach((ref) => {
          const chip = document.createElement('span');
          chip.className = 'chip';
          chip.textContent = `${ref.ref_kind}: ${ref.ref_id}`;
          evidenceList.appendChild(chip);
        });
        evidence.appendChild(evidenceList);
        center.appendChild(evidence);

        const historySummary = document.createElement('div');
        historySummary.className = 'section';
        const hs = data.state_panel.history_summary || {};
        historySummary.innerHTML = `<h4>history summary</h4><div class="meta">recent updates: ${hs.recent_update_count || 0}</div><div class="meta">latest trigger: ${hs.latest_update_trigger_type || 'n/a'}</div><div class="meta">latest reason: ${hs.latest_update_reason || 'n/a'}</div><div class="meta">change kind: ${hs.latest_change_kind || 'n/a'}</div>`;
        const hsBadges = document.createElement('div');
        hsBadges.className = 'chip-row';
        (hs.interpretation_badges || []).forEach((badge) => {
          const chip = document.createElement('span');
          chip.className = 'chip';
          chip.textContent = badge;
          hsBadges.appendChild(chip);
        });
        historySummary.appendChild(hsBadges);
        center.appendChild(historySummary);

        const diffSummary = document.createElement('div');
        diffSummary.className = 'section';
        const ds = data.state_panel.diff_summary || {};
        diffSummary.innerHTML = `<h4>compare to previous</h4><div class="meta">${ds.diff_class || ds.state || 'n/a'} / changed fields: ${ds.changed_field_count || 0}</div><div class="meta">${ds.provenance_only ? 'canonical drift 없음, provenance 강화' : 'canonical change detected or pending comparison'}</div>`;
        const dsBadges = document.createElement('div');
        dsBadges.className = 'chip-row';
        (ds.interpretation_badges || []).forEach((badge) => {
          const chip = document.createElement('span');
          chip.className = 'chip';
          chip.textContent = badge;
          dsBadges.appendChild(chip);
        });
        diffSummary.appendChild(dsBadges);
        if (ds.compare_to_previous_href) {
          const link = document.createElement('a');
          link.className = 'nav';
          link.href = ds.compare_to_previous_href;
          link.textContent = 'open latest vs previous';
          diffSummary.appendChild(link);
        }
        center.appendChild(diffSummary);
      }
      page.appendChild(center);

      const right = document.createElement('div');
      right.className = 'panel';
      right.innerHTML = '<h3>History & Compare</h3>';
      const preview = document.createElement('div');
      preview.className = 'section';
      preview.innerHTML = `<div><strong>latest preview</strong></div><div class="meta">${(data.latest_state_preview || {}).packet_texture_label || 'n/a'} / ${(data.latest_state_preview || {}).maturation_state_label || 'n/a'}</div><div class="meta">${(data.latest_state_preview || {}).traceability_status_label || 'n/a'} / ${((data.latest_state_preview || {}).updated_at || '')}</div>`;
      right.appendChild(preview);

      const lineage = document.createElement('div');
      lineage.className = 'section';
      const history = data.history_drilldown || {};
      const latestLink = history.latest_lineage_link || {};
      lineage.innerHTML = `<div><strong>latest lineage</strong></div><div class="meta">${latestLink.summary || 'no_history_yet'}</div><div class="meta">${latestLink.latest_update_trigger_type || 'n/a'} / ${latestLink.latest_update_reason || 'n/a'}</div><div class="meta">${latestLink.latest_updated_at || ''}</div>`;
      const lineBadges = document.createElement('div');
      lineBadges.className = 'chip-row';
      ((data.history_summary || {}).interpretation_badges || []).forEach((badge) => {
        const chip = document.createElement('span');
        chip.className = 'chip';
        chip.textContent = badge;
        lineBadges.appendChild(chip);
      });
      lineage.appendChild(lineBadges);
      right.appendChild(lineage);

      const timeline = document.createElement('div');
      timeline.className = 'section';
      timeline.innerHTML = '<h4>recent history</h4>';
      ((history || {}).items || []).forEach((item) => {
        const block = document.createElement('div');
        block.className = 'timeline-item';
        const chips = (item.changed_fields || []).length ? item.changed_fields.join(', ') : 'provenance_only_update';
        block.innerHTML = `<div><strong>${item.updated_at || ''}</strong></div><div class="meta">${item.trigger_badge || 'unknown'} / ${item.update_reason || 'n/a'}</div><div class="meta">${chips}</div>`;
        const itemBadges = document.createElement('div');
        itemBadges.className = 'chip-row';
        (item.interpretation_badges || []).forEach((badge) => {
          const chip = document.createElement('span');
          chip.className = 'chip';
          chip.textContent = badge;
          itemBadges.appendChild(chip);
        });
        block.appendChild(itemBadges);
        if (item.compare_to_previous_href) {
          const link = document.createElement('a');
          link.className = 'nav';
          link.href = item.compare_to_previous_href;
          link.textContent = 'compare to previous';
          block.appendChild(link);
        }
        const details = document.createElement('details');
        const summary = document.createElement('summary');
        summary.textContent = 'lineage details';
        details.appendChild(summary);

        const labels = document.createElement('div');
        labels.className = 'chip-row';
        (item.change_labels || []).forEach((label) => {
          const chip = document.createElement('span');
          chip.className = 'chip';
          chip.textContent = label;
          labels.appendChild(chip);
        });
        details.appendChild(labels);

        const canonical = document.createElement('pre');
        canonical.textContent = JSON.stringify(item.canonical_snapshot || {}, null, 2);
        details.appendChild(canonical);

        const refs = document.createElement('div');
        refs.className = 'chip-row';
        (item.evidence_refs || []).forEach((ref) => {
          const chip = document.createElement('span');
          chip.className = 'chip';
          chip.textContent = `${ref.ref_kind}: ${ref.ref_id}`;
          refs.appendChild(chip);
        });
        details.appendChild(refs);

        const exp = document.createElement('div');
        exp.className = 'meta';
        exp.textContent = item.experimental_namespace_present ? 'experimental namespace present (hidden by default)' : 'no experimental namespace';
        details.appendChild(exp);

        block.appendChild(details);
        timeline.appendChild(block);
      });
      if (!((history || {}).items || []).length) {
        const empty = document.createElement('div');
        empty.className = 'empty';
        empty.textContent = 'no_history_yet';
        timeline.appendChild(empty);
      }
      right.appendChild(timeline);

      const compacted = document.createElement('div');
      compacted.className = 'section';
      compacted.innerHTML = '<h4>compacted older history</h4>';
      const older = (((history || {}).older_compacted || {}).older_nodes || []);
      older.forEach((node) => {
        const card = document.createElement('div');
        card.className = 'asset-card';
        if (node.node_type === 'summary') {
          card.innerHTML = `<strong>${node.covered_record_count} compacted records</strong><div class="meta">${node.covered_range_start || ''} -> ${node.covered_range_end || ''}</div><div class="meta">provenance_only=${node.provenance_only_count || 0}, canonical_change=${node.canonical_change_count || 0}</div><div class="meta">${(node.notable_shift_types || []).join(', ') || 'no notable shift types'}</div>`;
        } else if (node.node_type === 'anchor') {
          const item = node.item || {};
          card.innerHTML = `<strong>anchor: ${item.updated_at || ''}</strong><div class="meta">${item.trigger_badge || 'unknown'} / ${item.update_reason || 'n/a'}</div><div class="meta">${(item.interpretation_badges || []).join(', ') || 'anchor'}</div>`;
        }
        compacted.appendChild(card);
      });
      if (!older.length) {
        const empty = document.createElement('div');
        empty.className = 'empty';
        empty.textContent = 'no_compacted_older_history';
        compacted.appendChild(empty);
      }
      right.appendChild(compacted);

      const diffPanel = document.createElement('div');
      diffPanel.className = 'section';
      diffPanel.innerHTML = '<h4>state change diff</h4>';
      const diff = data.state_change_diff || {};
      if (diff.state === 'loaded') {
        const summary = document.createElement('div');
        summary.innerHTML = `<div><strong>${diff.diff_class}</strong></div><div class="meta">${diff.current_trigger || 'n/a'} / ${diff.current_reason || 'n/a'}</div><div class="meta">${diff.previous_updated_at || 'n/a'} -> ${diff.current_updated_at || 'n/a'}</div><div class="meta">${diff.provenance_only ? 'provenance_only_update' : (diff.changed_fields || []).join(', ')}</div>`;
        diffPanel.appendChild(summary);

        const changedChips = document.createElement('div');
        changedChips.className = 'chip-row';
        (diff.changed_fields || []).forEach((field) => {
          const chip = document.createElement('span');
          chip.className = 'chip';
          chip.textContent = field;
          changedChips.appendChild(chip);
        });
        if (!(diff.changed_fields || []).length) {
          const chip = document.createElement('span');
          chip.className = 'chip';
          chip.textContent = 'provenance_only';
          changedChips.appendChild(chip);
        }
        diffPanel.appendChild(changedChips);

        const diffBadges = document.createElement('div');
        diffBadges.className = 'chip-row';
        (diff.interpretation_badges || []).forEach((badge) => {
          const chip = document.createElement('span');
          chip.className = 'chip';
          chip.textContent = badge;
          diffBadges.appendChild(chip);
        });
        diffPanel.appendChild(diffBadges);

        (diff.field_rows || []).filter((row) => row.changed).forEach((row) => {
          const field = document.createElement('div');
          field.className = 'diff-row';
          let body = `<strong>${row.field_name}</strong><div class="meta">${JSON.stringify(row.old_value)} -> ${JSON.stringify(row.new_value)}</div>`;
          if (row.added_items || row.removed_items) {
            body += `<div class="meta">added: ${(row.added_items || []).join(', ') || 'none'} / removed: ${(row.removed_items || []).join(', ') || 'none'}</div>`;
          }
          field.innerHTML = body;
          diffPanel.appendChild(field);
        });

        if (diff.provenance_only) {
          const thin = document.createElement('div');
          thin.className = 'meta';
          thin.textContent = 'canonical 8필드 변화 없음. provenance와 evidence만 강화된 update.';
          diffPanel.appendChild(thin);
        }
      } else if (diff.state === 'no_previous_state') {
        const empty = document.createElement('div');
        empty.className = 'empty';
        empty.textContent = 'no_previous_state';
        diffPanel.appendChild(empty);
      } else {
        const empty = document.createElement('div');
        empty.className = 'empty';
        empty.textContent = 'state_unavailable';
        diffPanel.appendChild(empty);
      }
      right.appendChild(diffPanel);

      const compareList = document.createElement('div');
      compareList.className = 'section';
      compareList.innerHTML = '<h4>compare entry</h4>';
      ((data.compare_entry || {}).related_assets || []).forEach((item) => {
        const card = document.createElement('div');
        card.className = 'asset-card';
        card.innerHTML = `<strong>${item.asset_name}</strong><div class="meta">${item.packet_texture} / ${item.maturation_state}</div><div class="meta">${(item.reasons || []).join(', ')}</div>`;
        compareList.appendChild(card);
      });
      if (!((data.compare_entry || {}).related_assets || []).length) {
        const empty = document.createElement('div');
        empty.className = 'empty';
        empty.textContent = 'no_compare_candidates';
        compareList.appendChild(empty);
      }
      right.appendChild(compareList);
      page.appendChild(right);

      app.appendChild(page);
    })();
  </script>
</body>
</html>
"""
