from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(100), unique=True)
    email = Column(String(50), unique=True)
    password = Column(String(255))
    role = Column(String(100))


class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True)
    event_name = Column(String(100))
    description = Column(String(200))
    location = Column(String(200))
    event_date = Column(DateTime)
    total_seats = Column(Integer)
    available_seats = Column(Integer)


class Registration(Base):
    __tablename__ = "registrations"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    event_id = Column(Integer, ForeignKey("events.id"))
    registration_date = Column(DateTime)


class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True)
    ticket_number = Column(String(50), unique=True)
    registration_id = Column(Integer, ForeignKey("registrations.id"))