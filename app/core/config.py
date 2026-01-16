from pydantic import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "Generic API"
    JWT_SECRET: str
    DB_URL: str

    class Config:
        env_file = ".env"


settings = Settings()
