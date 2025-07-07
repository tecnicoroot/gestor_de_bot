from models.models import Usuario
from models.dao.user_dao import UsuarioDAO
from sqlalchemy.orm import sessionmaker
from typing import Optional, List
import bcrypt

class UsuarioService:
    def __init__(self, session_factory: sessionmaker):
        self.session_factory = session_factory

    def registrar_usuario(self, username: str, senha: str) -> Usuario:
        with UsuarioDAO(self.session_factory) as dao:
            if dao.user_name(username):
                raise ValueError("Usuário já existe.")
            novo_usuario = Usuario(username=username, password=senha)
            return dao.create(novo_usuario)

    def autenticar_usuario(self, username: str, senha: str) -> bool:
        with UsuarioDAO(self.session_factory) as dao:
            usuario = dao.user_name(username)
            if usuario and bcrypt.checkpw(senha.encode(), usuario.password):
                return True
            return False

    def redefinir_senha(self, username: str, nova_senha: str) -> bool:
        with UsuarioDAO(self.session_factory) as dao:
            return dao.redefinir_senha(username, nova_senha)

    def buscar_usuario(self, usuario_id: int) -> Optional[Usuario]:
        with UsuarioDAO(self.session_factory) as dao:
            return dao.get_by_id(usuario_id)

    def buscar_usuario_name(self, username: str) -> Optional[Usuario]:
        with UsuarioDAO(self.session_factory) as dao:
            return dao.user_name(username)

    

    def listar_usuarios(self) -> List[Usuario]:
        with UsuarioDAO(self.session_factory) as dao:
            return dao.get_all()
