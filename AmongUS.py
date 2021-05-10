import turtle

# turtle.Screen().bgcolor("black")

a = turtle.Turtle()
a.pencolor('black')
# a.shape('circle')
a.width(9)

# body
a.fillcolor('orange')
a.begin_fill()
a.speed(5)

a.right(90)
a.forward(20)

for i in range(36):
    a.forward(2)
    a.right(5)

a.forward(100)

for i in range(180):
    a.forward(0.9)
    a.right(1)

a.forward(100)

for i in range(30):
    a.forward(2)
    a.right(5)

a.right(30)
a.forward(40)

a.left(90)
a.backward(5)
a.left(3)
a.forward(20)

a.end_fill()


#glass
a.penup()
a.goto(-5,90)
a.pendown()

a.fillcolor('light blue')
a.begin_fill()

a.right(183)
a.forward(50)

for i in range(37):
    a.forward(2)
    a.right(5)

a.left(5)
a.forward(45)

for i in range(37):
    a.forward(2)
    a.right(5)

a.end_fill()

#tail
a.fillcolor('orange')
a.penup()
a.goto(-45,0)
a.right(175)
a.pendown()
a.begin_fill()

a.forward(20)
a.right(90)

a.forward(70)

a.right(90)
a.forward(20)

a.right(90)
a.forward(80)

a.end_fill()


#red one

a.penup()
a.goto(200,0)
a.pendown()

# body
a.fillcolor('red')
a.begin_fill()
a.speed(5)

#a.right(90)
a.forward(20)

for i in range(36):
    a.forward(2)
    a.right(5)

a.forward(100)

for i in range(180):
    a.forward(0.9)
    a.right(1)

a.forward(100)

for i in range(30):
    a.forward(2)
    a.right(5)

a.right(30)
a.forward(40)

a.left(90)
a.backward(5)
a.left(3)
a.forward(20)

a.end_fill()


#glass
a.penup()
a.goto(195,90)
a.pendown()

a.fillcolor('light blue')
a.begin_fill()

a.right(183)
a.forward(50)

for i in range(37):
    a.forward(2)
    a.right(5)

a.left(5)
a.forward(45)

for i in range(37):
    a.forward(2)
    a.right(5)

a.end_fill()

#tail
a.fillcolor('red')
a.penup()
a.goto(155,0)
a.right(175)
a.pendown()
a.begin_fill()

a.forward(20)
a.right(90)

a.forward(70)

a.right(90)
a.forward(20)

a.right(90)
a.forward(80)

a.end_fill()
a.penup()


a.hideturtle()

