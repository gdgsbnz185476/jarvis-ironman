from core.brain import ask_ai

def validate(output):
    result = ask_ai(f"""
You are a critic agent.

Check if this response is:
- correct
- safe
- useful

Response:
{output}

Reply YES or NO with a reason.
""")

    return "YES" in result.upper()
