"""
Name: events.py
Description:This file will contain the model definition for events operations.
"""

from pydantic import BaseModel
from typing import List


class BaseEvent(BaseModel):
    title: str
    image: str
    description: str
    tags: List[str]
    location: str

    class Config:
        json_schema_extra = {
            "example": {
                "title": "Music Concert",
                "image": "https://linktomyimage.com/image.png",
                "description": "We will be discussing the contents of the FastAPI book in this event.Ensure to come with your own copy to win gifts!",
                "tags": ["python", "fastapi", "book", "launch"],
                "location": "Google Meet",
            }
        }


class Event(BaseEvent):
    id: str
    class Config:
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
