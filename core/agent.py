from core.planner import create_plan
from core.router import execute
from core.memory import save_memory
from core.voice import speak

def run_agent(user_input):
    plan = create_plan(user_input)

    results = []

    for step in plan["steps"]:
        result = execute(step)
        results.append(result)

    final = " | ".join(results)

    save_memory(f"Task: {user_input} | Result: {final}")

    speak(final)

    return final