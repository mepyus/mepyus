# viewer http reachability check v1

## verdict

reachable

## executed commands

```bash
python3 --version
python3 -m py_compile app/core/runtime/viewer_server.py scripts/run_viewer_server.py
python3 scripts/run_viewer_server.py runtime 127.0.0.1 8421
python3 scripts/run_viewer_server.py runtime 127.0.0.1 8423
python3 scripts/run_viewer_server.py runtime 127.0.0.1 8531
curl -i http://127.0.0.1:8531/operating-ui-phase1
curl -i http://127.0.0.1:8531/operating-ui-history
python3 - <<'PY'
import urllib.request
base='http://127.0.0.1:8531'
phase1=urllib.request.urlopen(base + '/operating-ui-phase1').read().decode('utf-8')
history=urllib.request.urlopen(base + '/operating-ui-history').read().decode('utf-8')
print({
 'phase1_has_operating': 'Operating: observe now' in phase1,
 'phase1_has_history_companion': 'History Companion: time-axis read' in phase1,
 'phase1_has_phase1_shell': 'phase1 shell' in phase1,
 'phase1_has_phase2_history': 'phase2 history' in phase1,
 'history_has_open_main': 'Open in Main Operating Set' in history,
 'history_has_main_set_nav': 'main operating set' in history,
 'history_has_open_in_phase': 'Open in Phase' in history,
 'history_has_restore_state': 'Restore State' in history,
 'history_has_replay_in': 'replay in' in history.lower(),
})
PY
```

## bind result

- runtime
  - Python `3.8.0`
- startup command confirmed
  - [run_viewer_server.py](/Users/sungsookim/universe/vectorfl_replica/scripts/run_viewer_server.py)
- bind attempts
  - `127.0.0.1:8421`
    - blocked by port collision: `OSError: [Errno 48] Address already in use`
  - `127.0.0.1:8423`
    - blocked inside sandbox bind path: `PermissionError: [Errno 1] Operation not permitted`
  - `127.0.0.1:8531`
    - successful outside-sandbox bind
    - startup log: `viewer_server: http://127.0.0.1:8531`

## route reachability result

- `/operating-ui-phase1`
  - reachable
  - confirmed by outside-sandbox `curl -i`
  - returned `HTTP/1.0 200 OK`
- `/operating-ui-history`
  - reachable
  - confirmed by outside-sandbox `curl -i`
  - returned `HTTP/1.0 200 OK`

## rendered check result

- confirmed on reachable `Main Operating Set`
  - `Operating: observe now`
  - `Explore: build path`
  - `Search: direct access`
  - `Memory: saved paths`
  - `Similar: local re-query`
  - `History Companion: time-axis read`
- confirmed on reachable `History Companion`
  - `Open in Main Operating Set`
  - `main operating set`
- phase language not exposed in reachable HTML
  - `phase1 shell`: absent
  - `phase2 history`: absent
  - `Open in Phase`: absent
  - `Restore State`: absent
  - `replay in`: absent

## blocker layer

No app-structure blocker remains for this check.

Observed blockers were environment-layer only:

- port collision on `8421`
- sandbox bind restriction when trying to open a localhost server from the sandbox
- sandbox-to-outside-sandbox localhost reachability mismatch during earlier curl attempts

These do not require page composition, route, or labeling changes.

## next smallest action

browser-level manual smoke check on `http://127.0.0.1:8531`
