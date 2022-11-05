# sqlalchemy
from sqlalchemy import create_engine, MetaData

# dotenv
from .config import Config

config = Config()

DB_HOST = config.DB_HOST
DB_PORT = config.DB_PORT
DB_TYPE = config.DB_TYPE
DB_USERNAME = config.DB_USERNAME
DB_PASSWORD = config.DB_PASSWORD
DB_DATABASE = config.DB_DATABASE

uri = f"{DB_TYPE}://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}"

engine = create_engine(uri)
meta = MetaData()
conn = engine.connect()
