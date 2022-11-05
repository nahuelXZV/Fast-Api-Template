# python
from typing import Optional

# pydantic
from pydantic import BaseModel, EmailStr, Field


class UserBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=50)
    email: EmailStr = Field(...)


class UserLogin(UserBase):
    password: str = Field(..., min_length=8, max_length=40)


class User(UserBase):
    id: Optional[int] = Field(None, title="User ID")


class UserUp(UserBase):
    password: str = Field(..., min_length=8, max_length=40)

# install pip install pydantic[email]
