#!/bin/bash

script_path="solve.py"
url_encoded_script=$(<"$script_path" python3 -c "import sys, urllib.parse; print(urllib.parse.quote(sys.stdin.read()))")
url="https://helsectf2024-2da207d37b091b1b4dff-not-cipher.chals.io/?program=$url_encoded_script"
curl "$url"

