from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract base class for characters."""

    @abstractmethod
    def __init__(self, first_name: str, is_alive=True):
        """Constructor for Character class."""

        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """Kill the character."""

        self.is_alive = False


class Stark(Character):
    """Represents a member of the Stark family."""

    def __init__(self, first_name: str, is_alive=True):
        """Constructor for Stark class."""

        super().__init__(first_name, is_alive)
