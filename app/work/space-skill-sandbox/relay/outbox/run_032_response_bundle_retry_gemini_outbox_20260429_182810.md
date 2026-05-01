# Gemini Run Result

- packet: app/work/space-skill-sandbox/outputs/next_gemini_task_packet_run_032_tool_affordance_response_bundle_retry_v0.md
- run_id: run_032_response_bundle_retry
- timestamp: 20260429_182810
- dry_run: false
- smoke_text: false
- output_format: json
- timeout_seconds: 180
- raw_result: app/work/space-skill-sandbox/outputs/gemini_raw_results/run_032_response_bundle_retry_gemini_raw_20260429_182810.json
- stderr_result: app/work/space-skill-sandbox/outputs/gemini_raw_results/run_032_response_bundle_retry_gemini_stderr_20260429_182810.log

## Result

Gemini CLI timed out after 180 seconds.

- timeout_seconds: 180
- command_attempted: gemini -p "<prompt redacted>" --output-format json
- gemini_path: /usr/local/bin/gemini
- gemini_version: 0.40.0
- stderr_result: app/work/space-skill-sandbox/outputs/gemini_raw_results/run_032_response_bundle_retry_gemini_stderr_20260429_182810.log
- likely_state: auth_or_network_or_interactive_wait
- next_manual_check: gemini -p "Reply with exactly: GEMINI_SMOKE_OK" --output-format json

## Stderr Tail

      '      }\n' +
      '    ],\n' +
      '    "status": "RESOURCE_EXHAUSTED",\n' +
      '    "details": [\n' +
      '      {\n' +
      '        "@type": "type.googleapis.com/google.rpc.ErrorInfo",\n' +
      '        "reason": "MODEL_CAPACITY_EXHAUSTED",\n' +
      '        "domain": "cloudcode-pa.googleapis.com",\n' +
      '        "metadata": {\n' +
      '          "model": "gemini-3-flash-preview"\n' +
      '        }\n' +
      '      }\n' +
      '    ]\n' +
      '  }\n' +
      '}\n' +
      ']',
    headers: {
      'alt-svc': 'h3=":443"; ma=2592000,h3-29=":443"; ma=2592000',
      'content-length': '630',
      'content-type': 'application/json; charset=UTF-8',
      date: 'Wed, 29 Apr 2026 09:28:28 GMT',
      server: 'ESF',
      'server-timing': 'gfet4t7; dur=11055',
      vary: 'Origin, X-Origin, Referer',
      'x-cloudaicompanion-trace-id': 'e15457675866f256',
      'x-content-type-options': 'nosniff',
      'x-frame-options': 'SAMEORIGIN',
      'x-xss-protection': '0'
    },
    status: 429,
    statusText: 'Too Many Requests',
    request: {
      responseURL: 'https://cloudcode-pa.googleapis.com/v1internal:streamGenerateContent?alt=sse'
    }
  },
  error: undefined,
  status: 429,
  Symbol(gaxios-gaxios-error): '6.7.1'
}
Attempt 1 failed: You have exhausted your capacity on this model. Your quota will reset after 3s.. Retrying after 5645ms...

No repository files were modified by this runner.
