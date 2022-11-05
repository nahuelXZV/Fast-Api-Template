from sqlalchemy import Column, Integer, String, DateTime, Boolean, Table
from utils.db import meta, engine

users = Table(
    "tokens",
    meta,
    Column("id", Integer, primary_key=True),
    Column("access_token", String(255), unique=True, nullable=False),
    Column("token_type", String(255), nullable=False),
    # foreign key
    Column("user_id", Integer, nullable=False, foreign_key="users.id"),
)

meta.create_all(engine)
