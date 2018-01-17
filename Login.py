import uuid
import hashlib


def hash_password(password):
    # uuid is used to generate a random number
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt


def check_password(hashed_password, user_password):
    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()

choice = input('What would you like to do: \n \n 1: Sign up \n 2: Log in \n 3: I forgot my password! \n')
if choice == 1:
    usern = input('Please enter your username: ')
    password = input('Please enter a password: ')
    exec(usern + ' = hash_password(password)')
    print(usern)
    print(exec(usern))
elif choice == 2:
    old_pass = input('Now please enter the password again to check: ')
    if check_password(hashed_password, old_pass):
        print('You entered the right password')
    else:
        print('I am sorry but the password does not match')
elif choice == 3:
    print("That sounds like a you problem.")
