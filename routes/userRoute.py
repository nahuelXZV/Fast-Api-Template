# fastapi
from fastapi import APIRouter

# schemas
from schemas.userSchema import User, UserUp, UserLogin

# controllers
from controllers.userController import get_all, get_one, create, delete, update

# init variables
router = APIRouter()


# Get all users
@router.get("/", response_model=list[User], status_code=200, summary="Get all users")
def get_users():
    return get_all()


# Get a user
@router.get("/{id}", response_model=User, status_code=200, summary="Get a user")
def get_user(id: int):
    return get_one(id)


# Create a new user
@router.post("/", response_model=User, status_code=201, summary="Create a new user")
def create_user(user: UserUp):
    return create(user)


# Delete a user
@router.delete("/{id}", response_model=User, status_code=200, summary="Delete a user")
def delete_user(id: int):
    return delete(id)


# Update a user
@router.put("/{id}", status_code=200, summary="Update a user")
def update_user(id: int, user: UserUp):
    return update(id, user)
