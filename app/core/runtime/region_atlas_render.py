from __future__ import annotations

from typing import Dict, Optional
import json


def render_region_atlas_html(data: Optional[Dict[str, object]] = None, api_path: str = "/api/atlas") -> str:
    payload_block = (
        f'<script id="atlas-data" type="application/json">{json.dumps(data, ensure_ascii=False)}</script>'
        if data is not None
        else ""
    )
    bootstrap = (
        "const embedded = document.getElementById('atlas-data');\n"
        "const data = embedded ? JSON.parse(embedded.textContent) : await (await fetch('"
        + api_path +
        "')).json();"
    )
    return """<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Region Atlas</title>
  <style>
    body { margin: 0; font-family: Georgia, serif; background: #f4ede2; color: #1f2937; }
    .page { max-width: 1380px; margin: 0 auto; padding: 24px; }
    .topbar { display: flex; gap: 12px; flex-wrap: wrap; margin-bottom: 18px; }
    .link { display: inline-block; padding: 8px 12px; border-radius: 999px; background: #fff8ef; border: 1px solid #d8ccb9; color: #6d4c2f; text-decoration: none; }
    .summary { color: #6b7280; margin-bottom: 18px; }
    .grid { display: grid; grid-template-columns: minmax(0, 1fr) 340px; gap: 20px; }
    .main-column { display: grid; gap: 18px; }
    .regions { display: grid; grid-template-columns: repeat(auto-fit, minmax(290px, 1fr)); gap: 16px; }
    .card { background: rgba(255,250,242,0.94); border: 1px solid #d8ccb9; border-radius: 18px; padding: 16px; box-shadow: 0 12px 24px rgba(73, 52, 33, 0.06); cursor: pointer; }
    .card.selected { border-color: #8b5e34; box-shadow: 0 14px 28px rgba(73, 52, 33, 0.12); }
    .meta { color: #6b7280; font-size: 13px; margin-bottom: 8px; }
    .chips { display: flex; gap: 8px; flex-wrap: wrap; margin: 8px 0 12px; }
    .chip { background: #efe4d2; border-radius: 999px; padding: 4px 8px; font-size: 12px; }
    .landmark { padding: 8px 10px; border-radius: 12px; background: #fff; border: 1px solid #eadfce; margin-top: 8px; font-size: 13px; }
    .bridge-atlas { background: rgba(255,250,242,0.94); border: 1px solid #d8ccb9; border-radius: 18px; padding: 16px; }
    .bridge-list { background: rgba(255,250,242,0.94); border: 1px solid #d8ccb9; border-radius: 18px; padding: 16px; position: sticky; top: 18px; height: fit-content; }
    .bridge { padding: 10px 0; border-top: 1px solid #eadfce; }
    .bridge:first-child { border-top: 0; padding-top: 0; }
    .strength { color: #6d4c2f; font-size: 12px; }
    .inspector-block { margin-top: 14px; }
    .inspector-block h3 { margin: 0 0 8px; font-size: 14px; color: #6d4c2f; text-transform: uppercase; letter-spacing: 0.04em; }
    .source-link { display: inline-block; margin: 4px 6px 0 0; color: #6d4c2f; text-decoration: none; }
    .bridge-actions { display: flex; gap: 8px; flex-wrap: wrap; margin-top: 8px; }
    .bridge-action { display: inline-block; padding: 6px 10px; border: 1px solid #d8ccb9; border-radius: 999px; background: #fff8ef; color: #6d4c2f; text-decoration: none; font-size: 12px; }
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
      const topbar = document.createElement("div");
      topbar.className = "topbar";
      [['/','space'], ['/dust','dust'], ['/source','source'], ['/terrain','terrain'], ['/atlas','atlas']].forEach(([href, label]) => {
        const link = document.createElement('a');
        link.className = 'link';
        link.href = href;
        link.textContent = label;
        topbar.appendChild(link);
      });
      page.appendChild(topbar);
      const summary = document.createElement("div");
      summary.className = "summary";
      summary.textContent = `regions ${data.summary.region_count} / bridges ${data.summary.bridge_count}`;
      page.appendChild(summary);

      const grid = document.createElement("div");
      grid.className = "grid";
      const mainColumn = document.createElement("div");
      mainColumn.className = "main-column";
      const regions = document.createElement("div");
      regions.className = "regions";
      const topLevelBridges = document.createElement("section");
      topLevelBridges.className = "bridge-atlas";
      const bridgeList = document.createElement("aside");
      bridgeList.className = "bridge-list";
      let selectedRegionId = (new URLSearchParams(window.location.search)).get('local_space_id') || ((data.regions || [])[0] && data.regions[0].local_space_id) || null;
      const buildAtlasEvidenceHref = (pathname, payload) => {
        const url = new URL(pathname, window.location.origin);
        Object.entries(payload || {}).forEach(([key, value]) => {
          if (value !== null && value !== undefined && String(value) !== '') {
            url.searchParams.set(key, String(value));
          }
        });
        url.searchParams.set('from', 'atlas');
        url.searchParams.set('return_href', selectedRegionId ? `/atlas?local_space_id=${encodeURIComponent(selectedRegionId)}` : '/atlas');
        url.searchParams.set('return_label', 'Back to Atlas');
        url.searchParams.set('origin_route', 'atlas');
        if (selectedRegionId) {
          url.searchParams.set('origin_local_space_id', selectedRegionId);
          const selectedRegion = (data.regions || []).find((row) => row.local_space_id === selectedRegionId);
          if (selectedRegion) {
            url.searchParams.set('origin_region_label', selectedRegion.label || selectedRegion.local_space_id || '');
          }
        }
        return url.pathname + '?' + url.searchParams.toString();
      };

      const renderBridgeActions = (row) => {
        const actions = document.createElement("div");
        actions.className = "bridge-actions";
        if ((row.source_links || []).length) {
          const sourceLink = document.createElement("a");
          sourceLink.className = "bridge-action";
          sourceLink.href = buildAtlasEvidenceHref('/source', {
            source_ref: row.source_links[0].source_ref,
            origin_bridge_id: row.bridge_id || '',
            origin_source_ref: row.source_links[0].source_ref || '',
          });
          sourceLink.textContent = "Open Source Evidence";
          actions.appendChild(sourceLink);
        } else {
          const sourceState = document.createElement("span");
          sourceState.className = "meta";
          sourceState.textContent = "Open Source Evidence 없음";
          actions.appendChild(sourceState);
        }
        if ((row.dust_links || []).length) {
          const dustLink = document.createElement("a");
          dustLink.className = "bridge-action";
          dustLink.href = buildAtlasEvidenceHref('/dust', {
            dust_id: row.dust_links[0].dust_id,
            origin_bridge_id: row.bridge_id || '',
            origin_dust_id: row.dust_links[0].dust_id || '',
            origin_source_ref: ((row.source_links || [])[0] || {}).source_ref || '',
          });
          dustLink.textContent = "Open Dust Evidence";
          actions.appendChild(dustLink);
        } else {
          const dustState = document.createElement("span");
          dustState.className = "meta";
          dustState.textContent = "Open Dust Evidence 없음";
          actions.appendChild(dustState);
        }
        return actions;
      };

      const renderBridgeEvidenceRow = (row, title) => {
        const block = document.createElement("div");
        block.className = "landmark";
        const heading = document.createElement("div");
        heading.style.fontWeight = "bold";
        heading.textContent = title;
        block.appendChild(heading);
        const line = document.createElement("div");
        line.style.marginTop = "6px";
        line.textContent = row.reason_line || "bridge reason 없음";
        block.appendChild(line);
        if ((row.anchor_hints || []).length) {
          const hint = document.createElement("div");
          hint.className = "meta";
          hint.style.marginTop = "6px";
          hint.textContent = `hints: ${(row.anchor_hints || []).join(', ')}`;
          block.appendChild(hint);
        }
        block.appendChild(renderBridgeActions(row));
        return block;
      };

      const renderInspector = () => {
        const region = (data.regions || []).find((row) => row.local_space_id === selectedRegionId) || null;
        bridgeList.innerHTML = '';
        const bTitle = document.createElement("h2");
        bTitle.textContent = region ? region.label : "Region Inspector";
        bridgeList.appendChild(bTitle);
        if (!region) {
          const empty = document.createElement("div");
          empty.className = "meta";
          empty.textContent = "선택된 region 없음";
          bridgeList.appendChild(empty);
          return;
        }
        const meta = document.createElement("div");
        meta.className = "meta";
        meta.textContent = `scene ${region.dominant_scene} / role ${region.dominant_role || '-'} / materials ${region.material_count}`;
        bridgeList.appendChild(meta);

        const why = document.createElement("div");
        why.className = "inspector-block";
        why.innerHTML = `<h3>Why Region Exists</h3><div class="landmark">${region.why_region_exists || '설명 없음'}</div>`;
        bridgeList.appendChild(why);

        const rep = document.createElement("div");
        rep.className = "inspector-block";
        rep.innerHTML = `<h3>Representative Anchors</h3>`;
        const chips = document.createElement("div");
        chips.className = "chips";
        (region.representative_anchors || []).forEach((value) => {
          const chip = document.createElement("span");
          chip.className = "chip";
          chip.textContent = `${value.anchor_type}:${value.display_label}`;
          chips.appendChild(chip);
        });
        if (!chips.childElementCount) chips.innerHTML = '<span class="meta">없음</span>';
        rep.appendChild(chips);
        bridgeList.appendChild(rep);

        const support = document.createElement("div");
        support.className = "inspector-block";
        support.innerHTML = `<h3>Supporting Anchors</h3>`;
        const supportChips = document.createElement("div");
        supportChips.className = "chips";
        (region.supporting_anchors || []).forEach((value) => {
          const chip = document.createElement("span");
          chip.className = "chip";
          chip.textContent = `${value.anchor_type}:${value.display_label}`;
          supportChips.appendChild(chip);
        });
        if (!supportChips.childElementCount) supportChips.innerHTML = '<span class="meta">없음</span>';
        support.appendChild(supportChips);
        bridgeList.appendChild(support);

        const conn = document.createElement("div");
        conn.className = "inspector-block";
        conn.innerHTML = `<h3>Bridge Reasons</h3>`;
        (region.connections || []).forEach((connRow) => {
          conn.appendChild(renderBridgeEvidenceRow(connRow, connRow.peer_label || "peer region"));
        });
        if (!(region.connections || []).length) {
          const row = document.createElement("div");
          row.className = "meta";
          row.textContent = "연결 없음";
          conn.appendChild(row);
        }
        bridgeList.appendChild(conn);

        const landmarks = document.createElement("div");
        landmarks.className = "inspector-block";
        landmarks.innerHTML = `<h3>Landmarks</h3>`;
        (region.landmarks || []).forEach((landmark) => {
          const row = document.createElement("div");
          row.className = "landmark";
          row.textContent = `${landmark.label}  (${landmark.scene}${landmark.observer_role ? '/' + landmark.observer_role : ''})`;
          landmarks.appendChild(row);
        });
        bridgeList.appendChild(landmarks);

        const links = document.createElement("div");
        links.className = "inspector-block";
        links.innerHTML = `<h3>Source Links</h3>`;
        (region.source_links || []).forEach((linkRow) => {
          const link = document.createElement("a");
          link.className = "source-link";
          link.href = buildAtlasEvidenceHref('/source', {
            source_ref: linkRow.source_ref,
            origin_source_ref: linkRow.source_ref || '',
          });
          link.textContent = linkRow.label || linkRow.source_ref;
          links.appendChild(link);
        });
        if (!(region.source_links || []).length) {
          const row = document.createElement("div");
          row.className = "meta";
          row.textContent = "source link 없음";
          links.appendChild(row);
        }
        bridgeList.appendChild(links);

        const dustLinks = document.createElement("div");
        dustLinks.className = "inspector-block";
        dustLinks.innerHTML = `<h3>Dust Links</h3>`;
        (region.dust_links || []).forEach((linkRow) => {
          const link = document.createElement("a");
          link.className = "source-link";
          link.href = buildAtlasEvidenceHref('/dust', {
            dust_id: linkRow.dust_id,
            origin_dust_id: linkRow.dust_id || '',
          });
          link.textContent = linkRow.label || linkRow.dust_id;
          dustLinks.appendChild(link);
        });
        if (!(region.dust_links || []).length) {
          const row = document.createElement("div");
          row.className = "meta";
          row.textContent = "dust jump 없음";
          dustLinks.appendChild(row);
        }
        bridgeList.appendChild(dustLinks);

        const rejected = document.createElement("div");
        rejected.className = "inspector-block";
        rejected.innerHTML = `<h3>Rejected Overlap</h3>`;
        const rejectedState = region.rejected_overlap_state || { available: false, items: [] };
        if (rejectedState.available === false) {
          const row = document.createElement("div");
          row.className = "meta";
          row.textContent = "not available yet";
          rejected.appendChild(row);
        } else if ((rejectedState.items || []).length) {
          const chips = document.createElement("div");
          chips.className = "chips";
          (rejectedState.items || []).forEach((value) => {
            const chip = document.createElement("span");
            chip.className = "chip";
            chip.textContent = value;
            chips.appendChild(chip);
          });
          rejected.appendChild(chips);
        } else {
          const row = document.createElement("div");
          row.className = "meta";
          row.textContent = "none";
          rejected.appendChild(row);
        }
        bridgeList.appendChild(rejected);
      };

      const renderTopLevelBridges = () => {
        topLevelBridges.innerHTML = "";
        const title = document.createElement("h2");
        title.textContent = "Bridge Atlas";
        topLevelBridges.appendChild(title);
        const meta = document.createElement("div");
        meta.className = "meta";
        meta.textContent = "selected region 없이도 bridge evidence를 바로 열 수 있습니다.";
        topLevelBridges.appendChild(meta);
        (data.bridges || []).forEach((row) => {
          topLevelBridges.appendChild(
            renderBridgeEvidenceRow(row, `${row.from_label || "from"} → ${row.to_label || "to"}`)
          );
        });
        if (!(data.bridges || []).length) {
          const empty = document.createElement("div");
          empty.className = "meta";
          empty.textContent = "bridge 없음";
          topLevelBridges.appendChild(empty);
        }
      };

      const renderCards = () => {
        regions.innerHTML = '';
        data.regions.forEach((region) => {
          const card = document.createElement("section");
          card.className = "card" + (region.local_space_id === selectedRegionId ? " selected" : "");
          card.dataset.localSpaceId = region.local_space_id;
          const title = document.createElement("h2");
          title.textContent = region.label;
          card.appendChild(title);
          const meta = document.createElement("div");
          meta.className = "meta";
          meta.textContent = `scene ${region.dominant_scene} / role ${region.dominant_role || '-'} / materials ${region.material_count}`;
          card.appendChild(meta);

          const chips = document.createElement("div");
          chips.className = "chips";
          (region.anchor_summary || []).forEach((value) => {
            const chip = document.createElement("span");
            chip.className = "chip";
            chip.textContent = value;
            chips.appendChild(chip);
          });
          card.appendChild(chips);

          const supportTitle = document.createElement("div");
          supportTitle.className = "meta";
          supportTitle.textContent = "supporting anchors";
          card.appendChild(supportTitle);
          const supportChips = document.createElement("div");
          supportChips.className = "chips";
          (region.supporting_anchor_summary || []).forEach((value) => {
            const chip = document.createElement("span");
            chip.className = "chip";
            chip.textContent = value;
            supportChips.appendChild(chip);
          });
          card.appendChild(supportChips);

          const whyLine = document.createElement("div");
          whyLine.className = "landmark";
          whyLine.textContent = region.why_region_exists || '설명 없음';
          card.appendChild(whyLine);

          card.addEventListener('click', () => {
            selectedRegionId = region.local_space_id;
            const url = new URL(window.location.href);
            url.searchParams.set('local_space_id', selectedRegionId);
            window.history.replaceState({}, '', url);
            renderCards();
            renderInspector();
          });

          regions.appendChild(card);
        });
      };

      renderCards();
      renderInspector();
      renderTopLevelBridges();

      mainColumn.appendChild(regions);
      mainColumn.appendChild(topLevelBridges);
      grid.appendChild(mainColumn);
      grid.appendChild(bridgeList);
      page.appendChild(grid);
      app.appendChild(page);
    })();
  </script>
</body>
</html>
"""
