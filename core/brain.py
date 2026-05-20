import os
import requests
from dotenv import load_dotenv
from core.memory.vector_memory import search_memory, add_memory

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")


def ask_ai(prompt):

    if not GROQ_API_KEY:
        return "Error: Missing API key"

    try:
        # 🧠 MEMORY RETRIEVAL
        memory = search_memory(prompt)
        memory_context = "\n".join(memory)

        # 🧠 SYSTEM PROMPT (FIXED)
        system_prompt = f"""
You are Jarvis, an advanced AI assistant like Iron Man's JARVIS.

Rules:
- Be confident, precise, slightly formal
- Never say generic filler like "I need to rethink that"
- Always provide a useful answer or structured response
- If unsure, make a best logical attempt

Recent memory:
{memory_context}
"""

        full_prompt = f"""
User request:
{prompt}
"""

        url = "https://api.groq.com/openai/v1/chat/completions"

        headers = {
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        }

        data = {
            "model": "llama-3.3-70b-versatile",
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": full_prompt}
            ]
        }

        r = requests.post(url, headers=headers, json=data, timeout=20)
        res = r.json()

        if "error" in res:
            return res["error"]["message"]

        reply = res["choices"][0]["message"]["content"]

        # 🧠 SAVE MEMORY
        add_memory(f"User: {prompt} | Jarvis: {reply}")

        return reply

    except Exception as e:
        return f"Brain error: {str(e)}"