import uuid
import hashlib
import os


def hash_password(password):
    # uuid is used to generate a random number
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt


def check_password(hashed_password, user_password):
    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()

while 1==1:
    mchoice = input('What would you like to do: \n \n 1: Sign up \n 2: Log in \n 3: I forgot my password! \n')

    if mchoice == "1":
        usern = input('Please enter your username: ')
        password = input('Please enter a password: ')
        exec(usern + ' = hash_password(password)')
        os.system('cls')
    elif mchoice == "2":
        check_u = input('Username: ')
        check_p = input('Password: ')
        if check_password(eval(check_u), check_p):
            print('You entered the right password')
            input('Press enter to continue...')
        else:
            print('I am sorry but the password does not match')
            input('Press enter to continue...')
    elif mchoice == "3":
        print("That sounds like a you problem.")
        input('Press enter to continue...')
