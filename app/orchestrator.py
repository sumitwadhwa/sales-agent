from app.agents.search_agent import SearchAgent
from app.agents.pricing_agent import PricingAgent

class SalesOrchestrator:
    def __init__(self, db):
        self.db = db

    async def run_search(self, keyword: str):
        return await SearchAgent(self.db).search(keyword)

    async def run_pricing(self, product_id: int):
        return await PricingAgent(self.db).get_price(product_id)

