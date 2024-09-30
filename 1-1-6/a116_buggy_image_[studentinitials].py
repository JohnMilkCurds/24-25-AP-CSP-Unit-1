#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
painter = trtl.Turtle()
painter.pensize(40)
painter.circle(20)
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