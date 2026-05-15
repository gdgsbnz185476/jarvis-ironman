import json

MEM_FILE = "memory.json"

def load_memory():
    try:
        with open(MEM_FILE, "r") as f:
            return f.read()
    except:
        return ""

def save_memory(text):
    data = load_memory()
    data += "\n" + text

    with open(MEM_FILE, "w") as f:
        f.write(data)