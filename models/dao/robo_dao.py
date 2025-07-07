from models.dao.base import BaseDAO
from models.models import Robo
from typing import List, Optional
from sqlalchemy.exc import SQLAlchemyError


class RoboDAO(BaseDAO):
    def get_by_id(self, robo_id: int) -> Optional[Robo]:
        return self.session.query(Robo).filter_by(id=robo_id).first()

    def get_all(self) -> List[Robo]:
        return self.session.query(Robo).all()

    def create(self, robo: Robo) -> Robo:
        self.session.add(robo)
        self.session.flush()
        return robo

    def delete(self, robo: Robo) -> None:
        self.session.delete(robo)

    def update(self, robo: Robo) -> Robo:
        self.session.flush()
        return robo