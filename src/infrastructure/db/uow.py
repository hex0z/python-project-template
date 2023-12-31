from sqlalchemy.orm import Session

from application.common.interfaces.uow import UnitOfWork


class UnitOfWorkImpl(UnitOfWork):
    def __init__(self, session: Session) -> None:
        self._session = session

    def commit(self) -> None:
        self._session.commit()

    def rollback(self) -> None:
        self._session.rollback()
