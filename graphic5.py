import turtle

def draw_attractive_design3():
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    pen = turtle.Turtle()
    pen.speed(10)
    turtle.bgcolor("black")  
    pen.pensize(2)

    for i in range(180):
        pen.color(colors[i % 6])
        pen.forward(100)
        pen.left(59)
        pen.forward(50)
        pen.left(91)
        pen.forward(50)
        pen.left(59)
        pen.forward(100)
        pen.right(121)

    pen.hideturtle()

draw_attractive_design3()

turtle.done()