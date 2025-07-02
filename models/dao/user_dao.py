from models.models import Usuario
import bcrypt
from sqlalchemy.orm import Session

class UsuarioDAO:
    def __init__(self, db: Session):
        self.db = db

    def criar(self, username: str, senha: str) -> bool:
        senha_hash = bcrypt.hashpw(senha.encode(), bcrypt.gensalt())
        novo_usuario = Usuario(username=username, password=senha_hash)
        try:
            self.db.add(novo_usuario)
            self.db.commit()
            return True
        except Exception:
            self.db.rollback()
            return False

    def autenticar(self, username: str, senha: str) -> bool:
        usuario = self.db.query(Usuario).filter_by(username=username).first()
        if usuario and bcrypt.checkpw(senha.encode(), usuario.password):
            return True
        return False

    def redefinir_senha(self, username: str, nova_senha: str) -> bool:
        usuario = self.db.query(Usuario).filter_by(username=username).first()
        if usuario:
            usuario.password = bcrypt.hashpw(nova_senha.encode(), bcrypt.gensalt())
            self.db.commit()
            return True
        return False

    def listar_usuarios(self):
        return self.db.query(Usuario).all()
