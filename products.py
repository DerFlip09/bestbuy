class Product:
    """
    A class representing a product with name, price, and quantity.

    :param name: Name of the product.
    :param price: Price of the product.
    :param quantity: Quantity of the product in stock.
    :raises ValueError: If any of the input values are invalid.
    """

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = float(price)
        self.quantity = quantity
        self.active = True
        if name == "" or price < 0 or quantity < 0:
            raise ValueError("The product information is wrong. Give valid input.")

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
        if self.quantity + quantity < 0:
            print("There is not enough product in stock!")
        else:
            self.quantity += quantity
            if self.quantity == 0:
                self.active = False
            return True

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
        print(f"{self.name}, Price: {self.price}$, Quantity: {self.quantity}")

    def buy(self, quantity):
        """
        Processes the purchase by reducing stock and calculating total cost.

        :param quantity: Number of items to buy.
        :return: Total price for the purchase.
        :raises ValueError: If not enough items are in stock.
        """
        if not self.set_quantity(-quantity):
            raise ValueError("Not enough items in stock")
        return self.price * quantity

