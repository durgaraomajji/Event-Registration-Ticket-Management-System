from pydantic import BaseModel, EmailStr, Field
from datetime import datetime

class UserRegister(BaseModel):
    username: str
    email: EmailStr
    password: str
    role: str


class UserLogin(BaseModel):
    username: str
    password: str


class EventCreate(BaseModel):
    event_name: str
    description: str
    location: str
    event_date: datetime
    total_seats: int = Field(gt=0)


class EventResponse(EventCreate):
    id: int
    available_seats: int

    class Config:
        from_attributes = True