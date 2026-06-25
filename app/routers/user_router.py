from fastapi import APIRouter

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.get("/profile")
def profile():
    return {
        "message": "User Profile"
    }