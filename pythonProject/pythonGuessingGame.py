#Gusseing Game

import random

low_number = 1
high_number = 100

answer = random.randint(low_number,high_number)
guesses = 0
is_running = True
print("Welcome to python Guessing Game")
print("       .......          ")
print(f"Select a number between {low_number} and {high_number}.")
while is_running:
    guess = input("Enter your Guess : ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < low_number or guess > high_number:
            print("This number is out of range ")
            print(f"Select a number between {low_number} and {high_number}")
        elif guess > answer:
            print("Your number is too High.Try again !!!")
        elif guess < answer:
            print("Your number is too low.Try agin !!!")
        else:
            print(f"Correct answer was {answer}")
            print(f"The number of guesses {guesses}:")
    else:
        print("Invalid guess ")
        print(f"Select a number between {low_number} and {high_number}")



