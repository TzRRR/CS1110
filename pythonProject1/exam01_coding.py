#Tianze Ren (tr2bx)
def show_one_higher():
    """
    This function gives the value of 1 higher than the user's input value。
    :return: the value of user's input plus 1
    """
    value = int(input('Enter a number: '))
    value_ = value + 1
    print('One more than', str(value), 'is', str(value_))



def roll_two(a,b):
    """
    This functions takes the roll of two dice and returns their result.
    :param a: the value of the first dice
    :param b: the value of the second dice
    :return: the result of the roll
    """
    if a == b:
        return 'YOU WIN'
    elif (a + b) % 2 == 0:
        return a+b
    elif (a + b) % 2 == 1:
        return a*b



def initials(first, last, middle = 'x'):
    """
    This function returns the name initials for a full name
    :param first: the first name of a full name
    :param last: the last name of a full name
    :param middle: the middle name of a full name
    :return: the name initial
    """
    first = first.lower()
    last = last.lower()
    middle = middle.lower()
    return first[0] + middle[0] + last[0]
