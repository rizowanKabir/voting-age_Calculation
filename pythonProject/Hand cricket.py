import random as rd

score=0

while True:
    player_1 = int(input("player 1: "))
    player_2 = rd.randint(1, 7)

    if player_1 > 7 or player_1 < 1:
        print("Please, enter a valid value (1-7)")
        continue
    else:
        if player_1 != player_2:
            score += player_1
            print(f"player 2: {player_2}")
        else:
            print(player_2)
            print("OUT!!!!!!!!!!!")
            break

print(f"Your score is: {score}")
