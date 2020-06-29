# Hello
# Austin Dial
# Jun 26, 2020
#
#   Contains functions for testing.
#


# -------------------- DEFINE FUNCTIONS -------------------- #


def string_to_integer(value):
    """Convert a string to an integer. If impossible, return 'Error.'"""

    try:
        number = int(value)
    except ValueError:
        number = "Error."

    return number


def int_to_float(value):
    """Convert an integer to a float. If impossible, return 'Error.'"""

    try:
        number = float(value)
    except ValueError:
        number = "Error."

    return number


def check_registrants(name):
    """Check if a name appears within the registrants list."""

    # Imagine pulling a list of registrants from Event Espresso or something
    registrants = list(["Sally", "Micheal"])

    # Okay, now check if the given name is within that list
    try:
        if name in registrants:
            return 1
        else:
            return 0
    except TypeError:
        return "Error."


def uncovered_function(param):
    """A function which is not covered by a test. This should show up during coverage testing."""
    print(f"Hello {param}!")
