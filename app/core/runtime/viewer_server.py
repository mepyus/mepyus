from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Callable, Dict, List
import json
from urllib.parse import parse_qs, urlencode, urlparse

from app.runtime.dust_field import build_dust_field_data, render_dust_field_html
from app.runtime.graph_view import build_space_graph_view_data, render_space_graph_view_html
from app.runtime.live_input import ingest_live_input
from app.runtime.measurement_view import build_measurement_view_data, render_measurement_view_html
from app.runtime.operating_ui_demo import (
    build_operating_ui_composition_demo_data,
    render_operating_ui_composition_demo_html,
)
from app.runtime.operating_ui_live import (
    build_operating_ui_live_composition_data,
    render_operating_ui_live_composition_html,
)
from app.runtime.operating_ui_phase1 import (
    build_operating_ui_phase1_shell_data,
    create_phase1_memory_sticker,
    save_phase1_path_residue,
    render_operating_ui_phase1_shell_html,
)
from app.runtime.operating_ui_history import (
    build_operating_ui_history_shell_data,
    render_operating_ui_history_shell_html,
)
from app.runtime.active_asset_first_pass_alignment import ensure_active_asset_first_pass_fragments
from app.runtime.saved_connections import create_saved_connection_from_candidate
from app.runtime.user_page_shell import (
    _build_explore_candidates,
    _build_explore_reading_context,
    _build_source,
    render_user_explore_page,
    render_user_memory_page,
    render_user_operating_page,
    render_user_search_page,
    render_user_similar_page,
)
from app.runtime.process_console_view import build_process_console_view_data, render_process_console_view_html
from app.runtime.region_atlas import build_region_atlas_data, render_region_atlas_html
from app.runtime.source_view import build_source_fragment_view_data, render_source_fragment_html
from app.runtime.terrain_map import build_terrain_map_data, render_terrain_map_html
from app.runtime.vectorfl_paper_operable_api import build_vectorfl_paper_operable_state
from app.runtime.vectorfl_paper_operable_shell import render_vectorfl_paper_operable_shell
from app.runtime.vectorfl_integrated_engine_api import (
    build_vectorfl_integrated_engine_state,
    create_implementation_brief_from_supervisor_gate,
    create_implementation_launch_gate,
    create_supervisor_gate_from_synthesis,
    create_vectorfl_integrated_engine_operating_dialogue,
    create_vectorfl_integrated_engine_worker_launch_draft,
    create_vectorfl_integrated_engine_worker_session,
    create_worker_session_from_current_context,
    create_vectorfl_integrated_engine_assignment,
    create_vectorfl_integrated_engine_supervisor_route,
    create_vectorfl_integrated_engine_work_packet,
    harvest_integrated_engine_language_loop,
    mark_integrated_engine_cli_session,
    run_codex_assignment_bridge,
    run_integrated_engine_cli_session,
    run_integrated_engine_language_loop,
    run_internal_read_from_supervisor_route,
    run_synthesis_from_internal_read,
    run_vectorfl_integrated_engine_worker_launch_draft,
)
from app.runtime.vectorfl_integrated_engine_shell import render_vectorfl_integrated_engine_shell


def run_viewer_server(runtime_root: Path, host: str = "127.0.0.1", port: int = 8421) -> None:
    runtime_root = runtime_root.resolve()

    class ViewerServerHandler(BaseHTTPRequestHandler):
        def do_GET(self) -> None:
            parsed = urlparse(self.path)
            request_path = parsed.path
            query = parse_qs(parsed.query)
            if request_path in {"/", "/index.html"}:
                self._respond_html(
                    render_space_graph_view_html(
                        build_space_graph_view_data(runtime_root),
                        interactive=True,
                    )
                )
                return
            if request_path in {"/dust", "/dust.html"}:
                self._respond_html(render_dust_field_html(build_dust_field_data(runtime_root)))
                return
            if request_path in {"/source", "/source.html"}:
                self._respond_html(render_source_fragment_html(api_path="/api/source"))
                return
            if request_path in {"/terrain", "/terrain.html"}:
                self._respond_html(render_terrain_map_html(api_path="/api/terrain"))
                return
            if request_path in {"/atlas", "/atlas.html"}:
                self._respond_html(render_region_atlas_html(api_path="/api/atlas"))
                return
            if request_path in {"/measurements", "/measurements.html"}:
                self._respond_html(render_measurement_view_html(api_path="/api/measurements"))
                return
            if request_path in {"/process-console", "/process-console.html"}:
                self._respond_html(
                    render_process_console_view_html(
                        build_process_console_view_data(
                            runtime_root,
                            asset_id=_single(query, "asset_id"),
                            filters=_filters_from_query(query),
                            sort_by=_single(query, "sort_by") or "updated_at",
                            compare_index=_int_value(query, "compare_index"),
                            debug=_single(query, "debug") in {"1", "true", "yes"},
                        ),
                        api_path=self.path if request_path.startswith("/api/") else f"/api/process-console{parsed.query and ('?' + parsed.query) or ''}",
                    )
                )
                return
            if request_path in {"/operating-ui-demo", "/operating-ui-demo.html"}:
                case = _single(query, "case") or "a"
                self._respond_html(
                    render_operating_ui_composition_demo_html(
                        build_operating_ui_composition_demo_data(runtime_root, case=case),
                        api_path=f"/api/operating-ui-demo?case={case}",
                    )
                )
                return
            if request_path in {"/operating-ui-live", "/operating-ui-live.html"}:
                asset_id = _single(query, "asset_id") or None
                sort_by = _single(query, "sort_by") or "updated_at"
                live_mode = _single(query, "live_mode") or None
                compare_mode = _single(query, "compare_mode") or None
                query_suffix = []
                if asset_id:
                    query_suffix.append(f"asset_id={asset_id}")
                if sort_by and sort_by != "updated_at":
                    query_suffix.append(f"sort_by={sort_by}")
                if live_mode:
                    query_suffix.append(f"live_mode={live_mode}")
                if compare_mode:
                    query_suffix.append(f"compare_mode={compare_mode}")
                api_path = "/api/operating-ui-live"
                if query_suffix:
                    api_path += "?" + "&".join(query_suffix)
                self._respond_html(
                    render_operating_ui_live_composition_html(
                        build_operating_ui_live_composition_data(
                            runtime_root,
                            asset_id=asset_id,
                            sort_by=sort_by,
                            live_mode=live_mode,
                            compare_mode=compare_mode,
                        ),
                        api_path=api_path,
                    )
                )
                return
            if request_path in {"/operating-ui-phase1", "/operating-ui-phase1.html"}:
                asset_id = _single(query, "asset_id") or None
                sort_by = _single(query, "sort_by") or "updated_at"
                live_mode = _single(query, "live_mode") or None
                compare_mode = _single(query, "compare_mode") or None
                query_suffix = []
                if asset_id:
                    query_suffix.append(f"asset_id={asset_id}")
                if sort_by and sort_by != "updated_at":
                    query_suffix.append(f"sort_by={sort_by}")
                if live_mode:
                    query_suffix.append(f"live_mode={live_mode}")
                if compare_mode:
                    query_suffix.append(f"compare_mode={compare_mode}")
                api_path = "/api/operating-ui-phase1"
                if query_suffix:
                    api_path += "?" + "&".join(query_suffix)
                self._respond_html(
                    render_operating_ui_phase1_shell_html(
                        build_operating_ui_phase1_shell_data(
                            runtime_root,
                            asset_id=asset_id,
                            sort_by=sort_by,
                            live_mode=live_mode,
                            compare_mode=compare_mode,
                            history_snapshot_ref=_single(query, "history_snapshot_ref") or None,
                            history_cluster_ref=_single(query, "history_cluster_ref") or None,
                            history_trace_ref=_single(query, "history_trace_ref") or None,
                            history_reread_summary=_single(query, "history_reread_summary") or None,
                            history_source_note=_single(query, "history_source_note") or None,
                        ),
                        api_path=api_path,
                    )
                )
                return
            if request_path in {"/operating-ui-history", "/operating-ui-history.html"}:
                asset_id = _single(query, "asset_id") or None
                sort_by = _single(query, "sort_by") or "updated_at"
                query_suffix = []
                if asset_id:
                    query_suffix.append(f"asset_id={asset_id}")
                if sort_by and sort_by != "updated_at":
                    query_suffix.append(f"sort_by={sort_by}")
                api_path = "/api/operating-ui-history"
                if query_suffix:
                    api_path += "?" + "&".join(query_suffix)
                self._respond_html(
                    render_operating_ui_history_shell_html(
                        build_operating_ui_history_shell_data(
                            runtime_root,
                            asset_id=asset_id,
                            sort_by=sort_by,
                        ),
                        api_path=api_path,
                    )
                )
                return
            if request_path in {"/operating", "/operating.html"}:
                self._respond_html(
                    render_user_operating_page(
                        runtime_root,
                        asset_id=_single(query, "asset_id") or None,
                        selected_row_key=_single(query, "selected_row_key") or None,
                    )
                )
                return
            if request_path in {"/explore", "/explore.html"}:
                self._respond_html(
                    render_user_explore_page(
                        runtime_root,
                        object_id=_single(query, "object_id") or None,
                        candidate_id=_single(query, "candidate_id") or None,
                    )
                )
                return
            if request_path == "/actions/save-explore-candidate":
                asset_id = _single(query, "asset_id") or None
                candidate_id = _single(query, "candidate_id") or None
                source = _build_source(runtime_root, asset_id=asset_id)
                candidates = _build_explore_candidates(
                    source["selected_asset"],
                    raw_asset=source.get("raw_selected_asset") or {},
                )
                target = None
                if candidate_id:
                    for candidate in candidates:
                        if candidate.get("id") == candidate_id:
                            target = candidate
                            break
                if target is None and candidates:
                    target = candidates[0]
                if target is None:
                    self._redirect(
                        _path_with_query(
                            "/explore",
                            asset_id=source.get("selected_asset_id") or asset_id,
                            save_status="no_candidate",
                        )
                    )
                    return
                reading_context = _build_explore_reading_context(
                    asset_id=source.get("selected_asset_id") or asset_id or "",
                    raw_asset=source.get("raw_selected_asset") or {},
                    candidate=target,
                )
                if not reading_context.get("object_paragraph_text") or not reading_context.get("value_paragraph_text"):
                    self._redirect(
                        _path_with_query(
                            "/explore",
                            object_id=source.get("selected_asset_id") or asset_id,
                            candidate_id=target.get("id"),
                            save_status="needs_validation",
                        )
                    )
                    return
                ensure_active_asset_first_pass_fragments(
                    runtime_root,
                    raw_asset=source.get("raw_selected_asset") or {},
                )
                record, _created = create_saved_connection_from_candidate(
                    runtime_root,
                    candidate=target,
                    reading_context=reading_context,
                )
                self._redirect(
                    _path_with_query(
                        "/memory",
                        connection_id=record.get("id"),
                    )
                )
                return
            if request_path in {"/search", "/search.html"}:
                self._respond_html(
                    render_user_search_page(
                        runtime_root,
                        q=_single(query, "q"),
                        mode=_single(query, "mode") or "object",
                        result_id=_single(query, "result_id") or None,
                    )
                )
                return
            if request_path in {"/memory", "/memory.html"}:
                self._respond_html(
                    render_user_memory_page(
                        runtime_root,
                        connection_id=_single(query, "connection_id") or None,
                    )
                )
                return
            if request_path in {"/similar", "/similar.html"}:
                self._respond_html(
                    render_user_similar_page(
                        runtime_root,
                        seed_id=_single(query, "seed_id") or None,
                        similar_id=_single(query, "similar_id") or None,
                    )
                )
                return
            if request_path in {"/vectorfl-paper", "/vectorfl-paper.html"}:
                self._respond_html(
                    render_vectorfl_paper_operable_shell(
                        build_vectorfl_paper_operable_state(runtime_root)
                    )
                )
                return
            if request_path in {"/vectorfl-engine", "/vectorfl-engine.html"}:
                self._respond_html(
                    render_vectorfl_integrated_engine_shell(
                        build_vectorfl_integrated_engine_state(runtime_root)
                    )
                )
                return
            if request_path in {"/vectorfl-engine/team", "/vectorfl-engine/team.html"}:
                self._respond_html(
                    render_vectorfl_integrated_engine_shell(
                        build_vectorfl_integrated_engine_state(runtime_root),
                        page="team",
                    )
                )
                return
            if request_path in {"/vectorfl-engine/operate", "/vectorfl-engine/operate.html"}:
                self._respond_html(
                    render_vectorfl_integrated_engine_shell(
                        build_vectorfl_integrated_engine_state(runtime_root),
                        page="engine",
                    )
                )
                return
            if request_path in {"/vectorfl-engine/vectorfl", "/vectorfl-engine/vectorfl.html"}:
                self._respond_html(
                    render_vectorfl_integrated_engine_shell(
                        build_vectorfl_integrated_engine_state(runtime_root),
                        page="vectorfl",
                    )
                )
                return
            if request_path in {"/vectorfl-engine/engine", "/vectorfl-engine/engine.html"}:
                self._respond_html(
                    render_vectorfl_integrated_engine_shell(
                        build_vectorfl_integrated_engine_state(runtime_root),
                        page="engine",
                    )
                )
                return
            if request_path in {"/vectorfl-engine/internal", "/vectorfl-engine/internal.html"}:
                self._respond_html(
                    render_vectorfl_integrated_engine_shell(
                        build_vectorfl_integrated_engine_state(runtime_root),
                        page="internal",
                    )
                )
                return
            if request_path in {"/vectorfl-engine/synthesis", "/vectorfl-engine/synthesis.html"}:
                self._respond_html(
                    render_vectorfl_integrated_engine_shell(
                        build_vectorfl_integrated_engine_state(runtime_root),
                        page="synthesis",
                    )
                )
                return
            if request_path == "/api/graph":
                self._respond_json(build_space_graph_view_data(runtime_root))
                return
            if request_path == "/api/dust":
                self._respond_json(build_dust_field_data(runtime_root))
                return
            if request_path == "/api/source":
                self._respond_json(build_source_fragment_view_data(runtime_root))
                return
            if request_path == "/api/terrain":
                self._respond_json(build_terrain_map_data(runtime_root))
                return
            if request_path == "/api/atlas":
                self._respond_json(build_region_atlas_data(runtime_root))
                return
            if request_path == "/api/measurements":
                self._respond_json(build_measurement_view_data(runtime_root))
                return
            if request_path == "/api/process-console":
                self._respond_json(
                    build_process_console_view_data(
                        runtime_root,
                        asset_id=_single(query, "asset_id"),
                        filters=_filters_from_query(query),
                        sort_by=_single(query, "sort_by") or "updated_at",
                        compare_index=_int_value(query, "compare_index"),
                        debug=_single(query, "debug") in {"1", "true", "yes"},
                    )
                )
                return
            if request_path == "/api/operating-ui-demo":
                self._respond_json(
                    build_operating_ui_composition_demo_data(
                        runtime_root,
                        case=_single(query, "case") or "a",
                    )
                )
                return
            if request_path == "/api/operating-ui-live":
                self._respond_json(
                    build_operating_ui_live_composition_data(
                        runtime_root,
                        asset_id=_single(query, "asset_id") or None,
                        sort_by=_single(query, "sort_by") or "updated_at",
                        live_mode=_single(query, "live_mode") or None,
                        compare_mode=_single(query, "compare_mode") or None,
                    )
                )
                return
            if request_path == "/api/operating-ui-phase1":
                self._respond_json(
                    build_operating_ui_phase1_shell_data(
                        runtime_root,
                        asset_id=_single(query, "asset_id") or None,
                        sort_by=_single(query, "sort_by") or "updated_at",
                        live_mode=_single(query, "live_mode") or None,
                        compare_mode=_single(query, "compare_mode") or None,
                        history_snapshot_ref=_single(query, "history_snapshot_ref") or None,
                        history_cluster_ref=_single(query, "history_cluster_ref") or None,
                        history_trace_ref=_single(query, "history_trace_ref") or None,
                        history_reread_summary=_single(query, "history_reread_summary") or None,
                        history_source_note=_single(query, "history_source_note") or None,
                    )
                )
                return
            if request_path == "/api/operating-ui-history":
                self._respond_json(
                    build_operating_ui_history_shell_data(
                        runtime_root,
                        asset_id=_single(query, "asset_id") or None,
                        sort_by=_single(query, "sort_by") or "updated_at",
                    )
                )
                return
            if request_path == "/api/vectorfl-paper/state":
                self._respond_json(build_vectorfl_paper_operable_state(runtime_root))
                return
            if request_path == "/api/vectorfl-engine/state":
                self._respond_json(build_vectorfl_integrated_engine_state(runtime_root))
                return
            if request_path == "/health":
                self._respond_json({"status": "ok", "runtime_root": str(runtime_root)})
                return
            self._respond_json({"error": "not found"}, status=HTTPStatus.NOT_FOUND)

        def do_POST(self) -> None:
            request_path = urlparse(self.path).path
            if request_path == "/api/vectorfl-engine/actions/work-packet":
                content_length = int(self.headers.get("Content-Length", "0"))
                raw_body = self.rfile.read(content_length) if content_length else b"{}"
                try:
                    payload = json.loads(raw_body.decode("utf-8"))
                except json.JSONDecodeError:
                    self._respond_json({"error": "invalid json body"}, status=HTTPStatus.BAD_REQUEST)
                    return

                try:
                    record = create_vectorfl_integrated_engine_work_packet(runtime_root, payload)
                except ValueError as error:
                    self._respond_json({"error": str(error)}, status=HTTPStatus.BAD_REQUEST)
                    return
                except Exception as error:
                    self._respond_json({"error": "internal error", "detail": str(error)}, status=HTTPStatus.INTERNAL_SERVER_ERROR)
                    return

                self._respond_json(record, status=HTTPStatus.CREATED)
                return
            if request_path == "/api/vectorfl-engine/actions/assignment":
                content_length = int(self.headers.get("Content-Length", "0"))
                raw_body = self.rfile.read(content_length) if content_length else b"{}"
                try:
                    payload = json.loads(raw_body.decode("utf-8"))
                except json.JSONDecodeError:
                    self._respond_json({"error": "invalid json body"}, status=HTTPStatus.BAD_REQUEST)
                    return

                try:
                    record = create_vectorfl_integrated_engine_assignment(runtime_root, payload)
                except ValueError as error:
                    self._respond_json({"error": str(error)}, status=HTTPStatus.BAD_REQUEST)
                    return
                except Exception as error:
                    self._respond_json({"error": "internal error", "detail": str(error)}, status=HTTPStatus.INTERNAL_SERVER_ERROR)
                    return

                self._respond_json(record, status=HTTPStatus.CREATED)
                return
            if request_path == "/api/vectorfl-engine/actions/worker-session":
                content_length = int(self.headers.get("Content-Length", "0"))
                raw_body = self.rfile.read(content_length) if content_length else b"{}"
                try:
                    payload = json.loads(raw_body.decode("utf-8"))
                except json.JSONDecodeError:
                    self._respond_json({"error": "invalid json body"}, status=HTTPStatus.BAD_REQUEST)
                    return

                try:
                    record = create_vectorfl_integrated_engine_worker_session(runtime_root, payload)
                except ValueError as error:
                    self._respond_json({"error": str(error)}, status=HTTPStatus.BAD_REQUEST)
                    return
                except Exception as error:
                    self._respond_json({"error": "internal error", "detail": str(error)}, status=HTTPStatus.INTERNAL_SERVER_ERROR)
                    return

                self._respond_json(record, status=HTTPStatus.CREATED)
                return
            if request_path == "/api/vectorfl-engine/actions/worker-session/from-current-context":
                try:
                    record = create_worker_session_from_current_context(runtime_root)
                except ValueError as error:
                    self._respond_json({"error": str(error)}, status=HTTPStatus.BAD_REQUEST)
                    return
                except Exception as error:
                    self._respond_json({"error": "internal error", "detail": str(error)}, status=HTTPStatus.INTERNAL_SERVER_ERROR)
                    return

                self._respond_json(record, status=HTTPStatus.CREATED)
                return
            if request_path == "/api/vectorfl-engine/actions/operating-dialogue":
                content_length = int(self.headers.get("Content-Length", "0"))
                raw_body = self.rfile.read(content_length) if content_length else b"{}"
                try:
                    payload = json.loads(raw_body.decode("utf-8"))
                except json.JSONDecodeError:
                    self._respond_json({"error": "invalid json body"}, status=HTTPStatus.BAD_REQUEST)
                    return

                try:
                    record = create_vectorfl_integrated_engine_operating_dialogue(runtime_root, payload)
                except ValueError as error:
                    self._respond_json({"error": str(error)}, status=HTTPStatus.BAD_REQUEST)
                    return
                except Exception as error:
                    self._respond_json({"error": "internal error", "detail": str(error)}, status=HTTPStatus.INTERNAL_SERVER_ERROR)
                    return

                self._respond_json(record, status=HTTPStatus.CREATED)
                return
            if request_path == "/api/vectorfl-engine/actions/worker-launch-draft":
                content_length = int(self.headers.get("Content-Length", "0"))
                raw_body = self.rfile.read(content_length) if content_length else b"{}"
                try:
                    payload = json.loads(raw_body.decode("utf-8"))
                except json.JSONDecodeError:
                    self._respond_json({"error": "invalid json body"}, status=HTTPStatus.BAD_REQUEST)
                    return

                try:
                    record = create_vectorfl_integrated_engine_worker_launch_draft(runtime_root, payload)
                except ValueError as error:
                    self._respond_json({"error": str(error)}, status=HTTPStatus.BAD_REQUEST)
                    return
                except Exception as error:
                    self._respond_json({"error": "internal error", "detail": str(error)}, status=HTTPStatus.INTERNAL_SERVER_ERROR)
                    return

                self._respond_json(record, status=HTTPStatus.CREATED)
                return
            if request_path == "/api/vectorfl-engine/actions/run-worker-launch-draft":
                content_length = int(self.headers.get("Content-Length", "0"))
                raw_body = self.rfile.read(content_length) if content_length else b"{}"
                try:
                    payload = json.loads(raw_body.decode("utf-8"))
                except json.JSONDecodeError:
                    self._respond_json({"error": "invalid json body"}, status=HTTPStatus.BAD_REQUEST)
                    return

                try:
                    record = run_vectorfl_integrated_engine_worker_launch_draft(runtime_root, payload)
                except ValueError as error:
                    self._respond_json({"error": str(error)}, status=HTTPStatus.BAD_REQUEST)
                    return
                except Exception as error:
                    self._respond_json({"error": "internal error", "detail": str(error)}, status=HTTPStatus.INTERNAL_SERVER_ERROR)
                    return

                self._respond_json(record, status=HTTPStatus.CREATED)
                return
            if request_path == "/api/vectorfl-engine/actions/cli-session/run":
                content_length = int(self.headers.get("Content-Length", "0"))
                raw_body = self.rfile.read(content_length) if content_length else b"{}"
                try:
                    payload = json.loads(raw_body.decode("utf-8"))
                except json.JSONDecodeError:
                    self._respond_json({"error": "invalid json body"}, status=HTTPStatus.BAD_REQUEST)
                    return

                try:
                    record = run_integrated_engine_cli_session(runtime_root, payload)
                except ValueError as error:
                    self._respond_json({"error": str(error)}, status=HTTPStatus.BAD_REQUEST)
                    return
                except Exception as error:
                    self._respond_json({"error": "internal error", "detail": str(error)}, status=HTTPStatus.INTERNAL_SERVER_ERROR)
                    return

                self._respond_json(record, status=HTTPStatus.CREATED)
                return
            if request_path == "/api/vectorfl-engine/actions/cli-session/mark":
                content_length = int(self.headers.get("Content-Length", "0"))
                raw_body = self.rfile.read(content_length) if content_length else b"{}"
                try:
                    payload = json.loads(raw_body.decode("utf-8"))
                except json.JSONDecodeError:
                    self._respond_json({"error": "invalid json body"}, status=HTTPStatus.BAD_REQUEST)
                    return

                try:
                    record = mark_integrated_engine_cli_session(runtime_root, payload)
                except ValueError as error:
                    self._respond_json({"error": str(error)}, status=HTTPStatus.BAD_REQUEST)
                    return
                except Exception as error:
                    self._respond_json({"error": "internal error", "detail": str(error)}, status=HTTPStatus.INTERNAL_SERVER_ERROR)
                    return

                self._respond_json(record, status=HTTPStatus.CREATED)
                return
            if request_path == "/api/vectorfl-engine/actions/language-loop/run":
                content_length = int(self.headers.get("Content-Length", "0"))
                raw_body = self.rfile.read(content_length) if content_length else b"{}"
                try:
                    payload = json.loads(raw_body.decode("utf-8"))
                except json.JSONDecodeError:
                    self._respond_json({"error": "invalid json body"}, status=HTTPStatus.BAD_REQUEST)
                    return

                try:
                    record = run_integrated_engine_language_loop(runtime_root, payload)
                except ValueError as error:
                    self._respond_json({"error": str(error)}, status=HTTPStatus.BAD_REQUEST)
                    return
                except Exception as error:
                    self._respond_json({"error": "internal error", "detail": str(error)}, status=HTTPStatus.INTERNAL_SERVER_ERROR)
                    return

                self._respond_json(record, status=HTTPStatus.CREATED)
                return
            if request_path == "/api/vectorfl-engine/actions/language-loop/harvest":
                content_length = int(self.headers.get("Content-Length", "0"))
                raw_body = self.rfile.read(content_length) if content_length else b"{}"
                try:
                    payload = json.loads(raw_body.decode("utf-8"))
                except json.JSONDecodeError:
                    self._respond_json({"error": "invalid json body"}, status=HTTPStatus.BAD_REQUEST)
                    return

                try:
                    record = harvest_integrated_engine_language_loop(runtime_root, payload)
                except ValueError as error:
                    self._respond_json({"error": str(error)}, status=HTTPStatus.BAD_REQUEST)
                    return
                except Exception as error:
                    self._respond_json({"error": "internal error", "detail": str(error)}, status=HTTPStatus.INTERNAL_SERVER_ERROR)
                    return

                self._respond_json(record, status=HTTPStatus.CREATED)
                return
            if request_path == "/api/vectorfl-engine/actions/run-codex-assignment":
                try:
                    record = run_codex_assignment_bridge(runtime_root)
                except ValueError as error:
                    self._respond_json({"error": str(error)}, status=HTTPStatus.BAD_REQUEST)
                    return
                except Exception as error:
                    self._respond_json({"error": "internal error", "detail": str(error)}, status=HTTPStatus.INTERNAL_SERVER_ERROR)
                    return

                self._respond_json(record, status=HTTPStatus.CREATED)
                return
            if request_path == "/api/vectorfl-engine/actions/supervisor-route":
                content_length = int(self.headers.get("Content-Length", "0"))
                raw_body = self.rfile.read(content_length) if content_length else b"{}"
                try:
                    payload = json.loads(raw_body.decode("utf-8"))
                except json.JSONDecodeError:
                    self._respond_json({"error": "invalid json body"}, status=HTTPStatus.BAD_REQUEST)
                    return

                try:
                    record = create_vectorfl_integrated_engine_supervisor_route(runtime_root, payload)
                except ValueError as error:
                    self._respond_json({"error": str(error)}, status=HTTPStatus.BAD_REQUEST)
                    return
                except Exception as error:
                    self._respond_json({"error": "internal error", "detail": str(error)}, status=HTTPStatus.INTERNAL_SERVER_ERROR)
                    return

                self._respond_json(record, status=HTTPStatus.CREATED)
                return
            if request_path == "/api/vectorfl-engine/actions/run-internal-read":
                try:
                    record = run_internal_read_from_supervisor_route(runtime_root)
                except ValueError as error:
                    self._respond_json({"error": str(error)}, status=HTTPStatus.BAD_REQUEST)
                    return
                except Exception as error:
                    self._respond_json({"error": "internal error", "detail": str(error)}, status=HTTPStatus.INTERNAL_SERVER_ERROR)
                    return

                self._respond_json(record, status=HTTPStatus.CREATED)
                return
            if request_path == "/api/vectorfl-engine/actions/run-synthesis":
                try:
                    record = run_synthesis_from_internal_read(runtime_root)
                except ValueError as error:
                    self._respond_json({"error": str(error)}, status=HTTPStatus.BAD_REQUEST)
                    return
                except Exception as error:
                    self._respond_json({"error": "internal error", "detail": str(error)}, status=HTTPStatus.INTERNAL_SERVER_ERROR)
                    return

                self._respond_json(record, status=HTTPStatus.CREATED)
                return
            if request_path == "/api/vectorfl-engine/actions/supervisor-gate":
                content_length = int(self.headers.get("Content-Length", "0"))
                raw_body = self.rfile.read(content_length) if content_length else b"{}"
                try:
                    payload = json.loads(raw_body.decode("utf-8"))
                except json.JSONDecodeError:
                    self._respond_json({"error": "invalid json body"}, status=HTTPStatus.BAD_REQUEST)
                    return

                try:
                    record = create_supervisor_gate_from_synthesis(runtime_root, payload)
                except ValueError as error:
                    self._respond_json({"error": str(error)}, status=HTTPStatus.BAD_REQUEST)
                    return
                except Exception as error:
                    self._respond_json({"error": "internal error", "detail": str(error)}, status=HTTPStatus.INTERNAL_SERVER_ERROR)
                    return

                self._respond_json(record, status=HTTPStatus.CREATED)
                return
            if request_path == "/api/vectorfl-engine/actions/implementation-brief":
                try:
                    record = create_implementation_brief_from_supervisor_gate(runtime_root)
                except ValueError as error:
                    self._respond_json({"error": str(error)}, status=HTTPStatus.BAD_REQUEST)
                    return
                except Exception as error:
                    self._respond_json({"error": "internal error", "detail": str(error)}, status=HTTPStatus.INTERNAL_SERVER_ERROR)
                    return

                self._respond_json(record, status=HTTPStatus.CREATED)
                return
            if request_path == "/api/vectorfl-engine/actions/implementation-launch-gate":
                content_length = int(self.headers.get("Content-Length", "0"))
                raw_body = self.rfile.read(content_length) if content_length else b"{}"
                try:
                    payload = json.loads(raw_body.decode("utf-8"))
                except json.JSONDecodeError:
                    self._respond_json({"error": "invalid json body"}, status=HTTPStatus.BAD_REQUEST)
                    return

                try:
                    record = create_implementation_launch_gate(runtime_root, payload)
                except ValueError as error:
                    self._respond_json({"error": str(error)}, status=HTTPStatus.BAD_REQUEST)
                    return
                except Exception as error:
                    self._respond_json({"error": "internal error", "detail": str(error)}, status=HTTPStatus.INTERNAL_SERVER_ERROR)
                    return

                self._respond_json(record, status=HTTPStatus.CREATED)
                return
            if request_path == "/api/operating-ui-phase1/path-residue":
                content_length = int(self.headers.get("Content-Length", "0"))
                raw_body = self.rfile.read(content_length) if content_length else b"{}"
                try:
                    payload = json.loads(raw_body.decode("utf-8"))
                except json.JSONDecodeError:
                    self._respond_json({"error": "invalid json body"}, status=HTTPStatus.BAD_REQUEST)
                    return

                try:
                    record = save_phase1_path_residue(
                        runtime_root,
                        object_id=str(payload.get("object_id") or "").strip() or None,
                        lens_id=str(payload.get("lens_id") or "").strip() or None,
                        position_value=str(payload.get("position_value") or "").strip() or None,
                        preview_ready=bool(payload.get("preview_ready")),
                    )
                except Exception as error:
                    self._respond_json({"error": "internal error", "detail": str(error)}, status=HTTPStatus.INTERNAL_SERVER_ERROR)
                    return

                self._respond_json(record, status=HTTPStatus.CREATED)
                return
            if request_path == "/api/operating-ui-phase1/stickers":
                content_length = int(self.headers.get("Content-Length", "0"))
                raw_body = self.rfile.read(content_length) if content_length else b"{}"
                try:
                    payload = json.loads(raw_body.decode("utf-8"))
                except json.JSONDecodeError:
                    self._respond_json({"error": "invalid json body"}, status=HTTPStatus.BAD_REQUEST)
                    return

                try:
                    record = create_phase1_memory_sticker(
                        runtime_root,
                        object_id=str(payload.get("object_id") or "").strip(),
                        lens_id=str(payload.get("lens_id") or "").strip(),
                        position_value=str(payload.get("position_value") or "").strip(),
                        preview_connection_summary=str(payload.get("preview_connection_summary") or "").strip(),
                        why_selected_short=str(payload.get("why_selected_short") or "").strip() or None,
                        why_mode=str(payload.get("why_mode") or "").strip() or None,
                        optional_note=str(payload.get("optional_note") or "").strip() or None,
                        seed_ref=str(payload.get("seed_ref") or "").strip() or None,
                    )
                except ValueError as error:
                    self._respond_json({"error": str(error)}, status=HTTPStatus.BAD_REQUEST)
                    return
                except Exception as error:
                    self._respond_json({"error": "internal error", "detail": str(error)}, status=HTTPStatus.INTERNAL_SERVER_ERROR)
                    return

                self._respond_json(record, status=HTTPStatus.CREATED)
                return
            if request_path != "/api/ingest":
                self._respond_json({"error": "not found"}, status=HTTPStatus.NOT_FOUND)
                return

            content_length = int(self.headers.get("Content-Length", "0"))
            raw_body = self.rfile.read(content_length) if content_length else b"{}"
            try:
                payload = json.loads(raw_body.decode("utf-8"))
            except json.JSONDecodeError:
                self._respond_json({"error": "invalid json body"}, status=HTTPStatus.BAD_REQUEST)
                return

            try:
                result = ingest_live_input(runtime_root, payload)
            except ValueError as error:
                self._respond_json({"error": str(error)}, status=HTTPStatus.BAD_REQUEST)
                return
            except Exception as error:
                self._respond_json({"error": "internal error", "detail": str(error)}, status=HTTPStatus.INTERNAL_SERVER_ERROR)
                return

            self._respond_json(result, status=HTTPStatus.CREATED)

        def log_message(self, format: str, *args: object) -> None:
            return

        def _respond_html(self, html: str) -> None:
            body = html.encode("utf-8")
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def _respond_json(self, payload: Dict[str, object], status: HTTPStatus = HTTPStatus.OK) -> None:
            body = json.dumps(payload, ensure_ascii=False, indent=2).encode("utf-8")
            self.send_response(status)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def _redirect(self, location: str) -> None:
            self.send_response(HTTPStatus.SEE_OTHER)
            self.send_header("Location", location)
            self.send_header("Content-Length", "0")
            self.end_headers()

    def _single(query: Dict[str, List[str]], key: str) -> str:
        values = query.get(key) or []
        return values[0] if values else ""

    def _filters_from_query(query: Dict[str, List[str]]) -> Dict[str, str]:
        filters: Dict[str, str] = {}
        for key in [
            "packet_texture",
            "grounding_status",
            "emergence_status",
            "carryover_risk",
            "maturation_state",
            "traceable_only",
        ]:
            value = _single(query, key)
            if value:
                filters[key] = value
        return filters

    def _int_value(query: Dict[str, List[str]], key: str) -> int:
        value = _single(query, key)
        if not value:
            return 0
        try:
            return int(value)
        except ValueError:
            return 0

    def _path_with_query(path: str, **query: str) -> str:
        clean = {key: value for key, value in query.items() if value not in (None, "")}
        if not clean:
            return path
        return path + "?" + urlencode(clean)

    server = ThreadingHTTPServer((host, port), ViewerServerHandler)
    print("viewer_server: http://%s:%s" % (host, port))
    print("runtime_root: %s" % runtime_root)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
