from datetime import date, datetime
from decimal import Decimal

from pydantic import BaseModel, Field, ConfigDict
from enum import Enum


class ExpenseCategory(str, Enum):
    FOOD = "Alimentação"
    TRANSPORT = "Transporte"
    LEISURE = "Lazer"


class ExpenseCreate(BaseModel):
    description: str = Field(min_length=1, max_length=150)
    amount: Decimal = Field(gt=0, max_digits=10, decimal_places=2)
    category: ExpenseCategory  # str = Field(min_length=1, max_length=50)
    payment_method: str = Field(min_length=1, max_length=50)
    occurred_at: date


class ExpenseResponse(ExpenseCreate):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
