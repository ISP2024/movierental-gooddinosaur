import re
import unittest
from customer import Customer
from rental import Rental
from movie_catalog import MovieCatalog


class CustomerTest(unittest.TestCase):
    """ Tests of the Customer class"""

    def setUp(self):
        """Test fixture contains:

        c = a customer
        movies = list of some movies
        """
        self.c = Customer("Movie Mogul")
        self.new_movie = MovieCatalog().get_movie("Dune: Part Two")
        self.regular_movie = MovieCatalog().get_movie("The Batman")
        self.childrens_movie = MovieCatalog().get_movie("Turning Red")
        print(self.new_movie.genre)

    def test_total_charge_no_rentals(self):
        """Test total charge with no rentals."""
        self.assertEqual(self.c.total_charge(), 0.00)

    def test_total_charge_with_rentals(self):
        """Test total charge with multiple rentals."""
        self.c.add_rental(Rental(self.new_movie, 3))
        self.c.add_rental(Rental(self.regular_movie, 4))
        self.c.add_rental(Rental(self.childrens_movie, 5))

        expected_total = 9.00 + 5.0 + 4.50
        self.assertEqual(self.c.total_charge(), expected_total)

    def test_total_rental_points_no_rentals(self):
        """Test total rental points with no rentals."""
        self.assertEqual(self.c.total_rental_points(), 0)

    def test_total_rental_points_with_rentals(self):
        """Test total rental points with multiple rentals."""
        self.c.add_rental(Rental(self.new_movie, 3))
        self.c.add_rental(Rental(self.regular_movie, 4))
        self.c.add_rental(Rental(self.childrens_movie, 5))

        expected_points = 3 + 1 + 1
        self.assertEqual(self.c.total_rental_points(), expected_points)

    def test_statement(self):
        stmt = self.c.statement()
        # get total charges from statement using a regex
        pattern = r".*Total [Cc]harges\s+(\d+\.\d\d).*"
        matches = re.match(pattern, stmt, flags=re.DOTALL)
        self.assertIsNotNone(matches)
        self.assertEqual("0.00", matches[1])
        # add a rental
        self.c.add_rental(Rental(self.new_movie, 4))  # days
        stmt = self.c.statement()
        matches = re.match(pattern, stmt.replace('\n', ''), flags=re.DOTALL)
        self.assertIsNotNone(matches)
        self.assertEqual("12.00", matches[1])
