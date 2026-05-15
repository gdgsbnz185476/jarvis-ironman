from core.tools import open_app, open_website, create_file
from core.critic import validate

def execute(step):

    try:
        # allow both dict and string inputs safely
        if isinstance(step, str):
            step = {"action": "chat", "input": step}

        if not validate(step):
            return "Blocked unsafe action"

        action = step.get("action", "chat")
        inp = step.get("input", "")

        if action == "open_app":
            return open_app(inp)

        if action == "open_website":
            return open_website(inp)

        if action == "create_file":
            if isinstance(inp, dict):
                return create_file(inp.get("path", ""), inp.get("content", ""))
            return "Invalid file input"

        if action == "chat":
            return inp

        return "Unknown action"

    except Exception as e:
        return f"Router error: {str(e)}"