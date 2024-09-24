import products
import store


# setup initial stock of inventory
product_list = [ products.Product("MacBook Air M2", price=1450, quantity=100),
                 products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 products.Product("Google Pixel 7", price=500, quantity=250)
               ]

best_buy = store.Store(product_list)

def start(store_obj):
    print(f"   Store Menu\n"
          f"   {10 * "-"}\n"
          f"1. List all products in store\n"
          f"2. Show total amount in store\n"
          f"3. Make an order\n"
          f"4. Quit")
    user_input = int(input("Please choose a number: "))

