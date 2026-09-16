import json
import os

FILE_NAME = "quotes.json"

def save_quote(record):
    history = load_all_quotes()
    history.append(record)
    with open(FILE_NAME, "w") as f:
        json.dump(history, f, indent=4)

def load_all_quotes():
    if not os.path.exists(FILE_NAME):
        return []
    try:
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    except (IOError, json.JSONDecodeError):
        return []