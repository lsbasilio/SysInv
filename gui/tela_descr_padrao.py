import PySimpleGUI as sg
from model.entities.descrpadrao import DescrPadrao
from model.services.descrpadraoservice import DescrPadraoService
from util import util


# Criar as janelas e estilos (layout)
class JanelaDescrPadrao:

    entity = DescrPadrao()
    service = DescrPadraoService()

    lista = []

    size_input = 50  # util.get_size_input()

    def __init__(self):

        self.lista_entity = self.service.find_all()

        # Lista para popular a combobox
        for descr in self.lista_entity:
            self.lista.append(descr.__str__())

        self.entity = self.lista_entity[0]

        self.window, self.event, self.values = None, None, None

        sg.theme(util.get_tema_janelas())

        self.layout = [
            [sg.Text('Código Descrição Padrão')],
            [sg.Combo(self.lista, size=(self.size_input - 2, util.height_combo), default_value=self.lista[0], readonly=True, enable_events=True, key='descrpadrao')],
            [sg.Text('Descrição')],
            #[sg.Input(size=(self.size_input, 1), default_text=self.lista_entity[0].get_descricao(), key='descricaoantiga')],
            [sg.Button('Novo', size=(8, 1)), sg.Button('Salvar', size=(8, 1)), sg.Button('Excluir', size=(8, 1))],
            [sg.Multiline(enter_submits=False, autoscroll=True, size=(self.size_input - 2, 1), default_text=self.lista_entity[0].get_descricao(), key='descricao')]
        ]

    def get_dados(self, janela, id):
        self.entity = self.service.find_by_id(id)
        if self.entity is not None:
            self.update_form_data(janela, self.entity)
        else:
            sg.popup('Descrição Padrão não encontrada!')

    def update_form_data(self, janela, descrpadrao):
        janela.FindElement('descricao').Update(descrpadrao.get_descricao())

    # Gravando os dados no Banco
    def grava_dados(self, janela):
        self.service.save_or_update(self.entity)
        self.update_form_data(janela, self.entity)

    # Salvando os dados da Descr Padrao
    def salvar(self, janela, descricaoatual, descricaonova):
        self.entity.set_descricao(descricaonova)
        x = self.lista.index(descricaoatual)
        self.lista[x] = self.entity.__str__()
        janela.FindElement('descrpadrao').Update(values=self.lista, size=(self.size_input - 2, util.height_combo), set_to_index=x, readonly=True)
        self.grava_dados(janela)
        sg.popup('Dados da Descrição Padrão salvos com sucesso!')

    def excluir(self, janela):
        self.lista.remove(self.entity.__str__())    # remove da Lista
        self.service.remove(self.entity)    # remove do Banco
        janela.FindElement('descrpadrao').Update(values=self.lista, size=(util.width_combo, util.height_combo),
                                            set_to_index=0, readonly=True)
        self.entity = self.lista_entity[0]
        self.update_form_data(janela, self.entity)
        sg.popup('Descrição Padrão excluída com sucesso!')

    def botao_salvar(self, janela):

        descricaoatual = janela.FindElement('descrpadrao').Get()
        descricaonova = janela.FindElement('descricao').get()


#        print("'" + texto + "'")
        descricaonova = util.retira_caracteres_especiais(descricaonova)
        print("'" + descricaonova + "'")

        if descricaonova is None or descricaonova == '':
            sg.popup('O Campo Descrição está em branco!')
        else:
            self.salvar(janela, descricaoatual, descricaonova)

    def botao_excluir(self, janela):
        if sg.popup_yes_no('Deseja excluir a Descrição Padrão?') == 'Yes':
            self.excluir(janela)