# Hello Module Test - Functional
# Austin Dial
# Jun. 26 2020
#
#   This program defines a set of tests to against the hello
#   module within this project hierarchy. The module is imported
#   from the top project directory.
#
#   There are two testing strategies: functional testing and class
#   -based oop testing. This program demonstrates the functional
#   testing route.
#
#   Then functional tests are constructed for each function within
#   the module. The assert function makes a claim about the result
#   of the test. If the assertion is true under evaluation, then
#   test passes. Otherwise, the test fails because it violates
#   the assertion.
#
#   To execute these tests, run `pytest` from within the testing
#   directory. Alternatively, run `pytest -v` for verbosity.
#


# -------------------- IMPORT MODULES -------------------- #


# FROM top_hierarchy import module.function
# from project.hello import string_to_integer

# IMPORT top_hierachy.module as module
import project.hello as hello



# -------------------- DEFINE TESTS -------------------- #


# Define a test for one specific function
def test_string_to_integer():
    """Test the string_to_integer function within hello module."""
    
    # Test something which is meant to throw an error
    result = hello.string_to_integer("5.0")
    assert result == "Error."
    
    # Test something which is meant to work successfully
    result = hello.string_to_integer("900")
    assert result == 900
    
    
# ...
def test_int_to_float():
    """Test the int_to_float function within hello module."""
    
    # Test something which is meant to throw an error
    result = hello.int_to_float("hello")
    assert result == "Error."
    
    # Test something which is meant to work successfully
    result = hello.int_to_float(5)
    assert result == 5.0
    
    
# ...
def test_check_registrants():
    """Test the string_to_integer function within hello module."""
    
    # Test something which is meant to throw an error
    result = hello.check_registrants("Eric")
    assert result == 0
    
    # Test something which is meant to work successfully
    result = hello.check_registrants("Sally")
    assert result == 1