# Craig Dill (cd9au)
"""
This program demonstrates Python operators used in calculations,
+, -, *, **, /, //, % and sometimes the data types of results generated
by these operators
"""
print(5 + 9, type(5 + 9))                        # integer addition
print(5 + 9.0, type(5 + 9.0))                    # promotion int + float is float
print("George " + "Washington", type("George " + "Washington"))  # string concatenation
print("Mark"*3 + 2 * "Sue", type("Mark" * 3 + 2 * "Sue"))  # string replication
input("1. Press enter to continue.\n")

print(3.234243 * 56.24, type(3.234243 * 56.24))  # float multiplication
print(9.5 / 2.3, type(9.5 / 2.3))                # float division
print(2 ** 3, type(2 ** 3))                      # exponentiation of ints
print(2 ** 3.4, type(2 ** 3.4))                  # exponentiation of floats
print(25 % 6, type(25 % 6))                      # finding a remainder
print(1 % 2, 2 % 2, 3 % 2, 4 % 2, type(1 % 2))   # even numbers % 2 is 0
print(6 // 4, type(6 // 4))                      # // is integer division of ints, no decimal
print(6.3//4.7, type(6.3//4.7))                  # no remainder division of floats, ?.0
print(6 / 4, type(6 / 4), 6 / 6, type(6 / 6))    # float division, decimal part
print(5.0 + 1, 5.0 * 1, 5.0 / 1, 5.0 - 1, 5.0 ** 1, 3 * str(5.0))
input("2. Press enter to continue.\n")

print(float(1), 1 + 1.0)        # int coerced to float
print(int(2.5), int(2.5) + 2)   # float coerced to int
print("One as a numeral is " + str(1))  # int coerced to string, only strings concatenate
print("R" + str(2) + "D" + str(2))    # int coerced to string, only strings concatenate
print("G" + "o" * 2 + "se")     # string replication and concatenation, note "o" * "2" doesn't work
print(format(5.1236, ".3f"))    # 5.124
print(round(5.1236, 3))         # 5.124
input("3. Press enter to continue.\n")

print(input('Enter String: '))  # input returns the user response, which is then printed
print(int(input('Enter int: ')))  # input returns user response, coerced to int, printed
print(float(input('Enter float: ')))  # input returns user response, coerced to float, printed
input("\n4. Press enter to continue.")

print(chr(65), chr(66), chr(65 + 25))  # print Unicode characters for codes 65, 66, 90
print(chr(97), chr(98), chr(97 + 25))  # print Unicode characters for codes 97, 98, 122
print(chr(48), chr(49), chr(48 + 9))   # print Unicode characters for codes 48, 49, 57
print(ord('A'), ord('a'), ord('0'))    # print Unicode for the characters
print(len("Howdy Pilgrim"))            # len() returns number of characters in string
print(max(1, 2, 3, 4), max('a', 'b', 'c', 'Z'))  # careful, UNICODE!
print(min(1, 2, 3, 4), min('a', 'b', 'c', 'Z'))  # careful, UNICODE!
print(pow(10, 2))                      # does it work for floats?
