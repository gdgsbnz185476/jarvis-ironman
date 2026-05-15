def validate(step):
    """
    Basic safety check for actions
    """
    dangerous_keywords = [
        "rm -rf",
        "shutdown",
        "format",
        "delete system",
        "kill"
    ]

    # If step is not a dict, allow it
    if not isinstance(step, dict):
        return True

    content = str(step.get("input", "")).lower()

    for word in dangerous_keywords:
        if word in content:
            return False

    return True
