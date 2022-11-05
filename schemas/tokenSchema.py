# python
from typing import Optional

# pydantic
from pydantic import BaseModel, Field


class Token(BaseModel):
    access_token: str = Field(...)
    token_type: str = Field(...)


class TokenData(BaseModel):
    user_id: int = Field(...)
