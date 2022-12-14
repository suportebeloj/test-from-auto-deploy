from sqlmodel import Session

from internal.ports.framework_right import DbportInterface
from .models import OperationHistory

class Adapter(DbportInterface):

    def AddToHistory(self, answer, opration) -> OperationHistory:
        operation_history = OperationHistory(answer=answer, operation=opration)
        
        with Session(self.db) as session:
            session.add(operation_history)
            session.commit()

            session.refresh(operation_history)
        
        return operation_history
