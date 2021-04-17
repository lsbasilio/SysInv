import PySimpleGUI as sg
from model.services.centrodecustoservice import CentroDeCustoService
from model.entities.centrodecusto import CentroDeCusto
from util import util


# Criar as janelas e estilos (layout)
class JanelaCcusto:

    entity = CentroDeCusto()
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

    def get_ccusto_lista(self, id):     # Não está sendo utilizada
        for ccusto in self.lista_entity:
            if ccusto.get_ccusto_id() == int(id):
                return ccusto
        return None

    def get_dados(self, janela, id):
        self.entity = self.service.find_by_id(int(id))
        if self.entity is not None:
            self.update_form_data(janela, self.entity)
        else:
            sg.popup('Centro de Custo não encontrado!')

    def ativar(self, janela, id):
        # entity = self.service.find_by_id(id)
        if self.entity is not None:
            self.entity.ativar()
            self.service.save_or_update(self.entity)
            self.update_form_data(janela, self.entity)
            sg.popup('Centro de Custo ativado com sucesso!')
        else:
            sg.popup('Centro de Custo a ativar não encontrado!')

    def botao_ativar(self, janela, id):
        try:

            ccusto_ativo = self.service.find_ccusto_ativo()

            if util.try_parse_to_int(id) is None:
                sg.popup('Código de Centro de Custo inválido!')
            elif ccusto_ativo is not None and ccusto_ativo.get_ccusto_id() != int(id):
                if sg.popup_yes_no('Já existe outro Centro de Custo Ativo!\nDeseja ativar mesmo assim?') == 'Yes':
                    self.service.altera_status_ccusto_ativo()
                    self.ativar(janela, id)
            else:
                self.ativar(janela, id)

        except ValueError as e:
            sg.popup(f'Erro ao ativar o Centro de Custo: {e}')










