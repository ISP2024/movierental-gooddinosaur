import unittest
from movie_catalog import MovieCatalog
from rental import Rental


class RentalTest(unittest.TestCase):
    """Test cases for the Rental class."""
    def setUp(self):
        """Set up a MovieCatalog instance and sample movies for testing."""
        self.new_movie = MovieCatalog().get_movie("Dune: Part Two")
        self.regular_movie = MovieCatalog().get_movie("The Batman")
        self.childrens_movie = MovieCatalog().get_movie("Turning Red")

    def test_rental_price(self):
        """Test that the rental price is calculated correctly."""
        rental = Rental(self.new_movie, 1)
        self.assertEqual(rental.get_price(), 3.0)
        rental = Rental(self.new_movie, 5)
        self.assertEqual(rental.get_price(), 15.0)

        rental = Rental(self.regular_movie, 2)
        self.assertEqual(rental.get_price(), 2.0)
        rental = Rental(self.regular_movie, 5)
        self.assertEqual(rental.get_price(), 6.5)

        rental = Rental(self.childrens_movie, 3)
        self.assertEqual(rental.get_price(), 1.5)
        rental = Rental(self.childrens_movie, 5)
        self.assertEqual(rental.get_price(), 4.5)

    def test_rental_points(self):
        """Test that frequent renter points are computed correctly."""
        rental = Rental(self.new_movie, 1)
        self.assertEqual(rental.get_rental_points(), 1)
        rental = Rental(self.new_movie, 5)
        self.assertEqual(rental.get_rental_points(), 5)

        rental = Rental(self.regular_movie, 1)
        self.assertEqual(rental.get_rental_points(), 1)
        rental = Rental(self.regular_movie, 3)
        self.assertEqual(rental.get_rental_points(), 1)

        rental = Rental(self.childrens_movie, 1)
        self.assertEqual(rental.get_rental_points(), 1)
        rental = Rental(self.childrens_movie, 5)
        self.assertEqual(rental.get_rental_points(), 1)
