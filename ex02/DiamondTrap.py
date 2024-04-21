from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Represents a King character."""

    def __init__(self, first_name: str, is_alive=True):
        """Constructor for King class."""

        super().__init__(first_name, is_alive)

    def set_eyes(self, color: str):
        """Set the eye color of the King."""

        self.eyes = color

    def set_hairs(self, color: str):
        """Set the hair color of the King."""

        self.hairs = color

    def get_eyes(self) -> str:
        """Return the eye color of the King."""

        return self.eyes

    def get_hairs(self) -> str:
        """Return the hair color of the King."""

        return self.hairs

    _eyes = property(get_eyes, set_eyes)
    _hairs = property(get_hairs, set_hairs)
