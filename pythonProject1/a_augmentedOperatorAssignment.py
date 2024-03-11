# Craig Dill cd9au
"""
Augmented assignment operators (self modifying operators)
using operation equals (op equals).
"""

count1 = count2 = 0  # chained assignment, both count1 and count2 have 0
count1 += 1   # augmented operator equivalent to count1 = count1 + 1
count2 -= 1   # augmented operator equivalent to count2 = count2 - 1
print(count1, count2)

total = 0
num1, num2, num3, num4 = 100, 50, 4, 2
total += num1       # equivalent to total = total + num1, total is 100
total -= num2       # equivalent to total = total - num2, total is 50
total *= num3       # equivalent to total = total * num3, total is 200
total /= num4       # total = total / num4, total is 100.0 (float division)
total //= 10        # total = total(float) //(integer divide) by 10 total=10.0
total %= 4          # total = remainder of total divide by 4 is 2.0
total **= 2         # total = total squared, total is 4.0
total //= 3.0       # total = total(float) //(integer) divide by 3.0 is 1.0
print(total)
