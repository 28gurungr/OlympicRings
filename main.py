import turtle

screen = turtle.Screen()
screen.screensize(500, 500)
screen.bgcolor("tan")

t = turtle.Turtle()

t.setheading(0)

t.penup()
t.goto(-80,15)
t.pendown()
t.pencolor("blue")
t.circle(35)

t.penup()
t.goto(0,15)
t.pendown()
t.pencolor("black")
t.circle(35)

t.penup()
t.goto(80,15)
t.pendown()
t.pencolor("red")
t.circle(35)

t.penup()
t.goto(40,-15)
t.pendown()
t.pencolor("green")
t.circle(35)

t.penup()
t.goto(-40,-15)
t.pendown()
t.pencolor("yellow")
t.circle(35)

t.penup()
t.goto(0,100)
t.pencolor("purple")

t.write("Winter Olympics", font=('arial',40,"bold",),align="center")

t.goto(0,-100)
t.pencolor("purple")

t.write("2026", font=('arial',40,"bold",),align="center")

#LAST LINE OF CODE
turtle.done()

