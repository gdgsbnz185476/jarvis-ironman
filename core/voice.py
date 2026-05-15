import speech_recognition as sr
import os

recognizer = sr.Recognizer()
recognizer.energy_threshold = 300
recognizer.dynamic_energy_threshold = True
recognizer.pause_threshold = 0.6

def listen():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = recognizer.listen(source, timeout=5)

        text = recognizer.recognize_google(audio)
        return text.lower()

    except:
        return ""
    

def speak(text):
    print("Jarvis:", text)
    os.system(f'say -v Daniel "{text}"')