from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.models import Pricing

class PricingAgent:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_price(self, product_id: int):
        query = select(Pricing).where(Pricing.product_id == product_id)
        result = await self.db.execute(query)
        return result.scalar_one_or_none()

