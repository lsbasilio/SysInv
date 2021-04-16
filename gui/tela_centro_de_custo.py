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
            [sg.Combo(self.lista, size=(45, 1), default_value=self.CcustoAtivo.__str__(), readonly=True, enable_events=True, key='ccusto')],
            [sg.Text('Descrição')],
            [sg.Input(size=(self.size_input, 1), default_text=self.CcustoAtivo.get_descricao(), key='descricao')],
            [sg.Text('Data Início')],
            [sg.Input(size=(self.size_input, 1), default_text=self.CcustoAtivo.get_data_inicio(), key='data_inicio', readonly=True)],
            [sg.Text('Data Fim')],
            [sg.Input(size=(self.size_input, 1), default_text=self.CcustoAtivo.get_data_fim(), key='data_fim', readonly=True)],
            [sg.Text('Status')],
            [sg.Input(size=(self.size_input, 1), default_text=self.CcustoAtivo.get_status(), key='status', readonly=True)],
            [sg.Text('Bens Pendentes: '), sg.Text(self.CcustoAtivo.get_pendentes(), size=(10, 1), key='pendentes')],
            [sg.Text('Bens Inventariados: '), sg.Text(self.CcustoAtivo.get_inventariados(), size=(10, 1), key='inventariados')],
            [sg.Text('Bens Novos: '), sg.Text(self.CcustoAtivo.get_novos(), size=(10, 1), key='novos')],
            [sg.Button('Novo', size=(8, 1)), sg.Button('Ativar', size=(8, 1)), sg.Button('Encerrar', size=(9,1)), sg.Button('Salvar', size=(8,1))]
        ]

    def update_form_data(self, janela, ccusto):
        janela.FindElement('descricao').Update(ccusto.get_descricao())
        janela.FindElement('data_inicio').Update(ccusto.get_data_inicio())
        janela.FindElement('data_fim').Update(ccusto.get_data_fim())
        janela.FindElement('status').Update(ccusto.get_status())
        janela.FindElement('pendentes').Update(str(ccusto.get_pendentes()))
        janela.FindElement('inventariados').Update(str(ccusto.get_inventariados()))
        janela.FindElement('novos').Update(str(ccusto.get_novos()))

    def get_dados(self, janela, id):
        for ccusto in self.lista_entity:
            if ccusto.get_ccusto_id() == int(id):
                self.update_form_data(janela, ccusto)
                break

    def ativar(self, janela, id):
        try:
            ccusto_ativo = self.service.find_ccusto_ativo()

            if util.try_parse_to_int(id) is None:
                sg.popup('Código de Centro de Custo inválido!')
            elif ccusto_ativo is not None and ccusto_ativo.get_ccusto_id() != int(id):
                sg.popup('Já existe Centro de Custo Ativo!')
            else:
                for ccusto in self.lista_entity:
                    if ccusto.get_ccusto_id() == int(id):
                        ccusto.ativar()
                        self.service.save_or_update(ccusto)
                        self.update_form_data(janela, ccusto)
                        sg.popup('Centro de Custo ativado com sucesso!')
        except ValueError as e:
            sg.popup(f'Erro ao ativar o Centro de Custo: {e}')










