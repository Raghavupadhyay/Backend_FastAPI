from fastapi import APIRouter, Depends, HTTPException
from app.schemas.item import ItemCreate, ItemRead
from app.db.session import SessionLocal
from app.models.item import Item
from fastapi_jwt_auth import AuthJWT

router = APIRouter(tags=["items"], prefix="/items")

@router.post("/", response_model=ItemRead, status_code=201)
def create_item(item: ItemCreate, Authorize: AuthJWT = Depends()):

    Authorize.jwt_required()
    username = Authorize.get_jwt_subject()

    db = SessionLocal()
    new_item = Item(name=item.name, description=item.description)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

@router.get("/", response_model=list[ItemRead])
def list_items():
    db = SessionLocal()
    return db.query(Item).all()
