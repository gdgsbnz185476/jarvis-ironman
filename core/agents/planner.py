from core.brain import ask_ai

def plan(task):
    return ask_ai(f"Break this into steps: {task}")
