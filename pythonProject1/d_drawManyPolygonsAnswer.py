# Craig Dill cd9au Some turtle graphics
import random
import turtle


def draw_shape():
    tom.penup()
    tom.goto(x, y)
    tom.pendown()
    rand_color_side = random.randint(0, len(colors)-1)
    rand_color_fill = random.randint(0, len(colors) - 1)
    tom.color(colors[rand_color_side], colors[rand_color_fill])
    distance = random.randint(10, 60)
    tom.begin_fill()                  # notice begin_fill, not color, to fill shapes
    for side in range(num_sides):
        tom.forward(distance)
        tom.left(360.0/num_sides)
    tom.end_fill()                    # after shape drawn, end fill color
tom = turtle.Turtle()
colors = ["red", "blue", "green", "yellow", "cyan", "orange", "magenta", "black"]
tom.speed()
num_shapes = random.randint(1, 20)
for shape_count in range(num_shapes):
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    num_sides = random.randint(3, 8)
    draw_shape()
turtle.done()
