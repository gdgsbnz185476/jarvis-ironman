import os

def open_app(app_name):
    try:
        os.system(f"open -a '{app_name}'")
        return f"Opened {app_name}"
    except Exception as e:
        return str(e)
