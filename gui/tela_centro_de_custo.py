import PySimpleGUI as sg
from util import util
from model.entities.centrodecusto import CentroDeCusto
from model.services.centrodecustoservice import CentroDeCustoService


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
            [sg.Input(size=(42, 1), key='descricao')]
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
                print('Está lendo')
                self.janela.hide()
                self.janelaprincipal.un_hide()
                break

            ccusto_selecionado = self.values['ccusto']
            id_ccusto = ccusto_selecionado.split(' - ')

            for ccusto in self.lista_entity:
                if ccusto.get_ccusto_id() == int(id_ccusto[0]):
                    self.window.FindElement('descricao').Update(ccusto.get_descricao())
                    break

            #for indice in range(0, len(self.lista_entity)):




