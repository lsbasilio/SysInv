import PySimpleGUI as sg
from model.entities.bens import Bens
from model.services.bensservice import BensService
from util import util


# Criar as janelas e estilos (layout)
class JanelaInventario:

    entity = Bens()
    service = BensService()

    lista = []

    size_input = util.size_input

    def __init__(self):

        self.window, self.event, self.values = None, None, None

        sg.theme(util.get_tema_janelas())

        self.col_layout = [
            [sg.Text('Centro de Custo Ativo')],
            [sg.Input(size=(self.size_input, 1), key='ccustoativo')],
            [sg.Text('Número do Bem', size=(20, 1)), sg.Text('Número Anterior')],
            [sg.Input(size=(23, 1)), sg.Input(size=(22, 1))],
            [sg.Text('Centro de Custo Atual')],
            [sg.Input(size=(self.size_input, 1), key='ccustoatual')],
            [sg.Text('Descrição Padrão')],
            [sg.Combo(self.lista, size=(util.width_combo, util.height_combo), readonly=True, enable_events=True,
                    key='descrpadrao')],
            [sg.Text('Descrição do Bem')],
            [sg.Multiline(enter_submits=False, autoscroll=True, size=(self.size_input - 2, 5))],
            [sg.Text('Situação')],
            [sg.Input(size=(self.size_input, 1))],
            [sg.Text('Descrição Complementar')],
            [sg.Combo(self.lista, size=(util.width_combo, util.height_combo), readonly=True, enable_events=True,
                      key='descrcomplementar')],
            [sg.Multiline(enter_submits=False, autoscroll=True, size=(self.size_input - 2, 5))],
            [sg.Text('Marca')],
            [sg.Input(size=(self.size_input, 1))],
            [sg.Text('Modelo')],
            [sg.Input(size=(self.size_input, 1))],
            [sg.Text('Número de Série')],
            [sg.Input(size=(self.size_input, 1))],
            [sg.Text('Usuário')],
            [sg.Input(size=(self.size_input, 1))],
            [sg.Text('Observação')],
            [sg.Input(size=(self.size_input, 1))],
            [sg.Text('Status do Bem')],
            [sg.Input(size=(self.size_input, 1))],
            [sg.Button('Inventariar', size=(9, 1)), sg.Button('Limpar', size=(8, 1)), sg.Button('Próxima >>', size=(9, 1)), sg.Button('Sair', size=(8, 1))]
        ]

        self.layout = [[sg.Column(self.col_layout, scrollable=True, vertical_scroll_only=True, size=(400, 400))]]

