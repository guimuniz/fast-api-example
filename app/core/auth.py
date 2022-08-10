from fastapi import Security
from fastapi.security.api_key import APIKeyHeader

from app.core.config import Settings
from app.schemas.erros import UnauthorizedErrorResponse

settings = Settings()


api_key_header = APIKeyHeader(name="API_KEY", auto_error=False)


async def api_key_validate(api_key: str = Security(api_key_header)):
    if api_key != settings.API_KEY:
        raise UnauthorizedErrorResponse()
