import sys


if __name__ == "__main__":
    if (len(sys.argv) != 2):
        print("Usage: ft_ancient_text.py <file>\n")
        sys.exit(1)
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{sys.argv[1]}'")
    try:
        opened_file = open(sys.argv[1], "r")
        print("---\n")
        content = opened_file.read()
        print(f"{content}")
        print("\n---")
        opened_file.close()
        print(f"File '{sys.argv[1]}' closed.")
    except Exception as e:
        print(f"Error opening file '{sys.argv[1]}': {e}\n")
