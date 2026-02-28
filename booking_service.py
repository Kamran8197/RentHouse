from sqlmodel import Session
from models import Booking, House
from fastapi import HTTPException
from datetime import date


def create_booking(
    session: Session,
    house_id: int,
    tenant_id: int,
    start_date: date,
    end_date: date,
):
    # 🔹 Validation
    if end_date <= start_date:
        raise HTTPException(status_code=400, detail="End date cannot be before start date")

    house = session.get(House, house_id)
    if not house or not house.is_available:
        raise HTTPException(status_code=404, detail="House not available")

    # 🔹 Automatic price calculation
    days = (end_date - start_date).days
    total_price = days * house.price_per_night

    booking = Booking(
        house_id=house_id,
        tenant_id=tenant_id,
        start_date=start_date,
        end_date=end_date,
        total_price=total_price,
        status="pending",
    )

    session.add(booking)
    session.commit()
    session.refresh(booking)

    return booking