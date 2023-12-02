"""
Name: events.py
Description:This file will contain the model definition for events operations.
"""

from pydantic import BaseModel,Field
from beanie import Document
from typing import Optional, List

from uuid import UUID, uuid4
class BaseEvent(BaseModel):
    title: str
    image: str
    description: str
    location:str
    class Config:
        arbitrary_types_allowed = True
        
        json_schema_extra = {
            "example": {
                "title": "Music Concert",
                "image": "https://linktomyimage.com/image.png",
                "description": "We will be discussing the contents of the FastAPI book in this event.Ensure to come with your own copy to win gifts!",
                "tags": ["python", "fastapi", "book", "launch"],
                "location": "Google Meet",
            }
        }


class Event(Document):
    id: UUID = Field(alias="_id",default_factory=uuid4)
    creator:Optional[str]
    title: str
    image: str
    description: str
    location:str
    class Config:
        arbitrary_types_allowed = True
        populate_by_name=True
        json_encoders={UUID: str}
        json_schema_extra = {
            "example": {
                "id": "1",
                "title": "Music Concert",
                "image": "https://linktomyimage.com/image.png",
                "description": "We will be discussing the contents of the FastAPI book in this event.Ensure to come with your own copy to win gifts!",
                "tags": ["python", "fastapi", "book", "launch"],
                "location": "Google Meet",
            }
        }
    class Settings:
        name = "events"

class EventUpdate(BaseModel):
    title: Optional[str]
    image: Optional[str]
    description: Optional[str]
    tags: Optional[List[str]]
    location: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "title": "FastAPI Book Launch",
                "image": "https://linktomyimage.com/image.png",
                "description": "We will be discussing the contents of the FastAPI book in this event. Ensure to come with your own copy to win gifts!",
                "tags": ["python", "fastapi", "book", "launch"],
                "location": "Google Meet",
            }
        }