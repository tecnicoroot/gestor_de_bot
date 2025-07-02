from database.db import SessionLocal, engine
from models.dao.user_dao import UsuarioDAO
from views.principal_view import PrincipalView

class LoginController:
    def __init__(self, view):
        self.view = view
        self.db = SessionLocal()
        self.user_dao = UsuarioDAO(self.db)

    def autenticar(self, usuario, senha):
        try:
            if self.user_dao.autenticar(usuario, senha):
                self.view.withdraw()
                self.abrir_principal()
            else:
                               
                self.view.exibir_erro("Usuário ou senha incorretos")
        finally:
            self.db.close()

    def abrir_principal(self):
        principal = PrincipalView(self.view)
        principal.grab_set()
