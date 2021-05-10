import PySimpleGUI as sg
from model.entities.bens import Bens
from model.entities.descrpadrao import DescrPadrao
from model.entities.descrcomplementar import DescrComplementar
from model.services.bensservice import BensService
from model.services.descrpadraoservice import DescrPadraoService
from model.services.descrcomplementarservice import DescrComplementarService
from model.services.centrodecustoservice import CentroDeCustoService
from model.services.locaisservice import LocaisService
import model.entities.enum.bens_status as Status
from util import util


# Criar as janelas e estilos (layout)
class JanelaInventario:

    entity = Bens()
    service = BensService()

    ccusto_service = CentroDeCustoService()
    local_service = LocaisService()

    entity_descr_padrao = DescrPadrao()
    entity_descr_compl  = DescrComplementar()

    descr_padrao_service = DescrPadraoService()
    descr_compl_service = DescrComplementarService()

    lista_descr_padrao = []
    lista_descr_compl = []
    lista_local = []

    size_input = util.size_input

    def __init__(self):

        self.ccusto_ativo = None
        self.entity = None

        self.lista_entity_padrao = self.descr_padrao_service.find_all()
        self.lista_entity_compl = self.descr_compl_service.find_all()
        self.lista_entity_local = self.local_service.find_all()

        # Lista para popular a combobox de Local
        for local in self.lista_entity_local:
            self.lista_local.append(local.__str__())

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
            [sg.Input(size=(23, 1), enable_events=True, key='numero_bem'), sg.Input(size=(22, 1), key='numero_ant')],
            [sg.Text('Status do Bem')],
            [sg.Input(size=(self.size_input, 1), key='status', readonly=True)],
            [sg.Text('Data do Inventário')],
            [sg.Input(size=(self.size_input, 1), key='datainv', readonly=True)],
            [sg.Text('Centro de Custo Atual')],
            [sg.Input(size=(self.size_input, 1), key='ccustoatual', readonly=True)],
            [sg.Text('Local')],
            [sg.Combo(self.lista_local, size=(util.width_combo, util.height_combo), readonly=True,
                      enable_events=True, default_value=self.lista_local[0], key='local')],
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
            [sg.Button('Inventariar', size=(9, 1)), sg.Button('Limpar', size=(8, 1)), sg.Button('Cancelar', size=(9, 1)), sg.Button('Sair', size=(8, 1))]
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

    def mostra_dados(self, janela):

        janela.FindElement('numero_ant').Update(self.entity.get_numero_bemant())

        ccusto_atual = self.ccusto_service.find_by_id(self.entity.get_ccusto_id())
        if ccusto_atual is not None:
            janela.FindElement('ccustoatual').Update(ccusto_atual.__str__())

        local_atual = self.local_service.find_by_id(self.entity.get_local_id())
        if local_atual is not None:
            x = self.lista_local.index(local_atual.__str__())
            janela.FindElement('local').Update(values=self.lista_local,
                                               size=(util.width_combo, util.height_combo),
                                               set_to_index=x, readonly=True)
        janela.FindElement('datainv').Update(self.entity.get_data_inv())
        janela.FindElement('descricao_bem').Update(self.entity.get_descricao())
        janela.FindElement('situacao').Update(self.entity.get_situacao())
        janela.FindElement('marca').Update(self.entity.get_marca())
        janela.FindElement('modelo').Update(self.entity.get_modelo())
        janela.FindElement('numero_serie').Update(self.entity.get_numeroserie())
        janela.FindElement('usuario').Update(self.entity.get_usuario())
        janela.FindElement('observacao').Update(self.entity.get_observacao())
        janela.FindElement('status').Update(self.entity.get_status())

    # TODO: Limpar os Dados do Bem
    def limpa_dados(self, janela, limpa_numero_bem=False, txtstatus=''):
        # Numero do Bem
        if limpa_numero_bem:
            janela.FindElement('numero_bem').Update('')

        # Numero Anterior
        janela.FindElement('numero_ant').Update('')
        # Data do Inventário
        janela.FindElement('datainv').Update('')
        # Ccusto Atual
        janela.FindElement('ccustoatual').Update('')

        # Descrição do Bem
        janela.FindElement('descricao_bem').Update('')
        # Situação
        janela.FindElement('situacao').Update('')
        # Marca
        janela.FindElement('marca').Update('')
        # Modelo
        janela.FindElement('modelo').Update('')
        # Numero de Serie
        janela.FindElement('numero_serie').Update('')
        # Usuario
        janela.FindElement('usuario').Update('')
        # Observacao
        janela.FindElement('observacao').Update('')
        # Status
        janela.FindElement('status').Update(txtstatus)

    # TODO: Finalizar a Tela de Inventário

    def valida_numero_bem(self, numero):
        if util.try_parse_to_int(numero) is None:
            sg.popup('Número do Bem inválido!')
            return False
        return True

    def update_form_data(self, janela, id):

        # Validar Numero do Bem
        if id != '':
            if not self.valida_numero_bem(id):
                return
        else:
            self.limpa_dados(janela)
            return

        self.entity = self.service.find_by_id(int(id))

        if self.entity is not None:
            self.mostra_dados(janela)
        else:
            self.limpa_dados(janela)
            janela.FindElement('status').Update(Status.status_texto[Status.BensStatus.Nao_Encontrado])

    def get_form_data(self, janela):
        self.entity.set_ccusto_id(int(util.get_id(self.ccusto_ativo.__str__())))
        self.entity.set_local_id(int(util.get_id(janela.FindElement('local').get())))
        descricao = janela.FindElement('descricao_bem').get()
        descricao = util.retira_caracteres_especiais(descricao)
        descricao_compl = janela.FindElement('descricao_compl_bem').get()
        descricao_compl = util.retira_caracteres_especiais(descricao_compl)
        if descricao_compl != '':
            descricao = descricao + ' ' + descricao_compl
        self.entity.set_descricao(descricao)
        self.entity.set_situacao(janela.FindElement('situacao').get())
        self.entity.set_marca(janela.FindElement('marca').get())
        self.entity.set_modelo(janela.FindElement('modelo').get())
        self.entity.set_numeroserie(janela.FindElement('numero_serie').get())
        self.entity.set_usuario(janela.FindElement('usuario').get())
        self.entity.set_observacao(janela.FindElement('observacao').get())

    def valida_dados(self, janela, id):
        if id == '':
            sg.popup('Número do Bem em branco!')
            return False
        if not self.valida_numero_bem(id):
            return False
        if janela.FindElement('descricao_bem').get().strip(' ') == '':
            sg.popup('Descrição do Bem não informada!')
            return False

        return True

    def botao_inventariar(self, janela, id):
        if self.valida_dados(janela, id):
            #self.entity = self.service.find_by_id(int(id))
            if self.entity is None:
                self.entity = Bens()
                self.entity.set_numero_bem(id)

            self.get_form_data(janela)
            self.entity.inventariar()
            self.service.save_or_update(self.entity)
            self.limpa_dados(janela, True, f'Bem {self.entity.get_numero_bem()} Inventariado')

    # TODO: Limpar Dados e Cancelar Inventário
