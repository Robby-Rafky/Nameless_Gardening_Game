from useful_functions import *


class Targeter:
    """
    A class responsible for targeting and selecting areas within the game grid.

    Attributes:
        game (Game): The game instance.
        limit_x (int): The maximum x-coordinate limit.
        limit_y (int): The maximum y-coordinate limit.

    Methods:
        __init__(self, game): Initialize the Targeter instance.
        within_limits(self, x, y): Check if the given coordinates are within the grid limits.
        target_area(self, radius, x, y): Get the list of coordinates within the specified radius around the given center coordinates.
    """

    def __init__(self, game):
        """Initialize the Targeter instance.

        Args:
            game (Game): The game instance.
        """
        self.game = game
        self.limit_x = 0
        self.limit_y = 0

    def within_limits(self, x, y):
        """Check if the given coordinates are within the grid limits.

        Args:
            x (int): The x-coordinate to check.
            y (int): The y-coordinate to check.

        Returns:
            bool: True if the coordinates are within the limits, False otherwise.
        """
        if 0 <= x <= self.limit_x and 0 <= y <= self.limit_y:
            return True
        else:
            return False

    def target_area(self, radius, x, y):
        """Get the list of coordinates within the specified radius around the given center coordinates.

        Args:
            radius (int): The radius of the target area.
            x (int): The x-coordinate of the center.
            y (int): The y-coordinate of the center.

        Returns:
            list: A list of coordinate tuples within the target area.
        """
        targets = []
        diameter = 1 + radius * 2
        for a in range(diameter):
            for b in range(diameter):
                coord_x = (x - radius) + a
                coord_y = (y - radius) + b
                if self.within_limits(coord_x, coord_y):
                    if coord_y != y or coord_x != x:
                        targets.append((coord_x, coord_y))
        return targets
