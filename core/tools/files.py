def create_file(path, content=""):
    try:
        with open(path, "w") as f:
            f.write(content)
        return f"File created at {path}"
    except Exception as e:
        return str(e)
