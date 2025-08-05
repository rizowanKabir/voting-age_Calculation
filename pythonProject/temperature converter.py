unit = input("Enter the temperature in celsius or farenheit(C/F): ")
temp = float(input("Enter the temperature is : "))

if unit == "C":
    temp = round((temp * 9) / 5 +32,1)
    print(f"The temperature in fahrenheit is: {temp} F")

elif unit == "F":
    temp = round((temp - 32) * 5 / 9,1)
    print(f"The temperature in celsius is: {temp} C")

else:
    print(f"{unit} is an invalid measurement ")