from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime

from app.models import Event
from app.schemas import EventCreate
from app.dependencies import get_db

router = APIRouter(
    prefix="/events",
    tags=["Events"]
)

@router.post("/")
def create_event(
    event: EventCreate,
    db: Session = Depends(get_db)
):

    if event.event_date <= datetime.now():
        raise HTTPException(
            400,
            "Event date must be future"
        )

    new_event = Event(
        **event.dict(),
        available_seats=event.total_seats
    )

    db.add(new_event)
    db.commit()

    return {"message": "Event Created"}


@router.get("/")
def get_events(
    location: str = None,
    status: str = None,
    db: Session = Depends(get_db)
):

    query = db.query(Event)

    if location:
        query = query.filter(
            Event.location == location
        )

    if status == "upcoming":
        query = query.filter(
            Event.event_date > datetime.now()
        )

    return query.all()


@router.get("/{id}")
def get_event(
    id: int,
    db: Session = Depends(get_db)
):
    return db.query(Event).filter(
        Event.id == id
    ).first()


@router.put("/{id}")
def update_event(
    id: int,
    event: EventCreate,
    db: Session = Depends(get_db)
):
    db_event = db.query(Event).filter(
        Event.id == id
    ).first()

    for key, value in event.dict().items():
        setattr(db_event, key, value)

    db.commit()

    return {"message": "Updated"}


@router.delete("/{id}")
def delete_event(
    id: int,
    db: Session = Depends(get_db)
):
    event = db.query(Event).filter(
        Event.id == id
    ).first()

    db.delete(event)
    db.commit()

    return {"message": "Deleted"}