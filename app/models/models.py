from sqlalchemy import Column, Integer, String, Float
from app.core.database import Base

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    config = Column(String)

class Pricing(Base):
    __tablename__ = 'pricing'
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer)
    price = Column(Float)

