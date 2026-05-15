import webbrowser

def run(query):
    webbrowser.open(query)
    return f"Opened {query}"
