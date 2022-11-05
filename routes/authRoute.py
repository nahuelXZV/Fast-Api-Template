# fastapi
from fastapi import APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends

# schemas
from schemas.userSchema import User, UserUp, UserLogin
from schemas.tokenSchema import Token

# controllers
from controllers.authController import authenticate_user, generate_token

# init variables
router = APIRouter()


@router.post("/login", response_model=Token, status_code=200, summary="Login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    access_token = generate_token(form_data.username, form_data.password)
    return Token(access_token=access_token, token_type="bearer")
