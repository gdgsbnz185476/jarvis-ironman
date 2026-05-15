from core.voice import listen
from core.agent import run_agent
import time

def boot():
    print("JARVIS OS MODE ACTIVE")

    while True:
        try:
            user = listen()

            if not user:
                continue

            if "shutdown" in user:
                print("Stopping Jarvis OS")
                break

            run_agent(user)

        except Exception as e:
            print("Recovered:", e)
            time.sleep(1)

if __name__ == "__main__":
    boot()
