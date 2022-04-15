import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    """Create tests for Employee class."""

    def setUp(self) :
        """Create object Employee to work with on tests."""
        self.employee = Employee("Marta", "Szuran", "950000")

    def test_give_default_raise(self):
        """Test checking default raise (5000) is valid."""
        employee_raise = self.employee.give_raise()
        self.assertEqual(employee_raise, 955000)

    def test_give_custom_raise(self):
        """Test checking if custom raise is valid."""
        employee_raise = self.employee.give_raise("100000")
        self.assertEqual(employee_raise, 1050000)
