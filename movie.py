from price_strategy import NEW_RELEASE, REGULAR, CHILDREN


class Movie:
    """
    A movie available for rent.
    """
    # The types of movies (price_code). 
    REGULAR = 0
    NEW_RELEASE = 1
    CHILDRENS = 2

    def __init__(self, title, price_code):
        # Initialize a new movie. 
        self.title = title
        self.price_code = price_code
        self.price_strategy = self.get_price_strategy()

    def get_price_strategy(self):
        """Select the appropriate price strategy based on the price code."""
        if self.price_code == Movie.NEW_RELEASE:
            return NEW_RELEASE
        elif self.price_code == Movie.REGULAR:
            return REGULAR
        elif self.price_code == Movie.CHILDRENS:
            return CHILDREN
        else:
            raise ValueError(f"Unrecognized price code: {self.price_code}")

    def get_price(self, days_rented):
        """Return the rental price for a given number of rented days."""
        return self.price_strategy.get_price(days_rented)

    def get_rental_points(self, days_rented):
        """Return the rental points for a given number of rented days."""
        return self.price_strategy.get_rental_points(days_rented)

    def get_price_code(self):
        # get the price code
        return self.price_code

    def get_title(self):
        return self.title

    def __str__(self):
        return self.title
