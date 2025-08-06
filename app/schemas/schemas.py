from pydantic import BaseModel

class ProductSearchRequest(BaseModel):
    keyword: str

class ProductResponse(BaseModel):
    id: int
    name: str
    description: str
    config: str

class PriceResponse(BaseModel):
    product_id: int
    price: float

