from sqlmodel import create_engine, select, Session, SQLModel

from internal.adapters.framework.right.db.db import Adapter
from internal.adapters.framework.right.db.models import OperationHistory

engine = create_engine("sqlite://")  # create sqlite database in memory
SQLModel.metadata.create_all(engine)
adapter = Adapter(db=engine)


def test_save_historic():

    operation = adapter.AddToHistory(1, "addition")

    with Session(engine) as session:
        stmt = select(OperationHistory).where(
            OperationHistory.id == operation.id)
        operation_history = session.exec(stmt).one()

        assert operation_history is not None
        assert operation_history.id == operation.id
        assert operation_history.answer == operation.answer
        assert operation_history.operation == operation.operation
