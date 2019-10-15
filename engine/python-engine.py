import sys
import json

with open('en_input.json') as f:
    data = json.load(f)

print(data)

sys.stdout.flush()
