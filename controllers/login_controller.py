from database.db import SessionLocal, engine
from models.dao.user_dao import UsuarioDAO
from views.principal_view import PrincipalView
from views.sobre_view import SobreView

class LoginController:
    def __init__(self, view):
        self.view = view
        self.db = SessionLocal()
        self.user_dao = UsuarioDAO(self.db)
        self.sobre_janela = None  # <-- Controlador da janela "Sobre"

    def autenticar(self, usuario, senha):
        try:
            if self.user_dao.autenticar(usuario, senha):
                self.view.withdraw()
                user_login = self.user_dao.usuario(usuario)

                self.abrir_principal(user_login)
            else:
                               
                self.view.exibir_erro("Usuário ou senha incorretos")
        finally:
            self.db.close()

    def abrir_principal(self, user_login):
        principal = PrincipalView(self.view, user_login)
        principal.grab_set()

    def abrir_sobre(self):
        if self.sobre_janela is None or not self.sobre_janela.winfo_exists():
            self.sobre_janela = SobreView(self.view)
            
        else:
            self.sobre_janela.focus_force()  # Foca na janela já aberta
