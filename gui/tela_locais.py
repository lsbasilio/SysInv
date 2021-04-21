import PySimpleGUI as sg
from model.entities.locais import Locais
from model.services.locaisservice import LocaisService
from util import util


# Criar as janelas e estilos (layout)
class JanelaLocais:

    entity = Locais()
    service = LocaisService()

    lista = []

    size_input = util.size_input

    def __init__(self):

        self.lista_entity = self.service.find_all()

        # Lista para popular a combobox
        for locais in self.lista_entity:
            self.lista.append(locais.__str__())

        self.entity = self.lista_entity[0]

        self.window, self.event, self.values = None, None, None

        sg.theme(util.get_tema_janelas())

        self.layout = [
            [sg.Text('Locais')],
            [sg.Combo(self.lista, size=(util.width_combo, util.height_combo), default_value=self.lista[0], readonly=True, enable_events=True, key='locais')],
            [sg.Text('Descrição')],
            [sg.Input(size=(self.size_input, 1), default_text=self.lista_entity[0].get_descricao(), key='descricao')],
            [sg.Button('Novo', size=(8, 1)), sg.Button('Salvar', size=(8, 1)), sg.Button('Excluir', size=(8, 1))]
        ]

    def get_dados(self, janela, id):
        self.entity = self.service.find_by_id(int(id))
        if self.entity is not None:
            self.update_form_data(janela, self.entity)
        else:
            sg.popup('Local não encontrado!')

    # TODO: Finalizar Tela de Locais

    def update_form_data(self, janela, locais):
        janela.FindElement('descricao').Update(locais.get_descricao())

    # Gravando os dados no Banco
    def grava_dados(self, janela):
        self.service.save_or_update(self.entity)
        self.update_form_data(janela, self.entity)

    # Salvando os dados do Local
    def salvar(self, janela, descricaoatual, descricaonova):
        self.entity.set_descricao(descricaonova)
        x = self.lista.index(descricaoatual)
        self.lista[x] = self.entity.__str__()
        janela.FindElement('locais').Update(values=self.lista, size=(util.width_combo, util.height_combo), set_to_index=x, readonly=True)
        self.grava_dados(janela)
        sg.popup('Dados do Local salvos com sucesso!')

    def excluir(self, janela):
        self.lista.remove(self.entity.__str__())    # remove da Lista
        self.service.remove(self.entity)    # remove do Banco
        janela.FindElement('locais').Update(values=self.lista, size=(util.width_combo, util.height_combo),
                                            set_to_index=0, readonly=True)

        self.entity = self.lista_entity[0]
        self.update_form_data(janela, self.entity)
        sg.popup('Local excluído com sucesso!')

    # Botão Salvar Local
    def botao_salvar(self, janela):

        descricaoatual = janela.FindElement('locais').Get()
        descricaonova = janela.FindElement('descricao').get()

        if descricaonova is None or descricaonova == '':
            sg.popup('O Campo Descrição está em branco!')
        else:
            self.salvar(janela, descricaoatual, descricaonova)

    def botao_excluir(self, janela):
        if sg.popup_yes_no('Deseja excluir o Local?') == 'Yes':
            self.excluir(janela)


