# Tianze Ren (tr2bx)
number = int(input("Pick a number between 1 and 10: "))
number_ = (number * 2 + 5) * 50
birthday = int(input("If you've already had a birthday this year, enter 1771. Otherwise, enter 1770: "))
born = int(input("Enter the year that you were born: "))
number_ = number_ + birthday
number_ = number_ - born
print('The magic number is "' + str(number_) + '". That means you are ' + str(number_ - number * 100) + '!')