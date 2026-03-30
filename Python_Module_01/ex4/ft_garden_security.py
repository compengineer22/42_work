class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        if height < 0:
            print(f"{self.name} : Error, height can't be negative")
            print("Height update rejected")
            self._height = 0.0
        else:
            self._height = height
        if age < 0:
            print(f"{self.name} : Error, age can't be negative")
            print("Age update rejected")
            self._age = 0
        else:
            self._age = age

    def show(self) -> None:
        print(
             f"{self.name.capitalize()}: "
             f"{self._height:.1f}cm, {self._age} days old")

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self.name.capitalize()} :"
                  f" Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = height
            print(f"Height updated: {height}cm")

    def set_age(self, age:  int) -> None:
        if age < 0:
            print(f"{self.name.capitalize()} : Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = age
            print(f"Age updated: {age} days")

    def get_age(self) -> int:
        return self._age

    def get_height(self) -> float:
        return self._height


if __name__ == "__main__":
    print("=== Garden Security System ===")

    rose = Plant("rose", 15, 10)

    print("Plant Created: ", end="")
    rose.show()
    print("")

    rose.set_height(25)
    rose.set_age(30)
    print("")

    rose.set_height(-10)
    rose.set_age(-30)
    print("")

    print("Current state: ", end="")
    rose.show()
