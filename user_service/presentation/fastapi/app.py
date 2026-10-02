from starlette.middleware.cors import CORSMiddleware

from fastapi import FastAPI
from user_service.config.settings import UserSettings


class App:
    def __init__(self, settings: UserSettings):
        self.app = FastAPI(title=settings.PROJECT_NAME, root_path=settings.ROOT_PATH)

        origins = ["*"]

        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=origins,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    @classmethod
    def get_app(cls, settings: UserSettings) -> FastAPI:
        user_app_instance = cls(settings=settings)
        return user_app_instance.app
