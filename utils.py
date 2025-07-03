def centralizar_janela(janela, largura, altura, forcar_visivel=False):
    """
    Centraliza a janela na tela, com suporte para monitores com diferentes resoluções e escalas DPI.
    
    :param janela: instância da janela (Tk, CTk ou Toplevel)
    :param largura: largura desejada da janela
    :param altura: altura desejada da janela
    :param forcar_visivel: garante que a janela não fique fora da tela mesmo em setups com múltiplos monitores
    """
    janela.update_idletasks()  # Atualiza geometria interna antes de medir

    # Obtém dimensões da tela
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()
    print(f" {largura_tela} X{altura_tela}")
    # Calcula coordenadas para centralizar
    pos_x = int((largura_tela / 2) - (largura / 2))
    
    pos_y = int((altura_tela / 2) - (altura / 2))

    # Opcional: evita posições negativas caso a janela seja maior que a tela
    if forcar_visivel:
        pos_x = max(pos_x, 0)
        pos_y = max(pos_y, 0)

    print(f"{largura}x{altura}+{pos_x}+{pos_y}")
    janela.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")



def rgb_para_hex(r, g, b):
    return f"#{r:02x}{g:02x}{b:02x}"