from core.agents.planner import plan
from core.agents.executor import execute
from core.agents.critic import validate
from core.agents.memory_agent import save_memory
from core.brain import ask_ai


def run_task(goal):

    # 1. PLAN
    steps = plan(goal)

    # 2. BREAK INTO ACTION
    execution = ask_ai(f"""
You are an execution engine.

Goal:
{goal}

Plan:
{steps}

Return ONLY structured actions like:
action + input format.
""")

    # 3. CRITIC CHECK
    if not validate(execution):
        execution = "RETRY_REQUIRED"

    # 4. MEMORY
    save_memory({
        "goal": goal,
        "plan": steps,
        "execution": execution
    })

    return execution
