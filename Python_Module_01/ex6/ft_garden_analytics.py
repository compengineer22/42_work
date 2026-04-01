class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = float(height)
        self.age = age
        self._stats = Plant.Stats()
        self.is_tree = 0

    def show(self) -> None:
        print(
             f"{self.name.capitalize()}: "
             f"{self.height:.1f}cm, {self.age} days old")
        self._stats.show_calls += 1

    def grow(self, increase: float) -> None:
        self.height += increase
        self._stats.grow_call += 1

    def age_c(self, days: int) -> None:
        self.age += days
        self._stats.age_calls += 1

    class Stats:
        def __init__(self):
            self.age_calls = 0
            self.grow_call = 0
            self.show_calls = 0
            self.produce_shade_calls = 0

        def display(self) -> None:
            print(f"Stats: {self.grow_call} grow,"
                  f"{self.age_calls} age, {self.show_calls} show")

    @classmethod
    def anonymous(cls):
        return cls("Unknown plant", 0, 0)

    @staticmethod
    def age_checker(age: int) -> None:
        if age < 365:
            print(f"Is {age} days more than a year? -> False")
        else:
            print(f"Is {age} days more than a year? -> True")


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


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age, color)
        self.seeds = 0

    def bloom(self):
        super().bloom()
        self.seeds = 42

    def show(self):
        super().show()
        print(f"Seeds: {self.seeds}")


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = float(trunk_diameter)
        self.produce_shade_calls = 0
        self.is_tree = 1

    def produce_shade(self) -> None:
        print(f"Tree {self.name.capitalize()} now produces a shade of"
              f" {self.height}cm long and {self.trunk_diameter}cm wide.")
        self._stats.produce_shade_calls += 1

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter}cm")


def dis_stats(plant: Plant):
    print(f"[statistics for {plant.name}]")
    plant._stats.display()

    if plant.is_tree == 1:
        print(f"{plant._stats.produce_shade_calls} shade")


if __name__ == "__main__":
    f = Flower("rose", 15, 10, "red")
    t = Tree("Oak", 200, 365, 5)
    s = Seed("Sunflower", 80, 45, "yellow")
    print("=== Garden statistics ===")
    Plant.age_checker(30)
    Plant.age_checker(400)

    print("\n=== Flower")
    f.show()
    dis_stats(f)
    print(f"[asking the {f.name} to grow and bloom]")
    f.grow(8)
    f.bloom()
    f.show()
    dis_stats(f)

    print("\n=== Tree")
    t.show()
    dis_stats(t)
    print(f"[asking the {t.name} to produce shade]")
    t.produce_shade()
    dis_stats(t)

    print("\n=== Seed")
    s.show()
    print(f"[make {s.name} grow, age and bloom]")
    s.grow(30)
    s.age_c(20)
    s.bloom()
    s.show()
    dis_stats(s)

    print("\n=== Anonymous")
    unknown = Plant.anonymous()
    unknown.show()
    dis_stats(unknown)
