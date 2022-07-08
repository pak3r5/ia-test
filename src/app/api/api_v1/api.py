
from fastapi import APIRouter
from app.api.api_v1.endpoints import product, user, order

api_router = APIRouter()
api_router.include_router(product.router, prefix='/api/v1/products', tags=['Products'])
api_router.include_router(user.router, prefix='/api/v1/users', tags=['Users'])
api_router.include_router(order.router, prefix='/api/v1/orders', tags=['Orders'])

