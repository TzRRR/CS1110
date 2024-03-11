import turtle
win = turtle.Screen()       # alternative: turtle.setup(600,600),turtle.bgcolor("purple")
win.setup(600, 600)         # setup() force window to 600x600
win.bgcolor("purple")       # bgcolor() set background color
joy = turtle.Turtle()       # create the turtle and name it joy
#turtle.done()
joy.penup()                 # raise the turtle so goto does not draw a line
joy.goto(-300, -300)        # turtle starts at 0,0 center, move turtle to bottom left
joy.pendown()               # prepare to draw
joy.color("white")          # line and fill color are same, specify only one color
joy.begin_fill()            # tell turtle to fill shape after drawing the shape
joy.forward(600)            # draw the rectangle, forward/turn four times
joy.left(90)
joy.forward(100)
joy.left(90)
joy.forward(600)
joy.left(90)
joy.forward(100)
joy.left(90)
joy.end_fill()              # this is end of snowy yard so fill in with color white
#turtle.done()
joy.penup()                 # move turtle to start of red house wall
joy.goto(-200, -200)
joy.pendown()
joy.color("red")            # set the wall color and indicate must fill in the shape
joy.begin_fill()
joy.forward(400)            # draw the rectangle with four pairs of forward/left
joy.left(90)
joy.forward(200)
joy.left(90)
joy.forward(400)
joy.left(90)
joy.forward(200)
joy.left(90)
joy.end_fill()              # end of red house wall so fill rectangle with red
#turtle.done()
joy.penup()
joy.goto(-210, 0)
joy.pendown()
joy.color("white")
joy.begin_fill()
joy.forward(420)            # do the roof rectangle
joy.left(90)
joy.forward(100)
joy.left(90)
joy.forward(420)
joy.left(90)
joy.forward(100)
joy.left(90)
joy.end_fill()

joy.penup()                 # print the HAPPY HOLIDAYS!
joy.goto(-240, -280)
joy.pendown()
joy.color("yellow")
joy.write("HAPPY HOLIDAYS!", font=("Arial", 40, "bold"))
joy.color("white")          # hide the turtle in the snow

joy.penup()
turtle.done()               # have fun, change, add, do your own thing however you want
