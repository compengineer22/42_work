from typing import Generator
import random


def gen_event() -> Generator[tuple[str, str], None, None]:
    players = ["Alice", "Bob", "Charlie", "Dylan"]
    actions = [
        "runs",
        "eat",
        "sleep",
        "grab",
        "move",
        "climbe",
        "swim",
        "use",
        "release"
        ]
    while True:
        name = random.choice(players)
        action = random.choice(actions)
        yield (name, action)


def consume_event(
        events: list[tuple[str, str]]
        ) -> Generator[tuple[str, str], None, None]:
    while len(events) > 0:
        index = random.randrange(len(events))
        event = events.pop(index)
        yield event


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    event_gen = gen_event()
    for i in range(1000):
        event = next(event_gen)
        print(f"Event {i}: "
              f"Player {event[0]} did action {event[1]}")
    my_list = list()
    for i in range(10):
        my_list.append(next(event_gen))
    print(f"Built list of 10 events: {my_list}")

    for event in consume_event(my_list):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {my_list} ")
