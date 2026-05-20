from core.tools.system import open_app
from core.tools.files import create_file

def execute(step):
    action = step.get("action")
    data = step.get("data")

    if action == "open_app":
        return open_app(data)

    if action == "create_file":
        return create_file(data["path"], data.get("content", ""))

    return "No valid action found"
