import os

def run(command):
    if "open youtube" in command:
        os.system("open https://youtube.com")
        return "Opening YouTube"

    return "Command not allowed"
