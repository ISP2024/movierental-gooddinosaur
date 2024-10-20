from price_strategy import PriceStrategy, NEW_RELEASE, REGULAR, CHILDREN


class Movie:
    """
    A movie available for rent.
    """
    # The types of movies (price_code). 
    NEW_RELEASE = NEW_RELEASE
    REGULAR = REGULAR
    CHILDRENS = CHILDREN

    def __init__(self, title: str, price_code: PriceStrategy):
        """Initialize a new movie with a price strategy."""
        self.title = title
        self.price_code = price_code

    def get_price_code(self) -> PriceStrategy:
        """Get the price code of the movie (the price strategy)."""
        return self.price_code

    def get_title(self) -> str:
        """Get the title of the movie."""
        return self.title

    def __str__(self) -> str:
        """Return a string representation of the movie."""
        return self.title
