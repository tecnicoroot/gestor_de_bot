import customtkinter as ctk
from controllers.login_controller import LoginController
from utils import centralizar_janela  # se estiver separado

class LoginView(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Login")
        self.geometry("300x200")
        largura = 300
        altura = 200
        centralizar_janela(self, largura, altura)

        self.controller = LoginController(self)

        # Configure grid layout
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=2)

        # Usuário
        self.label_user = ctk.CTkLabel(self, text="Usuário")
        self.label_user.grid(row=0, column=0, padx=10, pady=(20, 5), sticky="e")

        self.entry_user = ctk.CTkEntry(self)
        self.entry_user.grid(row=0, column=1, padx=10, pady=(15, 5), sticky="we")

        # Senha
        self.label_pass = ctk.CTkLabel(self, text="Senha")
        self.label_pass.grid(row=1, column=0, padx=10, pady=5, sticky="e")

        self.entry_pass = ctk.CTkEntry(self, show="*")
        self.entry_pass.grid(row=1, column=1, padx=10, pady=5, sticky="we")

        # Botão de login
        self.btn_login = ctk.CTkButton(self, text="Entrar", command=self.autenticar)
        self.btn_login.grid(row=2, column=0, columnspan=2, pady=10)

        # Mensagem de erro
        self.label_erro = ctk.CTkLabel(self, text="", text_color="red")
        self.label_erro.grid(row=3, column=0, columnspan=2)

        # Enter para login
        self.bind("<Return>", lambda event: self.autenticar())
        self.entry_user.focus_set()

    def autenticar(self):
        usuario = self.entry_user.get()
        senha = self.entry_pass.get()
        self.label_erro.configure(text="")  # limpa antes de tentar
        self.controller.autenticar(usuario, senha)

    def exibir_erro(self, mensagem):
        print(f"Exibindo erro: {mensagem}")  # ← Debug
        if self.label_erro:
            self.label_erro.configure(text=mensagem)
        