class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name.capitalize()}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    plant1 = Plant("rose",25,30)
    plant2 = Plant("sunflower",80,45)
    plant3 = Plant("castus",15,120)

    plants = [plant1,plant2,plant3]

    for plant in plants:
        plant.show()
