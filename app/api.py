from fastapi import APIRouter, Depends
from . import schemas, service, config
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()

@router.post("/search", response_model=list[schemas.ProductOut])
async def search_products(query: schemas.ProductQuery, db: AsyncSession = Depends(config.get_db)):
    return await service.get_products(db, query.keyword)

@router.get("/price/{product_id}", response_model=schemas.PriceOut)
async def get_price(product_id: int, db: AsyncSession = Depends(config.get_db)):
    return await service.get_price(db, product_id)
