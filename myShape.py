def square( t, distance ):
    for times in range(4):
        t.forward(distance)
        t.left(90)

def triangle( t, distance ):
    for times in range(3):
        t.forward(distance)
        t.left(120)

def pentagon( t, distance ):
    for times in range(5):
        t.forward(distance)
        t.left(72)

def polygon(t,distance,side):
    angle=360 /side
    t.begin_fill()
    for times in range (side):
        t.forward(distance)
        t.left(angle)
    t.end_fill()

def move (t,x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
def circle(t,size):
    t.begin_fill()
    t.circle(size)
    t.end_fill()

def idk(t):
    for times in range(16):
        for times in range(4):
            t.right(45)
    
            for times in range(100):
                for times in range(10):
                    t.forward(50)
                    t.left(90)
                for times in range(10):
                    t.forward(50)
                    t.right(90)
            t.home()
