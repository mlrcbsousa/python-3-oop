class calculator:
    """A class to perform basic operations on a vector."""

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Calculate the dot product of two vectors."""

        print(f"Dot product is: {sum([a * b for a, b in zip(V1, V2)])}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Add two vectors together."""

        print(f"Add Vector is : {[float(a + b) for a, b in zip(V1, V2)]}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Subtract two vectors."""

        print(f"Sous Vector is: {[float(a - b) for a, b in zip(V1, V2)]}")
