from promotions import *


class Product:
    """
    A class representing a product with name, price, and quantity.

    :param name: Name of the product.
    :param price: Price of the product.
    :param quantity: Quantity of the product in stock.
    :raises ValueError: If any of the input values are invalid.
    """

    def __init__(self, name, price, quantity):

        # Error handling name
        if not isinstance(name, str):
            raise TypeError(f"Name needs to be a string: {type(name).__name__} was given")
        if not name.strip():
            raise ValueError("Name cannot be empty")

        # Error handling price
        if not isinstance(price, (float, int)):
            raise TypeError(f"Price needs to be an integer or a float number: {type(price).__name__} was given")
        if price < 0:
            raise ValueError("Price needs to be positive")

        # Error handling quantity
        if not isinstance(quantity, int):
            raise TypeError(f"Quantity needs to be an integer: {type(quantity).__name__} was given")
        if quantity < 0:
            raise ValueError("Quantity needs to be positive")

        # Instance Variables
        self._name = name
        self._price = float(price)
        self._active = True
        self._member = None
        self.quantity = quantity

    def __lt__(self, product):
        return self._price < product.price

    def __gt__(self, product):
        return self._price > product.price

    def __ge__(self, product):
        return self._price >= product.price

    def __le__(self, product):
        return self._price <= product.price

    def __eq__(self, product):
        return self._price == product.price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if not isinstance(price, (int, float)):
            raise TypeError(f"Price needs to be an integer or a float number: {type(price).__name__} was given")
        if price < 0:
            raise ValueError("Price needs to be positive")

        self._price = price

    @property
    def name(self):
        return self._name

    @property
    def quantity(self):
        """
        Returns the current quantity of the product.

        :return: int, quantity of product.
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """
        Updates the product quantity and deactivates the product if quantity reaches 0.

        :param quantity: Quantity to add/subtract from the current stock.
        :return: True if the quantity was updated, False if not enough in stock.
        """
        if not isinstance(quantity, int):
            raise TypeError(f"Quantity needs to be an integer: {type(quantity).__name__} was given")
        if quantity < 0:
            raise ValueError("Quantity needs to be positive")

        self._quantity = quantity
        if self._quantity == 0:
            self.deactivate()

    @property
    def is_active(self):
        """
        Checks if the product is active (i.e., in stock).

        :return: bool, True if active, False otherwise.
        """
        return self._active

    def activate(self):
        """
        Activates the product, marking it as in stock.
        """
        self._active = True

    def deactivate(self):
        """
        Deactivates the product, marking it as out of stock.
        """
        self._active = False

    @property
    def promotion(self):
        return self._member

    @promotion.setter
    def promotion(self, promotion):
        if not isinstance(promotion, Promotion):
            raise TypeError(f"Promotion needs to be an Instance form class Promotion: "
                            f"{type(promotion).__name__} was given")
        self._member = promotion

    def __str__(self):
        """
        Displays product details including name, price, and quantity.
        """
        return f"{self._name}, Price: {self._price}$, Quantity: {self._quantity}, Promotion: {self._member}"

    def buy(self, quantity):
        """
        Processes the purchase by reducing stock and calculating total cost.

        :param quantity: Number of items to buy.
        :return: Total price for the purchase.
        :raises ValueError: If not enough items are in stock.
        """
        if not isinstance(quantity, int):
            raise TypeError(f"Quantity needs to be an integer: {type(quantity).__name__} was given")
        if quantity < 0:
            raise ValueError("Quantity needs to be positive")
        if not self.is_active:
            raise TypeError(f"Product {self._name} is not active")
        if quantity > self._quantity:
            raise ValueError(f"Not enough quantity in stock for {self._name}")
        if self._member is not None:
            total_price = self._member.apply_promotion(product=self, quantity=quantity)
            self._quantity -= quantity
            return total_price

        total_price = self._price * quantity
        self._quantity -= quantity
        return total_price


class NonStockedProduct(Product):
    def __init__(self, name, price):
        super().__init__(name, price, quantity=0)
        self._active = True

    def __str__(self):
        """
        Displays product details including name, price, and quantity.
        """
        return f"{self._name}, Price: {self._price}$, Promotion: {self._member}"

    def buy(self, quantity):
        if not isinstance(quantity, int):
            raise TypeError(f"Quantity needs to be an integer: {type(quantity).__name__} was given")
        if quantity < 0:
            raise ValueError("Quantity needs to be positive")
        if self._member is not None:
            total_price = self._member.apply_promotion(product=self, quantity=quantity)
            return total_price

        total_price = self._price * quantity
        return total_price


class LimitedProduct(Product):
    def __init__(self, name, price, quantity, limit):
        super().__init__(name, price, quantity)
        if not isinstance(limit, int):
            raise TypeError(f"Limit needs to be an integer: {type(limit).__name__} was given")
        if limit < 0:
            raise ValueError("Limit needs to be positive")
        self._limit = limit

    @property
    def limit(self):
        return self._limit

    @limit.setter
    def limit(self, limit):
        if not isinstance(limit, int):
            raise TypeError(f"Limit needs to be an integer: {type(limit).__name__} was given")
        if limit < 0:
            raise ValueError("Limit needs to be positive")
        self._limit = limit

    def buy(self, quantity):
        if not isinstance(quantity, int):
            raise TypeError(f"Quantity needs to be an integer: {type(quantity).__name__} was given")
        if quantity < 0:
            raise ValueError("Quantity needs to be positive")
        if self._limit < quantity:
            raise ValueError(f"Quantity needs to be in range of the Limit ({self._limit})")
        if self._member is not None:
            total_price = self._member.apply_promotion(product=self, quantity=quantity)
            self.quantity -= quantity
            return total_price

        total_price = self._price * quantity
        self.quantity -= quantity
        return total_price
