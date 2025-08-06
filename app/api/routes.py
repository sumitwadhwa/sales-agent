from fastapi import APIRouter, Depends
from app.core.database import get_db
from app.schemas.schemas import ProductSearchRequest, ProductResponse, PriceResponse
from app.orchestrator import SalesOrchestrator

router = APIRouter()

@router.post("/search", response_model=list[ProductResponse])
async def search_products(payload: ProductSearchRequest, db=Depends(get_db)):
    orchestrator = SalesOrchestrator(db)
    return await orchestrator.run_search(payload.keyword)

@router.get("/price/{product_id}", response_model=PriceResponse)
async def get_price(product_id: int, db=Depends(get_db)):
    orchestrator = SalesOrchestrator(db)
    result = await orchestrator.run_pricing(product_id)
    if result:
        return {"product_id": product_id, "price": result.price}
    return {"product_id": product_id, "price": 0.0}

