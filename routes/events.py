from models.events import Event
from fastapi import APIRouter, HTTPException, status, Body
from typing import List

event_router = APIRouter(
    tags=['Event'])



#define routes
events = []


@event_router.get("/", response_model=List[Event])
async def get_events() -> List[Event]:
    return events

@event_router.get("/{id}", response_model=Event)
async def get_event(id: int) -> Event:
    for event in events:
        if event.id == id:
            return event
    raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail="Event not found")


@event_router.post("/new_event")
async def create_event(body: Event = Body(...)) -> dict:
    events.append(body)
    return {"message":"Event created successfully"}


@event_router.delete("/{id}")
async def delete_event(id: int) -> dict:
    for event in events:
        if event.id == id:
            events.remove(event)
            return {"message":"Event deleted successfully"}
    raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail="Event not found")

@event_router.delete("/")
async def delete_all_events() -> dict:
    events.clear()
    return {"message": "Events deleted successfully"}
