import unittest
from pricing import price_code_for_movie
from movie import Movie
from price_strategy import NEW_RELEASE, REGULAR, CHILDREN


class TestPricing(unittest.TestCase):

    def test_new_release(self):
        movie = Movie("Top Gun: Maverick", 2024, ["Action"])
        self.assertEqual(price_code_for_movie(movie), NEW_RELEASE)

    def test_children_movie(self):
        movie = Movie("Toy Story", 1995, ["Children"])
        self.assertEqual(price_code_for_movie(movie), CHILDREN)

    def test_regular_movie(self):
        movie = Movie("The Godfather", 1972, ["Drama"])
        self.assertEqual(price_code_for_movie(movie), REGULAR)

    def test_childrens_with_plural(self):
        movie = Movie("Frozen", 2013, ["Childrens"])
        self.assertEqual(price_code_for_movie(movie), CHILDREN)

    def test_children_with_mixed_case(self):
        movie = Movie("The Lion King", 1994, ["cHiLdReN"])
        self.assertEqual(price_code_for_movie(movie), CHILDREN)

    def test_childrens_with_mixed_case(self):
        movie = Movie("The Lion King", 1994, ["cHiLdReNs"])
        self.assertEqual(price_code_for_movie(movie), CHILDREN)


if __name__ == "__main__":
    unittest.main()
