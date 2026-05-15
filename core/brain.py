import os
import requests

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MODEL = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")


def ask_ai(prompt, memory=""):
    url = "https://api.groq.com/openai/v1/chat/completions"

    system = """
You are JARVIS, an autonomous AI agent.

You do NOT just respond.
You:
1. Understand goal
2. Decide if tools are needed
3. Execute step-by-step reasoning internally

If action is needed, output ONLY JSON:

{
  "action": "tool_name",
  "input": "value"
}

TOOLS:
- open_app
- open_website
- create_file
- run_terminal_command
- sleep

If no action needed, respond normally.

You are always proactive, not passive.
"""

    data = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": system + "\nMemory:\n" + memory},
            {"role": "user", "content": prompt}
        ]
    }

    r = requests.post(url, headers={
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }, json=data)

    res = r.json()

    if "error" in res:
        return {"type": "error", "content": res["error"]["message"]}

    reply = res["choices"][0]["message"]["content"]

    return {"type": "text", "content": reply}