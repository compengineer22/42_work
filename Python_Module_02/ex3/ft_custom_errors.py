class GardenError(Exception):
    def __init__(self, message="Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message="Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message="Unknown plant error") -> None:
        super().__init__(message)


def Check_plant(plant_name: str) -> None:
    if plant_name == "tomato":
        raise PlantError(f"The {plant_name} plant is wilting!")


def Check_water(water_level: int) -> None:
    if water_level < 30:
        raise WaterError("Not enough water in the tank!")


def test_specific_errors():
    print("Testing PlantError...")
    try:
        Check_plant("tomato")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    print("\nTesting WaterError...")
    try:
        Check_water(4)
    except WaterError as e:
        print(f"Caught WaterError: {e}")


def test_general_errors():
    print("\nTesting catching all garden errors...")
    try:
        Check_plant("tomato")
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    try:
        Check_water(4)
    except GardenError as e:
        print(f"Caught GardenError: {e}")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===\n")
    test_specific_errors()
    test_general_errors()
    print("\nAll custom error types work correctly!")
