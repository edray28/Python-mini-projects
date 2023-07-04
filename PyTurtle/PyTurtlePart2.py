import turtle
t = turtle.Turtle();
screen = turtle.Screen()

#Directions
def move_east():
    t.penup()
    t.setheading(0)
    t.fd(50)

def move_north():
    t.penup()
    t.setheading(90)
    t.fd(50)

def move_west():
    t.penup()
    t.setheading(180)
    t.fd(50)

def move_south():
    t.penup()
    t.setheading(270)
    t.fd(50)

#Shapes
def draw_square():
    t.begin_fill()
    t.color("green")
    t.pendown()
    for i in range(4):
        t.fd(30)
        t.rt(90)
    t.penup()
    t.end_fill()

def draw_circle():
    t.begin_fill()
    t.color("yellow")
    t.pendown()
    t.circle(15)
    t.penup()
    t.end_fill()
   
def draw_triangle():
    t.begin_fill()
    t.color("red")
    t.pendown()
    for i in range(3):
        t.left(120)
        t.forward(70)
    t.penup()
    t.end_fill()
   
#Shapes2
def draw_square2():
    t.begin_fill()
    t.color("pink")
    t.pendown()
    for i in range(4):
        t.fd(30)
        t.rt(90)
    t.penup()
    t.end_fill()

def draw_circle2():
    t.begin_fill()
    t.color("red")
    t.pendown()
    t.circle(15)
    t.penup()
    t.end_fill()
   
def draw_triangle2():
    t.begin_fill()
    t.color("green")
    t.pendown()
    for i in range(3):
        t.left(120)
        t.forward(100)
    t.penup()
    t.end_fill()

#Arrow Keys
screen.onkey(move_east,"Right")
screen.onkey(move_north,"Up")
screen.onkey(move_west,"Left")
screen.onkey(move_south,"Down")
screen.listen()

#Shapes Key
screen.onkey(draw_square,"s")
screen.onkey(draw_square2,"S")

screen.onkey(draw_circle,"c")
screen.onkey(draw_circle2,"C")

screen.onkey(draw_triangle,"t")
screen.onkey(draw_triangle2,"T")


turtle.done()

