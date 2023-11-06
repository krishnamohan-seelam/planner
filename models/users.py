"""
Name: models.py
Description:This file will contain the model definition for user operations.
"""
from pydantic import BaseModel, EmailStr
from typing import Optional, List
from sqlmodel import JSON, SQLModel, Field, Column
from typing import Optional, List
from models.events import Event


class User(SQLModel):
    email: EmailStr = Field(default=None, primary_key=True)
    password: str
    events: Optional[List[Event]] 

    class Config:
        arbitrary_types_allowed = True
        json_schema_extra = {
            "email": "fastapi@example.com",
            "username": "strong!!!",
            "events": [],
        }
class UserEmail(SQLModel):
    email:EmailStr = Field(default=None, primary_key=True)
    
class UserSignIn(SQLModel,table=True):
    email: EmailStr = Field(default=None, primary_key=True)
    password: str
 

    class Config:
        arbitrary_types_allowed = True
        json_schema_extra = {
            "email": "fastapi@example.com",
            "username": "strong!!!",
        }
