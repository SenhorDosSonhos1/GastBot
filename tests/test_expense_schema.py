import pytest
from pydantic import ValidationError
from app.schemas.expense import ExpenseCreate, ExpenseCategory
from datetime import datetime, timezone


def test_expense_category_success():
    category = ExpenseCreate(
        description="testing",
        amount=10,
        category="Transporte",
        payment_method="Pix",
        occurred_at=datetime.now(timezone.utc).date(),
    )

    assert category.category in [c.value for c in ExpenseCategory]


def test_expense_category_failed():
    with pytest.raises(ValidationError):
        ExpenseCreate(
            description="testing",
            amount=10,
            category="TRANSPORT",
            payment_method="Pix",
            occurred_at=datetime.now(timezone.utc).date(),
        )