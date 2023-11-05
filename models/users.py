"""
Name: models.py
Description:This file will contain the model definition for user operations.
"""
from pydantic import BaseModel, EmailStr
from typing import Optional, List
from models.events import Event


class User(BaseModel):
    email: EmailStr
    password: str
    events: Optional[List[Event]]

    class Config:
        json_schema_extra = {
            "email": "fastapi@example.com",
            "username": "strong!!!",
            "events": [],
        }

class UserSignIn(BaseModel):
    email: EmailStr
    password: str
 

    class Config:
        json_schema_extra = {
            "email": "fastapi@example.com",
            "username": "strong!!!",
        }
