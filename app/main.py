import uvicorn
from fastapi import Depends, FastAPI

from app.api import api_router
from app.core.config import settings
from app.core.security import security_middleware
from app.core.rate_limiter import limiter
from app.core.auth import api_key_validate

app = FastAPI(
    title=settings.PROJECT_NAME,
)
app.state.limiter = limiter

app.include_router(api_router, dependencies=[Depends(api_key_validate)])
app.middleware("http")(security_middleware)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)
