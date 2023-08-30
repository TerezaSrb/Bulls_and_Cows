"""
project_2.py: druhý projekt do Engeto Online Python Akademie
author: Tereza Srbová
email: terezasrbova.ts@gmail.com
discord: Tereza S#9721
"""
import random


def execute():
    print("-----------------------------------------------")
    number = generate_number()
    print(number)
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print("-----------------------------------------------")
    print("Enter a number:")
    print("-----------------------------------------------")
    guess_count = 0
    while True:
        guess = input()
        guess_count += 1
        if not is_input_valid(guess):
            print("Invalid input, try again.")
            print("-----------------------------------------------")
            continue
        bulls = calculate_bulls(number, int(guess))
        if bulls == len(str(number)):
            print(f"Correct, you've guessed the right "
                  f"number in {guess_count} guesses!")
            break
        cows = calculate_cows(number, int(guess)) - bulls
        grammatical_number_bulls = "" if bulls == 1 else "s"
        grammatical_number_cows = "" if cows == 1 else "s"
        print(f"{bulls} bull{grammatical_number_bulls}, "
              f"{cows} cow{grammatical_number_cows}")
        print("-----------------------------------------------")


def generate_number():
    while True:
        number = random.randint(1000, 9999)
        if len(set(str(number))) == len(str(number)):
            return number


def calculate_cows(target, guess):
    return len(set(str(target)).intersection(set(str(guess))))


def calculate_bulls(target, guess):
    hits = 0
    for i in range(len(str(target))):
        if str(target)[i] == str(guess)[i]:
            hits += 1
    return hits


def is_input_valid(input_number):
    return (all([ch.isnumeric() for ch in input_number]) and
            len(input_number) == 4 and int(input_number[0]) != 0 and
            len(set(str(input_number))) == len(str(input_number)))


if __name__ == "__main__":
    execute()
