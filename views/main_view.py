import platform
import customtkinter as ctk
from tkinter import messagebox

from controllers.main_controller import MainController
from utils import centralizar_janela_multi


class MainView(ctk.CTkToplevel):
    def __init__(self, master, user_login):
        super().__init__(master)
        self.master = master
        self.user_login = user_login
        self.title("Tela Principal")

        # Ajuste de DPI para Linux
        if platform.system() == "Linux":
            ctk.set_window_scaling(1.1)

        # Tamanho e centralização
        largura, altura = 1366, 768
        self.geometry(f"{largura}x{altura}")
        self.configure(fg_color="#f8f8f8")
        centralizar_janela_multi(self, largura, altura)

        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", self.fechar)

        # Controlador principal
        self.controller = MainController(self)

        # Fonte padrão
        fonte_titulo = ctk.CTkFont(family="Helvetica", size=20, weight="bold")
        fonte_botoes = ctk.CTkFont(family="Helvetica", size=14)

        # Label de boas-vindas
        self.label = ctk.CTkLabel(
            self,
            text=f"Bem-vindo! {self.user_login.username}",
            font=fonte_titulo,
            text_color="#2e7d32"
        )
        self.label.pack(pady=40)

        # Botão para abrir CRUD
        self.btn_crud = ctk.CTkButton(
            self,
            text="Abrir CRUD",
            font=fonte_botoes,
            command=self.controller.open_crud
        )
        self.btn_crud.pack(pady=10)

        # Botão de sair
        self.btn_sair = ctk.CTkButton(
            self,
            text="Sair",
            font=fonte_botoes,
            command=self.controller.exit
        )
        self.btn_sair.pack(pady=10)

    def fechar(self):
        if messagebox.askyesno("Sair", "Deseja realmente sair?"):
            self.destroy()
            self.master.deiconify()  # Reexibe janela de login
