from __future__ import annotations


def terrain_map_style() -> str:
    return """
    body { margin: 0; font-family: Georgia, serif; background: #efe7da; color: #1f2937; }
    .page { display: grid; grid-template-columns: minmax(0, 1fr) 360px; min-height: 100vh; }
    .stage { position: relative; overflow: auto; background:
      radial-gradient(circle at 20% 20%, rgba(255,255,255,0.8), transparent 24%),
      radial-gradient(circle at 80% 10%, rgba(191,149,93,0.14), transparent 16%),
      linear-gradient(180deg, #fbf6ee 0%, #efe7da 100%);
    }
    .sidebar { border-left: 1px solid #d8ccb9; padding: 18px; background: rgba(255,250,242,0.96); }
    .canvas-wrap { position: relative; width: 1600px; height: 1200px; margin: 0 auto; }
    canvas { width: 1600px; height: 1200px; display: block; }
    h1,h2,h3 { margin: 0 0 10px; }
    .topbar { display: flex; gap: 12px; flex-wrap: wrap; margin-bottom: 14px; }
    .link { display: inline-block; padding: 8px 12px; border-radius: 999px; background: #fff8ef; border: 1px solid #d8ccb9; color: #6d4c2f; text-decoration: none; }
    .metric { padding: 10px 12px; border-radius: 12px; border: 1px solid #eadfce; background: white; margin-bottom: 8px; }
    .legend-row { margin: 8px 0; font-size: 14px; }
    .swatch { display:inline-block; width: 12px; height: 12px; border-radius: 999px; margin-right: 6px; vertical-align: middle; }
    pre { white-space: pre-wrap; word-break: break-word; background: white; border: 1px solid #eadfce; border-radius: 12px; padding: 12px; }
"""


def terrain_map_script() -> str:
    return """
    const canvas = document.getElementById('terrain-canvas');
    const ctx = canvas.getContext('2d');
    const sceneColors = {
      explanation: '#c58f4c',
      comparison: '#7c3aed',
      reflection: '#8f5c2c',
      evidence: '#0f766e',
      unknown: '#64748b'
    };
    function rgba(hex, alpha) {
      const clean = hex.replace('#', '');
      const r = parseInt(clean.slice(0,2), 16);
      const g = parseInt(clean.slice(2,4), 16);
      const b = parseInt(clean.slice(4,6), 16);
      return 'rgba(' + r + ',' + g + ',' + b + ',' + alpha + ')';
    }
    function renderTerrainMap(data) {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      (data.cells || []).forEach(cell => {
        const base = sceneColors[cell.dominant_scene] || sceneColors.unknown;
        ctx.fillStyle = rgba(base, Math.max(0.06, 0.12 + cell.elevation * 0.24));
        ctx.fillRect(cell.x, cell.y, 28, 28);
        if (cell.fog > 0.42) {
          ctx.fillStyle = 'rgba(255,255,255,' + Math.min(0.32, cell.fog * 0.38) + ')';
          ctx.fillRect(cell.x, cell.y, 28, 28);
        }
      });
      (data.contour_lines || []).forEach(line => {
        const path = line.path || [];
        if (path.length < 2) return;
        const alpha = 0.08 + line.level * 0.14;
        ctx.strokeStyle = 'rgba(59,46,32,' + alpha + ')';
        ctx.lineWidth = 0.7 + line.level * 0.8;
        ctx.beginPath();
        ctx.moveTo(path[0].x, path[0].y);
        for (let i = 1; i < path.length; i += 1) ctx.lineTo(path[i].x, path[i].y);
        ctx.stroke();
      });
      (data.water_flows || []).forEach(flow => {
        const path = flow.path || [];
        if (path.length < 2) return;
        ctx.strokeStyle = 'rgba(37,99,235,' + Math.min(0.85, 0.25 + flow.strength * 0.7) + ')';
        ctx.lineWidth = 1.5 + flow.strength * 2.4;
        ctx.beginPath();
        ctx.moveTo(path[0].x, path[0].y);
        for (let i = 1; i < path.length; i += 1) ctx.lineTo(path[i].x, path[i].y);
        ctx.stroke();
      });
      (data.region_flows || []).forEach(flow => {
        const path = flow.path || [];
        if (path.length < 2) return;
        ctx.strokeStyle = 'rgba(14,116,144,' + Math.min(0.9, 0.28 + flow.strength * 0.62) + ')';
        ctx.lineWidth = 2 + flow.strength * 3.2;
        ctx.beginPath();
        ctx.moveTo(path[0].x, path[0].y);
        for (let i = 1; i < path.length; i += 1) ctx.lineTo(path[i].x, path[i].y);
        ctx.stroke();
        const mid = path[1] || path[0];
        const hint = (flow.anchor_hints || []).slice(0, 2).join(' · ');
        if (hint) {
          ctx.fillStyle = 'rgba(15,23,42,0.82)';
          ctx.font = '11px Georgia';
          ctx.fillText(hint, mid.x + 8, mid.y - 6);
        }
      });
      (data.wind_fields || []).forEach(wind => {
        const len = 18 + wind.strength * 24;
        const rad = (wind.direction || 0) * Math.PI / 180;
        const x2 = wind.x + Math.cos(rad) * len;
        const y2 = wind.y + Math.sin(rad) * len;
        ctx.strokeStyle = 'rgba(185,28,28,0.65)';
        ctx.setLineDash([5, 4]);
        ctx.lineWidth = 1.4;
        ctx.beginPath();
        ctx.moveTo(wind.x, wind.y);
        ctx.lineTo(x2, y2);
        ctx.stroke();
        ctx.setLineDash([]);
      });
      (data.fault_lines || []).forEach(fault => {
        ctx.fillStyle = 'rgba(185,28,28,0.75)';
        ctx.beginPath();
        ctx.arc(fault.x, fault.y, 3 + fault.severity * 4, 0, Math.PI * 2);
        ctx.fill();
      });
      (data.regions || []).forEach(region => {
        if (!region.material_count) return;
        const color = sceneColors[region.dominant_scene] || sceneColors.unknown;
        const left = region.x - region.width / 2;
        const top = region.y - region.height / 2;
        const radius = 16;
        ctx.fillStyle = rgba(color, Math.max(0.08, 0.1 + region.elevation * 0.18));
        ctx.beginPath();
        ctx.moveTo(left + radius, top);
        ctx.lineTo(left + region.width - radius, top);
        ctx.quadraticCurveTo(left + region.width, top, left + region.width, top + radius);
        ctx.lineTo(left + region.width, top + region.height - radius);
        ctx.quadraticCurveTo(left + region.width, top + region.height, left + region.width - radius, top + region.height);
        ctx.lineTo(left + radius, top + region.height);
        ctx.quadraticCurveTo(left, top + region.height, left, top + region.height - radius);
        ctx.lineTo(left, top + radius);
        ctx.quadraticCurveTo(left, top, left + radius, top);
        ctx.closePath();
        ctx.fill();
        ctx.strokeStyle = 'rgba(31,41,55,0.35)';
        ctx.lineWidth = 1.2;
        ctx.stroke();
        ctx.fillStyle = 'rgba(31,41,55,0.85)';
        ctx.font = '12px Georgia';
        const regionLabel = String(region.label || '').replace('.txt', '');
        ctx.fillText(regionLabel, region.x - Math.min(42, regionLabel.length * 2.8), top - 6);
        if (region.dominant_role) {
          ctx.fillStyle = 'rgba(109,76,47,0.92)';
          ctx.font = '11px Georgia';
          ctx.fillText(region.dominant_role, region.x - 18, top + region.height + 14);
        }
        const anchorSummary = (region.anchor_summary || []).slice(0, 3).join(' · ');
        if (anchorSummary) {
          ctx.fillStyle = 'rgba(31,41,55,0.68)';
          ctx.font = '10px Georgia';
          ctx.fillText(anchorSummary, left + 8, top + 16);
        }
        (region.landmarks || []).forEach((landmark) => {
          const featureColor = sceneColors[landmark.scene] || sceneColors.unknown;
          ctx.fillStyle = featureColor;
          ctx.beginPath();
          ctx.arc(landmark.x, landmark.y, 5.5, 0, Math.PI * 2);
          ctx.fill();
          ctx.fillStyle = 'rgba(31,41,55,0.82)';
          ctx.font = '10px Georgia';
          ctx.fillText(landmark.label, landmark.x + 8, landmark.y - 4);
        });
      });
      (data.fragment_points || []).forEach(point => {
        ctx.fillStyle = '#1f2937';
        ctx.beginPath();
        ctx.arc(point.x, point.y, 2.8, 0, Math.PI * 2);
        ctx.fill();
      });
      const regionSummary = (data.regions || []).map(region => {
        const anchors = (region.anchor_summary || []).slice(0, 4).join(', ');
        return `${String(region.label || '').replace('.txt','')}  scene=${region.dominant_scene} role=${region.dominant_role || '-'} materials=${region.material_count}\\nanchors: ${anchors || '-'}`;
      }).join('\\n\\n');
      const bridgeSummary = (data.region_flows || []).map(flow => {
        const hints = (flow.anchor_hints || []).join(', ');
        return `${flow.from_label} -> ${flow.to_label}\\nstrength=${flow.strength} hints=${hints || '-'}`;
      }).join('\\n\\n');
      document.getElementById('region-summary').textContent = regionSummary || 'no regions';
      document.getElementById('bridge-summary').textContent = bridgeSummary || 'no bridges';
    }
    window.renderTerrainMap = renderTerrainMap;

    const embedded = document.getElementById('terrain-data');
    if (embedded) {
      try {
        renderTerrainMap(JSON.parse(embedded.textContent));
      } catch (error) {
        console.warn('terrain inline parse failed', error);
      }
    }
"""
