import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")

MODEL = "llama-3.3-70b-versatile"

def ask_ai(prompt, memory):
    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    system = """
You are Jarvis, an autonomous AI agent.
You can decide:
- respond normally
- use tools (browser, system, files)
Return JSON like:
{
  "mode": "chat" or "tool",
  "tool": "browser/search/system/files",
  "input": "what to do",
  "response": "final answer"
}
"""

    data = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": system + "\nMemory:\n" + str(memory)},
            {"role": "user", "content": prompt}
        ]
    }

    r = requests.post(url, headers=headers, json=data)
    res = r.json()

    if "error" in res:
        return {"mode": "chat", "response": res["error"]["message"]}

    return res["choices"][0]["message"]["content"]

