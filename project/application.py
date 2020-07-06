# Application
# Austin Dial
# Jun 26, 2020
#
#   Contains functions for testing.
#

# -------------------- IMPORT MODULES -------------------- #

import requests



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
    """A function which is not covered by a test. This should show up during
        coverage testing."""
    print(f"Hello {param}!")


def string_to_bool(value):
    """Converts string values to native boolean states in Python."""
    
    true_vals = ['yes', 'y', '', '1']
    false_vals = ['no', 'n', '0']
    try:
        value = value.lower()
    except AttributeError:
        value = str(value).lower()
    if value in true_vals:
        return True
    elif value in false_vals:
        return False
    else:
        raise ValueError("Invalid input value: %s" % value)


def connect_to_api(endpoint):
    """Connects to an API and returns the response data."""
    
    # Form and call api
    url = "https://jsonplaceholder.typicode.com/posts/{}".format(endpoint)
    response = requests.get(url)
    
    # Handle response
    if response.status_code >= 400:
        return False
    else:
        return response.json()

