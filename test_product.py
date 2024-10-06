import pytest
from products import *
from promotions import *
from store import *


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
    assert not ipod.is_active
    ipad = Product("Ipad", price=100, quantity=150)
    assert ipad.is_active
    ipad.quantity = 0
    assert not ipod.is_active


#Test that product purchase modifies the quantity and returns the right output.
def test_buy_product():
    ipod = Product("Ipod", price=100, quantity=150)
    ipod.buy(100)
    assert ipod._quantity == 50


#Test that buying a larger quantity than exists invokes exception.
def test_buy_too_many_products():
    ipod = Product("Ipod", price=100, quantity=150)
    with pytest.raises(ValueError, match=f"Not enough quantity in stock for {ipod._name}"):
        ipod.buy(200)

def test_buy_nonstockproduct():
    windows = NonStockedProduct("Windows Licence", price=150)
    assert windows.buy(100) == 15000

def test_buy_limitedproduct():
    shipping = LimitedProduct("Shipping", price=10, quantity=20, limit=1)
    assert shipping.buy(1) == 10

def test_buy_out_of_limit():
    shipping = LimitedProduct("Shipping", price=10, quantity=20, limit=1)
    with pytest.raises(ValueError, match="Quantity needs to be "):
        shipping.buy(2)

def test_apply_promotion():
    ipod = Product("Ipod", price=100, quantity=150)
    second_for_half = SecondHalfPrice("Second for half!")
    ipod.promotion = second_for_half
    assert isinstance(ipod.promotion, Promotion)

def test_if_product_in_store():
    ipod = Product("Ipod", price=100, quantity=150)
    best_buy = Store([ipod])
    assert ipod in best_buy

def test_lower_than():
    ipod = Product("Ipod", price=100, quantity=150)
    ipad = Product("Ipod", price=150, quantity=150)
    assert ipod < ipad

def test_greater_than():
    ipod = Product("Ipod", price=100, quantity=150)
    ipad = Product("Ipod", price=150, quantity=150)
    assert ipad > ipod

if __name__ == '__main__':
    pytest.main()
