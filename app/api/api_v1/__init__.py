from fastapi import APIRouter

from app.api.api_v1 import healthz, examples
from app.core.config import settings

api_v1_router = APIRouter(prefix=settings.API_V1_STR)
api_v1_router.include_router(healthz.router)
api_v1_router.include_router(examples.router)
