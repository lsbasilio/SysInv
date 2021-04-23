import PySimpleGUI as sg
from model.entities.bens import Bens
from model.entities.descrpadrao import DescrPadrao
from model.entities.descrcomplementar import DescrComplementar
from model.services.bensservice import BensService
from model.services.descrpadraoservice import DescrPadraoService
from model.services.descrcomplementarservice import DescrComplementarService
from model.services.centrodecustoservice import CentroDeCustoService
from util import util


# Criar as janelas e estilos (layout)
class JanelaInventario:

    entity = Bens()
    service = BensService()

    ccusto_service = CentroDeCustoService()

    entity_descr_padrao = DescrPadrao()
    entity_descr_compl  = DescrComplementar()

    descr_padrao_service = DescrPadraoService()
    descr_compl_service = DescrComplementarService()

    lista_descr_padrao = []
    lista_descr_compl = []

    size_input = util.size_input

    def __init__(self):

        self.ccusto_ativo = None

        self.lista_entity_padrao = self.descr_padrao_service.find_all()
        self.lista_entity_compl = self.descr_compl_service.find_all()

        # Lista para popular a combobox Descr Padrão
        for descr in self.lista_entity_padrao:
            self.lista_descr_padrao.append(descr.__str__())

        # Lista para popular a combobox Descr Complementar
        for descrcompl in self.lista_entity_compl:
            self.lista_descr_compl.append(descrcompl.__str__())

        self.window, self.event, self.values = None, None, None

        sg.theme(util.get_tema_janelas())

        self.col_layout = [
            [sg.Text('Centro de Custo Ativo')],
            [sg.Input(size=(self.size_input, 1), key='ccustoativo')],
            [sg.Text('Número do Bem', size=(20, 1)), sg.Text('Número Anterior')],
            [sg.Input(size=(23, 1), enable_events=True, key='numero_bem'), sg.Input(size=(22, 1), key='numero_anterior')],
            [sg.Text('Centro de Custo Atual')],
            [sg.Input(size=(self.size_input, 1), key='ccustoatual')],
            [sg.Text('Descrição Padrão')],
            [sg.Combo(self.lista_descr_padrao, size=(util.width_combo, util.height_combo), readonly=True,
                      enable_events=True, default_value=self.lista_descr_padrao[0], key='descrpadrao')],
            [sg.Text('Descrição do Bem')],
            [sg.Multiline(enter_submits=False, autoscroll=True, size=(self.size_input - 2, 5), key='descricao_bem')],
            [sg.Text('Situação')],
            [sg.Input(size=(self.size_input, 1), key='situacao')],
            [sg.Text('Descrição Complementar')],
            [sg.Combo(self.lista_descr_compl, size=(util.width_combo, util.height_combo), readonly=True,
                      enable_events=True, default_value=self.lista_descr_compl[0], key='descrcomplementar')],
            [sg.Multiline(enter_submits=False, autoscroll=True, size=(self.size_input - 2, 5), key='descricao_compl_bem')],
            [sg.Text('Marca')],
            [sg.Input(size=(self.size_input, 1), key='marca')],
            [sg.Text('Modelo')],
            [sg.Input(size=(self.size_input, 1), key='modelo')],
            [sg.Text('Número de Série')],
            [sg.Input(size=(self.size_input, 1), key='numero_serie')],
            [sg.Text('Usuário')],
            [sg.Input(size=(self.size_input, 1), key='usuario')],
            [sg.Text('Observação')],
            [sg.Input(size=(self.size_input, 1), key='observacao')],
            [sg.Text('Status do Bem')],
            [sg.Input(size=(self.size_input, 1), key='status')],
            [sg.Button('Inventariar', size=(9, 1)), sg.Button('Limpar', size=(8, 1)), sg.Button('Próxima >>', size=(9, 1)), sg.Button('Sair', size=(8, 1))]
        ]

        self.layout = [[sg.Column(self.col_layout, scrollable=True, vertical_scroll_only=True, size=util.size_tela_inventario)]]

    def define_ccusto_ativo(self, janela):
        self.ccusto_ativo = self.ccusto_service.find_ccusto_ativo()
        if self.ccusto_ativo is not None:
            janela.FindElement('ccustoativo').Update(self.ccusto_ativo.__str__())

        return self.ccusto_ativo

    def get_dados_descr_padrao(self, janela, id):
        self.entity_descr_padrao = self.descr_padrao_service.find_by_id(id)
        if self.entity_descr_padrao is not None:
            janela.FindElement('descricao_bem').Update(self.entity_descr_padrao.get_descricao())
        else:
            sg.popup('Descrição Padrão não encontrada!')

    def get_dados_descr_compl(self, janela, id):
        self.entity_descr_compl = self.descr_compl_service.find_by_id(id)
        if self.entity_descr_compl is not None:
            janela.FindElement('descricao_compl_bem').Update(self.entity_descr_compl.get_descricao())
        else:
            sg.popup('Descrição Complementar não encontrada!')

    def update_form_data(self, janela):
        id = janela.FindElement('numero_bem').get()

        entity = self.service.find_by_id(int(id))
        if entity is not None:
            janela.FindElement('numero_anterior').Update(entity.get_numero_bemant())
            janela.FindElement('ccustoatual').Update(entity.get_ccusto_id())
            janela.FindElement('descricao_bem').Update(entity.get_descricao())
            janela.FindElement('situacao').Update(entity.get_situacao())
            janela.FindElement('marca').Update(entity.get_marca())
            janela.FindElement('modelo').Update(entity.get_modelo())
            janela.FindElement('numero_serie').Update(entity.get_numeroserie())
            janela.FindElement('usuario').Update(entity.get_usuario())
            janela.FindElement('observacao').Update(entity.get_observacao())
            janela.FindElement('status').Update(entity.get_status())

        # TODO: Finalizar a Tela de Inventário




