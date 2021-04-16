import PySimpleGUI as sg
from model.services.centrodecustoservice import CentroDeCustoService
from util import util


# Criar as janelas e estilos (layout)
class JanelaCcusto:

    service = CentroDeCustoService()

    size_input = util.get_size_input()

    def __init__(self):

        self.lista = []
        self.lista_entity = self.service.find_all()
        self.CcustoAtivo = self.lista_entity[0]  # Captura o Centro de Custo Ativo, se não houver pega o primeiro Ccusto

        # Lista para popular a combobox
        for ccusto in self.lista_entity:
            self.lista.append(ccusto.__str__())
            if ccusto.get_status() == 'Ativo':
                self.CcustoAtivo = ccusto

        self.window, self.event, self.values = None, None, None

        sg.theme(util.get_tema_janelas())

        self.layout = [
            [sg.Text('Centro de Custo')],
            [sg.Combo(self.lista, size=(40, 1), default_value=self.CcustoAtivo.__str__(), readonly=True, enable_events=True, key='ccusto')],
            [sg.Text('Descrição')],
            [sg.Input(size=(self.size_input, 1), default_text=self.CcustoAtivo.get_descricao(), key='descricao')],
            [sg.Text('Data Início')],
            [sg.Input(size=(self.size_input, 1), default_text=self.CcustoAtivo.get_data_inicio(), key='data_inicio', readonly=True)],
            [sg.Text('Data Fim')],
            [sg.Input(size=(self.size_input, 1), default_text=self.CcustoAtivo.get_data_fim(), key='data_fim', readonly=True)],
            [sg.Text('Status: ')],
            [sg.Input(size=(self.size_input, 1), default_text=self.CcustoAtivo.get_status(), key='status', readonly=True)],
            [sg.Text('Bens Pendentes: '), sg.Text(self.CcustoAtivo.get_pendentes(), size=(10, 1), key='pendentes')],
            [sg.Text('Bens Inventariados: '), sg.Text(self.CcustoAtivo.get_inventariados(), size=(10, 1), key='inventariados')],
            [sg.Text('Bens Novos: '), sg.Text(self.CcustoAtivo.get_novos(), size=(10, 1), key='novos')]
        ]

    def get_dados(self, janela, id):
        for ccusto in self.lista_entity:
            if ccusto.get_ccusto_id() == int(id):
                janela.FindElement('descricao').Update(ccusto.get_descricao())
                janela.FindElement('data_inicio').Update(ccusto.get_data_inicio())
                janela.FindElement('data_fim').Update(ccusto.get_data_fim())
                janela.FindElement('status').Update(str(ccusto.get_status()))
                janela.FindElement('pendentes').Update(str(ccusto.get_pendentes()))
                janela.FindElement('inventariados').Update(str(ccusto.get_inventariados()))
                janela.FindElement('novos').Update(str(ccusto.get_novos()))
                break




