from . import repository
from sqlalchemy.ext.asyncio import AsyncSession

async def get_products(session: AsyncSession, keyword: str):
    return await repository.fetch_products_by_keyword(session, keyword)

async def get_price(session: AsyncSession, product_id: int):
    return await repository.fetch_price_by_product_id(session, product_id)
