import turtle
import turtle as trtl
painter= trtl.Turtle()
painter.speed(50)
painter.goto(0,-550)
painter.begin_fill()
painter.fillcolor('black')
painter.circle(900)
painter.end_fill()

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
bodies = ['dark_golden_rod', 'dark_golden_rod', 'cyan', 'red','orange','dark_golden_rod','blue','cyan']
for planet in range(8):
    turtle.shape('circle')













wn = trtl.Screen()
wn.mainloop()