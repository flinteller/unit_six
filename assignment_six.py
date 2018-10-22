# Flint Eller
# 10/22/18
# Simulates the birthday paradox a number of times specified by the user

import random


def user_number():
    num = int(input("How many times wpuld you like to simulate the problem?"))
    return num


def generate(num):
    for y in range(num):
        for x in range(23):
            birthdays = random.randint(1, 365)
            # Create list with all numbers
    return birthdays


def print_birthdays(birthdays):
    print(birthdays)


def main():
    num = user_number()
    birthdays = generate(num)
    print_birthdays(birthdays)





main()
