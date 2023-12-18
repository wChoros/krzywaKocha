import turtle
def section(len):
    if(len<9):
        t.forward(len)
    else:
        section(len/3)

    t.left(60)

    if(len<9):
        t.forward(len)
    else:
        section(len/3)

    t.right(120)

    if(len<9):
        t.forward(len)
    else:
        section(len/3)

    t.left(60)

    if(len<9):
        t.forward(len)
    else:
        section(len/3)

t = turtle.Turtle()
t.speed(0)
t.penup()
t.left(180)
t.forward(364.5)
t.right(90)
t.forward(200)
t.right(90)
t.pendown()



section(243)
t.right(120)
section(243)
t.right(120)
section(243)
turtle.exitonclick()
