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
painter.penup()
#making the planets around the sun
mercury=trtl.Turtle()
mercury.shape('circle')
mercury.color('brown')
mercury.goto(100,0)
venus=trtl.Turtle()
Earth=trtl.Turtle()
mars=trtl.Turtle()
jupiter=trtl.Turtle()
saturn=trtl.Turtle()
uranus=trtl.Turtle()
neptune=trtl.Turtle()














wn = trtl.Screen()
wn.mainloop()
#BACKUP PLAN
'''
bodies = ['gray', 'sandybrown', 'blue', 'tomato','darkgoldenrod','goldenrod','lightblue','navy', 'cyan']
for planet in range(9):
    painter.goto(distance, 0)
    painter.color(bodies[planet])
    painter.shape('circle')
    painter.begin_fill()
    painter.fillcolor(bodies[planet])
    painter.circle(10)
    painter.end_fill()
'''