import sys


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: ft_stream_management.py <file>")
        sys.exit(1)

    filename = sys.argv[1]

    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{filename}'")

    try:
        opened_file = open(filename, "r")

        print("---")

        content = opened_file.read()
        print(content, end="")

        print("---")

        opened_file.close()
        print(f"File '{filename}' closed.")

    except Exception as e:
        print(f"[STDERR] Error opening file '{filename}': {e}",
              file=sys.stderr)
        sys.exit(1)

    print("Transform data:")
    print("---")

    transformed_lines = []

    try:
        opened_file = open(filename, "r")

        for line in opened_file:
            transformed = line.strip() + "#"
            transformed_lines.append(transformed)
            print(transformed)

        print("---")

        opened_file.close()

    except Exception as e:
        print(f"[STDERR] Error reading file '{filename}': {e}",
              file=sys.stderr)
        sys.exit(1)

    sys.stdout.write("Enter new file name (or empty): ")
    sys.stdout.flush()

    new_filename = sys.stdin.readline().strip()

    if new_filename == "":
        sys.exit(0)

    print(f"Saving data to '{new_filename}'")

    try:
        new_file = open(new_filename, "w")

        for line in transformed_lines:
            new_file.write(line + "\n")

        new_file.close()

    except Exception as e:
        print(f"[STDERR] Error opening file '{new_filename}': {e}",
              file=sys.stderr)
        print("Data not saved")
