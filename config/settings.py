import os
from functools import lru_cache

from dotenv import load_dotenv
from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")
    DATABASE_DRIVER: str | None = os.getenv("DATABASE_DRIVER")
    DATABASE_PORT: int | str | None = os.getenv("DATABASE_PORT")

    DATABASE_USER: str | None = os.getenv("MYSQL_USER")
    MYSQL_ROOT_PASSWORD: SecretStr | str | None = os.getenv("MYSQL_PASSWORD")

    RABBITMQ_DEFAULT_USER: str | None = os.getenv("RABBITMQ_DEFAULT_USER")
    RABBITMQ_DEFAULT_PASS: SecretStr | str | None = os.getenv("RABBITMQ_DEFAULT_PASS")

    REDIS_HOST: str | None = os.getenv("")
    REDIS_PORT: int | str | None = os.getenv("REDIS_PORT")
    REDIS_DB: int | str | None = os.getenv("REDIS_DB")
    SECRET_KEY: SecretStr | str | None = os.getenv("SECRET_KEY")
    REFRESH_SECRET_KEY: SecretStr | str | None = os.getenv("REFRESH_SECRET_KEY")
    ALGORITHM: str | None = os.getenv("ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES: int | str | None = os.getenv(
        "ACCESS_TOKEN_EXPIRE_MINUTES"
    )
    REFRESH_TOKEN_EXPIRE_DAYS: int | str | None = os.getenv("REFRESH_TOKEN_EXPIRE_DAYS")


@lru_cache
def get_setting() -> None:
    return Settings()
