from turtle import *
import colorsys
speed(0)
pensize(2)
bgcolor("black")
h=0.1
goto(300,-60)
for i in range(200):
    c=colorsys.hsv_to_rgb(h,1,1)
    pencolor(c)
    h+=0.006
    lt(150)
    circle(400-i,80)
done()