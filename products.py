class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = float(price)
        self.quantity = quantity
        self.active = True
        if name == "" or price < 0 or quantity < 0:
            raise ValueError("The product information is wrong. Give valid input.")

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        if self.quantity + quantity < 0:
            raise ValueError("There is not enough product in stock!")
        else:
            self.quantity += quantity
            if self.quantity == 0:
                self.active = False

    def is_active(self):
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        print(f"{self.name}, Price: {self.price}$, Quantity: {self.quantity}")

    def buy(self, quantity):
        try:
            self.set_quantity(-quantity)
        except ValueError as e:
            print(e)
        return self.price * quantity