import PySimpleGUI as sg
from gui.tela_centro_de_custo import JanelaCcusto
from gui.tela_locais import JanelaLocais
from util import util


# Criar as janelas e estilos (layout)
class JanelaPrincipal:

    janela = None

    def __init__(self):

        self.window, self.event, self.values = None, None, None

        size_botao = 25

        # Criar as janelas do Centro de Custo
        self.janela_ccusto = None
        self.janelaccusto = None  # Objeto da classe JanelaCcusto

        # Criar as janelas dos Locais
        self.janela_local  = None
        self.janelalocal = None  # Objeto da classe JanelaLocais


        sg.theme(util.get_tema_janelas())

        self.layout = [
            [sg.Image(filename=f'Imagens\BarCode.png', size=(100, 100))],
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
        self.janela_ccusto = None
        self.janela_local = None
        return self.janela

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
            if self.window == self.janela_ccusto and self.event == sg.WINDOW_CLOSED:
                self.janela_ccusto.hide()
                self.janela.un_hide()

            # Quando a janela de Local for fechada
            if self.window == self.janela_local and self.event == sg.WINDOW_CLOSED:
                self.janela_local.hide()
                self.janela.un_hide()

            # Quando queremos ir para janela de Centro de Custo
            if self.window == self.janela and self.event == 'Ativar Centro de Custo':
                self.janela.hide()
                self.janelaccusto = JanelaCcusto()
                self.janela_ccusto = sg.Window('Centro de Custo', layout=self.janelaccusto.layout, finalize=True)

            # Eventos da Janela de Centro de Custo
            if self.window == self.janela_ccusto and self.event == 'ccusto':
                ccusto_id = util.get_id(self.values['ccusto'])
                self.janelaccusto.get_dados(self.janela_ccusto, ccusto_id)

            # Quando queremos ir para janela de Local
            if self.window == self.janela and self.event == 'Locais':
                self.janela.hide()
                self.janelalocal = JanelaLocais()
                self.janela_local = sg.Window('Locais', layout=self.janelalocal.layout, finalize=True)

            # Eventos da Janela de Local
            if self.window == self.janela_local and self.event == 'locais':
                local_id = util.get_id(self.values['locais'])
                self.janelalocal.get_dados(self.janela_local, local_id)
