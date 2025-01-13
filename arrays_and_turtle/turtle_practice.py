import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("lightblue")

# Create a turtle
t = turtle.Turtle()
t.shape("turtle")
t.color("black")

#EXERSISE 1
"""
Drawing commands
side_length = 100
angle = 360/5
t.forward(50)
for i in range(4):
  t.left(angle)
  t.forward(side_length)
t.left(angle)
t.forward(50)
"""
#EXERSISE 2
"""
Drawing commands
side_length = 100
angle = 360/8
t.forward(50)
for i in range(7):
  t.left(angle)
  t.forward(side_length)
t.left(angle)
t.forward(50)
"""
#EXERSISE 3
"""
def shape(sides, color):
  side_length = 100
  angle = 360/sides
  t.fillcolor(color)
  t.begin_fill()
  t.forward(50)
  for i in range(sides-1):
    t.left(angle)
    t.forward(side_length)
  t.left(angle)
  t.forward(50)
  t.end_fill()

shape(3, "red")
"""

t.fillcolor("red")
t.begin_fill()
t.circle(80)
t.end_fill()

# Finish
turtle.done()