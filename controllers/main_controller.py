from views.crud_exemplo_view import CrudExemploView
from tkinter import messagebox
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
class MainController:
    def __init__(self, view):
        self.view = view

    def open_crud(self):
        crud = CrudExemploView(self.view)
        crud.grab_set()

    def exit(self):
        if messagebox.askyesno("Sair", "Deseja realmente sair?"):
            self.view.destroy()
            self.view.master.deiconify()  # Reexibe login
