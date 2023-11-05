"""
Name: users.py
Description: This file will handle routing operations such as the registration and signing-in of users.
"""
from fastapi import APIRouter, HTTPException,status
from models.users import User, UserSignIn

user_router = APIRouter(tags=["user"])
users = {}

@user_router.post("/signup")
def sign_in_user(data:UserSignIn) -> dict:
    if data.email in users:
        raise HTTPException(status_code =status.HTTP_409_CONFLICT,
                            detail= "User with email already exists")
    users[data.email]= data
    return {"message":"User successfully registered"}


@user_router.post("/signin")
async def sign_user_in(user: UserSignIn) -> dict:
    if user.email not in users:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User does not exist"
        )

    if users[user.email].password != user.password:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Wrong credential passed"
        )
    return {
        "message": "User signed in successfully"
    }


