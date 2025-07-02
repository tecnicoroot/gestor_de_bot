from views.crud_exemplo_view import CrudExemploView
from tkinter import messagebox

class PrincipalController:
    def __init__(self, view):
        self.view = view

    def abrir_crud(self):
        crud = CrudExemploView(self.view)
        crud.grab_set()

    def sair(self):
        if messagebox.askyesno("Sair", "Deseja realmente sair?"):
            self.view.destroy()
            self.view.master.deiconify()  # Reexibe login
