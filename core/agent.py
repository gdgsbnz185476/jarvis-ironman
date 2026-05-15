from core.brain import ask_ai
from core.memory import save_memory

def run_agent(user_input):

    try:
        prompt = f"You are Jarvis. Respond clearly: {user_input}"

        response = ask_ai(prompt)

        save_memory(f"User: {user_input} | Jarvis: {response}")

        return response

    except Exception as e:
        return f"Agent error: {str(e)}"