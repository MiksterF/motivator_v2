

import random
import json
import datetime
from pathlib import Path

# --- Quotes ---
QUOTES = [
    "You don’t have to be great to start, but you have to start to be great.",
    "Success is the sum of small efforts repeated day in and day out.",
    "Believe you can and you're halfway there.",
    "Don’t wait for opportunity. Create it.",
    "Dream big. Work hard. Stay humble."
]

# --- Daily goals ---
GOALS = [
    "Write down three things you're grateful for.",
    "Go for a 15-minute walk.",
    "Message a friend and check in.",
    "Read 10 pages of a book.",
    "Do 10 pushups or some light stretching."
]

DATA_FILE = Path("data.json")


def get_random_quote():
    return random.choice(QUOTES)


def get_random_goal():
    return random.choice(GOALS)


def save_achievement(achievement):
    today = str(datetime.date.today())
    data = {}

    if DATA_FILE.exists():
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = {}

    data[today] = achievement

    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    print("\n✅ Saved! Keep up the great work 💪")


def main():
    print("\n💬 Quote of the day:")
    print(f"\"{get_random_quote()}\"\n")

    print("🎯 Today's goal:")
    print(f"{get_random_goal()}\n")

    achievement = input("🏆 What did you achieve today?\n> ").strip()

    if achievement:
        save_achievement(achievement)
    else:
        print("\nNo achievement entered — that’s okay! Try again tomorrow 🌱")


if __name__ == "__main__":
    main()
