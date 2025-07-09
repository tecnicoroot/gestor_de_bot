import platform
import customtkinter as ctk
from utils import centralizar_janela_multi  # Certifique-se de que está implementado

class CrudExemploView(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.title("CRUD Exemplo")

        # Ajuste de DPI para Linux
        if platform.system() == "Linux":
            ctk.set_window_scaling(1.1)

        width, height = 420, 240
        self.geometry(f"{width}x{height}")
        self.configure(fg_color="#f0f0f0")  # Cor de fundo neutra
        centralizar_janela_multi(self, width, height)

        self.resizable(False, False)
        self.transient(master)
        self.focus_force()
        self.protocol("WM_DELETE_WINDOW", self.close)

        # Fonte segura
        fonte_padrao = ctk.CTkFont(family="Helvetica", size=14, weight="bold")

        # Label inicial
        self.label = ctk.CTkLabel(self, text="CRUD de Exemplo", font=fonte_padrao, text_color="#2e7d32")
        self.label.pack(pady=(30, 20))

        # Aqui você poderá adicionar futuramente: campos, botões, tabelas, etc.

    def close(self):
        self.destroy()
