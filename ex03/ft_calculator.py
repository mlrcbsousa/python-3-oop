class calculator:
    """A class to perform basic operations on a vector."""

    def print(func):
        """Print the vector after the operation."""
        def wrapper(*args):
            func(*args)
            print(args[0].vector)
        return wrapper

    def __init__(self, vector: list[float]) -> None:
        """Constructor for the calculator class."""

        self.vector = vector

    @print
    def __add__(self, object: int) -> None:
        """Add a value to the vector."""

        self.vector = [x + object for x in self.vector]

    @print
    def __mul__(self, object) -> None:
        """Multiply the vector by a value."""

        self.vector = [x * object for x in self.vector]

    @print
    def __sub__(self, object) -> None:
        """Subtract a value from the vector."""

        self.vector = [x - object for x in self.vector]

    @print
    def __truediv__(self, object) -> None:
        """Divide the vector by a value."""

        assert object != 0, "Cannot divide by zero."

        self.vector = [x / object for x in self.vector]
