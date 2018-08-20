#!/usr/bin/env nix-shell
#!nix-shell -p jq -i python3 -p python3Packages.requests

import requests
import json

import atexit
import os
import readline


histfile = os.path.join(".gremlin-history")
try:
    readline.read_history_file(histfile)
    # default history len is -1 (infinite), which may grow unruly
    readline.set_history_length(1000)
except FileNotFoundError:
    pass
atexit.register(readline.write_history_file, histfile)


while True:
    line = input("$ ")
    if line is None:
        break
    r = requests.post('http://localhost:8182', json= {'gremlin': line})
    print("code", r.status_code)
    body = r.json()
    print(json.dumps(body, indent=2, sort_keys=True))
