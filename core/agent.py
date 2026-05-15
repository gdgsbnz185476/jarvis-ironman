import json
from core.brain import ask_ai
from core.safety import allow_tool
from tools.system import run

def handle(user, memory):
    res = ask_ai(user, memory)

    try:
        data = json.loads(res)
    except:
        return str(res)

    mode = data.get("mode", "chat")

    if mode == "chat":
        return data.get("response", "No response")

    if mode == "tool":
        tool = data.get("tool", "")
        tool_input = data.get("input", "")

        if allow_tool(tool):
            return run(tool_input)

        return "Tool blocked for safety."

    return "Unknown mode."