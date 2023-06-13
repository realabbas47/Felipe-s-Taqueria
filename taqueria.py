MENU = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def place_order():
    total_cost = 0.0
    print("Welcome to Felipe's Taqueria!")
    print("Please enter the items you would like to order (one per line). Press Ctrl+D (Ctrl+Z on Windows) to finish.")

    try:
        while True:
            item = input().strip().title()

            if item == "":
                continue

            if item in MENU:
                total_cost += MENU[item]
                print(f"Total cost: ${total_cost:.2f}")
            else:
                print("Invalid item. Please try again.")

    except EOFError:
        pass

    print("\nThank you for your order!")
    print(f"Total cost: ${total_cost:.2f}")


if __name__ == "__main__":
    place_order()
