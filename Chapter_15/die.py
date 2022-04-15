# simulation of rolling one die

from random import randint


class Die:
    """Class for represent one die."""
    def __init__(self, num_sides=6):
        """In this case die is a cube. """
        self.num_sides = num_sides

    def roll(self):
        """Chose one number from (1-6)."""
        return randint(1, self.num_sides)
