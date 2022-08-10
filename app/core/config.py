from pydantic import BaseSettings


class Settings(BaseSettings):
    API_STR: str = "/api"
    API_V1_STR: str = "/v1"
    PROJECT_NAME: str = "Example API"
    BASE_URL: str
    API_KEY: str
    SECRET_KEY: str
    PASSPHRASE: str


settings = Settings()
