import platform
import customtkinter as ctk
import tkinter.font as tkfont

from utils import centralizar_janela_multi, rgb_para_hex


class AboutView(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.title("Sobre")

        # Detectar sistema operacional para possível ajuste de DPI
        if platform.system() == "Linux":
            ctk.set_window_scaling(1.1)

        width, height = 320, 240
        self.geometry(f"{width}x{height}")
        self.configure(fg_color="#aee1ab")

        centralizar_janela_multi(self, width, height)

        self.resizable(False, False)
        self.transient(master)  # Janela modal
        self.focus_force()

        # Aplica grab_set após um pequeno atraso
        self.after(10, self.apply_grab)

        # Fecha ao clicar no "X"
        self.protocol("WM_DELETE_WINDOW", self.close)

        # Fontes multiplataforma
        fonte_titulo = ctk.CTkFont(family="Helvetica", size=16, weight="bold")
        fonte_texto = ctk.CTkFont(family="Helvetica", size=12)

        # Título
        self.label_title = ctk.CTkLabel(
            self,
            text="Aplicativo Exemplo",
            font=fonte_titulo,
            text_color="#2e7d32"
        )
        self.label_title.pack(pady=(20, 10))

        # Descrição
        descricao = (
            "Este aplicativo foi desenvolvido para fins educacionais.\n\n"
            "Versão 1.0\n\n"
            "Desenvolvido por:\nDavid Luis da Silva / ChatGPT."
        )

        self.label_description = ctk.CTkLabel(
            self,
            text=descricao,
            font=fonte_texto,
            text_color="#1b5e20",
            justify="center",
            wraplength=280
        )
        self.label_description.pack(pady=(0, 20), padx=10)

    def apply_grab(self):
        try:
            self.grab_set()
        except Exception as e:
            print(f"Erro ao aplicar grab_set: {e}")

    def close(self):
        self.master.about_window = None
        self.destroy()
