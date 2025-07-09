from models.dao.base import BaseDAO
from models.models import Robot
from typing import List, Optional
from sqlalchemy.exc import SQLAlchemyError


class RoboDAO(BaseDAO):
    def get_by_id(self, robot_id: int) -> Optional[Robot]:
        return self.session.query(Robot).filter_by(id=robot_id).first()

    def get_all(self) -> List[Robot]:
        return self.session.query(Robot).all()

    def create(self, robot: Robot) -> Robot:
        self.session.add(robot)
        self.session.flush()
        return robot

    def delete(self, robot: Robot) -> None:
        self.session.delete(robot)

    def update(self, robot: Robot) -> Robot:
        self.session.flush()
        return robot