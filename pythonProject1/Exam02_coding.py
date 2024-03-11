# Tianze Ren (tr2bx)
def get_diagonal(grid):
    """
    This function takes in a list of lists and returns a list of its diagonal numbers.
    :param grid: a list of lists containing numbers
    :return: a list of its diagonal numbers.
    """
    index = 0
    dia = []
    for lst in grid:
        dia.append(lst[index])
        index += 1
    return dia



def sum_all(string):
    """
    This function takes in a string with spaces and commas, and returns the numerical sum of the string number
    :param string: a string of numbers with spaces and commas
    :return: the sum of the numbers
    """
    string.strip()
    string = string.split(",")
    num = 0
    for character in string:
        num += int(character)
    return num



def groceries(d,i,n):
    """
    This function takes a dictionary, a pair of key and value, and returns the new dictionary that has the pair added
    :param d: the dictionary
    :param i: the key of the pair
    :param n: the value of the pair
    :return: the new dictionary with the pair of key and value being added
    """
    if i in d:
        d[0] = n
    else:
        d[i] = n
    return d
