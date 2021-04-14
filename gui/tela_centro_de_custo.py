import PySimpleGUI as sg
from util import util


# Criar as janelas e estilos (layout)
class JanelaCcusto:

    def __init__(self):

        self.window, self.event, self.values = None, None, None

        sg.theme(util.get_tema_janelas())

        self.layout = [
            [sg.Text('Centro de Custo')]
        ]

    def retorna_janela(self):
        # Retorna Janela Centro de Custo
        return sg.Window('Centro de Custo', layout=self.layout, finalize=True)

    def iniciar_tela(self):
        pass
