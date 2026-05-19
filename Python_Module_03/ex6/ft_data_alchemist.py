import random


names = [
    "Alice", "bob", "Charlie", "dylan", "Emma",
    "Gregory", "john", "kevin", "Liam"
    ]
capitalized_players = [name.capitalize() for name in names]
capitalized_only = [name for name in names if name[0].isupper()]
scores = {name: random.randint(0, 1000) for name in capitalized_players}
av = round(sum(scores.values()) / len(scores), 2)
high_scores = {name: score for name, score in scores.items() if score > av}


if __name__ == "__main__":
    print("=== Game Data Alchemist ===\n")
    print(f"Initial list of players: {names}")
    print(f"New list with all names capitalized: {capitalized_players}")
    print(f"New list of capitalized names only: {capitalized_only}\n")
    print(f"Score dict: {scores}")
    print(f"Score average is {av}")
    print(f"High scores: {high_scores}")
