# core/wakeword.py
import speech_recognition as sr

def listen_for_wakeword():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        while True:
            audio = r.listen(source, phrase_time_limit=3)
            try:
                text = r.recognize_google(audio).lower()
                if "jarvis" in text:
                    return True
            except:
                pass