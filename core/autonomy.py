import time
from core.voice import listen
from core.agent import run_agent


WAKE_WORDS = [
    "jarvis",
    "hey jarvis",
    "ok jarvis",
    "yo jarvis"
]


class JarvisAutonomy:

    def __init__(self):
        self.running = True

    def start(self):
        print("🧠 Jarvis V25 Autonomy ONLINE")

        while self.running:
            try:
                text = listen()

                if not text:
                    continue

                text = text.lower().strip()
                print("Heard:", text)

                # shutdown command
                if "stop jarvis" in text or "shutdown jarvis" in text:
                    print("Shutting down autonomy...")
                    self.running = False
                    break

                # WAKE WORD DETECTION
                triggered = False
                command = text

                for word in WAKE_WORDS:
                    if word in text:
                        triggered = True
                        command = text.replace(word, "").strip()
                        break

                if triggered and command:
                    response = run_agent(command)
                    print("Jarvis:", response)

            except Exception as e:
                print("Autonomy error:", e)

            time.sleep(0.2)


def start_autonomy():
    JarvisAutonomy().start()