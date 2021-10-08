from fastapi import APIRouter
from shop.api import auth, users, orders, items

api_router = APIRouter()

api_router.include_router(auth.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(orders.router, prefix="/orders", tags=["orders"])
api_router.include_router(items.router, prefix="/items", tags=["items"])
