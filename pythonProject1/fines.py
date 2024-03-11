# Tianze ren (tr2bx)
def fine(speed_limit, my_speed, zone=None):
    """
    This is the function for the amount of fine a driver should take if the driver is driving
    over or below the speed limit.
    :param speed_limit: the legal maximum speed
    :param my_speed: the driver's speed
    :param zone: the area the driver is driving at
    :return fine_: the amount of money that the driver should be fined
    """
    if 20 > my_speed - speed_limit > 0:
        if zone == "school":
            fine_ = (my_speed - speed_limit) * 7
        elif zone == "work":
            fine_ = (my_speed - speed_limit) * 7
        elif zone == "residential":
            fine_ = (my_speed - speed_limit) * 8 + 200
        else:
            fine_ = (my_speed - speed_limit) * 6
    elif my_speed - speed_limit >= 20:
        fine_ = 350
    elif my_speed - speed_limit < 0:
        fine_ = 30
    elif my_speed == speed_limit:
        fine_ = 0
    return fine_



def demerits(speed_limit, my_speed):
    """
    This function is illustrating how many demerit points are deducted if a driver is driving over the speed limit.
    :param speed_limit: the legal maximum speed
    :param my_speed: the driver's speed
    :return points: the demerit points being deducted
    """
    points = 0
    if 9 >= my_speed - speed_limit >=1:
        points += 3
    elif 19 >= my_speed - speed_limit >=10:
        points += 4
    elif my_speed - speed_limit >=20:
        points += 6
    return points
