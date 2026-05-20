import time
from core.voice import listen
from core.orchestrator import run_pipeline

class AutonomyEngine:

    def __init__(self):
        self.running = True
        self.task_queue = []

    def start(self):
        print("🧠 V28 AUTONOMY ENGINE ONLINE")

        while self.running:
            try:
                text = listen()

                if not text:
                    continue

                text = text.lower().strip()
                print("Heard:", text)

                # STOP
                if "stop jarvis" in text:
                    self.running = False
                    break

                # AUTONOMOUS TASK MODE
                if "jarvis" in text:
                    command = text.replace("jarvis", "").strip()
                    if command:
                        result = run_pipeline(command)
                        print("JARVIS:", result)

                # AUTO MODE (no wake word needed)
                elif "auto" in text:
                    task = text.replace("auto", "").strip()
                    if task:
                        result = run_pipeline(task)
                        print("AUTO EXEC:", result)

            except Exception as e:
                print("Autonomy error:", e)

            time.sleep(0.2)


def start_autonomy():
    AutonomyEngine().start()
