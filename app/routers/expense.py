from fastapi import APIRouter, Depends
from app.schemas.expense import ExpenseCreate, ExpenseResponse

from sqlalchemy.orm import Session

from app.database import get_db
from app.models.expense import Expense

router = APIRouter(prefix="/expenses", tags=["Expenses"])


@router.post("", status_code=201, response_model=ExpenseResponse)
def create_expense(data: ExpenseCreate, db: Session = Depends(get_db)):
    expense = Expense(
        description=data.description,
        amount=data.amount,
        category=data.category,
        payment_method=data.payment_method,
        occurred_at=data.occurred_at,
    )

    db.add(expense)
    db.commit()
    db.refresh(expense)

    return expense
