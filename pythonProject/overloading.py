import random
target = random.randint(1,100)

while True:
    user_choice =input("Guess the target or quit(Q): ")
    if(user_choice == "Q"):
        break
    user_choice = int(user_choice)
    if(user_choice == target):
        print("Successfully you have done a great job !!!")
        break
    elif(user_choice < target):
        print("your number was too small. Take bigger choice....")
    else:
        print("your number was too big. Take smaller choice....")
print(".........Game over......!!!!")
