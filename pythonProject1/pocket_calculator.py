#Tiazne Ren (tr2bx)
current = 0
operation = ""
argument = 0
operation_ = "0"


def get_value():
    """
    This function returns the current value stored in the calculator.
    :return: the current value stored in the calculator
    """
    global current
    return current


def clear(argument_ = 0):
    """
    This function takes in an optional argument value, resets the global variables, and returns a current value.
    :param argument_: the optional argument
    :return: the current value
    """
    global operation
    global argument
    global current
    global operation_
    operation = ""
    argument = 0
    current = argument_
    operation_ = str(current)
    return current


def step(operator, int_added):
    """
    This function performs a calculation by taking a calculation operator and a number.
    :param operator: a arithmetic operator + - * or //
    :param int_added: the number added in the calculation
    :return: the result of the calculation
    """
    global operation
    global operation_
    global argument
    global current
    operation = operator
    argument = int_added
    operation_ = "(" + str(operation_) + ")" + str(operator) + str(int_added)
    if operator == "+":
        current += int_added
    elif operator == "-":
        current -= int_added
    elif operator == "*":
        current *= int_added
    elif operator == "//":
        current //= int_added
    return current


def repeat():
    """
    This function repeats the previous step of calculation, if there is not, it returns the current value.
    :return: the current value of calculation or the value after a repeated calculation
    """
    global current
    global operation
    if operation != "":
        current = step(operation, argument)
        return current
    else:
        return current


def get_expr():
    """
    This function returns the calculation expression in sequence of the whole process.
    :return: the string expression of the calculation process
    """
    global operation_
    return operation_
