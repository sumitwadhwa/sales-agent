from pydantic import BaseModel

class ProductQuery(BaseModel):
    keyword: str

class ProductOut(BaseModel):
    product_id: int
    name: str
    description: str

class PriceOut(BaseModel):
    product_id: int
    price: float

