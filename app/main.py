from fastapi import Depends, FastAPI
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.database import get_db

from app.models.expense import Expense

from app.routers.expense import router as expense_router

app = FastAPI()

app.include_router(expense_router)


@app.get("/")
def hello():
    return {"message": "API do GastBot está funcionando"}


@app.get("/health/db")
def check_database(db: Session = Depends(get_db)):
    db.execute(text("SELECT 1"))
    return {"database": "connected"}
