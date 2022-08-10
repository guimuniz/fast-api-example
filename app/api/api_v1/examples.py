import logging

from fastapi import APIRouter

from app.client.client import Client
from app.schemas.examples import Example
from app.schemas.erros import BadGatewayResponse

router = APIRouter(prefix="/examples", tags=["example"])

client = Client()

logger = logging.getLogger(__name__)


@router.get("/")
async def api_example() -> Example:
    try:
        response = await client.root()
    except Exception as error:
        logger.error(f"[root] error: {error}")
        raise BadGatewayResponse(detail=f"{error}")

    return [
        Example(
            name=example["name"],
            symbol=example["symbol"],
        )
        for example in response["examples"]
    ]
