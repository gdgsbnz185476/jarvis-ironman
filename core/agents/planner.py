from core.brain import ask_ai

def plan(task):
    return ask_ai(f"""
You are a planning agent.

Break this task into clear steps:

Task: {task}

Return steps as a simple numbered list.
""")
