from products import Product, NonStockedProduct


class Store:
    """
    A class representing a store containing multiple products.

    :param products: List of products available in the store.
    """

    def __init__(self, products):

        if not isinstance(products, list):
            raise TypeError(f"Expected products is a list of Product instances: {type(products).__name__} was given")
        if not all(isinstance(product, Product) for product in products):
            raise TypeError("Every product in products needs to be an instance of Product")

        self._products = products

    def __contains__(self, product):
        return product in self._products

    def __add__(self, store):
        return Store(self._products + store.all_products)

    def add_product(self, products):
        """
        Adds products to the store inventory.

        :param products: List of products to be added to the store.
        """
        self._products += products

    def remove_product(self, product):
        """
        Removes a product from the store inventory.

        :param product: The product to be removed.
        """
        self._products.remove(product)

    @property
    def total_quantity(self):
        """
        Calculates the total quantity of all products in the store.

        :return: int, total quantity of items.
        """
        total_quantity = 0
        for product in self._products:
            total_quantity += product.quantity
        return total_quantity

    @property
    def all_products(self):
        """
        Retrieves all active products (in stock) from the store.

        :return: List of active products.
        """
        active_products = []
        for product in self._products:
            if product.is_active:
                active_products.append(product)
        return active_products

    def order(self, shopping_list):
        """
        Processes an order from a shopping list and calculates the total price.

        :param shopping_list: List of tuples (product, quantity) to purchase.
        :return: Total price of the order or an error if insufficient stock.
        :raises ValueError: If there is not enough stock to fulfill the order.
        """
        for product, _ in shopping_list:
            if product not in self._products:
                raise ValueError(f"{product.name} not in store")
            if not product.is_active:
                raise ValueError(f"{product.name} is not active in the store")

            quantity = sum(quant for prod, quant in shopping_list if prod == product)
            if quantity > product.quantity and not isinstance(product, NonStockedProduct):
                raise ValueError(f"Quantity of purchase to high for {product.name}")

        total_price = 0
        for product, quantity in shopping_list:
            total_price += product.buy(quantity)
        return total_price
