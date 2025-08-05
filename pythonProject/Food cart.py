print("...........WELCOME TO THE RESTURANT...........")
print()
menu = {
    "pizza": 450.0,
    "burger": 250.0,
    "popcorn": 20.0,
    "French fries": 100.0,
    "cold coffee": 120.0,
    "lemon soda": 20.0,
    "Fried Chicken": 100,
    "Nachos": 150,
    "Naga Wings": 100,
    "Tea": 20,
}

cart = []
total = 0

print(".........MENU..............")
for key, value in menu.items():
    print(f"{key.title():12}: BDT {value:.2f}")
print(".............................")

while True:
    food = input("Select an item you like most (q to quit): ").lower().strip()
    if food == "q":
        break
    elif food in menu:
        cart.append(food)
        print(f"✅ {food.title()} added to your cart.")
    else:
        print("Item not found in menu. Please select a valid item.")

print("\n...........YOUR ORDER.........")
if cart:
    for food in cart:
        total += menu[food]
        print(f"- {food.title()}")
    print(f"\nTotal: BDT {total:.2f}")
else:
    print("You didn't order anything.")
