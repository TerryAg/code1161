"""Week 3, Exercise 3.

Steps on the way to making your own guessing game.
"""
from __future__ import division
from __future__ import print_function
import random


def advancedGuessingGame():
    """Play a guessing game with a user.

    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)

    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    marge it with code from excercise 1.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """
    lower = int_input("Enter the lower bound: ")
    upper = int_input("Enter the upper bound: ")
    while upper < lower:
        print("Your upper limit is lower than your lower limit!")
        upper = int_input("Enter the upper bound: ")

    random_int = random.randint(lower, upper)
    print(random_int)
    print("Guess the number between {} and {}!".format(lower, upper))
    while True:
        guess = int_input("Guess: ")
        if not lower <= guess <= upper:
            print("That is not in the range!")
            continue
        if guess > random_int:
            print("Too high!")
        elif guess < random_int:
            print("Too low!")
        else:
            return "You got it!"


def int_input(message=''):
    """Continually asks for an integer."""
    answer = raw_input(message)
    try:
        answer = int(answer)
        return answer
    except:
        print("Please input an integer only!")
        return int_input("Integer: ")


if __name__ == "__main__":
    print(advancedGuessingGame())
