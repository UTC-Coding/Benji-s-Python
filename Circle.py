# Imports required modules
import turtle
from random import randint

# Initializes the Turtle
wn = turtle.Screen()
bob = turtle.Turtle()

#Generates a random number
num = randint(0,20)

# Display the number
print("Your number is: ", num)

while 1==1:
    bob.forward(2)
    bob.left(num)

