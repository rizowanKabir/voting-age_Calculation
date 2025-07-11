print("write your phone number:")
number= input()

if len(number)>11:
    print("your number is too long")
elif len(number)<11:
    print("your number is too short")
elif len(number)==11:
    print("Thank you",number)