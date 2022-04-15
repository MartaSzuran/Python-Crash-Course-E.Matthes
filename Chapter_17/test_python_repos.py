import unittest
from python_repos import r


class NamesTestCase(unittest.TestCase):
    """Test for program python_repos.py"""

    def test_status_code(self):
        """Check if the status code is 200"""
        self.assertEqual(r.status_code, 200)
