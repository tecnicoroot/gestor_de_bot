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
        self.title("Sistema de Gestão")

        if platform.system() == "Linux":
            ctk.set_window_scaling(1.1)

        largura, altura = 1200, 700
        self.geometry(f"{largura}x{altura}")
        centralizar_janela_multi(self, largura, altura)
        self.configure(fg_color="#f5f5f5")
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", self.fechar)

        self.controller = MainController(self)

        # Fontes
        self.font_titulo = ctk.CTkFont(family="Helvetica", size=18, weight="bold")
        self.font_padrao = ctk.CTkFont(family="Helvetica", size=14)

        # Layout: Sidebar + Main Frame
        self.sidebar = ctk.CTkFrame(self, width=200, corner_radius=0, fg_color="#e0e0e0")
        self.sidebar.pack(side="left", fill="y")

        self.main_frame = ctk.CTkFrame(self, corner_radius=10, fg_color="white")
        self.main_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        # Sidebar (menu lateral)
        ctk.CTkLabel(self.sidebar, text="Menu", font=self.font_titulo, text_color="#2e7d32").pack(pady=(20, 10))

        self.btn_dashboard = ctk.CTkButton(self.sidebar, text="Dashboard", font=self.font_padrao, command=lambda: self.mostrar_frame("dashboard"))
        self.btn_dashboard.pack(pady=5, fill="x", padx=10)

        self.btn_crud = ctk.CTkButton(self.sidebar, text="CRUD Exemplo", font=self.font_padrao, command=lambda: self.mostrar_frame("crud"))
        self.btn_crud.pack(pady=5, fill="x", padx=10)

        self.btn_settings = ctk.CTkButton(self.sidebar, text="Configurações", font=self.font_padrao, command=lambda: self.mostrar_frame("settings"))
        self.btn_settings.pack(pady=5, fill="x", padx=10)

        self.btn_logout = ctk.CTkButton(self.sidebar, text="Sair", font=self.font_padrao, fg_color="red", hover_color="#990000", command=self.controller.exit)
        self.btn_logout.pack(pady=(40, 10), fill="x", padx=10)

        # Header
        self.header = ctk.CTkFrame(self.main_frame, fg_color="#f0f0f0", height=60)
        self.header.pack(fill="x", padx=10, pady=(10, 0))

        self.label_user = ctk.CTkLabel(self.header, text=f"Bem-vindo, {self.user_login.username}!", font=self.font_titulo, text_color="#1b5e20")
        self.label_user.pack(side="left", padx=20)

        # Área de conteúdo
        self.content = ctk.CTkFrame(self.main_frame, fg_color="white")
        self.content.pack(fill="both", expand=True, padx=10, pady=10)

        # Rodapé
        self.footer = ctk.CTkLabel(self.main_frame, text="© 2025 - Sistema Exemplo", font=("Helvetica", 10), text_color="gray")
        self.footer.pack(side="bottom", pady=10)

        # Frames reutilizáveis
        self.frames = {
            "dashboard": self.criar_frame_dashboard(),
            "crud": self.criar_crud_frame(),
            "settings": self.criar_configuracoes_frame()
        }

        self.mostrar_frame("dashboard")

    # ========== SEÇÕES ==========
    def criar_frame_dashboard(self):
        frame = ctk.CTkFrame(self.content, fg_color="white")
        label = ctk.CTkLabel(frame, text="Painel Principal", font=self.font_titulo, text_color="#2e7d32")
        label.pack(pady=40)
        return frame

    def criar_crud_frame(self):
        frame = ctk.CTkFrame(self.content, fg_color="white")

        label = ctk.CTkLabel(frame, text="Área de Cadastro de Usuários", font=self.font_titulo, text_color="#1e88e5")
        label.pack(pady=20)

        # Campos do formulário
        self.entry_nome = ctk.CTkEntry(frame, placeholder_text="Nome do usuário")
        self.entry_nome.pack(pady=5, padx=10)

        self.entry_email = ctk.CTkEntry(frame, placeholder_text="E-mail")
        self.entry_email.pack(pady=5, padx=10)

        self.entry_senha = ctk.CTkEntry(frame, placeholder_text="Senha", show="*")
        self.entry_senha.pack(pady=5, padx=10)

        # Botões de ação (simulados)
        btn_salvar = ctk.CTkButton(frame, text="Salvar", command=self.salvar_usuario)
        btn_salvar.pack(pady=(10, 2))

        btn_listar = ctk.CTkButton(frame, text="Listar usuários", command=self.listar_usuarios)
        btn_listar.pack(pady=2)

        btn_voltar = ctk.CTkButton(frame, text="Voltar", fg_color="gray", command=lambda: self.mostrar_frame("dashboard"))
        btn_voltar.pack(pady=(20, 0))

        return frame

    def criar_configuracoes_frame(self):
        frame = ctk.CTkFrame(self.content, fg_color="white")

        label = ctk.CTkLabel(frame, text="Configurações do Sistema", font=self.font_titulo, text_color="#f57c00")
        label.pack(pady=20)

        # Alternador de tema
        switch = ctk.CTkSwitch(frame, text="Modo escuro (visual)", command=self.alternar_tema)
        switch.pack(pady=10)

        # Entrada de tema padrão (simulada)
        entry_tema_padrao = ctk.CTkEntry(frame, placeholder_text="Tema padrão (ex: light/dark)")
        entry_tema_padrao.pack(pady=5, padx=10)

        return frame

    # ========== FUNÇÕES ==========
    def mostrar_frame(self, nome):
        for key, frame in self.frames.items():
            frame.pack_forget()  # esconde todos os frames
        frame = self.frames.get(nome)
        if frame:
            frame.pack(fill="both", expand=True)  # mostra só o frame desejado

    def alternar_tema(self):
        atual = ctk.get_appearance_mode()
        novo = "light" if atual == "dark" else "dark"
        ctk.set_appearance_mode(novo)

    def salvar_usuario(self):
        nome = self.entry_nome.get()
        email = self.entry_email.get()
        senha = self.entry_senha.get()
        print(f"Salvar: {nome}, {email}, {senha}")  # Substitua por lógica de banco de dados

    def listar_usuarios(self):
        print("Listar usuários...")  # Substitua por lógica de leitura

    def fechar(self):
        if messagebox.askyesno("Sair", "Deseja realmente sair?"):
            self.destroy()
            self.master.deiconify()
