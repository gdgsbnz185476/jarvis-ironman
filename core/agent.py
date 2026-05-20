from core.brain import ask_ai
from core.agents.planner import plan
from core.agents.critic import validate
from core.agents.memory_agent import save_memory

def run_agent(user_input):

    # 1. PLAN
    steps = plan(user_input)

    # 2. EXECUTE (LLM-based response for now)
    response = ask_ai(f"""
You are Jarvis.

User request:
{user_input}

Plan:
{steps}

Respond as final answer.
""")

    # 3. CRITIC CHECK
    if not validate(response):
        response = "I need to rethink that, sir."

    # 4. MEMORY
    save_memory({
        "input": user_input,
        "output": response
    })

    return response