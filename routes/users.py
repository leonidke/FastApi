from fastapi import APIRouter, HTTPException, status
from models.users import User, UserSignIn


user_router = APIRouter(
    tags=["User"]
)

users = {}

@user_router.post("/signup")
async def register_user(user: User)-> dict:
    if user.email in users:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User with email exists")
    users[user.email] = user
    return {"message": "User created successfully"}


@user_router.post("/login")
async def sign_user_in(user: UserSignIn)-> dict:
    if user.email not in users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    if users[user.email].password != user.password:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    return {"message": "User logged in successfully"}