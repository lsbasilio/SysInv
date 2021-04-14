import PySimpleGUI as sg
from gui.tela_centro_de_custo import JanelaCcusto
from util import util


# Criar as janelas e estilos (layout)
class JanelaPrincipal:

    janela = None

    def __init__(self):

        self.window, self.event, self.values = None, None, None
        size_botao = 25

        # Criar as janelas iniciais
        #self.janela = None
        self.janela_ccusto = None
        self.janelaccusto = None

        sg.theme(util.get_tema_janelas())

        self.layout = [
            [sg.Image(filename=f'Imagens\BarCode.png', size=(200, 200))],
            [sg.Button('Ativar Centro de Custo', size=(size_botao,0))],
            [sg.Button('Iniciar Inventário', size=(size_botao,0))],
            [sg.Button('Locais', size=(size_botao,0))],
            [sg.Button('Descr. Padrão', size=(size_botao,0))],
            [sg.Button('Descr. Complementar', size=(size_botao,0))],
            [sg.Button('Consultar Bens', size=(size_botao,0))]
        ]

    def retorna_janela(self):
        # Retorna Janela Principal
        self.janela = sg.Window('Tela Principal', layout=self.layout, finalize=True)
        return self.janela
        #return sg.Window('Tela Principal', layout=self.layout, finalize=True)


    def iniciar_tela(self):

        # Cria um loop de leitura de eventos
        while True:

            self.window, self.event, self.values = sg.read_all_windows()

            # Quando a janela principal for fechada
            if self.window == self.janela and self.event == sg.WINDOW_CLOSED:
                print('Fechou')
                self.janela.close()
                exit()
                break

            # Quando a janela de Centro de Custo for fechada
            if self.window == JanelaCcusto.janela and self.event == sg.WINDOW_CLOSED:
                self.janela_ccusto.hide()
                self.janela.un_hide()

            print('Voltou')

            # Quando queremos ir para outra janela
            if self.window == self.janela and self.event == 'Ativar Centro de Custo':
                print('Entrou')
                self.janela.hide()
                if self.janela_ccusto is None:
                    self.janelaccusto = JanelaCcusto()
                    self.janela_ccusto = self.janelaccusto.retorna_janela()
                    self.janelaccusto.janelaprincipal = self.janela
                    self.janelaccusto.iniciar_tela()
                else:
                    self.janela_ccusto.un_hide()

                #print(self.janela_ccusto.values['ccusto'])


