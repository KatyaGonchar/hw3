# JSON

import json

def create_json(filename, data):
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
