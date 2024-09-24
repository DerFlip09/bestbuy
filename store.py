class Store:
    """
    A class representing a store containing multiple products.

    :param products: List of products available in the store.
    """
    def __init__(self, products):
        self.products = products

    def add_product(self, products):
        """
        Adds products to the store inventory.

        :param products: List of products to be added to the store.
        """
        self.products += products

    def remove_product(self, product):
        """
        Removes a product from the store inventory.

        :param product: The product to be removed.
        """
        self.products.remove(product)

    def get_total_quantity(self):
        """
        Calculates the total quantity of all products in the store.

        :return: int, total quantity of items.
        """
        total_quantity = 0
        for product in self.products:
            total_quantity += product.get_quantity()
        return total_quantity

    def get_all_products(self):
        """
        Retrieves all active products (in stock) from the store.

        :return: List of active products.
        """
        active_products = []
        for product in self.products:
            if product.is_active():
                active_products.append(product)
        return active_products

    def order(self, shopping_list):
        """
        Processes an order from a shopping list and calculates the total price.

        :param shopping_list: List of tuples (product, quantity) to purchase.
        :return: Total price of the order or an error if insufficient stock.
        :raises ValueError: If there is not enough stock to fulfill the order.
        """
        total_price = 0
        for product, quantity in shopping_list:
            try:
                total_price += product.buy(quantity)
            except ValueError as e:
                return e
        return total_price
