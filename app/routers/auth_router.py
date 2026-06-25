from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.models import User
from app.schemas import UserRegister, UserLogin
from app.dependencies import get_db
from app.utils.security import hash_password, verify_password
from app.auth import create_token

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register")
def register(user: UserRegister, db: Session = Depends(get_db)):

    db_user = User(
        username=user.username,
        email=user.email,
        password=hash_password(user.password),
        role=user.role
    )

    db.add(db_user)
    db.commit()

    return {"message": "User Registered"}


@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):

    db_user = db.query(User).filter(
        User.username == user.username
    ).first()

    if not db_user:
        raise HTTPException(400, "Invalid Credentials")

    if not verify_password(
        user.password,
        db_user.password
    ):
        raise HTTPException(400, "Invalid Credentials")

    token = create_token(
        {
            "id": db_user.id,
            "role": db_user.role
        }
    )

    return {"access_token": token}