from core.voice import listen, speak
from core.agent import run_agent

def main():
    speak("Jarvis online")

    while True:
        user = listen()

        if not user:
            continue

        print("You:", user)

        if "exit" in user or "shutdown" in user:
            speak("Shutting down sir.")
            break

        reply = run_agent(user)

        print("Jarvis:", reply)

if __name__ == "__main__":
    main()
