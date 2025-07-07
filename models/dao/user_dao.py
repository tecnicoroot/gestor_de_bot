from models.dao.base import BaseDAO
from models.models import Usuario
import bcrypt
from typing import List, Optional
from sqlalchemy.orm import Session

class UsuarioDAO(BaseDAO):
    
    def get_by_id(self, usuario_id: int) -> Optional[Usuario]:
        return self.session.query(Usuario).filter_by(id=usuario_id).first()

    def get_all(self) -> List[Usuario]:
        return self.session.query(Usuario).all()

    def create(self, usuario: Usuario) -> Usuario:
        usuario.password = bcrypt.hashpw(usuario.password.encode(), bcrypt.gensalt())
        self.session.add(usuario)
        self.session.flush()
        return usuario

    def delete(self, usuario: Usuario) -> None:
        self.session.delete(usuario)

    def update(self, usuario: Usuario) -> Usuario:
        self.session.flush()
        return usuario

    def user_name(self, username: str) -> Optional[Usuario]:
        username =self.session.query(Usuario).filter_by(username=username).first()
        self.session.expunge(username)
        return username

    def redefinir_senha(self, username: str, nova_senha: str) -> bool:
        usuario = self.user_name(username)
        if usuario:
            usuario.password = bcrypt.hashpw(nova_senha.encode(), bcrypt.gensalt())
            return True
        return False

    def autenticar(self, username: str, senha: str) -> bool:
        usuario = self.user_name(username)
        if usuario and bcrypt.checkpw(senha.encode(), usuario.password):
            return True
        return False

    @staticmethod
    def password_verify(senha_em_texto: bytes, hash_armazenado: bytes) -> bool:
        return bcrypt.checkpw(senha_em_texto, hash_armazenado)
