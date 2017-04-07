"""Refactoring.

This excercise is very similar to week 2, exercise 2. It contains a complete
and working example, but it's very poorly written.

Your job is to go through it and make it as good as you can.

That means making it self-documenting wherever possible, adding comments where
it isn't. Take repeated code and make it into a function. Also use functions
to encapsulate concepts. If something is done many times, maybe a map or a loop
is called for. Etc.

The resulting file should read as close to english as possible.
It must also pass the linter.
"""

from __future__ import division
from __future__ import print_function
import requests

def countdown(message, start, stop, completion_message):
    for i in range(start, stop)[::-1]:
        print(message, i)
    print(completion_message)


""" This should be a function called tell_me_about_this_right_triangle
    it should return a dictionary of triangle facts, keys should include: Area,
    perimeter, height, base, hypotinuse aspect (could be tall or wide)
    It should optionally print information as a nicely formatted string. Make
    printing turned off by default but turned on with an optional argument."""

def calculate_hypotinuse(base, height):
    """A function which calculates the hypoteneuse of a triangle."""
    return (base**2 + height**2)**0.5


def get_triangle_facts(base, height, units="mm"):
    """ A function which returns facts about triangles."""
    return {"area": base*height,
            "perimeter": base+height+calculate_hypotinuse(base, height),
            "height": height,
            "base": base,
            "hypotinuse": calculate_hypotinuse(base, height),
            "aspect": "tall" if height > base else "wide",
            "units": units}


def tell_me_about_this_right_triangle(facts_dictionary, printing=False):
    """A function which describes a right-angled triangle."""

    if printing:
        return """
    This triangle is {area}{units}²
    It has a perimeter of {}{units}
    {height}
    |
    |     |\\
    |____>| \\  {hypotinuse}
          |  \\
          |   \\
          ------
          {base}

    This is a {aspect} triangle.
    """.format(facts_dictionary)


def print_triangle_things():
    """A function which prints facts about triangles."""
    base = 3
    height = 4
    facts_dictionary = get_triangle_facts(base, height, units="mm")
    print(tell_me_about_this_right_triangle(facts_dictionary))


def wordy_pyramid():
    """A function which makes a pyramid of words."""
    baseURL = "http://www.setgetgo.com/randomword/get.php?len="
    pyramid_list = []
    letter_range = range(3, 20, 2) + range(4, 21, 2)[::-1]
    for length in letter_range:
        r = requests.get(baseURL + str(length))
        pyramid_list.append(r.text)

    return pyramid_list


wordy_pyramid()


def get_a_word_of_length_n(n):
    """Returns a word of length-n"""
    url = "http://www.setgetgo.com/randomword/get.php?len="+str(n)
    return requests.get(url).text


def list_of_words_with_lengths(list_of_lengths):
    """."""
    pass
