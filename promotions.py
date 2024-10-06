from abc import ABC, abstractmethod


class Promotion(ABC):
    def __init__(self, name):
        self.member = name

    def __str__(self):
        return self.member

    @abstractmethod
    def apply_promotion(self, product, quantity):
        pass


class SecondHalfPrice(Promotion):
    def apply_promotion(self, product, quantity):
        total_sum = 0
        for count in range(1, quantity + 1):
            if count % 2 == 0:
                total_sum += 0.5 * product.price
            else:
                total_sum += product.price
        return total_sum


class ThirdOneFree(Promotion):
    def apply_promotion(self, product, quantity):
        total_sum = 0
        for count in range(1, quantity + 1):
            if count % 3 == 0:
                pass
            else:
                total_sum += product.price
        return total_sum


class PercentDiscount(Promotion):
    def __init__(self, name, percent):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity):
        disc_multiplier = (self.percent / 100) + 1
        return (product.price * quantity) * disc_multiplier
