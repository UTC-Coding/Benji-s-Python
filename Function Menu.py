import turtle
import random

# Initializes the Turtle
wn = turtle.Screen()
bob = turtle.Turtle()

# Initializes colours
colours = ["blue","black","brown","red","yellow","green","orange","beige","turquoise","pink"]

def circle():
    for count in range(400):
        bob.forward(2)
        bob.right(1)

def triangle():
    for count in range(3):
        bob.forward(10)
        bob.right(120)

def perp():
    for count in range(2000):
        bob.forward(count)
        bob.left(90)
        random.shuffle(colours)
        bob.color(colours[0])

choice = input('Please select an option: \n 1: Draw a triangle \n 2: Draw a circle \n 3: PERPETUAL MOTION!!! \n')
if choice == 1:
    triangle()
elif choice == 2:
    circle()
elif choice == 3:
    perp()
else:
    print("Just jump in a hole...")

turtle.exitonclick()