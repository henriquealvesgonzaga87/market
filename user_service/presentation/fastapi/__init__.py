from user_service.config.settings import get_user_setting
from user_service.presentation.fastapi.app import App

settings = get_user_setting()
app = App.get_app(settings=settings)
