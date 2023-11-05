"""
Name: events.py
Description: This file will handle routing operations such as creating, updating, and deleting events.
"""
from typing import List
from fastapi import APIRouter, Body, HTTPException, status
from models.events import BaseEvent,Event
from utils import get_id
event_router = APIRouter(tags=["Events"])

events = []


@event_router.get("/", response_model=List[Event])
async def retrieve_all_events() -> List[Event]:
    return events


@event_router.get("/{id}", response_model=Event)
async def retrieve_event(id: str) -> Event:
    for event in events:
        if event.id == id:
            return event
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Event with supplied ID does not exist",
    )

@event_router.post("/new_event")
async def add_event(body: BaseEvent = Body(...)) -> dict:
    event_dict = body.model_dump()
    event_dict["id"] =get_id()
    event =Event(**event_dict)
    events.append(event)
    return {"message": "Event created successfully"}


@event_router.delete("/{id}")
async def remove_event(id: str) -> dict:
    for event in events:
        if event.id == id:
            events.remove(event)
            return {"message": "Event deleted successfully"}
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event with supplied ID does not exist",
        )
@event_router.delete("/")
async def delete_all_events() -> dict:

    events.clear()

    return {

        "message": "Events deleted successfully"

    }