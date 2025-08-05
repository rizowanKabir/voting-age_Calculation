import random
import string
pass_len = 12
charval = string.ascii_letters+string.digits+string.punctuation

password = ""
for i in range(pass_len):
    password += random.choice(charval)
print("your random password is :",password)