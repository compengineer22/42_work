def input_temperature(temp_str: str) -> int:
    if int(temp_str) < 0:
        raise Exception(f"{temp_str}°C is too cold for plants (min 0°C)")
    if int(temp_str) > 40:
        raise Exception(f"{temp_str}°C is too hot for plants (max 40°C)")
    return int(temp_str)


def test_temperature(tem: str) -> None:
    print(f"\nInput data is '{tem}'")
    try:
        temp = input_temperature(tem)
        print(f"Temperature is now {temp}°C")
    except Exception as e:
        print(f"Caught input_temperature error: {e}")


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===")
    test_temperature("25")
    test_temperature("abc")
    test_temperature("100")
    test_temperature("-50")
    print("\nAll tests completed - program didn't crash!")
