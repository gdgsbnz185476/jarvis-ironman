import json
from core.brain import ask_ai

def create_plan(task):
    prompt = f"""
Break this task into steps:

Task: {task}

Return ONLY JSON:
{
  "steps": [
    {"action": "string", "input": "string"}
  ]
}
"""

    result = ask_ai(prompt)

    try:
        return json.loads(result)
    except:
        return {"steps": [{"action": "chat", "input": result}]}
