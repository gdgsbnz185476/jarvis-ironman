from core.voice import listen
from core.agent import run_agent
import time

def start_daemon():
    print("JARVIS GOD MODE ACTIVE")

    while True:
        try:
            user = listen()

            if not user:
                continue

            if "exit" in user or "shutdown" in user:
                print("Shutting down...")
                break

            run_agent(user)

        except Exception as e:
            print("Recovered from error:", e)
            time.sleep(1)