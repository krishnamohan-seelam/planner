"""
Name: users.py
Description: This file will handle routing operations such as the registration and signing-in of users.
"""
from fastapi import APIRouter, HTTPException,status
from models.users import User, UserSignIn
from database.connection import Database
 

user_router = APIRouter(tags=["user"])
user_database = Database(User)

@user_router.post("/signup")
async def register_user(new_user:UserSignIn) -> dict:
    user_exist = await User.find_one(User.email == new_user.email)
    if user_exist:
        raise HTTPException(status_code =status.HTTP_409_CONFLICT,
                            detail= "User with email already exists")
    user = User(**dict(new_user))
    await user_database.save(user)
    return {"message":"User successfully registered"}


@user_router.post("/signin")
async def sign_user_in(user_signin: UserSignIn) -> dict:
    user_exist = await User.find_one(User.email == user_signin.email)
    if not user_exist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User with email does not exist."
        )
    if user_exist.password != user_signin.password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid details passed."
        )
    return {
        "message": "User signed in successfully"
    }


