import turtle
ts = turtle.getscreen()
t = turtle.Turtle()


t.penup()
t.forward(50)
t.back(50)
t.right(90)
t.left(90)
t.home()
t.undo()
t.clear()
t.reset()
t.color("red")
t.circle(50)
t.begin_fill()
t.pendown()
t.circle(50)
t.end_fill()
t.reset()


#Simple Cartoon Character 
#Move to Middle
t.penup()
t.setpos(0,-250)

#Draw Circle
t.pendown()
t.color("#E8BEAC");
t.begin_fill();
t.circle(280)
t.end_fill();

#L-Eye
t.penup()
t.setpos(-140,120)
t.pendown()
t.color("black")
t.begin_fill()
t.circle(20)
t.end_fill();

#R-Eye
t.penup()
t.setpos(140,120)
t.pendown()
t.color("black")
t.begin_fill()
t.circle(20)
t.end_fill();

#MOTH
t.color("black","darkred")
t.begin_fill()
t.penup ()
t.goto (-100, -70)

t.right (90)
t.circle (100,180)
t.penup ()
t.goto (-100, -70)
t.pendown()
t.end_fill();
t.penup ()
t.right(90)
t.pendown ()
t.circle(-10,70)

#TEET
t.penup()
t.goto (-40, -70)
t.color("white")
t.pendown()

t.begin_fill()
for i in range(3):
    t.circle(50,47)

t.end_fill()
t.penup()

#LEAR
t.home()
t.color("black")
t.goto (-450,300)
t.pendown()
t.begin_fill()
t.circle(100)
t.end_fill()

#REAR
t.penup()
t.home()
t.color("black")
t.goto (450,300)
t.pendown()
t.begin_fill()
t.circle(100)
t.end_fill()
t.penup()
t.home()

turtle.done()