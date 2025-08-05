numbers={
    '0':'Zero',
    '1':'one',
    '2':'two',
    '3':'three',
    '4':'four',
    '5':'five',
    '6':'six',
    '7':'seven',
    '8':'eight',
    '9':'nine'
}
user_num=input(">")
for i in user_num:
    print(numbers.get(i,"(!)"),end="")
