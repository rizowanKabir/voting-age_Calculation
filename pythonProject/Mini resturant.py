
menu={
    'pizza':40,
    'Burger':50,
    'Pasta':30,
    'Clod coffe':20,
    'Salad':100,
    }
#Greetings

print("Welcome to Our resturant MYlove")
print("pizzza:40\nBurger:50\nPasta:30\nClod coffe:20\nSalad:100")
order_total= 0
item_1=input("Enter the name of item you want to oder=")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"your item{item_1}has been added to your order")
else:
    print(f"odered item {item_1} is not available yet")
another_item=input("Do you want another item to add?(yes/no)")
if another_item =="yes":
    item_2=input("Enter the name of second item to add=")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"item {item_2}has been added to your order")
    else:
        print(f"oder item{item_2} is not available yet")
print(f"The total amount of item to pay {order_total}")

