import os
import requests
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def ask_ai(prompt):

    if not GROQ_API_KEY:
        return "Error: Missing API key"

    try:
        url = "https://api.groq.com/openai/v1/chat/completions"

        headers = {
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        }

        data = {
            "model": "llama-3.1-70b-versatile",
            "messages": [
                {"role": "system", "content": "You are Jarvis AI."},
                {"role": "user", "content": prompt}
            ]
        }

        r = requests.post(url, headers=headers, json=data, timeout=20)
        res = r.json()

        if "error" in res:
            return res["error"]["message"]

        return res["choices"][0]["message"]["content"]

    except Exception as e:
        return f"Brain error: {str(e)}"