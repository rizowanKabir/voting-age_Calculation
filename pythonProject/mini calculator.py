first=input("Enter  the first number:")
operator=input("Enter the operators (+,-,*,/): ")
second=input("Enter the second number:")

first=int(first)
second=int(second)

if operator=="+":
    print(first+second)
elif operator=="-":
    print(first-second)
elif operator=="*":
    print(first*second)
elif operator=="/":
    print(first/second)
elif operator=="%":
    print(first%second)

else:
    print("operator invalided")

