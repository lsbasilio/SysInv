import PySimpleGUI as sg
from model.services.descrcomplementarservice import DescrComplementarService
from util import util


# Criar as janelas e estilos (layout)
class JanelaDescrComplementar:

    service = DescrComplementarService()

    size_input = 50

    def __init__(self):

        self.lista = []
        self.lista_entity = self.service.find_all()

        # Lista para popular a combobox
        for descr in self.lista_entity:
            self.lista.append(descr.__str__())

        self.window, self.event, self.values = None, None, None

        sg.theme(util.get_tema_janelas())

        self.layout = [
            [sg.Text('Código Descrição Complementar')],
            [sg.Combo(self.lista, size=(self.size_input - 2, 1), default_value=self.lista[0], readonly=True, enable_events=True, key='descrcomplementar')],
            [sg.Text('Descrição')],
            [sg.Input(size=(self.size_input, 1), default_text=self.lista_entity[0].get_descricao(), key='descricao')]
        ]

    def get_dados(self, janela, id):
        for descr in self.lista_entity:
            if descr.get_descricao_id() == id:
                janela.FindElement('descricao').Update(descr.get_descricao())