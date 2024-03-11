# Craig Dill (cd9au)
"""
This program identifies the Python data types used in CS 111x and
demonstrates dynamic binding.
"""
'''
Python data types used in CS 111x:
    int - used for whole integer numbers
    float - used for decimal numbers
    str - used for strings, a sequence of characters
    bool - short for boolean, used to hold either True or False
    list - used to store multiple values in an ordered sequence
    tuple - like a list, but read only
    dict - short for dictionary used to store info in key/value pairs
'''
'''
Immutable data types:
    int, float, str and bool are called immutable data types because once
    the value is assigned to memory the value cannot change. This does
    not mean you can’t reassign an immutable data type variable, it just
    means the variable will name a new location in memory. tuple is read only.

Mutable data types:
    list, and dict are called mutable because they can be changed
    in the same place in memory.
'''

# Use Python's type and print functions to display data types
print("Some data types:")
print("1 is data type", type(1))
print("1.0 is data type", type(1.0))
print("Tom is data type", type("Tom"))
print("True is data type", type(True))
input("\n1. Press enter to continue: ")

# demonstrate promotion: the product of int x float is float
number1 = 33
number2 = 3.33
number3 = number1 * number2
print(type(number1), type(number2), type(number3))
input("\n2. Press enter to continue: ")

# demonstrate dynamic binding: a variable can name any data type
dynamic = 1
print(dynamic, type(dynamic))
dynamic = 1.0
print(dynamic, type(dynamic))
dynamic = True
print(dynamic, type(dynamic))
