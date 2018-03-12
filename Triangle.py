from turtle import *
import time
from sys import exit

speed(100)
color('red', 'yellow')

#Triangle

begin_fill()
#How many sides does the shape have
for shape in range(3):
 forward(150)
 right(120)#Angle of the shape
end_fill()
time.sleep(2)
clear()

#Square

begin_fill()
#How many sides does the shape have
for shape in range(4):
 forward(150)
 right(90)#Angle of the shape
end_fill()
time.sleep(2)
clear()

#Hexagon

begin_fill()
#How many sides does the shape have
for shape in range(6):
 forward(100)
 right(60)#Angle of the shape
end_fill()
time.sleep(2)
clear()

#Pentagon

begin_fill()
#How many sides does the shape have
for shape in range(5):
 forward(150)
 right(72)#Angle of the shape
end_fill()
time.sleep(2)
clear()

print("Yay!")

# Everything else

import turtle
from turtle import *
bgcolor('black')
for starts in range(6):
 for i in range(30):
     color('red', 'yellow')
     begin_fill()
     forward(60)
     left(170)
     forward(100)
 end_fill()

clear()
bgcolor('white')

import random
def squares():
 for square in range (4):
     fd(80)
     left(90)
     penup()
     fd(40)
     pendown()
def main():
 for col in range(10):
     color('blue', 'white')
     pensize(2)
     begin_fill()
     squares()
     end_fill()
     left(90)
     fd(80)
main()

clear()

from turtle import *
color('red','green')
begin_fill()
circle(120, 180)
left(90)
fd(250)
end_fill()
done()

time.sleep(2)
clear()

tsegay = turtle.Turtle()
tsegay.penup()
#this line of code tells the computer to start drawing
#from the left side of the window
tsegay.goto(-300, 30)
tsegay.pendown()
tsegay.color("red", "orange")
radii = 10
#this line of code tells the computer to draw 6 circles
for circles in range(6):
 tsegay.begin_fill()
# this line of code tells the computer to draw 1 circle
 for circle in range (1):
     radii = radii + 10
     tsegay.circle(radii)
     tsegay.penup()
     tsegay.forward(150)
     tsegay.pendown()
     tsegay.end_fill()

time.sleep(2)
clear()

wn = turtle.Screen()
bob = turtle.Turtle()
bob.penup()
#This line of code tells the computer to start drawing from the left side of the window
bob.backward(300)
bob.pendown()
bob.color("Red", "Blue")
for squares in range(4): #this line of code tells the computer to draw 4 squares
 bob.begin_fill()
 for i in range (4): #this line of code draws 4 lines and 4 angles
     bob.forward(100)
     bob.right(90)
     bob.penup()
     bob.forward(200)
     bob.pendown()
     bob.end_fill()

time.sleep(2)
clear()
