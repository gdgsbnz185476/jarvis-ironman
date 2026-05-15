import traceback

def safe_run(func, *args):
    try:
        return func(*args)
    except Exception as e:
        print("Self-healing triggered:", e)
        traceback.print_exc()
        return "Recovered from error"
