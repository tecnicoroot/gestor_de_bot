from screeninfo import get_monitors
import tkinter as tk
from typing import Union

def centralizar_janela_multi(janela: Union[tk.Tk, tk.Toplevel], largura: int, altura: int, forcar_visivel: bool = True):
    """
    Centraliza a janela na tela onde ela está atualmente, suportando múltiplos monitores.

    :param janela: instância Tk ou Toplevel
    :param largura: largura desejada (pixels)
    :param altura: altura desejada (pixels)
    :param forcar_visivel: se True, impede que a janela fique em posição negativa
    """
    janela.update_idletasks()
    x_win = janela.winfo_x()
    y_win = janela.winfo_y()

    # Determina o monitor ativo usando coordenadas da janela
    monitores = get_monitors()
    monitor = None
    for m in reversed(monitores):
        if m.x <= x_win <= m.x + m.width and m.y <= y_win <= m.y + m.height:
            monitor = m
            break
    if monitor is None:
        monitor = next((m for m in monitores if m.is_primary), monitores[0])

    # Calcula posição central no monitor selecionado
    pos_x = monitor.x + (monitor.width - largura) // 2
    pos_y = monitor.y + (monitor.height - altura) // 2

    # Garante visibilidade caso forcar_visivel=True
    if forcar_visivel:
        pos_x = max(pos_x, monitor.x)
        pos_y = max(pos_y, monitor.y)

    janela.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")




def rgb_para_hex(r, g, b):
    return f"#{r:02x}{g:02x}{b:02x}"