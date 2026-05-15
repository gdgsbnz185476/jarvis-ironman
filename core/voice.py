import speech_recognition as sr
import os

r = sr.Recognizer()

r.energy_threshold = 300
r.dynamic_energy_threshold = True
r.pause_threshold = 0.6
r.phrase_threshold = 0.3
r.non_speaking_duration = 0.4

def listen():
    try:
        with sr.Microphone() as source:
            print("Listening...")

            r.adjust_for_ambient_noise(source, duration=0.3)

            audio = r.listen(
                source,
                timeout=5,
                phrase_time_limit=8
            )

        text = r.recognize_google(audio)

        return text.lower()

    except:
        return ""

def speak(text):
    print("Jarvis:", text)

    safe_text = text.replace('"', '').replace("'", "")

    os.system(f'say -v Daniel "{safe_text}"')