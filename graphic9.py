import turtle

def draw_attractive_design6():
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    pen = turtle.Turtle()
    pen.speed(10)
    turtle.bgcolor("black") 
    pen.pensize(2)

    for i in range(35):
        pen.color(colors[i % 6])
        pen.circle(100)
        pen.left(25)

    pen.hideturtle()

draw_attractive_design6()

turtle.done()