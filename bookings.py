from fastapi import APIRouter, Depends
from sqlmodel import Session
from database import get_session
from services.booking_service import create_booking
from datetime import date

router = APIRouter(prefix="/bookings", tags=["Bookings"])


@router.post("/")
def book_house(
    house_id: int,
    tenant_id: int,
    start_date: date,
    end_date: date,
    session: Session = Depends(get_session),
):
    return create_booking(session, house_id, tenant_id, start_date, end_date)