from fastapi import FastAPI

from app.database import Base, engine

from app.routers.auth_router import router as auth_router
from app.routers.user_router import router as user_router
from app.routers.event_router import router as event_router
from app.routers.registration_router import router as registration_router
from app.routers.ticket_router import router as ticket_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Event Registration System"
)

app.include_router(auth_router)
app.include_router(user_router)
app.include_router(event_router)
app.include_router(registration_router)
app.include_router(ticket_router)