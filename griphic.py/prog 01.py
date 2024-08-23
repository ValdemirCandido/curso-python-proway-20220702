import turtle
t = turtle.Turtle()  # Definitions and initializations
screen = turtle.Screen() 
screen. colormode(255)
t.pensize(4)


def parallelogram():
    t.forward(150)
    t.left(60)
    t.forward(150)
    t.left(120)
    t.forward(150)
    t.left(60)
    t.forward(150)
    t.left(140)


r = 255
g = b = 0
for i in range(18):  # python_graphic start of drawing procedure
    t.fillcolor((r, g, b))    
    t.begin_fill() 
    parallelogram()  # parallelogram function call
    t.end_fill() 
    r -= 8  # change of red to a slightly darker shade
t.ht()  # turtle hide
screen.exitonclick()
