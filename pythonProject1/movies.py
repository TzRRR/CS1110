def get_name(movie):
    """
    The function gets a list of movie related strings and returns the name of the movie
    :param movie: a list of movie related information
    :return: the name of the movie
    """
    return movie[0]


def get_gross(movie):
    """
    The function gets a list of movie related information and returns the gross earning of the movie
    :param movie: a list of movie related information
    :return: the gross earning of the movie
    """
    return movie[1]


def get_rating(movie):
    """
    The function gets a list of movie related information and returns the rating of the movie
    :param movie: a list of movie related information
    :return: the rating of the movie out of 10
    """
    return movie[3]


def get_num_ratings(movie):
    """
    The function gets a list of movie related information and returns the number of ratings of the movie
    :param movie: a list of movie related information
    :return: the number of ratings of the movie
    """
    return movie[4]


def better_movies(movie_name, lst):
    """
    This function gets a movie name and a list of lists containing movie related information
    :param movie_name: the name of a movie
    :param lst: a list of lists that contains movie related information
    :return: a list of all movies’ information that have a higher rating than that of movie_name
    """
    higher_rating = []
    for movie in lst:
        if movie_name == get_name(movie):
            comparing_rate = get_rating(movie)
            for movie in lst:
                rating = get_rating(movie)
                if rating > comparing_rate:
                    higher_rating.append(movie)
            return higher_rating


def average(category, lst):
    """

    :param category:
    :param lst:
    :return:
    """
    total = 0
    for movie in lst:
        if category == "rating":
            total += get_rating(movie)
        elif category == "gross":
            total += get_gross(movie)
        elif category == "number of ratings":
            total += get_num_ratings(movie)
    return total/len(lst)
