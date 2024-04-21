from S1E9 import Character


class Baratheon(Character):
    """Represents a member of the Baratheon family."""

    def __init__(self, first_name: str, is_alive=True):
        """Constructor for Character class."""

        super().__init__(first_name, is_alive, 'Baratheon', 'brown', 'dark')

    @classmethod
    def create_baratheon(cls, first_name: str, is_alive=True):
        """Create a Baratheon character."""

        return cls(first_name, is_alive)


class Lannister(Character):
    """Represents a member of the Lannister family."""

    def __init__(self, first_name: str, is_alive=True):
        """Constructor for Character class."""

        super().__init__(first_name, is_alive, 'Lannister', 'blue', 'light')

    @classmethod
    def create_lannister(cls, first_name: str, is_alive=True):
        """Create a Lannister character."""

        return cls(first_name, is_alive)
