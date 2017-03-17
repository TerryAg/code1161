# -*- coding: UTF-8 -*-
"""Week 3.

Modify each function until the tests pass.
"""
from __future__ import division
from __future__ import print_function


def loop_ranger(start, stop=None, step=1):
    """Return a list of numbers between start and stop in steps of step.

    Do this using any method apart from just using range()
    """
    L = []
    count = start
    while count < stop:
        L.append(count)
        count += step
    return L


def lone_ranger(start, stop, step):
    """Duplicate the functionality of range.

    Look up the docs for range() and wrap it in a 1:1 way
    """
    L = []
    count = start
    while count < stop:
        L.append(count)
        count += step
    return L


def two_step_ranger(start, stop):
    """Make a range that steps by 2.

    Sometimes you want to hide complexity.
    Make a range function that always has a step size of 2
    """
    L = []
    count = start
    while count < stop:
        L.append(count)
        count += 2
    return L


def gene_krupa_range(start, stop, even_step, odd_step):
    """Make a range that has two step sizes.

    make a list that instead of having evenly spaced steps
    has odd steps be one size and even steps be another.
    """
    L = []
    counter = 2
    while start < stop:
        L.append(start)
        if counter % 2:
            start += odd_step
            counter += 1
        else:
            start += even_step
            counter += 1
    print(L)
    return L


def stubborn_asker(low, high):
    """Ask for a number between low and high until actually given one.

    Ask for a number, and if the response is outside the bounds keep asking
    until you get a number that you think is OK
    """
    n = None
    low = int(low)
    high = int(high)
    while not (low < n < high):
        n = int(raw_input("Enter a number" +
                "between {} and {}: ".format(low, high)))
        if not low < n < high:
            print("That is out of bounds!")
    return n


def not_number_rejector():
    """Ask for a number repeatedly until actually given one.

    Ask for a number, and if the response is actually NOT a number (e.g. "cow",
    "six", "8!") then throw it out and ask for an actual number.
    When you do get a number, return it.
    """
    n = None
    while n is None:
        n = raw_input("Enter a number: ")
        try:
            n = int(n)
        except:
            print("That is not a number!")
            n = None
    return n


def super_asker(low, high):
    """Robust asking function.

    Combine stubborn_asker and not_number_rejector to make a function
    that does it all!
    """
    n = None
    low = int(low)
    high = int(high)
    while not (low < n < high):
        n = raw_input("Enter a number between {} and {}: ".format(low, high))
        try:
            n = int(n)
        except:
            print("That is not a number!")
    return n


if __name__ == "__main__":
    # this section does a quick test on your results and prints them nicely.
    # It's NOT the official tests, they are in tests.py as usual.
    # Add to these tests, give them arguments etc. to make sure that your
    # code is robust to the situations that you'll see in action.
    # NOTE: because some of these take user input you can't run them from
    # inside Atom, you need to run them from the terminal. E.g.:
    # ben@um:~/projects/git/code1161base$ python week3/exercise1.py

    print("\nloop_ranger", loop_ranger(1, 10, 2))
    print("\nlone_ranger", lone_ranger(1, 10, 3))
    print("\ntwo_step_ranger", two_step_ranger(1, 10))
    print("\ngene_krupa_range", gene_krupa_range(1, 20, 2, 5))
    print("\nstubborn_asker")
    stubborn_asker(30, 45)
    print("\nnot_number_rejector")
    not_number_rejector()
    print("\nsuper_asker")
    super_asker(33, 42)
