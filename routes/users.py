"""
Name: users.py
Description: This file will handle routing operations such as the registration and signing-in of users.
"""
from fastapi import APIRouter, HTTPException,status,Depends
from models.users import User, UserSignIn,UserEmail
from database.connection import get_session
from sqlmodel import select

user_router = APIRouter(tags=["user"])
users = {}

@user_router.post("/signup")
async def sign_in_user(new_user:UserSignIn,session=Depends(get_session)) -> dict:
    user = session.get(UserSignIn, new_user.email)
    if user:
        raise HTTPException(status_code =status.HTTP_409_CONFLICT,
                            detail= "User with email already exists")
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return {"message":"User successfully registered"}


@user_router.post("/signin")
async def sign_user_in(user_signin: UserSignIn,session=Depends(get_session)) -> dict:
    user = session.get(UserSignIn, user_signin.email)
    if user.email !=user_signin.email:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User does not exist"
        )

    if user.password != user_signin.password:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Wrong credential passed"
        )
    return {
        "message": "User signed in successfully"
    }


