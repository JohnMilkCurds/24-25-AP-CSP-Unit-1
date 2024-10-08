#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]

index=0
for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  t.penup()
  my_turtles.append(t)

# starting position of the turtle
startx = 0
starty = 0
direction=90
#moves the turtle to the place where the shape is made
for t in my_turtles:
  t.color(turtle_colors.pop())
  t.setheading(direction)
  t.pendown()
  t.goto(startx, starty)
  index+=1
  t.right(45)
  t.forward(50)
  direction=t.heading()
# where the turtle will move next
  startx = t.xcor()
  starty = t.ycor()
wn = trtl.Screen()
wn.mainloop()