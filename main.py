from cli_functions import *
import products
import store
import promotions


def print_menu(command_dispatcher):
    """
    Prints the store menu using the command dispatcher.

    :param command_dispatcher: Dictionary mapping command numbers to their descriptions and functions.
    """
    print(f"   Store Menu\n"
          f"   {10 * '-'}")
    for command_number, command_info in command_dispatcher.items():
        print(f"{command_number}. {command_info['description']}")


def start(store_obj):
    """
    Main loop for the store program, handling user input and executing corresponding functions.

    :param store_obj: Store object containing products.
    """
    command_dispatcher = {1: {"description": "List all products in store", "function": show_items},
                          2: {"description": "Show total amount in store", "function": show_total_amount},
                          3: {"description": "Make an order", "function": place_an_order},
                          4: {"description": "Quit", "function": None}}

    while True:
        print_menu(command_dispatcher)
        try:
            user_input = int(input("Please choose a number: ").strip())
        except ValueError:
            print("Please enter a number!")
            continue
        if user_input == 4:
            break
        elif 1 <= user_input <= 3:
            command_dispatcher[user_input]["function"](store_obj)
        else:
            print("Please choose a number from the menu!")


def main():
    """
    Initializes the product list and store, then starts the store interface.
    """
    try:
        # setup initial stock of inventory
        product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                        products.Product("Google Pixel 7", price=500, quantity=250),
                        products.NonStockedProduct("Windows License", price=125),
                        products.LimitedProduct("Shipping", price=10, quantity=250, limit=1)
                        ]

        # Create promotion catalog
        second_half_price = promotions.SecondHalfPrice("Second Half price!")
        third_one_free = promotions.ThirdOneFree("Third One Free!")
        thirty_percent = promotions.PercentDiscount("30% off!", percent=30)

        # Add promotions to products
        product_list[0].set_promotion(second_half_price)
        product_list[1].set_promotion(third_one_free)
        product_list[3].set_promotion(thirty_percent)
        best_buy = store.Store(product_list)
    except (ValueError, TypeError) as e:
        print(e)
        return

    start(best_buy)


if __name__ == "__main__":
    main()
