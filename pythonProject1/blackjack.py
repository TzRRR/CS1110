# Tianze Ren (tr2bx)
def card_to_value(card):
    """
    This function converts the parameter input to the numeric value according to the game rule
    :param card: the string expression of the card value
    :return: the numeric value of the card
    """
    cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"]
    if card == cards[0]:
        value = 1
    elif card in cards[1: 9]:
        value = int(card)
    else:
        value = 10
    return value


def hard_score(hand):
    """
    This functions takes the string expression of the cards in hand and return the total numeric value
    :param hand: the string expression of the cards in hand
    :return: the total numeric value of the cards in hand
    """
    total = 0
    for single in hand:
        total += card_to_value(single)
    return total


def soft_score(hand):
    """
    This function takes the string expression of the cards in hand and return the total numeric value.
    Especially, it takes the first Ace ("A") as 11 points.
    :param hand: the string expression of the cards in hand
    :return: the total numeric value of the cards in hand
    """
    total = 0
    for single in hand:
        total += card_to_value(single)
    if "A" in hand:
        total += 10
    return total
