import PySimpleGUI as sg
from gui.tela_centro_de_custo import JanelaCcusto


# Criar as janelas e estilos (layout)
class JanelaPrincipal:

    def __init__(self):

        self.window, self.event, self.values = None, None, None
        size_botao = 25

        # Criar as janelas iniciais
        self.janela = None
        self.janela_ccusto = None

        sg.theme('DarkTeal7')

        self.layout = [
            [sg.Button('Ativar Centro de Custo', size=(size_botao,0))],
            [sg.Button('Iniciar Inventário', size=(size_botao,0))],
            [sg.Button('Locais', size=(size_botao,0))],
            [sg.Button('Descr. Padrão', size=(size_botao,0))],
            [sg.Button('Descr. Complementar', size=(size_botao,0))],
            [sg.Button('Consultar Bens', size=(size_botao,0))]
        ]

    def retorna_janela(self):
        # Retorna Janela Principal
        #self.janela = sg.Window('Tela Principal', layout=layout, finalize=True)
        return sg.Window('Tela Principal', layout=self.layout, finalize=True)


    def iniciar_tela(self):
        # Cria um loop de leitura de eventos
        while True:
            self.window, self.event, self.values = sg.read_all_windows()

            # Quando a janela principal for fechada
            if self.window == self.janela and self.event == sg.WINDOW_CLOSED:
                self.janela.close()
                break

            # Quando a janela de Centro de Custo for fechada
            if self.window == self.janela_ccusto and self.event == sg.WINDOW_CLOSED:
                print('Fechou')
                self.janela_ccusto.hide()
                self.janela.un_hide()

            # Quando queremos ir para outra janela
            if self.window == self.janela and self.event =='Ativar Centro de Custo':
                print('Entrou')
                self.janela.hide()
                self.janelaccusto = JanelaCcusto()
                self.janela_ccusto = self.janelaccusto.retorna_janela()
                self.janelaccusto.iniciar_tela()
                

# Criar as janelas iniciais
janelaprincipal = JanelaPrincipal()
janelaprincipal.janela = janelaprincipal.retorna_janela()
janelaprincipal.iniciar_tela()