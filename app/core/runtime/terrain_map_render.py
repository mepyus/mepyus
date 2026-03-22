from __future__ import annotations

from typing import Dict, Optional
import json

from app.core.runtime.terrain_map_assets import terrain_map_script, terrain_map_style


def render_terrain_map_html(data: Optional[Dict[str, object]] = None, api_path: str = "/api/terrain") -> str:
    payload_block = (
        f'<script id="terrain-data" type="application/json">{json.dumps(data, ensure_ascii=False)}</script>'
        if data is not None
        else ""
    )
    summary = data["summary"] if data is not None else {}
    return """<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Terrain Map View</title>
  <style>
""" + terrain_map_style() + """
  </style>
</head>
<body>
  <div class="page">
    <main class="stage">
      <div class="canvas-wrap">
        <canvas id="terrain-canvas" width="1600" height="1200"></canvas>
      </div>
    </main>
    <aside class="sidebar">
      <div class="topbar">
        <a class="link" href="/">space</a>
        <a class="link" href="/dust">dust</a>
        <a class="link" href="/source">source</a>
        <a class="link" href="/terrain">terrain</a>
      </div>
      <h1>지형도</h1>
      <div class="metric" id="metric-a">fragment `""" + str(summary.get("fragment_count", "...")) + """` / imported points `""" + str(summary.get("imported_point_count", "...")) + """` / material `""" + str(summary.get("material_count", "...")) + """`</div>
      <div class="metric" id="metric-b">regions `""" + str(summary.get("local_space_count", "...")) + """` / bridges `""" + str(summary.get("bridge_count", "...")) + """` / terrain cells `""" + str(summary.get("terrain_cell_count", "...")) + """`</div>
      <div class="metric" id="metric-c">water `""" + str(summary.get("water_flow_count", "...")) + """` / wind `""" + str(summary.get("wind_field_count", "...")) + """` / region flow `""" + str(summary.get("region_flow_count", "...")) + """`</div>
      <div class="metric" id="metric-d">contours `""" + str(summary.get("contour_line_count", "...")) + """` / semantic cells `""" + str(summary.get("semantic_cell_field_count", "...")) + """`</div>
      <div class="metric" id="metric-e">semantic edges `""" + str(summary.get("semantic_edge_field_count", "...")) + """` / semantic regions `""" + str(summary.get("semantic_region_field_count", "...")) + """` / geometry `""" + str(summary.get("semantic_geometry_count", "...")) + """`</div>
      <div class="legend-row"><span class="swatch" style="background:#c58f4c"></span>explanation</div>
      <div class="legend-row"><span class="swatch" style="background:#7c3aed"></span>comparison</div>
      <div class="legend-row"><span class="swatch" style="background:#8f5c2c"></span>reflection</div>
      <div class="legend-row"><span class="swatch" style="background:#0f766e"></span>evidence</div>
      <div class="legend-row"><span class="swatch" style="background:#2563eb"></span>water flow</div>
      <div class="legend-row"><span class="swatch" style="background:#b91c1c"></span>wind / fault</div>
      <h3 style="margin-top:18px;">설명</h3>
      <pre>I = elevation
S = stability
observer_ambiguity = fog
scene = terrain biome
observer_role = feature function
observer_signals = wind/fault markers

semantic pipeline:
raw -> derived fields -> geometry -> terrain view</pre>
      <h3 style="margin-top:18px;">Region</h3>
      <pre id="region-summary">loading...</pre>
      <h3 style="margin-top:18px;">Bridge</h3>
      <pre id="bridge-summary">loading...</pre>
    </aside>
  </div>
  """ + payload_block + """
  <script>
""" + terrain_map_script() + """
    (async () => {
      const embedded = document.getElementById('terrain-data');
      const data = embedded ? JSON.parse(embedded.textContent) : await (await fetch('""" + api_path + """')).json();
      const s = data.summary || {};
      document.getElementById('metric-a').textContent = `fragment ${s.fragment_count} / imported points ${s.imported_point_count} / material ${s.material_count}`;
      document.getElementById('metric-b').textContent = `regions ${s.local_space_count} / bridges ${s.bridge_count} / terrain cells ${s.terrain_cell_count}`;
      document.getElementById('metric-c').textContent = `water ${s.water_flow_count} / wind ${s.wind_field_count} / region flow ${s.region_flow_count}`;
      document.getElementById('metric-d').textContent = `contours ${s.contour_line_count} / semantic cells ${s.semantic_cell_field_count}`;
      document.getElementById('metric-e').textContent = `semantic edges ${s.semantic_edge_field_count} / semantic regions ${s.semantic_region_field_count} / geometry ${s.semantic_geometry_count}`;
      window.__terrainData = data;
      if (typeof window.renderTerrainMap === 'function') {
        window.renderTerrainMap(data);
      } else if (typeof renderTerrainMap === 'function') {
        renderTerrainMap(data);
      }
    })();
  </script>
</body>
</html>
"""
