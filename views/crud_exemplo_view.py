import customtkinter as ctk

class CrudExemploView(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("CRUD Exemplo")
        self.geometry("400x200")

        self.label = ctk.CTkLabel(self, text="CRUD de exemplo")
        self.label.pack(pady=10)
