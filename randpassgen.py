#Ask user if they want to generate password
#If yes, ask for password lenght
#Generate password
#Print password
#If initial response is No, then exit program

import string
import random

characters=list(tring.ascii_letters + string.digits + "!@#$%^&*()")

def generate_password():
    password_lenght=int(input('How long would you like your password to be? '))

    random.shuffle(characters)

    password=[]

    for x in range(password_lenght):
        password.append(random.choice(characters))
    random.shuffle(password)

    password="".join(password)

    print(password)

option=input("Do you want to generate a password? (Yes/No")

if option == 'Yes':
    generate_password()
elif option == 'No':
    print('Program Ended')
    quit()
else:
    print('Invalid input, please input Yes or No')
    quit()
