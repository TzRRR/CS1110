# Craig Dill (cd9au)
"""
Variable naming rules and Assignment
"""
'''
Variable naming rules:
Variable names cannot be a Python reserved word
Variable names may consist only of characters a-z, A-Z, 0-9 and _
Variable names begin with a character a-z, A-Z or _
Variable names are case sensitive X and x are different variables
Variable names should always reflect the variable's purpose.
A variable to store my favorite activity might be named
my_favorite_activity or in camel case myFavoriteActivity.

Variable name examples, good or bad?
    x
    1st_name
    tom@berry_farms
    numGrades
'''
# variables are created using assignment statements
PI = 3.14
favorite_pie = "blueberry"
favorite_number = 3

# Python permits multiple assignments in one statement
num1, num2, num3 = 1, 2, 3
print(num1, num2, num3)

# Use assignment to swap values named by two variables
num2, num3 = num3, num2
print(num1, num2, num3)
print(17 % 5)