import os
os.system('cls')

#Ask for password lenght
#Generate password

import string
import secrets

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
numbers = string.digits
special = string.punctuation

caracteres = lowercase + uppercase + numbers + special

def generate_password():
    size=int(input('How long would you like your password to be? '))

    password = ''

    for i in range(size):
        password += ''.join(secrets.choice(caracteres))

    print(password)

generate_password()




