import turtle

leonardo = turtle.Turtle()
leonardo.penup()
HEXADECIMAL = 16
BINARY = 2
x = 300
font_size = 30
number = int(input("Enter integer between 0 and 2047 inclusive: "))
BASE = int(input("Please enter 2 or 16 to convert " + str(number) + " to binary or to hexadecimal: "))
leonardo.goto(-font_size * 4, font_size * 2)
leonardo.write(str(number) + " in base " + str(BASE) + " is", font=("Helvetica", font_size, "bold"))

remainder = number % BASE
number //= BASE
while number > 0:
    leonardo.goto(x, 0)
    leonardo.pendown()
    if remainder == 15:
        remainder = 'F'
    elif remainder == 14:
        remainder = 'E'
    elif remainder == 13:
        remainder = 'D'
    elif remainder == 12:
        remainder = 'C'
    elif remainder == 11:
        remainder = 'B'
    elif remainder == 10:
        remainder = 'A'
    leonardo.write(remainder, font=("Helvetica", font_size, "bold"))
    leonardo.penup()
    remainder = number % BASE
    x -= 60
    number //= BASE
leonardo.goto(x, 0)
leonardo.pendown()
if remainder == 15:
    remainder = 'F'
elif remainder == 14:
    remainder = 'E'
elif remainder == 13:
    remainder = 'D'
elif remainder == 12:
    remainder = 'C'
elif remainder == 11:
    remainder = 'B'
elif remainder == 10:
    remainder = 'A'
leonardo.write(remainder, font=("Helvetica", font_size, "bold"))
leonardo.penup()
turtle.done()
