#!/usr/bin/env python3
"""Materialize Gemini lite JSON from Gemini raw output after approved Gemini execution.
This script does not execute Gemini/Codex. It only validates/extracts local files.
"""
import json, os, re, sys
BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
OUT = os.path.join(BASE, 'outputs')
RAW = os.path.join(OUT, 'gemini_raw_output.txt')
LITE = os.path.join(OUT, 'gemini_lite_output.json')
REQUIRED_KEYS = [
    'observed_scope','repeated_patterns','candidate_items','uncertainties',
    'possible_risks','do_not_promote','questions_for_codex','completion_signal'
]

def stop(msg):
    print('STOP: ' + msg, file=sys.stderr)
    sys.exit(2)

def find_json_object(text):
    stripped = text.strip()
    try:
        return json.loads(stripped)
    except Exception:
        pass
    # Try fenced json block first.
    m = re.search(r'```(?:json)?\s*(\{.*?\})\s*```', text, flags=re.S)
    if m:
        return json.loads(m.group(1))
    # Conservative brace scan.
    starts = [i for i,ch in enumerate(text) if ch == '{']
    for s in starts:
        depth = 0
        for i in range(s, len(text)):
            if text[i] == '{': depth += 1
            elif text[i] == '}':
                depth -= 1
                if depth == 0:
                    cand = text[s:i+1]
                    try:
                        return json.loads(cand)
                    except Exception:
                        break
    stop('could not materialize a JSON object from Gemini raw output')

def main():
    if not os.path.isfile(RAW): stop('missing Gemini raw output: ' + RAW)
    obj = find_json_object(open(RAW, encoding='utf-8').read())
    if not isinstance(obj, dict): stop('Gemini lite object is not a JSON object')
    missing = [k for k in REQUIRED_KEYS if k not in obj]
    if missing: stop('Gemini lite JSON missing keys: ' + ', '.join(missing))
    if obj.get('completion_signal') != 'GEMINI_LITE_OUTPUT_DONE':
        stop('completion_signal is not GEMINI_LITE_OUTPUT_DONE')
    for k in REQUIRED_KEYS[:-1]:
        if not isinstance(obj.get(k), list): stop(k + ' must be an array')
    os.makedirs(OUT, exist_ok=True)
    with open(LITE, 'w', encoding='utf-8') as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)
        f.write('\n')
    print('verdict: GEMINI_LITE_OUTPUT_MATERIALIZED_AND_VALIDATED')
    print('wrote: ' + LITE)
if __name__ == '__main__':
    main()
