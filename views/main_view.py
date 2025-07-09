import customtkinter as ctk
from controllers.main_controller import MainController
from utils import centralizar_janela_multi
from tkinter import messagebox

class MainView(ctk.CTkToplevel):
    def __init__(self, master, user_login):
        super().__init__(master)
        self.master = master
        self.user_login = user_login
        self.title("Tela Principal")
        self.geometry("1366x786")
        largura = 1366
        altura = 786
        centralizar_janela_multi(self, largura, altura)
        self.controller = MainController(self)

        self.label = ctk.CTkLabel(self, text=f"Bem-vindo! {self.user_login.username}")
        self.label.pack(pady=20)

        self.btn_crud = ctk.CTkButton(self, text="Abrir CRUD", command=self.controller.open_crud)
        self.btn_crud.pack(pady=10)

        self.btn_sair = ctk.CTkButton(self, text="Sair", command=self.controller.exit)
        self.btn_sair.pack(pady=10)

        self.protocol("WM_DELETE_WINDOW", self.fechar)

    def fechar(self):
        
        if messagebox.askyesno("Sair", "Deseja realmente sair?"):
            self.destroy()
            self.master.deiconify()  # Reexibe janela de login se fechar principal
