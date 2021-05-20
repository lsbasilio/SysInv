import PySimpleGUI as sg
from util import util


class JanelaTrocaNumero:

    size_input = util.size_input

    def __init__(self):

        self.window, self.event, self.values = None, None, None
        sg.theme(util.get_tema_janelas())

        self.layout = [
            [sg.Text('Número Atual')],
            [sg.Input(size=(self.size_input, 1), key='numero_atual')],
            [sg.Text('Novo Número')],
            [sg.Input(size=(self.size_input, 1), key='numero_novo')],
            [sg.Button('Trocar', size=(8, 1)), sg.Button('Sair', size=(8, 1))]
        ]