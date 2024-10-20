from price_strategy import PriceStrategy, NEW_RELEASE, REGULAR, CHILDREN


class Movie:
    """
    A movie available for rent.
    """
    def __init__(self, title: str):
        """Initialize a new movie with a price strategy."""
        self.title = title

    def get_title(self) -> str:
        """Get the title of the movie."""
        return self.title

    def __str__(self) -> str:
        """Return a string representation of the movie."""
        return self.title
