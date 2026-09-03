from fastapi import FastAPI, Depends
from app.database import get_db
from sqlalchemy.orm import Session
from sqlalchemy import text

app = FastAPI()


@app.get("/")
def hello():
    return {"message": "API do GastBot está funcionando"}

@app.get("/health/db")
def check_database(db: Session = Depends(get_db)):
    db.execute(text("SELECT 1"))
    from app.database import DATABASE_URL
    print(repr(DATABASE_URL))
    return {"database": "connected"}