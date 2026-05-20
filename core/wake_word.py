import speech_recognition as sr
from core.agent import run_agent

WAKE_WORD = "jarvis"

r = sr.Recognizer()
r.dynamic_energy_threshold = True


def listen_wake_word():
    with sr.Microphone() as source:
        print("🎙️ Listening for wake word...")
        r.adjust_for_ambient_noise(source)

        while True:
            try:
                audio = r.listen(source, timeout=None)
                text = r.recognize_google(audio).lower()

                print("Heard:", text)

                if WAKE_WORD in text:
                    command = text.replace(WAKE_WORD, "").strip()

                    if command:
                        response = run_agent(command)
                        print("Jarvis:", response)

            except Exception as e:
                print("Wake error:", e)
