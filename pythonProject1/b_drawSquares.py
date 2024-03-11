# Mark Sherriff (mss2x)
import turtle
import random


def draw_square(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    rand_color = random.randint(0, len(colors) - 1)
    t.color(colors[rand_color])
    for count in range(4):
        t.forward(100)
        t.left(90)

win = turtle.Screen()
win.setup(600, 600)
win.bgcolor("#00FF00")
tom = turtle.Turtle()
tom.speed("fastest")  # or integer between 0 & 10 inclusive, no quotes
tom.shape("arrow")    # or turtle, circle, square, triangle, classic
colors = ["green", "red", "yellow", "orange", "pink", "cyan"]

for i in range(10):
    rand_x = random.randint(-250, 250)
    rand_y = random.randint(-250, 250)
    draw_square(tom, rand_x, rand_y)

turtle.done()
