# Mark Sherriff (mss2x), Craig Dill (cd9au)
import turtle


def draw_shape(sides):
    angle = 360.0 / sides
    for i in range(sides):
        if dana.color()[0] == "red":  # .color()[0] is side color
            dana.color("green")       # set side color to green
        else:
            dana.color("red")         # set side color to red
        dana.forward(100)
        dana.left(angle)
dana = turtle.Turtle()
dana.color("red", "green")  # side color is red, fill color (if used) is green
draw_shape(6)
dana.right(180)
draw_shape(5)
turtle.done()