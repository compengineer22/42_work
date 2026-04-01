def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature(tem: str) -> None:
    print(f"\nInput data is '{tem}'")
    try:
        temp = input_temperature(tem)
        print(f"Temperature is now {temp}°C")
    except Exception as e:
        print(f"Caught input_temperature error: {e}")


if __name__ == "__main__":
    print("=== Garden Temperature ===")
    test_temperature("25")
    test_temperature("abc")
    print("\nAll tests completed - program didn't crash!")
