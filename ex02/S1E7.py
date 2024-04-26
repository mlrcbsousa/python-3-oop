from S1E9 import Character


class Baratheon(Character):
    """Represents a member of the Baratheon family."""

    def __init__(self, first_name: str, is_alive=True):
        """Constructor for Character class."""

        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    @classmethod
    def create_baratheon(cls, first_name: str, is_alive=True):
        """Create a Baratheon character."""

        return cls(first_name, is_alive)

    def __str__(self):
        """Return a string representation of the object."""

        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Return a string representation of the object."""

        return self.__str__()


class Lannister(Character):
    """Represents a member of the Lannister family."""

    def __init__(self, first_name: str, is_alive=True):
        """Constructor for Character class."""

        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    @classmethod
    def create_lannister(cls, first_name: str, is_alive=True):
        """Create a Lannister character."""

        return cls(first_name, is_alive)

    def __str__(self):
        """Return a string representation of the object."""

        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Return a string representation of the object."""

        return self.__str__()
