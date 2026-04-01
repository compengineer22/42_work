def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        2/0
    elif operation_number == 2:
        open("Does/not/exist")
    elif operation_number == 3:
        "hi" + 3
    else:
        return

def test_error_typres() -> None:
    print("=== Garden Error Types Demo ===")
    for i in range(1,5):
        try:
            print(f"Testing operation {i}...")
            garden_operations(i)
            print("\nOperation completed successfully")
        except ValueError as e:
            print(f"Caught ValueError: {e}")
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}")
        except TypeError as e:
            print(f"Caught TypeError: {e}")



#     # Demonstrate catching multiple errors in one block
#     print("\n=== Multiple Error Catch Demo ===")
#     try:
#         garden_operations(0)  # ValueError
#         garden_operations(1)  # (won’t run if first fails)
#     except (ValueError, ZeroDivisionError) as e:
#         print(f"Caught multiple error types: {e}")

#     print("All error types tested successfully!")


# if __name__ == "__main__":
#     test_error_types()
if __name__ == "__main__":
    test_error_typres()