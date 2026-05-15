import json
import os

FILE = "memory.json"

def load_memory():
    if not os.path.exists(FILE):
        return []
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_memory(text):
    data = load_memory()
    data.append(text)

    with open(FILE, "w") as f:
        json.dump(data, f, indent=2)