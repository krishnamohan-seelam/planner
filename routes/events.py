"""
Name: events.py
Description: This file will handle routing operations such as creating, updating, and deleting events.
"""
from typing import List
from fastapi import APIRouter, HTTPException, status,Depends
from models.events import BaseEvent,Event,EventUpdate
from database.connection import get_session
from sqlmodel import select
from utils import get_uuid4
event_router = APIRouter(tags=["Events"])

events = []


@event_router.get("/", response_model=List[Event])
async def retrieve_all_events(session=Depends(get_session)) -> List[Event]:
    statement = select(Event)
    events = session.exec(statement).all()
    return events


@event_router.get("/{id}", response_model=Event)
async def retrieve_event(id: str,session=Depends(get_session)) -> Event:
    event = session.get(Event, id)
    if event:
        return event
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Event with supplied ID does not exist",
    )

@event_router.post("/new_event")
async def add_event(event: BaseEvent,session=Depends(get_session)) -> dict:
    event_dict = event.dict(exclude_unset=True)
    event_dict["id"] =get_uuid4()
    new_event =Event(**event_dict)
    session.add(new_event)
    session.commit()
    session.refresh(new_event)
    return {"message": "Event created successfully"}


@event_router.delete("/{id}")
async def remove_event(id: str,session=Depends(get_session)) -> dict:
    event = session.get(Event, id)
    if event:
        session.delete(event)
        session.commit()
        return {"message": "Event deleted successfully"}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Event with supplied ID does not exist",
    )

@event_router.put("/edit/{id}", response_model=Event)
async def update_event(id: str, new_data: EventUpdate, session=Depends(get_session)) -> Event:
    event = session.get(Event, id)
    if event:
        event_data = new_data.dict(exclude_unset=True)
        for key, value in event_data.items():
            setattr(event, key, value)
        session.add(event)
        session.commit()
        session.refresh(event)
        return event    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Event with supplied ID does not exist"
    )