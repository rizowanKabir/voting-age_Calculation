# Shopping Card Program
foods = []
prices = []
total = 0

while True:
    food = input("Enter your food you want to buy(Q to quit): ")
    if food == "Q":
        break
    else:
        price = float(input(f"Enter the price of ({food}): "))
        foods.append(food)
        prices.append(price)
print(".......YOUR CARD.........")
for food in foods:
    print(food,end=" ")
for price in prices:
    total += price
print()
print(f"Your total is: {total}:")


