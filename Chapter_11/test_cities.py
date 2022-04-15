import unittest
from city_functions import get_city_and_country


class NamesTestCase(unittest.TestCase):
    """Tests to program city_functions."""

    def test_city_and_country(self):
        """If dates like 'Santiago, Chile' are valid."""
        formatted_cc = get_city_and_country("santiago", "chile")
        self.assertEqual(formatted_cc, "Santiago, Chile")

    def test_city_country_population(self):
        """If dates like 'Santiago, Chile, 50000' are valid."""
        formatted_cc = get_city_and_country("santiago", "chile", "5000000")
        self.assertEqual(formatted_cc, "Santiago, Chile: 5000000")
