from fastapi import Security
from fastapi.security.api_key import APIKeyHeader

from app.core.exceptions import NotAuthorizedException
from app.core.config import Settings

settings = Settings()


api_key_header = APIKeyHeader(name="API_KEY", auto_error=False)


async def api_key_validate(api_key: str = Security(api_key_header)):
    if api_key != settings.API_KEY:
        raise NotAuthorizedException()
