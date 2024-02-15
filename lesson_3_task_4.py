import turtle
# Рисунок мыши "примитивно"
t = turtle.Turtle()

t.penup()
t.goto(0, -50)
t.pendown()
t.circle(50)

t.penup()
t.goto(-20, 50)
t.pendown()
t.circle(20)

t.penup()
t.goto(20, 50)
t.pendown()
t.circle(20)

t.penup()
t.goto(-25, 60)
t.pendown()
t.right(90)
t.circle(25, 180)

t.hideturtle()
turtle.done()
t.penup()


turtle.done()
