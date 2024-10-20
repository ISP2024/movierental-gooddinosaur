# Demonstrate the movie rental code.
# Create a customer with some movies and print a statement.

from movie import Movie
from rental import Rental
from customer import Customer
from movie_catalog import MovieCatalog


def make_movies():
    """Some sample movies."""
    movies = [
        Movie("Air", Movie.NEW_RELEASE),
        Movie("Oppenheimer", Movie.REGULAR),
        Movie("Frozen", Movie.CHILDRENS),
        Movie("Bitconned", Movie.NEW_RELEASE),
        Movie("Particle Fever", Movie.REGULAR)
    ]
    return movies


if __name__ == '__main__':
    # Create a customer with some rentals
    customer = Customer("Edward Snowden")
    days = 1
    for title in ["Air", "Oppenheimer", "Frozen", "Bitconned",
                  "Particle Fever"]:
        movie = MovieCatalog().get_movie(title)
        if movie:
            rental = Rental(movie, days)
            customer.add_rental(rental)
            days = (days + 2) % 5 + 1
    print(customer.statement())
