#   a116_ladybug.py
import turtle as trtl

# create ladybug head
painter = trtl.Turtle()
painter.pensize(40)
painter.circle(5)

# and body
painter.penup()
painter.goto(0, -55)
painter.color("red")
painter.pendown()
painter.pensize(40)
painter.circle(20)
painter.setheading(270)
painter.color("black")
painter.penup()
painter.goto(0, 5)
painter.pensize(2)
painter.pendown()
painter.forward(75)

# config dots
num_dots = 1
xpos = -20
ypos = -55
painter.pensize(10)

# draw two sets of dots
for line in range(2):
  painter.penup()
  painter.goto(xpos, ypos)
  painter.pendown()
  painter.circle(3)
  painter.penup()
  painter.goto(xpos + 30, ypos + 20)
  painter.pendown()
  painter.circle(2)

  # position next dots
  ypos = ypos + 25
  xpos = xpos + 0
  num_dot = num_dots + 1
leg_num = 8
leg_length = 150
spacing = 260 / leg_num
painter.pensize(5)
n = 0
while n < leg_num:
  painter.goto(0,0)
  painter.setheading(spacing*n)
  painter.forward(leg_length)
  n = n + 1
painter.hideturtle()

wn = trtl.Screen()
wn.mainloop()