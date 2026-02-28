from fastapi import APIRouter, Depends
from sqlmodel import Session
from database import get_session
from models import House
from services.house_service import create_house, search_houses, soft_delete_house
from typing import Optional, List

router = APIRouter(prefix="/houses", tags=["Houses"])


@router.post("/")
def add_house(house: House, session: Session = Depends(get_session)):
    return create_house(session, house)


@router.get("/search/")
def search(
    min_price: Optional[float] = None,
    max_price: Optional[float] = None,
    city: Optional[str] = None,
    rooms: Optional[int] = None,
    session: Session = Depends(get_session),
):
    return search_houses(session, min_price, max_price, city, rooms)


@router.delete("/{house_id}")
def delete_house(house_id: int, session: Session = Depends(get_session)):
    return soft_delete_house(session, house_id)