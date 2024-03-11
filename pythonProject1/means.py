#Tianze Ren (tr2bx)
def mean_all(table):
    """
    This function takes in a list of lists and calculates the means of all numbers in the list
    :param table: a list of lists
    :return: the mean of all numbers in the list
    """
    length1 = 0
    length2 = 0
    total = 0
    for lst in table:
        length1 = len(table)
        for num in lst:
            length2 = len(lst)
            total += num
    return (total / (length1*length2))


def mean_by_row(table):
    """
    This function takes in a list of lists and calculates the means by sublists in the parameter table
    :param table: a list of lists
    :return: the means of sublists in the parameter table
    """
    means = []
    total = 0
    length = 0
    for lst in table:
        for num in lst:
            length += 1
            total += num
        means.append(total / length)
        total = 0
        length = 0
    return means


def mean_by_col(table):
    """
    This function takes in a list of lists
    and calculates the means of all the values at a particular index in each of the sublists
    :param table: a list of lists
    :return: the means of all the values at a particular index in each of the sublists
    """
    means = []
    total = 0
    for lst in table:
        for index in range(len(lst)):
            for lst in table:
                total += lst[index]
            means.append(total / len(table))
            total = 0
    return means[0 : len(lst)]

