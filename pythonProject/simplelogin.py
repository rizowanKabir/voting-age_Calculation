user_name="rizowan"
pass_word="12345"
tries= 2
while tries > 0:
    user=input("Enter username:")
    passw=int(input("Enter pass: "))
    if(user== user_name and passw== pass_word):
        print("login successfully ")
        break
    else:
        tries -=1
        print("wrong attempt")
