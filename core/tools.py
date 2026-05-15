import os
import webbrowser
import subprocess


def sleep(seconds):
    import time
    time.sleep(seconds)
    return f"Slept for {seconds} seconds"


def open_app(app_name):
    try:
        subprocess.Popen(["open", "-a", app_name])
        return f"Opened {app_name}"
    except:
        return f"Failed to open {app_name}"


def open_website(url):
    webbrowser.open(url)
    return f"Opened {url}"


def create_file(path, content=""):
    with open(path, "w") as f:
        f.write(content)
    return f"File created at {path}"


def run_terminal_command(cmd):
    try:
        result = os.popen(cmd).read()
        return result if result else "Command executed"
    except Exception as e:
        return str(e)
