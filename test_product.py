import pytest
from products import *


#Test that creating a normal product works.
def test_valid_product():
    assert isinstance(Product("Ipod", price=100, quantity=150), Product)


#Test that creating a product with invalid details (empty name, negative price) invokes an exception.
def test_empty_name():
    with pytest.raises(ValueError, match="Name cannot be empty"):
        Product("", price=100, quantity=150)


def test_wrong_type_name():
    with pytest.raises(TypeError, match=f"Name needs to be a string: int was given"):
        Product(150, price=100, quantity=150)


def test_negative_price():
    with pytest.raises(ValueError, match="Price needs to be positive"):
        Product("Ipod", price=-100, quantity=150)


def test_wrong_type_price():
    with pytest.raises(TypeError, match=f"Price needs to be an integer or a float number: str was given"):
        Product("Ipod", price="Hello", quantity=150)


def test_negative_quantity():
    with pytest.raises(ValueError, match="Quantity needs to be positive"):
        Product("Ipod", price=100, quantity=-150)


def test_wrong_type_quantity():
    with pytest.raises(TypeError, match=f"Quantity needs to be an integer: str was given"):
        Product("Ipod", price=100, quantity="Hello")


#Test that when a product reaches 0 quantity, it becomes inactive.
def test_inactivation():
    ipod = Product("Ipod", price=100, quantity=0)
    assert ipod.is_active() is False
    ipad = Product("Ipad", price=100, quantity=150)
    ipad.set_quantity(0)
    assert ipod.is_active() is False


#Test that product purchase modifies the quantity and returns the right output.
def test_buy_product():
    ipod = Product("Ipod", price=100, quantity=150)
    ipod.buy(100)
    assert ipod.quantity == 50


#Test that buying a larger quantity than exists invokes exception.
def test_buy_too_many_products():
    ipod = Product("Ipod", price=100, quantity=150)
    with pytest.raises(ValueError, match=f"Not enough quantity in stock for {ipod.name}"):
        ipod.buy(200)


if __name__ == '__main__':
    pytest.main()
