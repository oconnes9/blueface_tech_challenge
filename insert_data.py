from app import database
from shoppingcart.product import Product

def insert_data():
    """
    Insert sample data
    """

    database.session.bulk_save_objects(
        [
            Product(name='Apple', price=1.0),
            Product(name='Banana', price=1.1),
            Product(name='Kiwi', price=3.0),
            Product(name='Bread', price=4.0),
            Product(name='Milk', price=1.5)
        ]
    )

    database.session.commit()