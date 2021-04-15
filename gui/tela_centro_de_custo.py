import PySimpleGUI as sg
from util import util
from model.entities.centrodecusto import CentroDeCusto
from model.services.centrodecustoservice import CentroDeCustoService
from util import util


# Criar as janelas e estilos (layout)
class JanelaCcusto:

    entity = CentroDeCusto()
    service = CentroDeCustoService()
    janela = None

    janelaprincipal = None

    def __init__(self):

        self.lista = []
        self.lista_entity = self.service.find_all()

        # Lista para popular a combobox
        for ccusto in self.lista_entity:
            self.lista.append(ccusto.__str__())

        self.window, self.event, self.values = None, None, None

        sg.theme(util.get_tema_janelas())

        self.layout = [
            [sg.Text('Centro de Custo')],
            [sg.Combo(self.lista, size=(40, 1), default_value=self.lista[0], readonly=True, enable_events=True, key='ccusto')],
            [sg.Text('Descrição')],
            [sg.Input(size=(42, 1), default_text=self.lista_entity[0].get_descricao(), key='descricao')],
            [sg.Text('Data Início')],
            [sg.Input(size=(42, 1), default_text=self.lista_entity[0].get_data_inicio(), key='data_inicio', readonly=True)],
            [sg.Text('Data Fim')],
            [sg.Input(size=(42, 1), default_text=self.lista_entity[0].get_data_fim(), key='data_fim', readonly=True)],
            [sg.Text('Status: ')],
            [sg.Input(size=(42, 1), default_text=self.lista_entity[0].get_status(), key='status', readonly=True)],
            [sg.Text('Bens Pendentes: '), sg.Text(self.lista_entity[0].get_pendentes(), size=(10, 1), key='pendentes')],
            [sg.Text('Bens Inventariados: '), sg.Text(self.lista_entity[0].get_inventariados(), size=(10, 1), key='inventariados')],
            [sg.Text('Bens Novos: '), sg.Text(self.lista_entity[0].get_novos(), size=(10, 1), key='novos')]
        ]

    def retorna_janela(self):
        # Retorna Janela Centro de Custo
        self.janela = sg.Window('Centro de Custo', layout=self.layout, finalize=True)
        return self.janela

        #return sg.Window('Centro de Custo', layout=self.layout, finalize=True)

    def iniciar_tela(self):
        while True:

            self.window, self.event, self.values = sg.read_all_windows()

            if self.event == sg.WINDOW_CLOSED:
                print('Fechou Ccusto')
                self.janela.hide()
                self.janelaprincipal.un_hide()
                break

            ccusto_id = util.get_id(self.values['ccusto'])
            self.get_dados(ccusto_id)

    def get_dados(self, id):
        for ccusto in self.lista_entity:
            if ccusto.get_ccusto_id() == int(id):
                self.window.FindElement('descricao').Update(ccusto.get_descricao())
                self.window.FindElement('data_inicio').Update(ccusto.get_data_inicio())
                self.window.FindElement('data_fim').Update(ccusto.get_data_fim())
                self.window.FindElement('status').Update(str(ccusto.get_status()))
                self.window.FindElement('pendentes').Update(str(ccusto.get_pendentes()))
                self.window.FindElement('inventariados').Update(str(ccusto.get_inventariados()))
                self.window.FindElement('novos').Update(str(ccusto.get_novos()))
                break




