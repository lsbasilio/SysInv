import PySimpleGUI as sg
from model.entities.descrcomplementar import DescrComplementar
from model.services.descrcomplementarservice import DescrComplementarService
from util import util


# Criar as janelas e estilos (layout)
class JanelaDescrComplementar:

    entity = DescrComplementar()
    service = DescrComplementarService()

    lista = []

    size_input = 50

    def __init__(self):

        self.lista_entity = self.service.find_all()

        # Lista para popular a combobox
        for descr in self.lista_entity:
            self.lista.append(descr.__str__())

        self.entity = self.lista_entity[0]

        self.window, self.event, self.values = None, None, None

        sg.theme(util.get_tema_janelas())

        self.layout = [
            [sg.Text('Código Descrição Complementar')],
            [sg.Combo(self.lista, size=(self.size_input - 2, 1), default_value=self.lista[0], readonly=True, enable_events=True, key='descrcomplementar')],
            [sg.Text('Descrição')],
            #[sg.Input(size=(self.size_input, 1), default_text=self.lista_entity[0].get_descricao(), key='descricao')],
            [sg.Multiline(enter_submits=False, autoscroll=True, size=(self.size_input - 2, 5),
                          default_text=self.lista_entity[0].get_descricao(), key='descricao')],
            [sg.Button('Novo', size=(8, 1)), sg.Button('Salvar', size=(8, 1)), sg.Button('Excluir', size=(8, 1))]
        ]

    def update_form_data(self, janela, descrcompl):
        janela.FindElement('descricao').Update(descrcompl.get_descricao())

    def get_dados(self, janela, id):
        self.entity = self.service.find_by_id(id)
        if self.entity is not None:
            self.update_form_data(janela, self.entity)
        else:
            sg.popup('Descrição Complementar não encontrada!')

    # Gravando os dados no Banco
    def grava_dados(self, janela):
        self.service.save_or_update(self.entity)
        self.update_form_data(janela, self.entity)

    def salvar(self, janela, descricaoatual, descricaonova):
        self.entity.set_descricao(descricaonova)
        x = self.lista.index(descricaoatual)
        self.lista[x] = self.entity.__str__()
        janela.FindElement('descrcomplementar').Update(values=self.lista, size=(self.size_input - 2, util.height_combo),
                                                 set_to_index=x, readonly=True)
        self.grava_dados(janela)
        sg.popup('Dados da Descrição Complementar salvos com sucesso!')

    def excluir(self, janela):
        self.lista.remove(self.entity.__str__())    # remove da Lista
        self.service.remove(self.entity)    # remove do Banco
        janela.FindElement('descrcomplementar').Update(values=self.lista, size=(util.width_combo, util.height_combo),
                                            set_to_index=0, readonly=True)
        self.entity = self.lista_entity[0]
        self.update_form_data(janela, self.entity)
        sg.popup('Descrição Complementar excluída com sucesso!')

    def botao_salvar(self, janela):

        descricaoatual = janela.FindElement('descrcomplementar').Get()
        descricaonova = janela.FindElement('descricao').get()

        descricaonova = util.retira_caracteres_especiais(descricaonova)

        if descricaonova is None or descricaonova == '':
            sg.popup('O Campo Descrição está em branco!')
        else:
            self.salvar(janela, descricaoatual, descricaonova)

    def botao_excluir(self, janela):
        if sg.popup_yes_no('Deseja excluir a Descrição Complementar?') == 'Yes':
            self.excluir(janela)