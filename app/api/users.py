from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.user import UserCreate, UserRead
from app.db.session import SessionLocal
from app.models.user import User
from app.utils.security import get_password_hash
from fastapi_jwt_auth import AuthJWT

router = APIRouter(tags=["users"], prefix="/users")

@router.post("/", response_model=UserRead, status_code=201)
def create_user(user: UserCreate):

    db = SessionLocal()
    if db.query(User).filter(User.email == user.email).first():
        raise HTTPException(status_code=400, detail="Email exists")

    new_user = User(
        username=user.username,
        email=user.email,
        hashed_password=get_password_hash(user.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user
