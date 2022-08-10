from pydantic import BaseModel


class Example(BaseModel):
    name: str
    symbol: str
