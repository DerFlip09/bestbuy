from abc import ABC, abstractmethod


class Promotion(ABC):
    """
    An abstract base class for defining promotions on products.

    :param name: The name of the promotion.
    """

    def __init__(self, name):
        self.member = name

    def __str__(self):
        """Returns the name of the promotion."""
        return self.member

    @abstractmethod
    def apply_promotion(self, product, quantity):
        """
        Abstract method to apply the promotion on a given product.

        :param product: The product to apply the promotion to.
        :param quantity: The quantity of the product being purchased.
        :return: Total price after applying the promotion.
        """
        pass


class SecondHalfPrice(Promotion):
    """
    A promotion that gives a second item at half price for every pair purchased.

    :param name: The name of the promotion (inherited from Promotion).
    """

    def apply_promotion(self, product, quantity):
        """
        Calculates the total price with the second item at half price.

        :param product: The product to apply the promotion to.
        :param quantity: The quantity of the product being purchased.
        :return: Total price after applying the second half price promotion.
        """
        total_sum = 0
        for count in range(1, quantity + 1):
            if count % 2 == 0:
                total_sum += 0.5 * product.price
            else:
                total_sum += product.price
        return total_sum


class ThirdOneFree(Promotion):
    """
    A promotion that offers one free item for every three purchased.

    :param name: The name of the promotion (inherited from Promotion).
    """

    def apply_promotion(self, product, quantity):
        """
        Calculates the total price with every third item free.

        :param product: The product to apply the promotion to.
        :param quantity: The quantity of the product being purchased.
        :return: Total price after applying the third item free promotion.
        """
        total_sum = 0
        for count in range(1, quantity + 1):
            if count % 3 == 0:
                pass  # No charge for every third item
            else:
                total_sum += product.price
        return total_sum


class PercentDiscount(Promotion):
    """
    A promotion that offers a percentage discount on the product price.

    :param name: The name of the promotion (inherited from Promotion).
    :param percent: The discount percentage to be applied.
    """

    def __init__(self, name, percent):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity):
        """
        Calculates the total price with a percentage discount applied.

        :param product: The product to apply the promotion to.
        :param quantity: The quantity of the product being purchased.
        :return: Total price after applying the percentage discount promotion.
        """
        disc_multiplier = (self.percent / 100) + 1
        return (product.price * quantity) * disc_multiplier
