import sys

if __name__ == "__main__":
    if (len(sys.argv) != 2):
        print("Usage: ft_ancient_text.py <file>\n")
        sys.exit(1)
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{sys.argv[1]}'")
    try:
        opened_file = open(sys.argv[1], "r")
        print("---\n")
        content = opened_file.read()
        print(f"{content}")
        print("\n---")
        opened_file.close()
        print(f"File '{sys.argv[1]}' closed.\n")
        print("Transform data:\n---\n")
        for line in content.splitlines():
            print(f"{line}#")
        print("\n---")
        new_file_name = input("Enter new file name (or empty): ")
        if (new_file_name):
            new = open(new_file_name, "w")
            for line in content.splitlines():
                new.write(f"{line}#\n")
            new.close()
            print(f"Saving data to '{new_file_name}'")
            print(f"Data saved in file '{new_file_name}'")
        else:
            print("No saving data.")
    except Exception as e:
        print(f"Error opening file '{sys.argv[1]}': {e}\n")
