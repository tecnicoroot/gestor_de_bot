from database.db import SessionLocal, engine
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from views.main_view import MainView
from views.about_view import AboutView
from services.user_service import UserService
class LoginController:
    def __init__(self, view):
        self.view = view
        self.db = SessionLocal()
        self.user_service = UserService(SessionLocal)
        self.about_window = None  # <-- Controlador da janela "Sobre"

    def authenticate(self, user, senha):
        try:
            if self.user_service.authenticate_user(user, senha):
                self.view.withdraw()
                user_login = self.user_service.search_user_name(user)
                self.open_main(user_login)
            else:
                               
                self.view.show_error("Usuário ou senha incorretos")
        finally:
            self.db.close()

    def open_main(self, user_login):
        principal = MainView(self.view, user_login)
        principal.grab_set()

    def show_about(self):
        if self.about_window is None or not self.about_window.winfo_exists():
            self.about_window = AboutView(self.view)
            
        else:
            self.about_window.focus_force()  # Foca na janela já aberta
