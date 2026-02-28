from sqlmodel import Session, select
from models import House
from typing import Optional, List


def create_house(session: Session, house: House):
    session.add(house)
    session.commit()
    session.refresh(house)
    return house


def search_houses(
    session: Session,
    min_price: Optional[float],
    max_price: Optional[float],
    city: Optional[str],
    rooms: Optional[int],
) -> List[House]:

    query = select(House).where(House.is_available == True)

    if min_price:
        query = query.where(House.price_per_night >= min_price)

    if max_price:
        query = query.where(House.price_per_night <= max_price)

    if city:
        query = query.where(House.city == city)

    if rooms:
        query = query.where(House.rooms == rooms)

    return session.exec(query).all()


def soft_delete_house(session: Session, house_id: int):
    house = session.get(House, house_id)
    if not house:
        return None

    house.is_available = False
    session.commit()
    session.refresh(house)
    return house