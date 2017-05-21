import os
import sys
from data_manager import *
from business_logic import *


def print_menu():
    """ Print menu items with corresponding numbers """
    menu = ["Get mentor names",
            "Get mentor nicknames",
            "Get full applicant name and phone number",
            "Add new applicant",
            "Update applicant data",
            "Delete applicant",
            "Exit program"
            ]
    number = 1
    print("Main Menu\n\n")
    for item in menu:
        print("({}) {}".format(number, item))
        number += 1


def select_menu():
    """Calls functions corresponding to the right number input by the user """
    user_input = input("\n\nSelect an option ")
    if user_input == "1":
        display_mentor_names()
    elif user_input == "2":
        display_nicknames()
    elif user_input == "3":
        try:
            display_name_and_number()
        except UnboundLocalError:
            print("Error: No such option")
            pass
    elif user_input == "4":
        add_new_applicant()
    elif user_input == "5":
        update_app_data()
    elif user_input == "6":
        delete_applicant()
    elif user_input == "7":
        os.system("clear")
        print("Exiting program")
        sys.exit(0)
    else:
        raise KeyError("There is no such option.")
    back = input("\n\nPress any button to get back to the Main menu")
