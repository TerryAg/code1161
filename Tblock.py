import turtle
import random

# Describe this function...
def draw_T():
  global x, y
  turtle.goto(x,y)
  turtle.pendown()
  turtle.color('#%06x' % random.randint(0, 2**24 - 1))
  draw_base()
  turtle.right(90)
  turtle.forward(100)
  draw_top()
  turtle.penup()

# Describe this function...
def draw_base():
  turtle.begin_fill()
  turtle.left(90)
  turtle.forward(100)
  turtle.right(90)
  turtle.forward(10)
  turtle.right(90)
  turtle.forward(100)
  turtle.right(90)
  turtle.forward(10)
  turtle.end_fill()

# Describe this function...
def draw_top():
  turtle.begin_fill()
  turtle.right(90)
  turtle.forward(75)
  turtle.left(90)
  turtle.forward(10)
  turtle.left(90)
  turtle.forward(140)
  turtle.left(90)
  turtle.forward(10)
  turtle.left(90)
  turtle.forward(65)
  turtle.end_fill()

# Describe this function...
def move_cursor():
  global x, y
  x = random.randint(-200, 200)
  y = random.randint(-200, 200)


x = 0
y = 0
turtle.speed(10)

for count in range(100):
  draw_T()
  move_cursor()