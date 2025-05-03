def load_key(path):
    try:
        with open(path, "rb") as f:
            return f.read().strip()
    except FileNotFoundError:
        return b""
