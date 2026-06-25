from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from uuid import uuid4

from app.models import Ticket
from app.dependencies import get_db

router = APIRouter(
    prefix="/tickets",
    tags=["Tickets"]
)

@router.get("/{registration_id}")
def generate_ticket(
    registration_id: int,
    db: Session = Depends(get_db)
):

    ticket = db.query(Ticket).filter(
        Ticket.registration_id == registration_id
    ).first()

    if not ticket:

        ticket = Ticket(
            registration_id=registration_id,
            ticket_number=str(uuid4())
        )

        db.add(ticket)
        db.commit()

    return ticket