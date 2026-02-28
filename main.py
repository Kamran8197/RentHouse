from fastapi import FastAPI
from database import engine
from sqlmodel import SQLModel
from routers import houses, bookings

app = FastAPI(docs_url="/docs")

SQLModel.metadata.create_all(engine)

app.include_router(houses.router)
app.include_router(bookings.router)