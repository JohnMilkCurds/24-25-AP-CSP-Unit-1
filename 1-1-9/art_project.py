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
def star():
    painter.circle(10)
# Making the sun
sun()
painter.penup()
painter.color('white')
painter.goto(280, 230)
painter.fillcolor('white')
star()
painter.goto()
painter.goto()
painter.goto()
painter.goto()
painter.goto()
painter.goto(-57,)
painter.goto()
painter.goto(64,-78)
painter.goto(-36,-73)
painter.goto(-74,64)
painter.goto(50,50)

#making the planets around the sun

def mercury():
    mercury=trtl.Turtle()
    mercury.penup()
    mercury.shape('circle')
    mercury.color('gray')
    mercury.goto(100,0)
def venus():
    venus=trtl.Turtle()
    venus.penup()
    venus.shape('circle')
    venus.color('sandybrown')
    venus.goto(150, 0)
def earth():
        earth=trtl.Turtle()
        earth.penup()
        earth.shape('circle')
        earth.color('blue')
        earth.goto(200, 0)
def mars():
    mars=trtl.Turtle()
    mars.penup()
    mars.shape('circle')
    mars.color('tomato')
    mars.goto(250, 0)
def jupiter():
    jupiter=trtl.Turtle()
    jupiter.penup()
    jupiter.shape('circle')
    jupiter.color('darkgoldenrod')
    jupiter.goto(300, 0)
def saturn():
    saturn=trtl.Turtle()
    saturn.penup()
    saturn.shape('circle')
    saturn.color('goldenrod')
    saturn.goto(350, 0)
def uranus():
    uranus=trtl.Turtle()
    uranus.penup()
    uranus.shape('circle')
    uranus.color('navy')
    uranus.goto(400, 0)
def neptune():
    neptune=trtl.Turtle()
    neptune.penup()
    neptune.shape('circle')
    neptune.color('cyan')
    neptune.goto(450, 0)
def planets():
    mercury()
    venus()
    earth()
    mars()
    jupiter()
    saturn()
    uranus()
    neptune()
planets()











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