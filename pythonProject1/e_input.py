# Craig Dill (cd9au)
"""
Program demonstrates input and data type coercion (type casting)
In CS 111x input means information provided by the program user via keyboard.
This information is assigned to a variable name.
"""

# input string values
name = input("Please enter your name (notice the space after the :): ")
sentence = input("Please enter a sentence: ")
garbage = input("Please type a bunch of gibberish: ")
print(name)
print(sentence)
print(garbage)
input("\n1. Press enter to continue: ")

# All data captured from keyboard by input is string data. String data is a
# sequence of characters.  Numeral characters have no numeric value.
num1 = input("Please enter an integer: ")  # input returns a string
num2 = input("Please enter another integer: ")
print(num1 + num2)  # both num1 and num2 are strings, this is concatenation
input("\n2. Press enter to continue: ")

# input string characters then convert to int.  Input MUST LOOK LIKE AN INTEGER
num1 = int(input("Please enter an integer: "))  # string input coerced to int
num2 = int(input("Please enter another integer: "))
print(num1 + num2)  # adding two ints
input("\n3. Press enter to continue: ")

# input integer characters then coerce to float, notice the output
num1 = float(input("Please enter an integer: "))  # integer characters now float
num2 = float(input("Please enter another integer: "))
print(num1 + num2)  # float + float is float
input("\n4. Press enter to continue: ")

# input float as float, input must look like a float or int
num1 = float(input("Please enter a decimal value: "))
num2 = float(input("Please enter another decimal value: "))
print(num1 + num2)
input("\n5. Press enter to continue: ")

# This actually works for gathering two inputs for one assignment statement.
num1, num2 = int(input("Enter first integer: ")), int(input("Enter second integer: "))
print(num1, num2)
