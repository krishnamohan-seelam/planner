"""
Name: events.py
Description: This file will handle routing operations such as creating, updating, and deleting events.
"""
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from models.events import BaseEvent, Event, EventUpdate
from auth.authenticate import authenticate
from uuid import UUID
from database.connection import Database

event_router = APIRouter(tags=["Events"])
event_database = Database(Event)


@event_router.get("/", response_model=List[Event])
async def retrieve_all_events() -> List[Event]:
    events = await event_database.get_all()
    return events


@event_router.get("/{id}", response_model=Event)
async def retrieve_event(id: str) -> Event:
    event = await event_database.get(UUID(id))
    if event:
        return event
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Event with supplied ID does not exist",
    )


@event_router.post("/new_event")
async def add_event(event: BaseEvent, user: str = Depends(authenticate)) -> dict:
    event_dict = event.dict(exclude_unset=True)
    event_dict["creator"] = user
    await event_database.save(Event(**event_dict))
    return {"message": "Event created successfully"}


@event_router.delete("/{id}")
async def remove_event(id: str, user: str = Depends(authenticate)) -> dict:
    event = await event_database.get(UUID(id))

    if event.creator != user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Event not found"
        )
    event_deleted = await event_database.delete(UUID(id))
    if event_deleted:
        return {"message": "Event deleted successfully"}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Event with supplied ID does not exist",
    )


@event_router.put("/edit/{id}", response_model=Event)
async def update_event(id: str, new_data: EventUpdate) -> Event:
    updated_event = await event_database.update(UUID(id), new_data)
    if not updated_event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event with supplied ID does not exist",
        )
    return updated_event
