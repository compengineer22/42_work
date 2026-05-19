import sys

if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    inventory: dict[str, int] = {}
    for i in range(1, len(sys.argv)):
        param = sys.argv[i]
        splited = param.split(":")
        if len(splited) != 2:
            print(f"Error - invalid parameter '{param}'")
            continue
        name = splited[0]
        quantity = splited[1]
        if name in inventory:
            print(f"Redundant item '{name}' - discarding")
            continue
        try:
            qty = int(quantity)
        except ValueError:
            print(f"Quantity error for '{name}':"
                  " invalid literal for int() with base 10: '{quantity}'")
            continue
        inventory[name] = qty

    print(f"Got inventory: {inventory}")

    item_list = list(inventory.keys())

    print(f"Item list: {item_list}")

    total_quantity = sum(inventory.values())

    print(
        f"Total quantity of the {len(inventory)} items: "
        f"{total_quantity}"
    )

    for item in inventory:
        percentage = (inventory[item] / total_quantity) * 100

        print(
            f"Item {item} represents "
            f"{round(percentage, 1)}%"
        )

    most_item = ""
    most_qty = -1

    for item in inventory:
        if inventory[item] > most_qty:
            most_qty = inventory[item]
            most_item = item

    least_item = ""
    least_qty = -1
    first = True

    for item in inventory:
        if first:
            least_qty = inventory[item]
            least_item = item
            first = False
        elif inventory[item] < least_qty:
            least_qty = inventory[item]
            least_item = item

    print(
        f"Item most abundant: "
        f"{most_item} with quantity {most_qty}"
    )

    print(
        f"Item least abundant: "
        f"{least_item} with quantity {least_qty}"
    )

    inventory.update({"magic_item": 1})

    print(f"Updated inventory: {inventory}")
