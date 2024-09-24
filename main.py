from cli_functions import *
import products
import store


def print_menu(command_dispatcher):
    """
    Displays the menu of available commands in the CLI.
    """
    print(f"   Store Menu\n"
          f"   {10 * "-"}")
    for command_number, command_info in command_dispatcher.items():
        print(f"{command_number}. {command_info['description']}")


def start(store_obj):
    command_dispatcher = {1: {"description": "List all products in store", "function": show_items},
                          2: {"description": "Show total amount in store", "function": show_total_amount},
                          3: {"description": "Make an order", "function": place_an_order},
                          4: {"description": "Quit", "function": None}}

    while True:
        print_menu(command_dispatcher)
        try:
            user_input = int(input("Please choose a number: "))
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
    try:
        product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                        products.Product("Google Pixel 7", price=500, quantity=250)]
        best_buy = store.Store(product_list)
    except ValueError as e:
        print(e)
        return

    start(best_buy)


if __name__ == "__main__":
    main()
