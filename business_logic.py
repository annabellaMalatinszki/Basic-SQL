from data_manager import *
import os


def display_mentor_names():
    os.system("clear")
    print("Mentors:\n\n")
    mentor_names = get_mentor_names()
    for name_pair in mentor_names:
        full_name = name_pair[0] + " " + name_pair[1]
        print(full_name)


def display_nicknames():
    os.system("clear")
    print("Mentor nicknames:\n\n")
    city = input("Choose a city: ")
    mentor_nicknames = get_mentor_nicknames(city)
    if mentor_nicknames:
        for nickname in mentor_nicknames:
            print(nickname[0])
    else:
        print("No such record found")


def display_name_and_number():
    os.system("clear")
    print("Get full applicant name and phone number by:\n\n")
    submenu = ["First name",
               "Last name",
               "Email",
               "Application Code"
               ]

    number = 1
    for item in submenu:
        print("\t({}) {}".format(number, item))
        number += 1
    user_input = input("\n\nSelect an option ")

    if user_input == "1":
        search_by = "first_name"
        str_criteria = "First name"
    elif user_input == "2":
        search_by = "last_name"
        str_criteria = "Last name"
    elif user_input == "3":
        search_by = "email"
        str_criteria = "Email"
    elif user_input == "4":
        search_by = "app_code"
        str_criteria = "Application code"

    display_name_number_by(search_by, str_criteria)


def display_name_number_by(search_by,  str_criteria):
    os.system("clear")
    print("Get full applicant name and phone number by {}:\n\n".format(str_criteria))
    criteria = input(str_criteria + ": ")

    try:
        name_and_number = get_name_number_by(search_by, criteria)
        print("\nName: {}\nPhone number: {}".format(name_and_number[0][0], name_and_number[0][1]))

    except IndexError:
        print("No such record found")


def add_new_applicant():
    os.system("clear")
    print("Add a new applicant:\n\n")
    first_name = input("First name: ")
    last_name = input("Last name: ")
    phone_number = input("Phone number: ")

    email = input("Email: ")
    cond = True
    while cond is True:
        application_code = input("Application code: ")
        try:
            int(application_code)
            cond = False
        except ValueError:
            print("Error: Application code must be an integer without spaces")
            continue

    new_applicant = add_new_applicant_data(first_name, last_name, phone_number, email, application_code)
    os.system("clear")
    print("Add a new applicant:\n\nNew applicant successfully added!\n\n")
    print("Name: {} {}\nPhone number: {}\nEmail: {}\nApplication code: {}".format(first_name, last_name, phone_number,
                                                                                  email, application_code))


def update_app_data():
    os.system("clear")
    print("Update phone number:\n\n")
    first_name = input("First name: ")
    last_name = input("Last name: ")
    new_phone_number = input("Phone number: ")

    try:
        updated_data = update_applicant_data(first_name, last_name, new_phone_number)
        os.system("clear")
        print("Update pone number:\n\nPhone number successfully updated!\n\n")
        print("\nName: {}\nPhone number: {}".format(updated_data[0][0],  updated_data[0][1]))

    except IndexError:
        print("No such record found")


def delete_applicant():
    os.system("clear")
    print("Delete applicant by email:\n\n")
    email = input("Email: ")

    try:
        deleted_user = delete_applicant_by_email(email)
        os.system("clear")
        print("Delete applicant by email:\n\n")
        print("Applicant {} {} successfully deleted.".format(deleted_user[0][0], deleted_user[0][1]))

    except IndexError:
        print("No such record found")
