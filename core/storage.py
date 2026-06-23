import json
import os

FILE = "password_manager/data/passwords.json"

def load_passwords():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        return json.load(f)

def save_passwords(passwords):
    os.makedirs("data", exist_ok=True)

    with open(FILE, "w") as f:
        json.dump(passwords, f, indent=4)