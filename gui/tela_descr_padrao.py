import PySimpleGUI as sg
from model.services.descrpadraoservice import DescrPadraoService
from util import util


# Criar as janelas e estilos (layout)
class JanelaDescrPadrao:

    service = DescrPadraoService()

    size_input = 50 # util.get_size_input()

    def __init__(self):

        self.lista = []
        self.lista_entity = self.service.find_all()

        # Lista para popular a combobox
        for descr in self.lista_entity:
            self.lista.append(descr.__str__())

        self.window, self.event, self.values = None, None, None

        sg.theme(util.get_tema_janelas())

        self.layout = [
            [sg.Text('Código Descrição Padrão')],
            [sg.Combo(self.lista, size=(self.size_input - 2, 1), default_value=self.lista[0], readonly=True, enable_events=True, key='descrpadrao')],
            [sg.Text('Descrição')],
            [sg.Input(size=(self.size_input, 1), default_text=self.lista_entity[0].get_descricao(), key='descricao')]
        ]

    def get_dados(self, janela, id):
        for descr in self.lista_entity:
            if descr.get_descricao_id() == id:
                janela.FindElement('descricao').Update(descr.get_descricao())