# Import required modules
from random import randint
from time import sleep as wait
done = 0

while done == 0:
    # Generate random number between 1 & 100
    answer=randint(1,100)
    print("Generated new number")
    correct = 0
    guess = 0
    again = "no"

    while correct == 0:
        guess = int(input("Please guess a number... \n"))
        if guess == answer:
            print("Spot on")
            again = input("Would you like to play again?")
            if again.lower() == "no":
                print("Ok, goodbye.")
                wait(2)
                exit()
        elif guess < answer:
            print("Too Low")
        elif guess > answer:
            print("Too High")