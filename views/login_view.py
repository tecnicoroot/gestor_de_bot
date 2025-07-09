import platform
import customtkinter as ctk
import tkinter.font as tkfont

from controllers.login_controller import LoginController
from utils import centralizar_janela_multi, rgb_para_hex


class LoginView(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Detecta o sistema operacional
        sistema = platform.system()

        # Escalonamento para Linux (DPI pode variar)
        if sistema == "Linux":
            ctk.set_window_scaling(1.1)

        self.title("Login")
        largura, altura = 320, 220
        self.geometry(f"{largura}x{altura}")
        self.configure(fg_color="#aee1ab")
        centralizar_janela_multi(self, largura, altura)

        self.controller = LoginController(self)

        # Configuração de layout responsivo
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=2)

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)

        # Fonte multiplataforma
        fonte_padrao = ctk.CTkFont(family="Helvetica", size=12, weight="bold")

        # Label Usuário
        self.label_user = ctk.CTkLabel(self, text="Usuário", font=fonte_padrao)
        self.label_user.grid(row=0, column=0, padx=10, pady=(20, 5), sticky="e")

        self.entry_user = ctk.CTkEntry(self)
        self.entry_user.grid(row=0, column=1, padx=10, pady=(15, 5), sticky="we")

        self.entry_user.bind("<FocusIn>", lambda e: self.entry_user.configure(border_color=rgb_para_hex(0, 128, 0)))
        self.entry_user.bind("<FocusOut>", lambda e: self.entry_user.configure(border_color="gray"))

        # Label Senha
        self.label_pass = ctk.CTkLabel(self, text="Senha", font=fonte_padrao)
        self.label_pass.grid(row=1, column=0, padx=10, pady=5, sticky="e")

        self.entry_pass = ctk.CTkEntry(self, show="*")
        self.entry_pass.grid(row=1, column=1, padx=10, pady=5, sticky="we")

        # Botão Entrar
        self.btn_login = ctk.CTkButton(self, text="Entrar", command=self.autenticar)
        self.btn_login.grid(row=2, column=0, columnspan=2, pady=5, padx=20, sticky="we")

        # Link "Sobre"
        font_link = ctk.CTkFont(underline=True)
        self.link_about = ctk.CTkLabel(self, text="Sobre", text_color="blue", cursor="hand2", font=font_link)
        self.link_about.grid(row=3, column=0, columnspan=2, pady=1)

        self.link_about.bind("<Button-1>", lambda e: self.show_about())
        self.link_about.bind("<Enter>", lambda e: self.link_about.configure(text_color="darkblue"))
        self.link_about.bind("<Leave>", lambda e: self.link_about.configure(text_color="blue"))

        # Mensagem de erro
        self.label_erro = ctk.CTkLabel(self, text="", text_color="red")
        self.label_erro.grid(row=4, column=0, columnspan=2)

        # Enter para autenticar
        self.bind("<Return>", lambda event: self.autenticar())
        self.entry_user.focus_set()

    def autenticar(self):
        user = self.entry_user.get()
        password = self.entry_pass.get()
        self.label_erro.configure(text="")  # limpa antes de tentar
        self.controller.authenticate(user, password)

    def show_about(self):
        self.controller.show_about()

    def show_error(self, mensagem):
        if self.label_erro:
            self.label_erro.configure(text=mensagem)
