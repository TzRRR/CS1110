# Tianze Ren (tr2bx)
dict_state_name = {}
dict_name_vote = {}
def add_state(name, votes):
    """
    This function is to store the election results for the given state within the global dict(s)
    :param name: the name of the state
    :param votes: a dictionary whose keys are the names of each candidate
    and whose values are the number of votes each candidate received in this state
    """
    Max_value = 0
    Max_name = ""
    global dict_state_name
    for candi in votes:
        if votes[candi] > Max_value:
            Max_value = votes[candi]          # the maximum value in the dict
            Max_name = candi                  # the corresponding key of the maximum value
    dict_state_name[name] = Max_name          # assign the new pair to the dict



def winner(college):
    """
    This function returns the winner of the election or
    "No Winner" if no candidate has votes more than half of the total
    :param college: a dictionary containing example states and their votes
    :return: the winner of the election or
    "No Winner" if no candidate has votes more than half of the total
    """
    global dict_name_vote, dict_state_name
    total = 0
    for state in dict_state_name:
        if state in college:
            if dict_state_name[state] in dict_name_vote:
                dict_name_vote[dict_state_name[state]] += college[state]
            else:
                dict_name_vote[dict_state_name[state]] = college[state]  # assign a new pair to the name vote dict
        else:
            college[state] = 0
    for name in dict_name_vote:
        total += dict_name_vote[name]
    for name in dict_name_vote:
        if dict_name_vote[name] > 1/2 * total:
            return name
    return "No Winner"
