import json
import os

FILE = "memory.json"

def load():
    if not os.path.exists(FILE):
        return []
    return json.load(open(FILE))

def save(data):
    json.dump(data, open(FILE, "w"), indent=2)

def add(entry):
    mem = load()
    mem.append(entry)
    save(mem)
