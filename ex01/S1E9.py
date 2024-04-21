from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract base class for characters."""

    @abstractmethod
    def __init__(
        self,
        first_name: str,
        is_alive=True,
        family_name=None,
        eyes=None,
        hairs=None
    ):
        """Constructor for Character class."""

        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = family_name
        self.eyes = eyes
        self.hairs = hairs

    def die(self):
        """Kill the character."""

        self.is_alive = False

    def __str__(self):
        """Return a string representation of the object."""

        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Return a string representation of the object."""

        return self.__str__()


class Stark(Character):
    """Represents a member of the Stark family."""

    def __init__(self, first_name: str, is_alive=True):
        """Constructor for Stark class."""

        super().__init__(first_name, is_alive, 'Stark', 'blue', 'dark')

    @classmethod
    def create_stark(cls, first_name: str, is_alive=True):
        """Create a Stark character."""

        return cls(first_name, is_alive)
