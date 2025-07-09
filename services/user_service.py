from models.models import User
from models.dao.user_dao import UserDAO
from sqlalchemy.orm import sessionmaker
from typing import Optional, List
import bcrypt

class UserService:
    def __init__(self, session_factory: sessionmaker):
        self.session_factory = session_factory

    def register_user(self, username: str, password: str) -> User:
        with User(self.session_factory) as dao:
            if dao.user_name(username):
                raise ValueError("Usuário já existe.")
            new_user = User(username=username, password=password)
            return dao.create(new_user)

    def authenticate_user(self, username: str, password: str) -> bool:
        with User(self.session_factory) as dao:
            user = dao.user_name(username)
            if user and bcrypt.checkpw(password.encode(), user.password):
                return True
            return False

    def reset_password(self, username: str, new_password: str) -> bool:
        with User(self.session_factory) as dao:
            return dao.redefinir_password(username, new_password)

    def search_user(self, user_id: int) -> Optional[User]:
        with User(self.session_factory) as dao:
            return dao.get_by_id(user_id)

    def search_user_name(self, username: str) -> Optional[User]:
        with User(self.session_factory) as dao:
            return dao.user_name(username)

    def list_users(self) -> List[User]:
        with User(self.session_factory) as dao:
            return dao.get_all()
