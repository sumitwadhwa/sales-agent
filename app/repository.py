from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from .models import Product, Price

async def fetch_products_by_keyword(session: AsyncSession, keyword: str):
    result = await session.execute(select(Product).filter(Product.name.ilike(f"%{keyword}%")))
    return result.scalars().all()

async def fetch_price_by_product_id(session: AsyncSession, product_id: int):
    result = await session.execute(select(Price).filter(Price.product_id == product_id))
    return result.scalar_one_or_none()
