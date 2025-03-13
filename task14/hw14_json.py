# JSON

import json

filename = "football_clubs.json"

def create_json():
    data = [
        {"name": "Bayern Munich", "country": "Germany", "wins": 80},
        {"name": "Borussia Dortmund", "country": "Germany", "wins": 60},
        {"name": "Real Madrid", "country": "Spain", "wins": 90},
        {"name": "FC Barcelona", "country": "Spain", "wins": 75},
        {"name": "Paris Saint-Germain", "country": "France", "wins": 65},
        {"name": "Olympique Marseille", "country": "France", "wins": 55},
    ]

    try:
        with open(filename, "w") as file:
            json.dump(data, file)
            print(f"JSON file '{filename}' was created.")
    except Exception as e:
        print(f"Error: {e}")


def find_most_winning_club():
    try:
        with open(filename, "r") as file:
            clubs = json.load(file)

        max_wins = max(club["wins"] for club in clubs)
        max_wins_club = next(club for club in clubs if club["wins"] == max_wins)

        print(f"Most winning club: {max_wins_club['name']}")
        print(f"Country: {max_wins_club['country']}")
        print(f"Wins: {max_wins_club['wins']}")

    except Exception as e:
        print(f"Error: {e}")


create_json()
find_most_winning_club()
