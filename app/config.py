import os
from pathlib import Path
from pydantic_settings import BaseSettings
from dotenv import load_dotenv


load_dotenv(".env", override=True)

class DefaultSettings(BaseSettings):
    ENV_STATE: str = "Default"
    BASE_DIR: Path = Path(__file__).parent.parent
    SECRET_KEY: str = ""
    SQLALCHEMY_DATABASE_URL: str = "default"
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False
    SHOW_SQLALCHEMY_LOG_MESSAGE: bool = False

    class config():
        env_file = ".env"


class DevSettings(DefaultSettings):
    ENV_STATE: str = "Dev"
    DEBUG_MODE: bool = True
    SQLALCHEMY_ECHO: bool = True


def get_setting() -> BaseSettings:
    env_state = os.getenv("ENV_STATE", "Dev")
    if env_state == "Dev":
        return DevSettings()
