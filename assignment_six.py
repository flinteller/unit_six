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


def print_birthdays(birthdays):
    print(birthdays)


def check_list(birthdays):
    for days in birthdays:
        if days in birthdays:
            print("yes")


def show_user(number_same):
    print(number_same, "times there were two of the same birthday")


def main():
    num = user_number()
    for y in range(num):
        birthdays = generate()
        print_birthdays(birthdays)
        number_same = check_list(birthdays)
        show_user(number_same)


main()
