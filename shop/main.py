from typing import List, Any

from fastapi import FastAPI, Depends, HTTPException

from shop.api import api_router

app = FastAPI()

app.include_router(api_router)
