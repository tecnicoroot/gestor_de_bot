import customtkinter as ctk
from utils import centralizar_janela, rgb_para_hex  # Certifique-se que esses utilitários existem
import tkinter.font as tkfont  # Para customizar fontes

class SobreView(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.title("Sobre")
        largura = 300
        altura = 200
        self.configure(fg_color="#aee1ab")
        centralizar_janela(self, largura, altura)

        self.resizable(False, False)
        self.transient(master)
        self.focus_force()

        # Espera 10 ms antes de aplicar o grab_set
        self.after(10, self.aplicar_grab)

        # Evento de fechamento
        self.protocol("WM_DELETE_WINDOW", self.fechar)

        # Conteúdo
        # Define uma fonte customizada
        fonte_titulo = ctk.CTkFont(family="Helvetica", size=16, weight="bold")
        fonte_texto = ctk.CTkFont(family="Helvetica", size=12)

        # Título
        self.label_titulo = ctk.CTkLabel(self, text="Aplicativo Exemplo", font=fonte_titulo, text_color="#2e7d32")
        self.label_titulo.pack(pady=(20, 10))

        # Texto de descrição
        self.label_descricao = ctk.CTkLabel(
            self,
            text="Este aplicativo foi desenvolvido para fins educacionais.\n\n\nVersão 1.0\n\n\nDesenvolvido por \nDavid Luis da Silva / ChatGPT.",
            font=fonte_texto,
            text_color="#1b5e20",
            justify="center",
            wraplength=250  # ← define a largura máxima do texto antes de quebrar
        )
        self.label_descricao.pack(pady=(0, 20),padx=(10))
    def aplicar_grab(self):
        try:
            self.grab_set()
        except Exception as e:
            print(f"Erro ao aplicar grab_set: {e}")

    def fechar(self):
        self.master.sobre_janela = None
        self.destroy()


