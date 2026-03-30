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
        self.height += increase

    def age_c(self, increase: int) -> None:
        self.age += increase


if __name__ == "__main__":
    print("=== Plant Factory Output ===")

    Rose = Plant("rose", 25, 30)
    Oak = Plant("Oak", 200, 365)
    Cactus = Plant("Cactus", 5, 90)
    Sunflower = Plant("Sunflower", 80, 45)
    Fern = Plant("Fern", 15, 120)

    plants = [Rose, Oak, Cactus, Sunflower, Fern]
    for plant in plants:
        print("Created: ",end="")
        plant.show()
