# app/core/config.py
from pydantic_settings  import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Agendador Inteligente"
    API_V1_STR: str = "/api/v1"

    POSTGRES_USER: str = "user_default"
    POSTGRES_PASSWORD: str = "password_default"
    POSTGRES_DB: str = "db_default"
    POSTGRES_SERVER: str = "localhost"
    POSTGRES_PORT: str = "5432"

    SECRET_KEY: str = "mysecretkey"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    ALGORITHM: str = "HS256"

    SMTP_SERVER: str = ""
    SMTP_PORT: int = 587
    SMTP_USERNAME: str = ""
    SMTP_PASSWORD: str = ""

    class Config:
        env_file = ".env"

settings = Settings()