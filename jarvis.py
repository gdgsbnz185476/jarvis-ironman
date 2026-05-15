from core.voice import listen, speak
from core.agent import handle
from core.memory import load, add
from core.wakeword import wait_for_wakeword

print("JARVIS v15 WAKEWORD ONLINE")

while True:

    wait_for_wakeword()

    speak("Yes sir.")

    user = listen()

    if not user:
        continue

    print("You:", user)

    if user in ["exit", "shutdown", "stop"]:
        speak("Shutting down sir.")
        break

    memory = load()

    reply = handle(user, memory)

    print("Jarvis:", reply)

    speak(reply)

    add({
        "user": user,
        "jarvis": reply
    })