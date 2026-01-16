from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.auth import Login, Token
from app.db.session import SessionLocal
from app.models.user import User
from app.utils.security import verify_password
from fastapi_jwt_auth import AuthJWT
from fastapi.encoders import jsonable_encoder

router = APIRouter(tags=["auth"], prefix="/auth")

@router.post("/login", response_model=Token)
def login(user: Login, Authorize: AuthJWT = Depends()):

    db = SessionLocal()
    db_user = db.query(User).filter(User.username == user.username).first()

    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access = Authorize.create_access_token(subject=db_user.username)
    refresh = Authorize.create_refresh_token(subject=db_user.username)

    return jsonable_encoder({"access": access, "refresh": refresh})
