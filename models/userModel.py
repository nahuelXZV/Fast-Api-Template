from sqlalchemy import Column, Integer, String, DateTime, Boolean, Table
from utils.db import meta, engine

users = Table(
    'users',
    meta,
    Column('id', Integer, primary_key=True),
    Column('email', String(80), unique=True, nullable=False),
    Column('password', String(255), nullable=False),
    Column('name', String(150), nullable=False))

meta.create_all(engine)
