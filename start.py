from core.voice import listen, speak
from core.agent import run_agent

def main():
    speak("Jarvis stable system online")

    while True:
        try:
            user = listen()

            if not user:
                continue

            print("You:", user)

            if user in ["exit", "quit", "shutdown"]:
                speak("Shutting down sir.")
                break

            reply = run_agent(user)

            print("Jarvis:", reply)
            speak(reply)

        except Exception as e:
            print("System error:", e)
            speak("I encountered an error but recovered")

if __name__ == "__main__":
    main()
