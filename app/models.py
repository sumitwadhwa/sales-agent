from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Product(Base):
    __tablename__ = "products"
    product_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)

class Price(Base):
    __tablename__ = "pricing"
    product_id = Column(Integer, primary_key=True, index=True)
    price = Column(Float)
