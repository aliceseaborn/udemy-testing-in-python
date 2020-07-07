# app Module Test - OOP
# Austin Dial
# Jun. 26 2020
#
#   This program defines a set of tests to against the app
#   module within this project hierarchy. The module is imported
#   from the top project directory.
#
#   There are two testing strategies: functional testing and class
#   -based oop testing. This program demonstrates the object oriented
#   testing route. The object route is useful when testing many
#   tests at once. The objects allow for tests to be aggregated.
#
#   Whereas under the functional approach each function within the
#   module is given its own test function, here each function is
#   tested within a class. These classes allow for us to collect
#   the tests into groups in order to organize them. This approach
#   becomes important as the number of units under test grows.
#
#   Unlike the functional approach, the objects created within the
#   testing framework allow for setup and teardown methods. These
#   functions are called respectively before and after each test
#   is executed.
#
#   Additionally, there are functions which can be called only
#   prior and after the class itself is called, rather than each
#   test.
#
#   Then functional tests are constructed for each function within
#   the module. The assert function makes a claim about the result
#   of the test. If the assertion is true under evaluation, then
#   test passes. Otherwise, the test fails because it violates
#   the assertion.
#
#   To execute these tests, run `pytest` from within the testing
#   directory. Alternatively, run `pytest -vs` for verbosity and
#   to prevent pytest from capturing the print statment outputs.
#


# -------------------- IMPORT MODULES -------------------- #


# FROM top_hierarchy import module.function
# from project.app import string_to_integer
from project import application as app

# IMPORT top_hierachy.module as module
# import project.app as app

# Pytest tools
import pytest



# -------------------- DEFINE TESTS -------------------- #


class TestConverters(object):
    
    # Define the setup function
    def setup(self):
        print("\nCalled before the test is executed.")
    
    # Define the teardown function
    def teardown(self):
        print("\nCalled after the test is executed.")
        
    # Define the class setup function
    def setup_class(cls):
        print("\nCalled before class is executed.")
        
    # Define the class teardown function
    def teardown_class(cls):
        print("\nCalled after class is executed.")
    
    # Define a test for one specific function
    def test_string_to_integer(self):
        """Test the string_to_integer function within app module."""
        
        # Test something which is meant to throw an error
        result = app.string_to_integer("5.0")
        assert result == "Error."
        
        # Test something which is meant to work successfully
        result = app.string_to_integer("900")
        assert result == 900
        
    # ...
    def test_int_to_float(self):
        """Test the int_to_float function within app module."""
        
        # Test something which is meant to throw an error
        result = app.int_to_float("app")
        assert result == "Error."
        
        # Test something which is meant to work successfully
        result = app.int_to_float(5)
        assert result == 5.0

    
class TestChecks(object):

    # Define a test for one specific function
    def test_check_registrants(self):
        """Test the string_to_integer function within app module."""
        
        # Test something which is meant to throw an error
        result = app.check_registrants("Eric")
        assert result == 0
        
        # Test something which is meant to work successfully
        result = app.check_registrants("Sally")
        assert result == 1
        
        
# Define a setup function
@pytest.fixture
def setup_entry():
    title = "testing title"
    body = "this is a testing\nbody for an api\ncall."
    
    keys = ["title", "body"]
    values = [title, body]
    
    return dict(zip({keys : values}))


# Demonstrate how to test a function which connects to an API
#   using conventional methods as well as fixtures.
class TestAPI(object):

    # Test the API call itself
    def test_connect_to_api(self):
        """Test the connect_to_api function within app module."""
        
        # Test something which is meant to throw an error
        result = app.connect_to_api(5000)
        assert result == False
        
        # Test something which is meant to work successfully
        result = app.connect_to_api(5)
        assert isinstance(result, dict)


# Demonstrate how many tests can be combined into one through
#   the process of parameterization.
class TestStringToBool(object):
    
    @pytest.mark.parametrize('user_input', ['Y', 'y', 'YES', 'yes', '1'])
    def test_true_values(self, user_input):
        assert app.string_to_bool(user_input) is True
        
    @pytest.mark.parametrize('user_input', ['N', 'n', 'NO', 'no', '0'])
    def test_false_values(self, user_input):
        assert app.string_to_bool(user_input) is False