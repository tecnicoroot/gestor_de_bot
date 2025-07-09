from sqlalchemy.orm import Session
#from models import Usuario, Robo
from typing import List, Optional,  Callable
from sqlalchemy.exc import SQLAlchemyError

class BaseDAO:
    def __init__(self, session_factory: Callable[[], Session]):
        self.session_factory = session_factory
        self.session: Optional[Session] = None

    def __enter__(self):
        self.session = self.session_factory()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.session:
            if exc_type:
                self.session.rollback()
            else:
                try:
                    self.session.commit()
                except Exception:
                    self.session.rollback()
                    raise
            self.session.close()