

pass_word = "sohag@123"

tries = 4
while tries > 0:
    user_input = input("Enter your password here: ")
    if user_input == pass_word:
        print("Access ready for login !!!!")
        break
    else:
        tries -= 1
        print(f"wrong password you cant login ....tries left {tries}")
    if tries == 0:
        print("Access denied")
