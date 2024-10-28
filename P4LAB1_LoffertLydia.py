# Lydia Loffert
# 10/28.2024
# P4LAB1
# Use loops to make shapes using turtle

# import turtle library
import turtle

window = turtle.Screen()
bobby = turtle.Turtle()

#graphics options
bobby.pensize(6)         #increase pensize (int)
bobby.pencolor("sienna")   #set color of lines (str)
bobby.shape("turtle")    #cursor shape

# While loop to draw 4 sides of square
line = 0
while line <4:
    bobby.right(90)
    bobby.forward(150)
    line += 1

# Change pen color for triangle
bobby.pencolor("red")

#For loop to draw 3 sides of triangle

for line2 in range(3):
    bobby.left(120)
    bobby.forward(150)
    



