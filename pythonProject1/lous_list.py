import urllib.request

def instructor_lectures(department, instructor):
    """
    This function gets a name of the instructor in a certain department
    and returns all the lectures this instructor is teaching
    :param department: the academic department the instructor is in
    :param instructor: the name of the instructor
    :return: a list of all classes the given instructor is teaching in the department
    """
    link = "http://cs1110.cs.virginia.edu/files/louslist/"
    stream = urllib.request.urlopen(link+department)
    stream = stream.readlines()
    class_list = []
    for line in stream:
        line_ = line.decode("UTF-8").strip().split("|")
        name = str(line_[4]).split("+")
        if name[0] == instructor and line_[5] == "Lecture":
            if line_[3] not in class_list:
                class_list.append(line_[3])
    return class_list


def compatible_classes(first_class, second_class, needs_open_space=False):
    """
    This function gets two class code and check if two classes are compatible
    :param first_class: the representing code of a class
    :param second_class: the representing code of a class
    :param needs_open_space: the condition that indicates whether the student needs open space in the class
    :return: True if two classes are compatible and False is two classes are not compatible
    given the condition of needs_open_space
    """
    link = "http://cs1110.cs.virginia.edu/files/louslist/"
    department_first = first_class.split()[0]
    department_second = second_class.split()[0]
    stream_first = urllib.request.urlopen(link + department_first).readlines()
    stream_second = urllib.request.urlopen(link + department_second).readlines()
    first_class = first_class.split("-")
    second_class = second_class.split("-")
    first_class_ = first_class[0].split(" ")
    second_class_ = second_class[0].split(" ")
    first_week = []
    second_week = []

    for line in stream_first:
        line_ = line.decode("UTF-8").strip().split("|")
        if first_class_[0] == line_[0] and first_class_[1] == line_[1] and first_class[1] == line_[2]:
            line_first = line_

    for line in stream_second:
        line_ = line.decode("UTF-8").strip().split("|")
        if second_class_[0] == line_[0] and second_class_[1] == line_[1] and second_class[1] == line_[2]:
            line_second = line_

    first_start = line_first[12]
    first_end = line_first[13]
    enrollment_first = int(line_first[16]) - int(line_first[15])
    first_week.append(line_first[7:12])

    second_start = line_second[12]
    second_end = line_second[13]
    enrollment_second = int(line_second[16]) - int(line_second[15])
    second_week.append(line_second[7:12])

    if needs_open_space:
        if enrollment_first != 0 or enrollment_second != 0:
            if int(first_start) <= int(second_start) <= int(first_end) or int(first_start) <= int(second_end) <= int(first_end):
                if first_week != second_week:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False
    elif needs_open_space == False:
        if int(first_start) <= int(second_start) <= int(first_end) or int(first_start) <= int(second_end) <= int(first_end):
            if first_week != second_week:
                return True
            else:
                return False
        else:
            return True





