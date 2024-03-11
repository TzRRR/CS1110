# string_ = "Python"
# def add_accolade(string):
#     global string_
#     string_ = string+" "+string_
#     return string_
#
# print(add_accolade("Useful"))
# print(add_accolade("The"))

# def income_taxes(name):
#     file = "incomes.csv"
#     data = open(file, "r")
#     for line in data:
#         line = line.strip().split(",")
#         if name == line[0]:
#             if line[1] <= 1000:
#                 tax = float(line[1]) * 0.1
#             else:
#                 tax = 100 + (line[1] - 1000) * 0.25
#             return tax

# def string_thing(my_string):
#     """
#
#     :param my_string:
#     :return:
#     """
#     b = True
#     for c in my_string:
#         b = not b
#     return b
# import re, urllib
#
# def everything(menu):
#     total = 0
#     price = re.compile(r"[0-9]+.[0-9]*")
#     price_ = price.findall(menu)
#     for number in price_:
#         total += float(number)
#     return total
#
# print(everything(menu = '''
# Spring Roll 1.70
# Lrg. Fries 13.00
# Lobster 110.05
# '''))
#
# def get_menu(URL):
#     stream = urllib.request.urlopen(URL)
#     stream = stream.readlines()
#     for line in stream:
#         line_ = line.decode("UTF-8").strip().split("|")
#         return everything(line_)
#
# def dict_to_csv(dict):


# def convert(n):
#     return int(n)
# def divide(a, b):
#     try:
#         return a/b
#     except:
#         print("yikes")
#         return -1
# def convert_divide(q, r):
#     thing1 = convert(q)
#     thing2 = convert(r)
#     print(divide(thing1, thing2))
# x = input()
# y = input()
# convert_divide(x,y)

# def meal_picker(a,b,c):
#     if a % 2 == 0:
#         if a > b or c > b:
#             return "Burger"
#     elif a % 3 == 0:
#         if b > a and b > c:
#             return "Salad"
#     if c > a or b > a+c:
#         return "Dumplings"
#     elif b + a > c and c - b > a:
#         return "Tacos"
#     else:
#         return "Fish"
#
# print(meal_picker(3, 4, 3))
#
# print(meal_picker(6, 8, 3))
# print(meal_picker(4, 6, 8))
# print(meal_picker(5, 8, 2))
# import re
# text = "The date was Jan 25, 1819 when the University of Virginia was founded."
#
# my_pattern = "(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) [0-9]{2}, ([0-9]+)"
#
# my_re = re.compile(my_pattern)
#
# for x in my_re.finditer(text):
#     print(x.group())
#     print(x.group(0))
#     print(x.group(1))
#     print(x.group(2))
#     print(x.groups())
#
# # a = "shit"
# print(a)
#
def exam_another_function(my_list_a, my_list_b):
    out = []
    for x in my_list_a:
        if x not in out:
            out.append(x)

    out.append(my_list_b[0])

    for y in my_list_b[1:5]:
        if y not in my_list_a:
            out.append(y)
    return out

first = [4,5,4,9,5,2]
second = [3,4,5,7,3,1]
answer = exam_another_function(first, second)
print(len(answer))
print(answer)


# def exception_question(a,b,c,d):
#     try:
#         x = int(a)
#         if b > c:
#             return x//c
#         else:
#             return d[2]
#     except TypeError:
#         return "T"
#     except ValueError:
#         return "V"
#     except IndexError:
#         return "I"
#
# print(exception_question(4.0, 1, 2, [2, 3, 4]))
# print(exception_question("4.5", 2, 2, [2, 3, 4]))
# print(exception_question("3", "2", "1", [2, 3, 4]))
# print(exception_question("3", 2, 1, [2, 3]))
# # print(exception_question(4.9, 2, 0, [2, 3, 4]))
# print(exception_question(4.9, -1, 0, [2, 3]))



