import json
from datetime import date

FILE = "data.json"


def load_data():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return []


def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)


def add_entry(energy, mood, sleep, notes=""):
    data = load_data()
    today = date.today().isoformat()

    new_entry = {
        "date": today,
        "energy": energy,
        "mood": mood,
        "sleep": sleep,
        "notes": notes
    }

    for i, entry in enumerate(data):
        if entry["date"] == today:
            print("🔄 Actualizando registro del día...")
            data[i] = new_entry
            save_data(data)
            return

    data.append(new_entry)
    save_data(data)


def get_last_days(n=7):
    data = load_data()
    return data[-n:]

def get_last_entry():
    data = load_data()

    if not data:
        return None

    return data[-1]