# Craig Dill (cd9au)
"""
This program demonstrates functions do not alter original values, known as arguments,
they return a new value leaving the original value unaltered.  Sometimes the returned
value is None, as is the case with the print function.  Some commonly used functions
are demonstrated: int(), float(), str(), print(), sqrt(), len(), max(), min(),
random(), randint(), randrange() seed(), round.
"""

# Expand the import statements (Click the +)
from math import sqrt
from random import random, randint, randrange

# Data type conversion functions do not convert the argument value.
# They return a new value based upon the argument value.  The argument is unaltered.
x = 1.56  # x is 1.56 and is used as the argument in the following statement
y = int(x)  # int(x) is 1, int() returns the truncated toward 0 integer of the argument
print(y, x)  # prints the returned value from int(x) which is 1, then prints x
print(int(x), x)  # same values as above statement print, x value unaltered
print("Bye", print('Hi'))  # Hi, new line, Bye None print('Hi') returns None
# To use sqrt() must either from math import sqrt, or import math and use math.sqrt()
print(sqrt(100))  # sqrt returns the square root of the argument, which is then printed
input("1. Press enter to continue:\n")

# Now some random number generation from the random module
# seed(3)  # use seed(value) if want the same pattern (predictable) of random numbers
print(random())  # random() returns a float between 0 inclusive and 1.0 excluded
# randint() returns int between argument 1 & argument 2, inclusive
print(randint(1, 10))
# randrange() returns int between argument 1 included, argument 2 excluded,
# and every other argument 3
print(randrange(1, 101, 2))
input("2. Press enter to continue:\n")

# Some practice with return values
# function input returns a string, which is then used as len's argument.
# len returns the number of characters in its argument.
# This number is print's argument.
print(len(input("Please enter a string: ")))

# input returns a string, passed as argument to float(), which returns the float value
# of the string argument.  This float value is squared (because of the arrangement of
# parenthesis this float value is squared, not an argument to sqrt()).  This process
# is repeated for another input number, the two results of this process are added
# together, then this sum is passed as an argument to sqrt(), which returns the
# square root of the argument.  This square root is passed as the argument to print()
# which prints the argument and returns None.
print(sqrt(float(input("Enter side1: "))**2 + (float(input("Enter side2: "))**2)), "is the third side length.")

num1, num2, num3 = 0, 1, 2
# max's return value is print's argument, min's return value is print's argument
print("Largest:", max(num1, num2, num3), "Smallest:", min(num1, num2, num3))

input("3. Press enter to continue:\n")
# Sometimes you WANT to CHANGE the data named by a variable.  Simple!
num1 = 1.0
print(num1, type(num1))
num1 = int(num1)
print(num1, type(num1))

input("4. Press enter to continue:\n")
num1 = 1.5
num2 = -1.5
print(int(num1), int(num2))
# round() can have 2 arguments: number to round, number of decimal places
print(round(num1), round(num2))
print("int truncates floats toward zero, round truncates away from zero.")
