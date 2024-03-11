# Tianze Ren tr2bx


def num_strings(list):
    """
    This function takes in a list of lists containing strings and return the total number of strings in the list
    :param list: a list of lists containing strings
    :return: the total number of strings in the list
    """
    total = 0
    for lists in list:
        for strings in lists:
            total += 1
    return total


def contacts(list):
    """
    This function takes a list of lists containing strings and prints them out into a csv file
    :param list: a list of lists containing strings
    :return: no return
    """
    file = open("contacts.txt", "w")
    for lists in list:
        for index in range(len(lists)):
            if index != int(len(lists) - 1):
                file.write(lists[index] + ",")
            else:
                file.write(lists[index])
        file.write("\n")
    file.close()


def find_elephant(url):
    """
    This function takes a website link and find if the website has the word "elephant" (case insensitive)
    :param url: the website link
    :return: True if the website contains the word "elephant", False if the website doesn't
    """
    import urllib.request, re
    stream = urllib.request.urlopen(url)
    stream = stream.read()
    stream = stream.decode('utf-8')
    find_elephant = re.compile(r"[Ee][Ll][Ee][Pp][Hh][Aa][Nn][Tt]")
    result = re.findall(find_elephant, stream)
    if len(result) != 0:
        return True
    else:
        return False


def results(file):
    """
    This function takes a csv file containing sports scores and returns the overall result
    :param file: a csv file containing sports scores
    :return: the result of sports game result
    """
    data = open(file, "r")
    data_ = data.readlines()
    data.close()
    dict = {}
    for line in data_:
        line = line.strip("\n").split(",")
        if line[1] > line[3]:
            if line[0] not in dict:
                dict[line[0]] = 1
            else:
                dict[line[0]] += 1
            if line[2] not in dict:
                dict[line[2]] = 0
        elif int(line[3]) > int(line[1]):
            if line[2] not in dict:
                dict[line[2]] = 1
            else:
                dict[line[2]] += 1
            if line[0] not in dict:
                dict[line[0]] = 0
    return dict


def num_orders(dict, list):
    """
    This function takes a dictionary containing dish information and a list containing order information
    :param dict: a dictionary containing information of dish availability
    :param list: a list containing information of orders
    :return: total number of filled orders
    """
    count = 0
    for index in range(len(list) + 1):
        for dish in dict:
            if count < len(list):
                if list[index] == dish:
                    if dict[dish] > 0:
                        dict[dish] -= 1
                        count += 1
                    else:
                        return count
            else:
                return count
            if list[index] not in dict.keys():
                return 0
