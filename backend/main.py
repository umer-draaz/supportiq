from fastapi import FastAPI, HTTPException
from sqlalchemy import text
from database import engine, Base
from models.user import User
from models.ticket import Ticket
from routers.auth import router as auth_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="SupportIQ API",
    description="AI-powered customer support intelligence platform",
    version="0.1.0"
)

app.include_router(auth_router)


@app.get("/")
def home():
    return {"message": "SupportIQ API is running"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/db-check")
def database_check():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))

        return {"database": "connected"}
    except Exception:
        raise HTTPException(
            status_code=503,
            detail="Database connection failed"
        )