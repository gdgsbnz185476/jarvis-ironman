from core.wakeword import listen_for_wakeword
from core.daemon import start_daemon
from core.voice import speak

print("JARVIS V20 GOD MODE READY")

while True:
    if listen_for_wakeword():
        speak("Yes sir. God mode activated.")
        start_daemon()