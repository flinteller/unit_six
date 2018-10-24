# Flint Eller
# 10/22/18
# Simulates the birthday paradox a number of times specified by the user

import random


def user_number():
    num = int(input("How many times would you like to simulate the problem?"))
    return num


def generate():
    birthdays = []
    for x in range(23):
        random_birthdays = random.randint(1, 365)
        birthdays.append(random_birthdays)
    return birthdays


def check_list(birthdays):
    birthday_set = set(birthdays)
    if len(birthday_set) < len(birthdays):
        return True
    else:
        return False


def show_user(number_same):
    print(number_same, "time(s) there were two of the same birthday")


def main():
    num = user_number()
    for y in range(num):
        birthdays = generate()
    number_same = 0
    if check_list(birthdays) == True:
        number_same += 1
    show_user(number_same)


main()
