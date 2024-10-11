from abc import ABC, abstractmethod


class PriceStrategy(ABC):
    _instances = {}

    @classmethod
    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super(PriceStrategy, cls).__new__(cls)
            cls._instances[cls] = instance
        return cls._instances[cls]

    @abstractmethod
    def get_price(self, days: int) -> float:
        """The price of this movie rental."""
        pass

    @abstractmethod
    def get_rental_points(self, days: int) -> int:
        """The frequent renter points earned for this rental."""
        pass


class RegularPriceStrategy(PriceStrategy):
    """Pricing strategy for regular movies."""

    def get_price(self, days):
        price = 2
        if days > 2:
            price += (days - 2) * 1.5
        return price

    def get_rental_points(self, days):
        return 1


class NewReleasePriceStrategy(PriceStrategy):
    """Pricing strategy for new release movies."""

    def get_price(self, days):
        return days * 3

    def get_rental_points(self, days):
        return days


class ChildrenPriceStrategy(PriceStrategy):
    """Pricing strategy for children's movies."""

    def get_price(self, days):
        price = 1.5
        if days > 3:
            price += (days - 3) * 1.5
        return price

    def get_rental_points(self, days):
        return 1


# Define instances of the strategies as named constants
NEW_RELEASE = NewReleasePriceStrategy()
REGULAR = RegularPriceStrategy()
CHILDREN = ChildrenPriceStrategy()
