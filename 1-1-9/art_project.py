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
    painter.begin_fill()
    painter.pendown()
    painter.circle(5)
    painter.penup()
    painter.end_fill()
# Making the sun
sun()
painter.penup()
painter.color('white')
painter.goto(280, 230)
painter.fillcolor('white')
star()
painter.goto(-100,-140)
star()
painter.goto(-260,262)
star()
painter.goto(187,-150)
star()
painter.goto(212,-103)
star()
painter.goto(-120,150)
star()
painter.goto(-170,-230)
star()
painter.goto(366,-170)
star()
painter.goto(247,-120)
star()
painter.goto(-196,-137)
star()
painter.goto(-274,164)
star()
painter.goto(104,209)
star()
painter.goto(112,-173)
star()
painter.goto(-240,150)
star()
painter.goto(-110,-230)
star()
painter.goto(165,-)
star()
painter.goto(217,-201)
star()
painter.goto(-193,-121)
star()
painter.goto(-214,124)
star()
painter.goto(200,200)
star()
painter.penup()


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