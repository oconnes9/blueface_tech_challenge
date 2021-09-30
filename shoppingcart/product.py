from app import database
from sqlalchemy import Column, Text, Float


class Product(database.Model):
    name = Column(Text, primary_key=True)
    price = Column(Float, nullable=False)