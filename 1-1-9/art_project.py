import turtle
import turtle as trtl
painter= trtl.Turtle()
painter.speed(50)
painter.goto(0,-550)
painter.begin_fill()
painter.fillcolor('black')
painter.circle(900)
painter.end_fill()
distance=100

def sun():
    painter.up()
    painter.goto(0, -80)
    painter.down()
    painter.color('orange')
    painter.begin_fill()
    painter.fillcolor('yellow')
    painter.circle(80)
    painter.end_fill()
# Making the sun
sun()
painter.penup()
#making the planets around the sun



    distance +=50













wn = trtl.Screen()
wn.mainloop()