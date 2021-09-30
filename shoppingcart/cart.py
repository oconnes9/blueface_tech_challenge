import typing

from .abc import ShoppingCart
from .product import Product

from currency_converter import CurrencyConverter


class ShoppingCart(ShoppingCart):
    def __init__(self):
        self._items = dict()

    def add_item(self, product_code: str, quantity: int):
        if product_code not in self._items:
            if Product.query.get(product_code):
                self._items[product_code] = quantity
            else:
                raise Exception("This item does not exist!")
        else:
            q = self._items[product_code]
            self._items[product_code] = q + quantity

    def print_receipt(self, currency: str) -> typing.List[str]:
        lines = []
        total = 0

        for item in self._items.items():
            price = self._get_product_price(item[0], currency) * item[1]
            total += price

            price_string = "€%.2f" % price

            lines.append(item[0] + " - " + str(item[1]) + ' - ' + price_string)

        lines.append("Total - " + "€%.2f" % total)

        return lines

    def _get_product_price(self, product_code: str, currency: str) -> float:
        product = Product.query.get(product_code)
        price = product.price
        if not currency == "USD":
            c = CurrencyConverter()
            price = c.convert(price, 'USD', currency)
        return price
