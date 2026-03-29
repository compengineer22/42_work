class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(
            f"{self.name.capitalize()}: "
            f"{self.height:.1f}cm, {self.age} days old")

    def grow(self, increase: float) -> None:
        self.height += round(increase)

    def age_c(self, increase: int) -> None:
        self.age += increase


if __name__ == "__main__":
    print("=== Garden Plant Growth ===")

    g_increase = 0.8
    a_increase = 1
    plant = Plant("red", 25, 30)
    initial_height = plant.height

    growth = 0
    print(f"=== Day {1} ===")
    plant.show()
    for i in range(2, 8):
        print(f"=== Day {i} ===")
        plant.grow(g_increase)
        plant.age_c(a_increase)
        plant.show()

    growth = round(plant.height - initial_height)
    print(f"Growth this week: {growth:.1f}cm")
