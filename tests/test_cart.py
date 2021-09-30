import pytest

from shoppingcart.cart import ShoppingCart

from currency_converter import CurrencyConverter


def test_add_item(test_database):
    cart = ShoppingCart()
    cart.add_item("Apple", 1)

    assert len(cart._items.items()) == 1
    assert ("Apple", 1) in cart._items.items()


def test_add_item_with_multiple_quantity(test_database):
    cart = ShoppingCart()
    cart.add_item("Apple", 2)

    assert len(cart._items.items()) == 1
    assert ("Apple", 2) in cart._items.items()


def test_add_different_items(test_database):
    cart = ShoppingCart()
    cart.add_item("Banana", 1)
    cart.add_item("Kiwi", 1)

    assert len(cart._items.items()) == 2
    assert ("Banana", 1) in cart._items.items()
    assert ("Kiwi", 1) in cart._items.items()


def test_print_receipt_one_item(test_database):
    cart = ShoppingCart()
    cart.add_item("Apple", 1)

    receipt = cart.print_receipt('USD')

    assert len(receipt) == 2
    assert receipt[0] == "Apple - 1 - €1.00"
    assert receipt[1] == "Total - €1.00"


def test_print_receipt_multiple_items(test_database):
    cart = ShoppingCart()
    cart.add_item("Apple", 2)
    cart.add_item("Kiwi", 1)

    receipt = cart.print_receipt('USD')

    assert len(receipt) == 3
    assert receipt[0] == "Apple - 2 - €2.00"
    assert receipt[1] == "Kiwi - 1 - €3.00"
    assert receipt[2] == "Total - €5.00"


def test_different_currency(test_database):
    cart = ShoppingCart()
    cart.add_item("Banana", 1)
    cart.add_item("Kiwi", 1)

    receipt = cart.print_receipt('EUR')

    c = CurrencyConverter()
    converted = c.convert(4.10, 'USD', 'EUR')
    price = "€%.2f" % converted

    assert receipt[2] == f"Total - {price}"


def test_item_does_not_exist(test_database):
    cart = ShoppingCart()

    with pytest.raises(Exception) as v:
        cart.add_item("Strawberries", 1)

    assert str(v.value) == "This item does not exist!"