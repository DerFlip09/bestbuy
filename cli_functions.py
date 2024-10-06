def show_items(store_obj):
    """
    Displays all products in the store.

    :param store_obj: Store object containing products.
    :type store_obj: Store
    """
    products_list = store_obj.all_products
    item_number = 1
    print(8 * "-")
    for product in products_list:
        print(f"{item_number}. {product}")
        item_number += 1
    print(8 * "-")


def show_total_amount(store_obj):
    """
    Shows the total number of items in the store.

    :param store_obj: Store object containing products.
    :type store_obj: Store
    """
    print(8 * "-")
    print(f"Total of {store_obj.total_quantity} items in store")
    print(8 * "-")


def ask_for_number(text):
    """
    Prompts the user for input and converts it to an integer.

    :param text: The prompt text to display to the user.
    :type text: str
    :return: Integer value input by the user or None if no input is given.
    :rtype: int or None
    """
    user_input = input(text)
    if not user_input:
        return None
    try:
        return int(user_input)
    except ValueError:
        print("Please enter a Number!")


def ask_order_item(number_of_products):
    """
    Asks the user to select a product and its quantity for the order.

    :param number_of_products: The total number of products available.
    :type number_of_products: int
    :return: A tuple containing the selected product index and quantity.
    :rtype: tuple(int, int) or (None, None)
    """
    while True:
        user_item_choice = ask_for_number("Which product # do you want? ")
        if user_item_choice is None:
            return None, None
        if 1 <= user_item_choice <= number_of_products:
            user_item_choice -= 1
            break
        print(f"Not found product with index {user_item_choice}")

    while True:
        user_quantity = ask_for_number("What amount do you want? ")
        if user_quantity is None or user_quantity >= 0:
            break
        print("Amount must be a positive Number!")
    return user_item_choice, user_quantity


def get_order_list(products_list):
    """
    Collects a list of ordered items from the user.

    :param products_list: List of available products in the store.
    :type products_list: list
    :return: List of tuples containing products and their ordered quantities.
    :rtype: list[tuple(Product, int)]
    """
    order_list = []
    while True:
        item_number, order_quantity = ask_order_item(len(products_list))
        if item_number is None or order_quantity is None:
            break
        order_list.append((products_list[item_number], order_quantity))
        print("Product added to list!\n")
    return order_list


def print_shopping_cart(order_list):
    """
    Displays the contents of the shopping cart.

    :param order_list: List of ordered items.
    :type order_list: list[tuple(Product, int)]
    """
    controlled_items = []
    complete_order_list = []
    for product, _ in order_list:
        if product not in controlled_items:
            quantity = sum(quant for prod, quant in
                           order_list if prod == product)
            controlled_items.append(product)
            complete_order_list.append((product, quantity))
    shopping_cart = "\n".join(f"{i + 1}. {product.name}, Price: {product.price}, "
                              f"Quantity: {quantity}" for i, (product, quantity) in
                              enumerate(complete_order_list))
    shopping_cart = shopping_cart or "Empty"
    print("*" * 8, "\n", "Your shopping cart:", shopping_cart)


def is_ordering_finished(order_list):
    """
    Checks if the user wants to continue ordering or finish.

    :param order_list: List of ordered items.
    :type order_list: list[tuple(Product, int)]
    :return: True if ordering is finished; False otherwise.
    :rtype: bool
    """
    print_shopping_cart(order_list)
    while True:
        confirmation = input("Do you want to continue (Yes or No/empty)? ")
        if confirmation.lower() == "yes":
            return False
        elif confirmation.lower() == "no" or not confirmation:
            return True
        else:
            print("Please confirm with yes or no/empty")


def place_an_order(store_obj):
    """
    Handles the process of placing an order by selecting products and quantities.

    :param store_obj: Store object containing products.
    :type store_obj: Store
    """
    products_list = store_obj.all_products
    order_list = []

    show_items(store_obj)
    print("When you want to finish your order, enter empty text")
    while True:
        order_list += get_order_list(products_list)
        if is_ordering_finished(order_list):
            break
    if order_list:
        try:
            total_sum = store_obj.order(order_list)
            print(f"{8 * '*'}\nOrder made! Total payment: {total_sum}")
        except (ValueError, TypeError) as e:
            print(f"There was an Error while processing your order: {e}")
            input("Press enter to continue...")
    else:
        print("Thanks for nothing")

