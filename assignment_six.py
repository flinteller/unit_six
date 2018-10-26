# Flint Eller
# 10/22/18
# Simulates the birthday paradox a number of times specified by the user

import random


def user_number():
    """
    Gets how many times the user wants to run the simulation
    :return: returns the number of times
    """
    num = int(input("How many times would you like to simulate the problem?"))
    return num


# This first line creates a blank list called birthdays"
def generate():
    """
    Creates a list of 23 random birthdays however many times the user said
    :return:
    All the lists
    """
    birthdays = []
    for x in range(23):
        random_birthdays = random.randint(1, 365)
        birthdays.append(random_birthdays)
    return birthdays


# A set deletes all duplicates and then we check if the list is longer than the set, if it is there was a match
def check_list(birthdays):
    """
    Checks to see if there is a duplicate in each list
    :param birthdays:
    :return: True is there is, False if not
    """
    birthday_set = set(birthdays)
    if len(birthday_set) < len(birthdays):
        return True
    else:
        return False


def show_user(number_same):
    """
    Prints to user the number of times there was a match
    :param number_same:
    :return: none
    """
    print(number_same, "time(s) there were two of the same birthday")


def main():
    num = user_number()
    number_same = 0
    for y in range(num):
        birthdays = generate()
        if check_list(birthdays) == True:
            number_same += 1
    show_user(number_same)
    print("This is about", number_same / num * 100, "% of the time.")


main()
