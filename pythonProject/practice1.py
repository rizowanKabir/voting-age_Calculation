check=""

while (check != 'sleep'):
    check = input(">").lower()

    if check == 'on':
        print("light turned on mode ")

    elif check == 'off':
        print("lighr turned off mode")
    elif check == 'sleep':
        break

    elif check == 'help':
        print('''
        1. on- light on
        2. off- light off
        3. sleep- exit program
        
        ''')
    else:
        print("i dont understand")
