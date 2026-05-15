import speech_recognition as sr
import os

r = sr.Recognizer()
r.dynamic_energy_threshold = True
r.pause_threshold = 0.6

def listen():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            r.adjust_for_ambient_noise(source, duration=0.3)
            audio = r.listen(source, timeout=6)

        return r.recognize_google(audio).lower()

    except:
        return ""

def speak(text):
    print("Jarvis:", text)
    os.system(f'say -v Daniel "{text}"')