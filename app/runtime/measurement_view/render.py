from __future__ import annotations

from typing import Dict, Optional
import json


def render_measurement_view_html(data: Optional[Dict[str, object]] = None, api_path: str = "/api/measurements") -> str:
    payload_block = (
        f'<script id="measurement-data" type="application/json">{json.dumps(data, ensure_ascii=False)}</script>'
        if data is not None
        else ""
    )
    bootstrap = (
        "const embedded = document.getElementById('measurement-data');\n"
        "const data = embedded ? JSON.parse(embedded.textContent) : await (await fetch('"
        + api_path +
        "')).json();"
    )
    return """<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Measurement View</title>
  <style>
    body { margin: 0; font-family: Georgia, serif; background: #f3efe8; color: #1f2937; }
    .page { max-width: 1280px; margin: 0 auto; padding: 24px; }
    .topbar { display: flex; gap: 12px; flex-wrap: wrap; margin-bottom: 18px; }
    .link { display: inline-block; padding: 8px 12px; border-radius: 999px; background: #fff8ef; border: 1px solid #d8ccb9; color: #6d4c2f; text-decoration: none; }
    .group { background: #fffaf3; border: 1px solid #d8ccb9; border-radius: 16px; padding: 16px; margin-bottom: 18px; }
    .meta { color: #6b7280; font-size: 14px; margin-bottom: 12px; }
    .record { border-top: 1px solid #eadfce; padding-top: 10px; margin-top: 10px; }
    .chips { display: flex; gap: 8px; flex-wrap: wrap; margin: 8px 0; }
    .chip { background: #efe4d2; border-radius: 999px; padding: 4px 8px; font-size: 12px; }
    pre { white-space: pre-wrap; word-break: break-word; background: #fff; padding: 12px; border-radius: 12px; border: 1px solid #eadfce; }
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
      [['/','space'], ['/dust','dust'], ['/source','source'], ['/measurements','measurements']].forEach(([href, label]) => {
        const link = document.createElement('a');
        link.className = 'link';
        link.href = href;
        link.textContent = label;
        topbar.appendChild(link);
      });
      page.appendChild(topbar);
      const summary = document.createElement("div");
      summary.className = "meta";
      summary.textContent = `measurements ${data.summary.measurement_count} / types ${data.summary.measurement_type_count} / batches ${data.summary.ingest_batch_count}`;
      page.appendChild(summary);
      if (data.batches && data.batches.length) {
        const batchSection = document.createElement("section");
        batchSection.className = "group";
        const batchTitle = document.createElement("h2");
        batchTitle.textContent = "recent ingest batches";
        batchSection.appendChild(batchTitle);
        data.batches.slice(0, 8).forEach((batch) => {
          const card = document.createElement("div");
          card.className = "record";
          const head = document.createElement("strong");
          head.textContent = `${batch.ingest_batch_id} (${batch.count})`;
          card.appendChild(head);
          const chips = document.createElement("div");
          chips.className = "chips";
          (batch.measurement_types || []).forEach((value) => {
            const chip = document.createElement("span");
            chip.className = "chip";
            chip.textContent = value;
            chips.appendChild(chip);
          });
          (batch.session_ids || []).forEach((value) => {
            const chip = document.createElement("span");
            chip.className = "chip";
            chip.textContent = value;
            chips.appendChild(chip);
          });
          card.appendChild(chips);
          batchSection.appendChild(card);
        });
        page.appendChild(batchSection);
      }
      data.groups.forEach((group) => {
        const section = document.createElement("section");
        section.className = "group";
        const title = document.createElement("h2");
        title.textContent = `${group.measurement_type} (${group.count})`;
        section.appendChild(title);
        group.records.forEach((record) => {
          const card = document.createElement("div");
          card.className = "record";
          const head = document.createElement("strong");
          head.textContent = `${record.fragment_id}  ${record.column_key}`;
          card.appendChild(head);
          const chips = document.createElement("div");
          chips.className = "chips";
          [record.origin, `confidence:${record.confidence}`, `provisional:${record.provisional}`, record.status].forEach((value) => {
            const chip = document.createElement("span");
            chip.className = "chip";
            chip.textContent = value;
            chips.appendChild(chip);
          });
          card.appendChild(chips);
          const body = document.createElement("pre");
          body.textContent = JSON.stringify(record.value, null, 2);
          card.appendChild(body);
          section.appendChild(card);
        });
        page.appendChild(section);
      });
      app.appendChild(page);
    })();
  </script>
</body>
</html>
"""
