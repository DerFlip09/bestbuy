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
        self.name = name
        self.price = float(price)
        self.active = True
        self.set_quantity(quantity)

    def get_quantity(self):
        """
        Returns the current quantity of the product.

        :return: int, quantity of product.
        """
        return self.quantity

    def set_quantity(self, quantity):
        """
        Updates the product quantity and deactivates the product if quantity reaches 0.

        :param quantity: Quantity to add/subtract from the current stock.
        :return: True if the quantity was updated, False if not enough in stock.
        """
        if not isinstance(quantity, int):
            raise TypeError(f"Quantity needs to be an integer: {type(quantity).__name__} was given")
        if quantity < 0:
            raise ValueError("Quantity needs to be positive")

        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self):
        """
        Checks if the product is active (i.e., in stock).

        :return: bool, True if active, False otherwise.
        """
        return self.active

    def activate(self):
        """
        Activates the product, marking it as in stock.
        """
        self.active = True

    def deactivate(self):
        """
        Deactivates the product, marking it as out of stock.
        """
        self.active = False

    def show(self):
        """
        Displays product details including name, price, and quantity.
        """
        return f"{self.name}, Price: {self.price}$, Quantity: {self.quantity}"

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
        if not self.is_active():
            raise TypeError(f"Product {self.name} is not active")
        if quantity > self.quantity:
            raise ValueError(f"Not enough quantity in stock for {self.name}")

        total_price = self.price * quantity
        self.set_quantity(self.quantity - quantity)
        return total_price
