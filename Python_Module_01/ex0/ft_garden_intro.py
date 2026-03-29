def display_plant_info(name: str, heigt: int, age: int) -> None:
    print("=== Welcom to My Garden ===")
    print(f"Plant: {name.capitalize()}")
    print(f"Height: {height}cm")
    print(f"Age: {age} days")
    print("\n=== End of Program ===")

if __name__ == "__main__":
    name = "blue"
    height = 25
    age = 30
    display_plant_info(name,height,age)