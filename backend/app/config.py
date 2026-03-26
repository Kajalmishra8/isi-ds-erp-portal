# app/config.py
from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str = 'HS256'
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    APP_NAME: str = 'ERP Portal'
    DEBUG: bool = False

    class Config:
        env_file = '.env'

@lru_cache()
def get_settings() -> Settings:
    return Settings()

settings = get_settings()