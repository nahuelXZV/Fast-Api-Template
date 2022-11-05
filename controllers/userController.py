# utils
from fastapi import HTTPException
from utils.db import conn
from utils.encrypt import pwd_context

# models
from models.userModel import users

# schemas
from schemas.userSchema import UserUp

# Get all users
def get_all():
    query = users.select()
    return conn.execute(query).fetchall()


# Get a user
def get_one(id: int):
    query = users.select(users.c.id == id)
    response = conn.execute(query).fetchone()
    # validar que no alla un error
    if response:
        return response
    else:
        # levantar una excepcion
        raise HTTPException(status_code=404, detail=f"User with id {id} not found")


# Create a new user
def create(user: UserUp):
    user = conn.execute(users.select(users.c.email == user.email)).fetchone()
    if user:
        raise HTTPException(status_code=400, detail="Email already registered")

    new_user = {
        "email": user.email,
        "name": user.name,
    }
    new_user["password"] = pwd_context.hash(user.password)
    query = users.insert().values(new_user)
    result = conn.execute(query)
    response = conn.execute(
        users.select(users.c.id == result.inserted_primary_key[0])
    ).fetchone()
    if response:
        return response
    else:
        raise HTTPException(status_code=404, detail=f"User not created")


# Delete a user
def delete(id: int):
    query = users.delete().where(users.c.id == id)
    response = conn.execute(query)
    if response:
        return {"message": "User deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail=f"User with id {id} not found")


# Update a user
def update(id: int, user: UserUp):
    userFind = conn.execute(
        users.select(users.c.email == user.email).where(users.c.id != id)
    ).fetchone()
    if userFind:
        raise HTTPException(status_code=400, detail="Email already registered")

    new_password = pwd_context.hash(user.password)
    query = (
        users.update()
        .values(name=user.name, email=user.email, password=new_password)
        .where(users.c.id == id)
    )
    response = conn.execute(query)
    if response:
        return {"message": "User updated successfully"}
    else:
        raise HTTPException(status_code=404, detail=f"User with id {id} not found")
