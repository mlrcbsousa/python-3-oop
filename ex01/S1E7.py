from S1E9 import Character


class Baratheon(Character):
    """Represents a member of the Baratheon family."""

    def __init__(self, first_name, is_alive=True):
        """Constructor for Character class."""

        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = self.__class__.__name__
        self.eyes = 'brown'
        self.hairs = 'dark'

    def __str__(self):
        """Return a string representation of the object."""

        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Return a string representation of the object."""

        return self.__str__()


class Lannister(Character):
    """Represents a member of the Lannister family."""

    def __init__(self, first_name, is_alive=True):
        """Constructor for Character class."""

        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = self.__class__.__name__
        self.eyes = 'blue'
        self.hairs = 'light'

    def __str__(self):
        """Return a string representation of the object."""

        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Return a string representation of the object."""

        return self.__str__()

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        """Create a Lannister character."""

        return cls(first_name, is_alive)
