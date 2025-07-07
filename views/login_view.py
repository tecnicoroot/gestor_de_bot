import customtkinter as ctk
from controllers.login_controller import LoginController
from utils import centralizar_janela_multi , rgb_para_hex# se estiver separado
import tkinter.font as tkfont  # Certifique-se de importar isso no início do seu arquivo

class LoginView(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Login")
        self.geometry("300x200")
        
        self.configure(fg_color="#aee1ab")  # OK: define cor de fundo da janela
        centralizar_janela_multi(self, 300, 200)
        
        self.controller = LoginController(self)

        # Configure grid layout
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=2)

        # Usuário
        bold_font = ctk.CTkFont(family="Arial", size=12, weight="bold")
        self.label_user = ctk.CTkLabel(self, text="Usuário", font=bold_font)
        self.label_user.grid(row=0, column=0, padx=10, pady=(20, 5))

        self.entry_user = ctk.CTkEntry(self)
        self.entry_user.grid(row=0, column=1, padx=10, pady=(15, 5), sticky="we")
        # Evento ao focar (clicar)
        self.entry_user.bind("<FocusIn>", lambda e: self.entry_user.configure(border_color=rgb_para_hex(0,128,0)))
        # Evento ao perder o foco (clicar fora)
        self.entry_user.bind("<FocusOut>", lambda e: self.entry_user.configure(border_color="gray"))
        
        # Senha
        self.label_pass = ctk.CTkLabel(self, text="Senha", font=bold_font)
        self.label_pass.grid(row=1, column=0, padx=10, pady=5)

        self.entry_pass = ctk.CTkEntry(self, show="*")
        self.entry_pass.grid(row=1, column=1, padx=10, pady=5, sticky="we")

        # Botão de login
        self.btn_login = ctk.CTkButton(self, text="Entrar", command=self.autenticar)
        self.btn_login.grid(row=2, column=0, columnspan=2, pady=5)

        self.link_sobre = ctk.CTkLabel(self, text="Sobre", text_color="blue", cursor="hand2")
        self.link_sobre.grid(row=3, column=0, columnspan=2, pady=1)

        # Sublinha o texto (simulando um link)
        font_link = ctk.CTkFont(underline=True)
        self.link_sobre.configure(font=font_link)

        # Evento de clique
        self.link_sobre.bind("<Button-1>", lambda e: self.exibir_sobre())
        self.link_sobre.bind("<Enter>", lambda e: self.link_sobre.configure(text_color="darkblue"))
        self.link_sobre.bind("<Leave>", lambda e: self.link_sobre.configure(text_color="blue"))

        # Mensagem de erro
        self.label_erro = ctk.CTkLabel(self, text="", text_color="red")
        self.label_erro.grid(row=4, column=0, columnspan=2)

        # Enter para login
        self.bind("<Return>", lambda event: self.autenticar())
        self.entry_user.focus_set()

    def autenticar(self):
        usuario = self.entry_user.get()
        senha = self.entry_pass.get()
        self.label_erro.configure(text="")  # limpa antes de tentar
        self.controller.autenticar(usuario, senha)

    
    def exibir_sobre(self):
        self.controller.abrir_sobre()
    
    def exibir_erro(self, mensagem):
        
        if self.label_erro:
            self.label_erro.configure(text=mensagem)
        