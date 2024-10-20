from movie import Movie


class Rental:
    """
    A rental of a movie by customer.
    From Fowler's refactoring example.

    A realistic Rental would have fields for the dates
    that the movie was rented and returned, from which the
    rental period is calculated.
    For simplicity of this application only days_rented is recorded.
    """

    def __init__(self, movie: Movie, days_rented: int):
        """Initialize a new movie rental object for
           a movie with known rental period (daysRented).
        """
        self.movie = movie
        self.days_rented = days_rented

    def get_movie(self) -> Movie:
        """Return the movie associated with this rental."""
        return self.movie

    def get_days_rented(self) -> int:
        """Return the number of days the movie has been rented."""
        return self.days_rented

    def get_price(self) -> float:
        """Calculate the rental price based on the days rented."""
        return self.movie.price_code.get_price(self.days_rented)

    def get_rental_points(self) -> int:
        """Calculate the frequent renter points for this rental."""
        return self.movie.price_code.get_rental_points(self.days_rented)
