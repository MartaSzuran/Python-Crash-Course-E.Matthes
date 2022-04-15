import unittest
from name_function import get_formatted_name


# good practise is to give name to test connected to the functions name and include word 'test'
class NamesTestCase(unittest.TestCase):
    """Tests for program 'name_function.py'"""

    def test_first_last_name(self):
        """If dates like 'Janis Joplin' are valid."""
        formatted_name = get_formatted_name("janis", "joplin")
        # assertion method
        # check if variable formatted_name is equal to the "Janis Joplin",
        # if not tell me about it
        self.assertEqual(formatted_name, "Janis Joplin")

    def test_first_last_middle_name(self):
        """Checking dates with first, last and middle name."""
        formatted_name = get_formatted_name("wolfgang", "mozart", "amadeus")
        self.assertEqual(formatted_name, "Wolfgang Amadeus Mozart")

# in pycharm I do not have to add unittest.main()
# unittest.main()


# output

# .
# ----------------------------------------------------------------------
# Ran 1 test in 0.000s

# OK

# '.' means that single test was passed
# next row shows time took
# OK means that all test in this test block was passed


# failed test
# Ran 1 test in 0.006s

# FAILED (errors=1)

# Error
# Traceback (most recent call last):
#   File "C:\Users\Marta\Desktop\GIT\Python-Crash-Course-E.Matthes\Chapter_11\test_name_function.py",
#   line 11, in test_first_last_name
#     formatted_name = get_formatted_name("janis", "joplin")
# TypeError: get_formatted_name() missing 1 required positional argument: 'last'


