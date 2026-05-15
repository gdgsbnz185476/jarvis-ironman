def allow_tool(tool):
    safe = ["browser", "system", "files"]
    return tool in safe
