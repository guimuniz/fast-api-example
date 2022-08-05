from fastapi import APIRouter


router = APIRouter(tags=["health"])


@router.get("/healthz")
async def healthz():
    return {"status": "OK"}


@router.get("/readiness")
async def readiness():
    return {"status": "OK"}
