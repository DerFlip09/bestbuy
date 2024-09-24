def show_items(store_obj):
    """
    Displays all products in the store.

    :param store_obj: Store object containing products.
    """
    products_list = store_obj.get_all_products()
    item_number = 1
    print(8 * "-")
    for product in products_list:
        print(f"{item_number}. ", end="")
        product.show()
        item_number += 1
    print(8 * "-")


def show_total_amount(store_obj):
    """
    Shows the total number of items in the store.

    :param store_obj: Store object containing products.
    """
    print(8 * "-")
    print(f"Total of {store_obj.get_total_quantity()} items in store")
    print(8 * "-")


def place_an_order(store_obj):
    """
    Handles the process of placing an order by selecting products and quantities.

    :param store_obj: Store object containing products.
    """
    show_items(store_obj)
    products_list = store_obj.get_all_products()
    order_list = []
    print("When you want to finish your order, enter empty text")
    while True:
        user_item_choice = input("Which product # do you want? ").strip()
        if not user_item_choice:
            break
        elif int(user_item_choice) > len(products_list):
            print("Error, product number is not in store!")
            continue
        user_quantity = input("What amount do you want? ").strip()
        if not user_quantity:
            break
        else:
            product = products_list[int(user_item_choice) - 1]
            quantity = int(user_quantity)
            if product.get_quantity() < quantity:
                print("There is not enough items in stock!")
                continue
            order_list.append((product, quantity))
            print("Product added to list!\n")
    print(order_list)
    total_sum = store_obj.order(order_list)
    print(f"{8 * '*'}\nOrder made! Total payment: {total_sum}")
