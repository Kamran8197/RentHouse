from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import date


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    email: str
    role: str
    is_active: bool = True


class House(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    owner_id: int = Field(foreign_key="user.id")
    title: str
    city: str
    price_per_night: float
    rooms: int
    is_available: bool = True


class Booking(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    house_id: int = Field(foreign_key="house.id")
    tenant_id: int = Field(foreign_key="user.id")
    start_date: date
    end_date: date
    total_price: float
    status: str = "pending"