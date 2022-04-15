from random import choice


class RandomWalk:
    """Class for generate randomly chosen values."""

    def __init__(self, num_points=5000):
        """Initialize random walk attributes"""
        self.num_points = num_points

        # x / y coordinates set on (0,0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Generate all points for random walk."""

        # making steps till get to the expected number or points
        while len(self.x_values) < self.num_points:

            # set another x / y values
            # last value plus chosen step
            next_x = self.get_step(self.x_values)
            next_y = self.get_step(self.y_values)

            if next_x == 0 and next_y == 0:
                continue

            # add new x / y values to the x_values/y_values lists
            self.x_values.append(next_x)
            self.y_values.append(next_y)

    def get_step(self, value):
        """Creating one step for random walk."""
        # set the direction and distance to reach in that direction
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4])
        step = direction * distance

        next_step = value[-1] + step

        return next_step
