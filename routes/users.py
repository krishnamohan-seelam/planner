"""
Name: users.py
Description: This file will handle routing operations such as the registration and signing-in of users.
"""
from fastapi import Depends,APIRouter, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from auth.jwt_handler import create_access_token
from models.users import User,TokenResponse,UserSignIn
from database.connection import Database
from auth.hash_password import HashPassword

hash_password = HashPassword()
user_router = APIRouter(tags=["user"])
user_database = Database(User)


@user_router.post("/signup")
async def register_user(new_user: UserSignIn) -> dict:
    user_exist = await User.find_one(User.email == new_user.email)
    if user_exist:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with email already exists",
        )
    hashed_password = hash_password.create_hash(new_user.password)
    new_user.password = hashed_password
    user = User(**dict(new_user))
    await user_database.save(user)
    return {"message": "User successfully registered"}


@user_router.post("/signin",response_model=TokenResponse)
async def sign_user_in(user_signin: OAuth2PasswordRequestForm = Depends()) -> dict:
    user_exist = await User.find_one(User.email == user_signin.username)
    if not user_exist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User with email does not exist.",
        )
    if hash_password.verify_hash(user_signin.password, user_exist.password):
        access_token = create_access_token(user_exist.email)
        return {"access_token": access_token, "token_type": "Bearer"}
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid details passed."
        )
