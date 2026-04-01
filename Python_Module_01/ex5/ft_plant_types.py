class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = float(height)
        self.age = age

    def show(self) -> None:
        print(
             f"{self.name.capitalize()}: "
             f"{self.height:.1f}cm, {self.age} days old")

    def grow(self, increase: float) -> None:
        self.height += increase

    def age_c(self, increase: int) -> None:
        self.age += increase


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.is_blooming = False

    def bloom(self) -> None:
        self.is_blooming = True

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if self.is_blooming:
            print(f" {self.name.capitalize()} is blooming beautifylly!")
        else:
            print(f" {self.name.capitalize()} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = float(trunk_diameter)

    def produce_shade(self) -> None:
        print(f"Tree {self.name.capitalize()} now produces a shade of"
              f" {self.height}cm long and {self.trunk_diameter}cm wide.")

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(self, name: str, height: float,
                 age: int, harvest_season: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.harvest_season.capitalize()}")
        print(f" Nutritional value: {self.nutritional_value}")

    def grow(self, amount: float) -> None:
        super().grow(amount)

    def age_c(self, days: int) -> None:
        super().age_c(days)
        self.nutritional_value += days


if __name__ == "__main__":
    f = Flower("rose", 15, 10, "red")
    t = Tree("Oak", 200, 365, 5)
    v = Vegetable("tomato", 5, 10, "april")

    print("=== Garden Plant Types ===")
    print("=== Flower")
    f.show()
    print(f"[asking the {f.name} to bloom]")
    f.bloom()
    f.show()
    print("\n=== Tree")
    t.show()
    print(f"[asking the {t.name} to produce shade]")
    t.produce_shade()
    print("\n=== Vegetable")
    v.show()
    v.grow(42)
    v.age_c(20)
    print(f"[make the {v.name} grow and age for {v.nutritional_value} days]")
    v.show()
