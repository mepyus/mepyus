from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Callable, Dict
import json

from app.runtime.dust_field import build_dust_field_data, render_dust_field_html
from app.runtime.graph_view import build_space_graph_view_data, render_space_graph_view_html
from app.runtime.live_input import ingest_live_input


def run_viewer_server(runtime_root: Path, host: str = "127.0.0.1", port: int = 8421) -> None:
    runtime_root = runtime_root.resolve()

    class ViewerServerHandler(BaseHTTPRequestHandler):
        def do_GET(self) -> None:
            if self.path in {"/", "/index.html"}:
                self._respond_html(
                    render_space_graph_view_html(
                        build_space_graph_view_data(runtime_root),
                        interactive=True,
                    )
                )
                return
            if self.path in {"/dust", "/dust.html"}:
                self._respond_html(render_dust_field_html(build_dust_field_data(runtime_root)))
                return
            if self.path == "/api/graph":
                self._respond_json(build_space_graph_view_data(runtime_root))
                return
            if self.path == "/api/dust":
                self._respond_json(build_dust_field_data(runtime_root))
                return
            if self.path == "/health":
                self._respond_json({"status": "ok", "runtime_root": str(runtime_root)})
                return
            self._respond_json({"error": "not found"}, status=HTTPStatus.NOT_FOUND)

        def do_POST(self) -> None:
            if self.path != "/api/ingest":
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

    server = ThreadingHTTPServer((host, port), ViewerServerHandler)
    print("viewer_server: http://%s:%s" % (host, port))
    print("runtime_root: %s" % runtime_root)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
