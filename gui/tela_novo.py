import PySimpleGUI as sg
from util import util


# Criar as janelas e estilos (layout)
class JanelaNovo:

    size_input = util.size_input

    def __init__(self, entity, service, lista):

        self.entity = entity
        self.service = service

        self.lista = lista

        self.window, self.event, self.values = None, None, None

        sg.theme(util.get_tema_janelas())

        self.layout = [
            [sg.Text('Novo Código')],
            [sg.Input(size=(self.size_input, 1), key='codigo')],
            [sg.Text('Nova Descrição')],
            [sg.Input(size=(self.size_input, 1), key='descricao')],
            [sg.Button('Salvar', size=(8, 1)), sg.Button('Cancelar', size=(8, 1))]
        ]

    def salvar(self, janela, janela_origem):

        self.service.save_or_update(self.entity)

        if janela_origem.Title == 'Locais':
            self.lista.append(self.entity.__str__())
            x = self.lista.index(self.entity.__str__())
            janela_origem.FindElement('locais').Update(values=self.lista, size=(util.width_combo, util.height_combo), set_to_index=x, readonly=True)
            janela_origem.FindElement('descricao').Update(self.entity.get_descricao())
            sg.popup('Local cadastrado com Sucesso!')

        elif janela_origem.Title == 'Descrição Padrão':
            self.lista.append(self.entity.__str__())
            self.lista.sort()
            x = self.lista.index(self.entity.__str__())
            janela_origem.FindElement('descrpadrao').Update(values=self.lista, size=(util.width_combo, util.height_combo),
                                                       set_to_index=x, readonly=True)
            janela_origem.FindElement('descricao').Update(self.entity.get_descricao())
            sg.popup('Descrição Padrão cadastrada com Sucesso!')

        elif janela_origem.Title == 'Descrição Complementar':
            self.lista.append(self.entity.__str__())
            self.lista.sort()
            x = self.lista.index(self.entity.__str__())
            janela_origem.FindElement('descrcomplementar').Update(values=self.lista, size=(util.width_combo, util.height_combo),
                                                       set_to_index=x, readonly=True)
            janela_origem.FindElement('descricao').Update(self.entity.get_descricao())
            sg.popup('Descrição Complementar cadastrada com Sucesso!')

    def botao_salvar(self, janela, janela_origem):
        # print(janela.FindElement('codigo').get())
        # print(janela.FindElement('descricao').get())

        codigo = ''

        if janela_origem.Title == 'Locais':
            codigo = int(janela.FindElement('codigo').get())
        elif janela_origem.Title == 'Descrição Padrão':
            codigo = janela.FindElement('codigo').get().upper()
        elif janela_origem.Title == 'Descrição Complementar':
            codigo = janela.FindElement('codigo').get().upper()

        descricao = janela.FindElement('descricao').get()

        # print(type(codigo))

        if codigo is None or codigo == '':
            sg.popup('Código não informado!')
        elif descricao is None or descricao == '':
            sg.popup('Descrição não informada!')
        else:
            if self.service.find_by_id(codigo) is not None:
                sg.popup('Código informado já existe!\nInforme outro código')
            else:
                if janela_origem.Title == 'Locais':
                    self.entity.set_local_id(codigo)
                elif janela_origem.Title == 'Descrição Padrão':
                    self.entity.set_descricao_id(codigo)
                elif janela_origem.Title == 'Descrição Complementar':
                    self.entity.set_descricao_id(codigo)

                self.entity.set_descricao(descricao)
                self.salvar(janela, janela_origem)
                janela.hide()
                janela_origem.un_hide()


