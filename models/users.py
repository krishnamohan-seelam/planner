"""
Name: models.py
Description:This file will contain the model definition for user operations.
"""
from typing import Optional, List
from beanie import Document, Link
from pydantic import BaseModel, EmailStr 
from models.events import Event
from beanie import Document


class User(Document):
    email: EmailStr 
    password: str
    events: Optional[List[Link[Event]]]

    class Settings:
        name = "users"

    class Config:
        schema_extra = {
            "example": {
                "email": "fastapi@packt.com",
                "password": "strong!!!",
                "events": [],
            }
        }

class UserSignIn(BaseModel):
    email: EmailStr
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str
