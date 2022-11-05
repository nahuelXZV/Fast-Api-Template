import os

from pydantic import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class Config(BaseSettings):
    DB_HOST: str = os.getenv("DB_HOST")  # type: str
    DB_PORT: str = os.getenv("DB_PORT")  # type: str
    DB_DATABASE: str = os.getenv("DB_DATABASE")  # type: str
    DB_USERNAME: str = os.getenv("DB_USERNAME")  # type: str
    DB_PASSWORD: str = os.getenv("DB_PASSWORD")  # type: str
    DB_TYPE: str = os.getenv("DB_TYPE")  # type: str
    
    SECRET_KEY: str = os.getenv("SECRET_KEY")  # type: str
    TOKEN_EXPIRE_MINUTES: int = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")  # type: int
