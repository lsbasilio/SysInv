import PySimpleGUI as sg
from gui.tela_centro_de_custo import JanelaCcusto
from gui.tela_locais import JanelaLocais
from gui.tela_descr_padrao import JanelaDescrPadrao
from gui.tela_descr_complementar import JanelaDescrComplementar
from gui.tela_novo import JanelaNovo
from util import util


# Criar as janelas e estilos (layout)
class JanelaPrincipal:

    janela = None

    def __init__(self):

        self.window, self.event, self.values = None, None, None

        size_botao = 25

        # Criar as janelas do Centro de Custo
        self.janela_ccusto = None
        self.janelaccusto = None  # Objeto da classe JanelaCcusto

        # Criar as janelas dos Locais
        self.janela_local  = None
        self.janelalocal = None  # Objeto da classe JanelaLocais

        # Criar as janelas de Descrição Padrão
        self.janela_descr_padrao = None
        self.janeladescrpadrao = None  # Objeto da classe JanelaDescrPadrao

        # Criar as janelas de Descrição Complementar
        self.janela_descr_compl = None
        self.janeladescrcompl = None  # Objeto da classe JanelaDescrComplementar

        # Criar as janelas de Novo
        self.janela_novo = None
        self.janelanovo = None

        sg.theme(util.get_tema_janelas())

        self.layout = [
            [sg.Image(filename=f'Imagens\BarCode.png', size=(100, 100))],
            [sg.Button('Ativar Centro de Custo', size=(size_botao, 0))],
            [sg.Button('Iniciar Inventário', size=(size_botao, 0))],
            [sg.Button('Locais', size=(size_botao, 0))],
            [sg.Button('Descr. Padrão', size=(size_botao, 0))],
            [sg.Button('Descr. Complementar', size=(size_botao, 0))],
            [sg.Button('Consultar Bens', size=(size_botao, 0))]
        ]

    def retorna_janela(self):
        # Retorna Janela Principal
        self.janela = sg.Window('Tela Principal', layout=self.layout, finalize=True)
        self.janela_ccusto = None
        self.janela_local = None
        self.janela_novo = None
        self.janela_descr_padrao = None
        self.janela_descr_compl = None
        return self.janela

    def iniciar_tela(self):

        # Cria um loop de leitura de eventos
        while True:

            self.window, self.event, self.values = sg.read_all_windows()

            # TODO: Agrupar os eventos das janelas

            ###### Eventos da janela principal #######
            if self.window == self.janela:
                if self.event == sg.WINDOW_CLOSED:
                    self.janela.close()
                    exit()
                    break

                # Quando queremos ir para janela de Centro de Custo
                if self.event == 'Ativar Centro de Custo':
                    self.janela.hide()
                    self.janelaccusto = JanelaCcusto()
                    self.janela_ccusto = sg.Window('Centro de Custo', layout=self.janelaccusto.layout,
                                                   finalize=True)

                # Quando queremos ir para janela de Local
                if self.event == 'Locais':
                    self.janela.hide()
                    self.janelalocal = JanelaLocais()
                    self.janela_local = sg.Window('Locais', layout=self.janelalocal.layout, finalize=True)

                # Quando queremos ir para janela de Descr Padrão
                if self.event == 'Descr. Padrão':
                    self.janela.hide()
                    self.janeladescrpadrao = JanelaDescrPadrao()
                    self.janela_descr_padrao = sg.Window('Descrição Padrão', layout=self.janeladescrpadrao.layout, finalize=True)

                # Quando queremos ir para janela de Descr Complementar
                if self.event == 'Descr. Complementar':
                    self.janela.hide()
                    self.janeladescrcompl = JanelaDescrComplementar()
                    self.janela_descr_compl = sg.Window('Descrição Complementar', layout=self.janeladescrcompl.layout, finalize=True)

            ###### Eventos da janela Centro de Custo #######
            # Quando a janela de Centro de Custo for fechada
            if self.window == self.janela_ccusto:
                if self.event == sg.WINDOW_CLOSED:
                    self.janela_ccusto.hide()
                    self.janela.un_hide()

                # Eventos da Janela de Centro de Custo
                if self.event == 'ccusto':
                    ccusto_id = util.get_id(self.values['ccusto'])
                    self.janelaccusto.get_dados(self.janela_ccusto, ccusto_id)

                # Se clicou no Botão Ativar Centro de Custo
                if self.event == 'Ativar':
                    ccusto_id = util.get_id(self.values['ccusto'])
                    self.janelaccusto.botao_ativar(self.janela_ccusto, ccusto_id)

                # Se clicou no Botão Encerrar Centro de Custo
                if self.event == 'Encerrar':
                    #ccusto_id = util.get_id(self.values['ccusto'])
                    self.janelaccusto.botao_encerrar(self.janela_ccusto)

                # Se clicou no Botão Salvar Centro de Custo
                if self.event == 'Salvar':
                    self.janelaccusto.botao_salvar(self.janela_ccusto)

            ###### Eventos da janela Locais #######
            # Quando a janela de Local for fechada
            if self.window == self.janela_local:
                if self.event == sg.WINDOW_CLOSED:
                    self.janela_local.hide()
                    self.janela.un_hide()

                # Eventos da Janela de Local
                if self.event == 'locais':
                    local_id = util.get_id(self.values['locais'])
                    self.janelalocal.get_dados(self.janela_local, local_id)

                # Se clicou no Botão Salvar Locais
                if self.event == 'Salvar':
                    self.janelalocal.botao_salvar(self.janela_local)

                # Se clicou no Botão Excluir Locais
                if self.event == 'Excluir':
                    self.janelalocal.botao_excluir(self.janela_local)

                # Se clicou no Botão Novo Local
                if self.event == 'Novo':
                    self.janela_local.hide()
                    self.janelanovo = JanelaNovo(self.janelalocal.entity, self.janelalocal.service, self.janelalocal.lista)
                    self.janela_novo = sg.Window('Novo Local', layout=self.janelanovo.layout, finalize=True)

            ###### Eventos da janela Descr Padrao #######
            # Quando a janela de Descr Padrão for fechada
            if self.window == self.janela_descr_padrao:
                if self.event == sg.WINDOW_CLOSED:
                    self.janela_descr_padrao.hide()
                    self.janela.un_hide()

                # Eventos da Janela de Descr Padrão
                if self.event == 'descrpadrao':
                    descr_id = util.get_id(self.values['descrpadrao'])
                    self.janeladescrpadrao.get_dados(self.janela_descr_padrao, descr_id)

                # Se clicou no Botão Salvar Descr Padrao
                if self.event == 'Salvar':
                    self.janeladescrpadrao.botao_salvar(self.janela_descr_padrao)

                # Se clicou no Botão Excluir Descr Padrao
                if self.event == 'Excluir':
                    self.janeladescrpadrao.botao_excluir(self.janela_descr_padrao)

                # Se clicou no Botão Nova Descr Padrao
                if self.event == 'Novo':
                    self.janela_descr_padrao.hide()
                    self.janelanovo = JanelaNovo(self.janeladescrpadrao.entity,
                                                 self.janeladescrpadrao.service,
                                                 self.janeladescrpadrao.lista)
                    self.janela_novo = sg.Window('Nova Descrição Padrão', layout=self.janelanovo.layout, finalize=True)

            ###### Eventos da janela Descr Complementar #######
            # Quando a janela de Descr Complementar for fechada
            if self.window == self.janela_descr_compl:
                if self.event == sg.WINDOW_CLOSED:
                    self.janela_descr_compl.hide()
                    self.janela.un_hide()

                # Eventos da Janela de Descr Complementar
                if self.event == 'descrcomplementar':
                    descr_id = util.get_id(self.values['descrcomplementar'])
                    self.janeladescrcompl.get_dados(self.janela_descr_compl, descr_id)

                # Se clicou no Botão Salvar Descr Complementar
                if self.event == 'Salvar':
                    self.janeladescrcompl.botao_salvar(self.janela_descr_compl)

                # Se clicou no Botão Excluir Descr Complementar
                if self.event == 'Excluir':
                    self.janeladescrcompl.botao_excluir(self.janela_descr_compl)

                # Se clicou no Botão Nova Descr Complementar
                if self.event == 'Novo':
                    self.janela_descr_compl.hide()
                    self.janelanovo = JanelaNovo(self.janeladescrcompl.entity,
                                                 self.janeladescrcompl.service,
                                                 self.janeladescrcompl.lista)
                    self.janela_novo = sg.Window('Nova Descrição Complementar', layout=self.janelanovo.layout, finalize=True)

            ###### Eventos da janela Novo #######

            # Quando a janela de Novo for fechada
            if self.window == self.janela_novo:
                if (self.event == sg.WINDOW_CLOSED or self.event == 'Cancelar'):
                    self.janela_novo.hide()
                    if self.janela_local is not None:
                        self.janela_local.un_hide()
                    elif self.janela_descr_padrao is not None:
                        self.janela_descr_padrao.un_hide()
                    elif self.janela_descr_compl is not None:
                        self.janela_descr_compl.un_hide()

                # Se clicou no Botão Salvar Novo
                if self.window == self.janela_novo and self.event == 'Salvar':
                    if self.janela_local is not None:
                        self.janelanovo.botao_salvar(self.janela_novo, self.janela_local)
                    elif self.janela_descr_padrao is not None:
                        self.janelanovo.botao_salvar(self.janela_novo, self.janela_descr_padrao)
                    elif self.janela_descr_compl is not None:
                        self.janelanovo.botao_salvar(self.janela_novo, self.janela_descr_compl)
