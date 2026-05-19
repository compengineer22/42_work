import math


def get_player_pos() -> tuple:
    while True:
        arg = input("Enter new coordinates as floats in format 'x,y,z': ")
        arguments = arg.split(',')
        if (len(arguments) != 3):
            print("Invalid syntax")
            continue
        try:
            x = float(arguments[0])
            y = float(arguments[1])
            z = float(arguments[2])
            return (x, y, z)
        except ValueError as e:
            for v in arguments:
                try:
                    float(v)
                except ValueError:
                    print(f"Error on parameter '{v}': {e}")
                    break


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")
    c1 = get_player_pos()
    print(f"Got a first tuple: {c1}")
    print(f"It includes: X={c1[0]}, Y={c1[1]}, Z={c1[2]}")
    d = math.sqrt(c1[0]**2 + c1[1]**2 + c1[2]**2)
    print(f"Distance to center: {round(d,2)}\n")
    print("Get a second set of coordinates")
    c2 = get_player_pos()
    d2 = math.sqrt((c1[0] - c2[0])**2 +
                   (c1[1] - c2[1])**2 + (c1[2] - c2[2])**2)
    print(f"Distance between the 2 sets of coordinates: {round(d2,2)}")
