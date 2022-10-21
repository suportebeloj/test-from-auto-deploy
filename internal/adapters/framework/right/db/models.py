from typing import Optional

from sqlmodel import Field, SQLModel


class OperationHistory(SQLModel, table=True):
    id: Field(default=None, primary_key=True)
    answer: Optional[int]
    operation: str
