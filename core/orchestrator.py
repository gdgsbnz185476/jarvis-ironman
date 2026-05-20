from core.agents.planner import plan
from core.agents.critic import validate
from core.agents.memory_agent import save_memory
from core.brain import ask_ai
from core.agents.task_agent import run_task


def run_pipeline(user_input):

    if user_input.startswith("do "):
        goal = user_input.replace("do ", "")
        return run_task(goal)

    # normal flow
    steps = plan(user_input)

    result = ask_ai(f"""
User:
{user_input}

Plan:
{steps}
""")

    save_memory({"input": user_input, "output": result})

    return result


def run_pipeline(user_input):

    # 1. PLAN
    steps = plan(user_input)

    # 2. EXECUTE (LLM simulation for now)
    result = ask_ai(f"""
You are Jarvis executing a task.

User request:
{user_input}

Plan:
{steps}

Return final execution result.
""")

    # 3. CRITIC CHECK
    if not validate(result):
        result = "I need to rethink that, sir."

    # 4. MEMORY
    save_memory({
        "input": user_input,
        "output": result
    })

    return result
