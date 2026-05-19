import random


ALL_ACHIEVEMENTS = {
        "Crafting Genius",
        "World Savior",
        "Master Explorer",
        "Collector Supreme",
        "Untouchable",
        "Boss Slayer",
        "Strategist",
        "Unstoppable",
        "Speed Runner",
        "Survivor",
        "Treasure Hunter",
        "First Steps",
        "Sharp Mind",
        "Hidden Path Finder"
    }


def gen_player_achievements() -> set:

    all_achievements_list = list(ALL_ACHIEVEMENTS)
    player_set: set[str] = set()
    amount = random.randint(3, len(all_achievements_list))
    while len(player_set) < amount:
        player_set.add(random.choice(all_achievements_list))
    return (player_set)


if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")
    Alice = gen_player_achievements()
    Bob = gen_player_achievements()
    Charlie = gen_player_achievements()
    Dylan = gen_player_achievements()
    all_unique = (Alice.union(Bob).union(Dylan)
                       .union(Charlie))
    all_common = (Alice
                  .intersection(Bob)
                  .intersection(Dylan)
                  .intersection(Charlie))
    print(f"Player Alice: {Alice}")
    print(f"Player Bob: {Bob}")
    print(f"Player Charlie: {Charlie}")
    print(f"Player Dylan: {Dylan}")
    Alice_only = Alice.difference(Bob.union(Dylan).union(Charlie))
    Bob_only = Bob.difference(Alice.union(Dylan).union(Charlie))
    Charlie_only = Charlie.difference(Bob.union(Dylan).union(Alice))
    Dylan_only = Dylan.difference(Bob.union(Alice).union(Charlie))
    print(f"\nAll distinct achievements: {all_unique}\n")
    print(f"Common achievements: {all_common}\n")
    print(f"Only Alice has: {Alice_only}")
    print(f"Only Bob has: {Bob_only}")
    print(f"Only Charlie has: {Charlie_only}")
    print(f"Only Dylan has: {Dylan_only}\n")
    print(f"Alice is missing: {all_unique.difference(Alice)}")
    print(f"Bob is missing: {all_unique.difference(Bob)}")
    print(f"Charlie is missing: {all_unique.difference(Charlie)}")
    print(f"Dylan is missing: {all_unique.difference(Dylan)}")
