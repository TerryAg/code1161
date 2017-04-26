# -*- coding: UTF-8 -*-
"""Refactoring.

This excercise is very similar to week 2, exercise 2. It contains a complete
and working example, but it's very poorly written.

Your job is to go through it and make it as good as you can.

That means making it self-documenting wherever possible, adding comments where
it isn't. Take repeated code and make it into a function. Also use functions
to encapsulate concepts. If something is done many times, maybe a map or a loop
is called for. Etc.

The resulting file should feel as close to english as possible.
It must also pass the linter.

This is the first file that will be run against the pydocstyle checker. If
you've run the week5_system_prep.sh file you should be getting blue linter dots
that show you where lintere errors are. If they aren't working, you should be
getting the errors in the test output.

Some functions will have directions as external comments, once you think you
are on top of it, take these comments out. Others won't have comments and
you'll need to figure out for yourself what to do.
"""

from __future__ import division
from __future__ import print_function


# return a lit of countdown messages, much like in the bad function above.
# It should say something different in the last message.
def countdown(message, start, stop, completion_message):
    """Count down."""
    if start < stop:
        a = [message for _ in range(start, stop)[::-1]]
        return a + [completion_message]
    return [message for _ in range(stop, start)[::-1]] + [completion_message]


# TRIANGLES

# This should be a series of functions that are ultimatly used by
# triangle_master
# It should eventually return a dictionary of triangle facts. It should
# optionally print information as a nicely formatted string. Make printing
# turned off by default but turned on with an optional argument.
# The stub functions are made for you, and each one is tested, so this should
# hand hold quite nicely.
def calculate_hypotenuse(base, height):
    """Calculate hypoteneuse."""
    return (base**2 + height**2)**0.5


def calculate_area(base, height):
    """Calculate area."""
    return base*height / 2


def calculate_perimeter(base, height):
    """Calculate perimeter."""
    return base + height + calculate_hypotenuse(base, height)


def calculate_aspect(base, height):
    """Calculate aspect."""
    if height > base:
        return "tall"
    elif height < base:
        return "wide"
    else:
        return "equal"


# Make sure you reuse the functions you've already got
# Don't reinvent the wheel
def get_triangle_facts(base, height, units="mm"):
    """Get triangle facts."""
    return {"area": calculate_area(base, height),
            "perimeter": calculate_perimeter(base, height),
            "height": height,
            "base": base,
            "hypotenuse": calculate_hypotenuse(base, height),
            "aspect": calculate_aspect(base, height),
            "units": units}


# this should return a multi line string that looks a bit like this:
#
# 15
# |
# |     |\
# |____>| \  17.0
#       |  \
#       |   \
#       ------
#       8
# This triangle is 60.0mm²
# It has a perimeter of 40.0mm
# This is a tall triangle.
#
# but with the values and shape that relate to the specific
# triangle we care about.
def tell_me_about_this_right_triangle(facts_dictionary):
    """Tell me about right triangles."""
    tall = """
            {height}
            |
            |     |\\
            |____>| \\  {hypotenuse}
                  |  \\
                  |   \\
                  ------
                  {base}"""
    wide = """
            {hypotenuse}
             ↓         ∕ |
                   ∕     | <-{height}
               ∕         |
            ∕------------|
              {base}"""
    equal = """
            {height}
            |
            |     |⋱
            |____>|  ⋱ <-{hypotenuse}
                  |____⋱
                  {base}"""

    pattern = ("This triangle is {area}{units}²\n"
               "It has a perimeter of {perimeter}{units}\n"
               "This is a {aspect} triangle.\n")

    facts = pattern.format(**facts_dictionary)
    height = facts_dictionary['height']
    hypotenuse = facts_dictionary['hypotenuse']
    base = facts_dictionary['base']
    aspect = facts_dictionary["aspect"]
    if aspect == "tall":
        return tall.format(height=height, hypotenuse=hypotenuse,
                           base=str(base) + "\n" + facts)
    elif aspect == "wide":
        return wide.format(height=height, hypotenuse=hypotenuse,
                           base=str(base) + "\n" + facts)
    elif aspect == "equal":
        return equal.format(height=height, hypotenuse=hypotenuse,
                            base=str(base) + "\n" + facts)


def triangle_master(base,
                    height,
                    return_diagram=False,
                    return_dictionary=False):
    """Get triangle facts."""
    d_facts = get_triangle_facts(base, height)
    picture = tell_me_about_this_right_triangle(d_facts)
    if return_diagram and return_dictionary:
        return {"diagram": picture, "facts": d_facts}
    elif return_diagram:
        return picture
    elif return_dictionary:
        return {"facts": d_facts}
    else:
        print("You're an odd one, you don't want anything!")


def wordy_pyramid():
    """Get wordy pyramid."""
    pyramid_list = list_of_words_with_lengths(range(3, 20, 2))
    pyramid_list.extend(list_of_words_with_lengths(range(3, 21)[::-2]))
    return pyramid_list


def get_a_word_of_length_n(length):
    """Get word length n."""
    import requests
    baseURL = "http://www.setgetgo.com/randomword/get.php?len="
    if length >= 3 and isinstance(length, int):
        return requests.get(baseURL+str(length)).text


def list_of_words_with_lengths(list_of_lengths):
    """Get list of words."""
    return [get_a_word_of_length_n(n) for n in list_of_lengths]
