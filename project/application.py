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

    true_vals = ["yes", "y", "", "1"]
    false_vals = ["no", "n", "0"]
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


def print_entry(entry):
    """Prints the title and body of the API entry."""

    # Local printing preferences
    total_length = 60
    left_ending = "|-----"
    ending_length = len(left_ending) + 1
    right_ending = left_ending[::-1]

    # Parse out values
    title = entry["title"]
    body = entry["body"]
    length = len(entry["title"])

    # Truncate strings which are too long
    if len(title) > 21:
        title = title[:21] + "..."

    # Truncate strings with odd numbered length
    if length % 2 != 0:
        title = title[: length - 2] + "..."

    # Try pretty printing the header
    n = int((total_length - 2 * ending_length - len(title)) / 2)
    print(left_ending + n * "-" + " " + title + " " + n * "-" + right_ending)

    # Try printing the body of the entry
    print(body)
