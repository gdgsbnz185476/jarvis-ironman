from core.tools import open_app, open_website, create_file, run_terminal_command
import json

def execute(step):
    action = step.get("action")
    inp = step.get("input")

    if action == "open_app":
        return open_app(inp)

    if action == "open_website":
        return open_website(inp)

    if action == "create_file":
        return create_file(inp["path"], inp.get("content", ""))

    if action == "run_terminal_command":
        return run_terminal_command(inp)

    return "Unknown action"
