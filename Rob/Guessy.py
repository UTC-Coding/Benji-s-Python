from random import randint as num
correct = 0
attempts = 0

def generate():
    num1 = num(1,1000)
    num2 = num(1,1000)
    yup = num1 + num2
    return yup

while correct == 0 and attempts < 5:
    guess = input("Guess the number!")
    yup = generate()
    attempts = attempts + 1
    if guess == yup:
        print("Correct!")
        correct = 1
    else:
        attempted = str(attempts)
        print("Nope! Attempts: " + attempted)
        correct = 0
        yup = generate()

yup = str(yup)
if correct == 0:
    print("You loose! Number was: " + yup)
elif correct == 1:
    print("Congrats! Number was: " + yup)
else:
    print("Damn it!")