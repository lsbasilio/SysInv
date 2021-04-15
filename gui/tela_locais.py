import PySimpleGUI as sg
from model.services.locaisservice import LocaisService
from util import util


# Criar as janelas e estilos (layout)
class JanelaLocais:

    service = LocaisService()

    size_input = 42

    def __init__(self):

        self.lista = []
        self.lista_entity = self.service.find_all()

        # Lista para popular a combobox
        for locais in self.lista_entity:
            self.lista.append(locais.__str__())

        self.window, self.event, self.values = None, None, None

        sg.theme(util.get_tema_janelas())

        self.layout = [
            [sg.Text('Locais')],
            [sg.Combo(self.lista, size=(40, 1), default_value=self.lista[0], readonly=True, enable_events=True, key='locais')],
            [sg.Text('Descrição')],
            [sg.Input(size=(self.size_input, 1), default_text=self.lista_entity[0].get_descricao(), key='descricao')]
        ]

    def get_dados(self, janela, id):
        for local in self.lista_entity:
            if local.get_local_id() == int(id):
                janela.FindElement('descricao').Update(local.get_descricao())