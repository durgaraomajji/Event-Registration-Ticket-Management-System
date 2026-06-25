from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime

from app.models import Event, Registration
from app.dependencies import get_db

router = APIRouter(
    prefix="/events",
    tags=["Registration"]
)

@router.post("/{event_id}/register")
def register_event(
    event_id: int,
    user_id: int,
    db: Session = Depends(get_db)
):

    event = db.query(Event).filter(
        Event.id == event_id
    ).first()

    if event.available_seats <= 0:
        raise HTTPException(
            400,
            "Seats Full"
        )

    existing = db.query(
        Registration
    ).filter(
        Registration.user_id == user_id,
        Registration.event_id == event_id
    ).first()

    if existing:
        raise HTTPException(
            400,
            "Already Registered"
        )

    reg = Registration(
        user_id=user_id,
        event_id=event_id,
        registration_date=datetime.now()
    )

    db.add(reg)

    event.available_seats -= 1

    db.commit()

    return {"message": "Registered"}