from core.voice import listen
from core.agent import run_agent

def start_daemon():

    print("V21 AUTONOMOUS MODE ACTIVE")

    while True:
        user = listen()

        if not user:
            continue

        if "exit" in user:
            break

        run_agent(user)