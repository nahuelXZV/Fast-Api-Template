# fastapi
from fastapi import FastAPI, Query

# routes
from routes.userRoute import router as user_router
from routes.authRoute import router as auth_router

# init app
app = FastAPI(
    title="FastAPI",
    description="Template for FastAPI",
    version="1.0.0",
    openapi_url="/api/v1/openapi.json",
    openapi_tags=[
        {"name": "Users", "description": "Operations with users"},
        {"name": "Auth", "description": "Operations with auth"},
    ],
)


# routes
@app.get("/", tags=["Root"])
def home():
    return {"Hello": "World"}


app.include_router(auth_router, prefix="/api/auth", tags=["Auth"])
app.include_router(user_router, prefix="/api/user", tags=["Users"])
