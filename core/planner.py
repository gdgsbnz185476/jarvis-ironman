import json
from core.brain import ask_ai

def create_plan(task):
    prompt = f"""
You are a planning engine.

Break this into steps.

Return STRICT JSON:
{{
  "steps": [
    {{"action": "...", "input": "..."}}
  ]
}}

Task: {task}
"""

    res = ask_ai(prompt)

    try:
        return json.loads(res)
    except:
        return {"steps": [{"action": "chat", "input": res}]}