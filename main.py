# Demonstrate the movie rental code.
# Create a customer with some movies and print a statement.

from movie import Movie
from rental import Rental
from customer import Customer
from price_strategy import *


def make_movies():
    """Some sample movies."""
    movies = [
        Movie("Air"),
        Movie("Oppenheimer"),
        Movie("Frozen"),
        Movie("Bitconned"),
        Movie("Particle Fever")
    ]
    return movies


if __name__ == '__main__':
    # Create a customer with some rentals
    customer = Customer("Edward Snowden")
    days = 1
    movie_types = [NEW_RELEASE, REGULAR, CHILDREN, NEW_RELEASE, REGULAR]
    movies = make_movies()
    for i in range(len(movies)):
        customer.add_rental(Rental(movies[i], days, movie_types[i]))
        days = (days + 2) % 5 + 1
    print(customer.statement())
