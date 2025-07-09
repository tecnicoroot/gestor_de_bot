import customtkinter as ctk
from utils import centralizar_janela_multi, rgb_para_hex  # Certifique-se que esses utilitários existem
import tkinter.font as tkfont  # Para customizar fontes

class AboutView(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.title("Sobre")
        width = 300
        height = 200
        self.configure(fg_color="#aee1ab")
        centralizar_janela_multi(self, width, height)

        self.resizable(False, False)
        self.transient(master)
        self.focus_force()

        # Espera 10 ms antes de aplicar o grab_set
        self.after(10, self.apply_grab)

        # Evento de fechamento
        self.protocol("WM_DELETE_WINDOW", self.close)

        # Conteúdo
        # Define uma fonte customizada
        source_title = ctk.CTkFont(family="Helvetica", size=16, weight="bold")
        source_text = ctk.CTkFont(family="Helvetica", size=12)

        # Título
        self.label_title = ctk.CTkLabel(self, text="Aplicativo Exemplo", font=source_title, text_color="#2e7d32")
        self.label_title.pack(pady=(20, 10))

        # Texto de descrição
        self.label_description = ctk.CTkLabel(
            self,
            text="Este aplicativo foi desenvolvido para fins educacionais.\n\n\nVersão 1.0\n\n\nDesenvolvido por \nDavid Luis da Silva / ChatGPT.",
            font=source_text,
            text_color="#1b5e20",
            justify="center",
            wraplength=250  # ← define a width máxima do texto antes de quebrar
        )
        self.label_description.pack(pady=(0, 20),padx=(10))
    def apply_grab(self):
        try:
            self.grab_set()
        except Exception as e:
            print(f"Erro ao aplicar grab_set: {e}")

    def close(self):
        self.master.about_window = None
        self.destroy()


