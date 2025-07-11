secret_number=6
guess_count=1
guess_limit=3

while guess_count<= guess_limit:


      user_guess_number=int(input("guess>"))
      guess_count += 1
if user_guess_number ==secret_number:
    print("you will be win !!")



else:
    print("you will be lose")
