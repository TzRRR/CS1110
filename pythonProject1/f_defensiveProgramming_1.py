# Craig Dill (cd9au)
"""
Using float and int to defend against bad integer input
"""
# int truncates toward 0 (both positive and negative)
# round rounds away from 0 (both positive and negative)

# defensive programming, coerce string to float, then float to int
first = int(float(input("Please enter an integer (but user enters float): ")))
second = int(float(input("Please enter another integer (but user enters float): ")))
print(first, second)

# demonstrate difference when use round rather than int
first = round(float(input("Please enter an integer (but user enters float): ")))
second = round(float(input("Please enter another integer (but user enters float): ")))
print(first, second)
