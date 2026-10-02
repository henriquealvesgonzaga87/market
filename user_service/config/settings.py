import os
from functools import lru_cache

from dotenv import load_dotenv
from pydantic_settings import SettingsConfigDict

from config.settings import Settings

load_dotenv()


class UserSettings(Settings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    PROJECT_NAME: str = "User-Service"
    ROOT_PATH: str = "/user-service"
    PREFIX: str = "/api/v1/user"

    USERS_DATABASE_HOST: str | None = os.getenv("USERS_DATABASE_HOST")
    USERS_DATABASE_NAME: str | None = os.getenv("USERS_DATABASE_NAME")


@lru_cache
def get_user_setting() -> None:
    return UserSettings()
