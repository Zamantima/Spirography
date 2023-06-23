import turtle
from turtle import Turtle, Screen
from random import randint
tim = Turtle()
tim.speed("fastest")
turtle.colormode(255)

def color_generator():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    color_tuple = (r,g,b)
    return color_tuple


def spirograph(gap_size):
    for _ in range(int(360 / gap_size)):
        tim.color(color_generator())
        tim.circle(50)
        tim.setheading(tim.heading() + gap_size)

spirograph(10)



Screen = Screen()
Screen.exitonclick()