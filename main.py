from gui.tela_principal import JanelaPrincipal


class StartAplicacao:
    # Criar as janelas iniciais
    janelaprincipal = JanelaPrincipal()
    janelaprincipal.janela = janelaprincipal.retorna_janela()
    janelaprincipal.iniciar_tela()

