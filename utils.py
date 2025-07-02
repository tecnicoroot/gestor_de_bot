def centralizar_janela(janela, largura, altura):
    janela.update_idletasks()  # Garante que a geometria esteja correta
    
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()

    pos_x = (largura_tela -largura) // 2
    pos_y = (altura_tela  - altura) // 2

    janela.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")
