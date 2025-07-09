from models.dao.base import BaseDAO
from models.models import User
import bcrypt
from typing import List, Optional
from sqlalchemy.orm import Session

class UserDAO(BaseDAO):
    
    def get_by_id(self, user_id: int) -> Optional[User]:
        return self.session.query(User).filter_by(id=user_id).first()

    def get_all(self) -> List[User]:
        return self.session.query(User).all()

    def create(self, user: User) -> User:
        user.password = bcrypt.hashpw(user.password.encode(), bcrypt.gensalt())
        self.session.add(user)
        self.session.flush()
        return user

    def delete(self, user: User) -> None:
        self.session.delete(user)

    def update(self, user: User) -> User:
        self.session.flush()
        return user

    def user_name(self, username: str) -> Optional[User]:
        username =self.session.query(User).filter_by(username=username).first()
        self.session.expunge(username)
        return username

    def redefinir_senha(self, username: str, nova_senha: str) -> bool:
        user = self.user_name(username)
        if user:
            user.password = bcrypt.hashpw(nova_senha.encode(), bcrypt.gensalt())
            return True
        return False

    def autenticar(self, username: str, senha: str) -> bool:
        user = self.user_name(username)
        if user and bcrypt.checkpw(senha.encode(), user.password):
            return True
        return False

    @staticmethod
    def password_verify(senha_em_texto: bytes, hash_armazenado: bytes) -> bool:
        return bcrypt.checkpw(senha_em_texto, hash_armazenado)
