from pytest import fixture

from app import database
from insert_data import insert_data

@fixture(scope='function')
def test_database():
    """
    Set up the database.
    """
    database.drop_all()
    database.create_all()
    insert_data()
    yield database
    database.drop_all()