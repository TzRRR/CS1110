# Craig Dill (cd9au)
"""
This is a "special" docstring because it is the first docstring
occurring in the module.  The first docstring of a module should
as a minimum, summarize what the module does.

This program demonstrates the Python print() function for output.
It also demonstrates use of '', "" and """""" to permit outputting
apostrophes and quotes as part of the output string.  It then
demonstrates escape sequences as part of the output string.  It
then demonstrates use of the comma operator and the plus
operator to output strings.  It then demonstrates use of the sep
and end arguments of the print() function.  Finally,
formatting numbers for cleaner output is demonstrated.
"""

# demonstrating print, '', "", """"""
print('The professor wishes you success')
print()  # This outputs a blank line between the previous & next line
print("The professor wishes you success")
print("""The professor wishes you success""")
print('The professor wishes you "success"')
print("The professor wishes you 'success'")
print("""The "professor" wishes you 'success'""")
input("\n1. Press enter to continue: ")  # This pauses program

# Demonstrate escape sequences
print("programming\tis\tgreat!")  # \t is escape sequence for tab
print("programming\nis\ngreat!")  # \n is escape sequence for newline
# \\ is escape sequence for backslash
print("The path to the file is: C:\\programming\\is\\great")
# \" is the escape sequence for ", \' is the escape sequence for '
input("\n2. Press enter to continue: ")

# Demonstrate comma separator and + operator
# In string context the + operator is the concatenation operator
print("Mary", "had", "a", "little", "lamb")  # comma separator
print("Mary" + "had" + "a" + "little" + "lamb")  # concatenation operator
print("7", "77", "777")
# Next, numbers in quotes are strings and concatenate
print("7" + "77" + "777")
input("\n3. Press enter to continue: ")

print(7, 77, 777)
# Numbers not in quotes, now + operator is addition
print(7 + 77 + 777)
input("\n4. Press enter to continue: ")

# Using the print argument sep, notice the separation between values
print("Jim", "John", "Joe", sep="")
print("Jim", "John", "Joe", sep="****")
input("\n5. Press enter to continue: ")

# Using the print argument end, notice the separation between prints
print("Jim", end="")
print("John", end="")
print("Joe", end="")
input("\n6. Press enter to continue: ")

# formatting numeric output
print(format(77.77777, ".2f"))
print(format((98 + 96.5 + 92 + 87.5) / 4, ".2f"))
input("\n7. Press enter to continue: ")

'''
The following example vertically aligns the decimal points of a formatted
number list using a minimum field length preceding the decimal point in the
format arguments, and inserting the newline escape sequence between each
formatted number.
'''
print(format(1.234567, "10.2f") + "\n" + format(12.34567, "10.2f") +
      "\n" + format(123.4567, "10.2f") + "\n" + format(1234.567, "10.2f") +
      "\n" + format(12345.67, "10.2f") + "\n" + format(123456.7, "10.2f") +
      "\n" + format(1234567, "10.2f"))
print("Does the format function round the least significant place?")
