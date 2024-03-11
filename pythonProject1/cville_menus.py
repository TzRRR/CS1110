# Henry Voter and Tianze Ren (hwv4ug & tr2bx)
# Lab 100
# Charlottesville Menus

Boylan_Heights_Menu = {
                        "Room 121 Burger" : 12
                        , "Double Trouble Burger" : 15
                        , "Mozzarella Sticks" : 9
                        , "BBQ Chicken Nachos" : 12}


def add_menu_item(dict, name, price):
    """
    This function adds a pair of dish name and price to a menu
    :param dict: the menu
    :param name: the name of the dish
    :param price: the price of the dish
    """
    dict[name] = price



def calculate_order(dict, list, tip = .18):
    """
    This function takes the menu, the list of order, and an optional parameter of tip,
     and then it returns the total price
    :param dict: the menu of the restaurant
    :param list: the order of dishes a person wants to order
    :param tip: the tip in percentage
    :return: the total price
    """
    total = 0
    try:
        for dish in list:
            total += dict[dish]
    except:
        print("This list item cannot be ordered")
    return (total*(1+int(tip)))*1.06


def print_the_menu(dict):
    """
    This function prints out the menu
    :param dict: the menu of the restaurant
    """
    for dish in dict:
        print(dish, "--", dict[dish], end = "/n")


all_cville_restaurants = {
                            "Boylan_Heights":Boylan_Heights_Menu,
}


def place_mega_order(mega_menu, order):
    for dish in mega_menu:
        calculate_order(mega_menu, order)



