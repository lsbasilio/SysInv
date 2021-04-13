import PySimpleGUI as sg
#from gui.tela_principal import JanelaPrincipal


# Criar as janelas e estilos (layout)
class JanelaCcusto:

    def __init__(self):

        self.window, self.event, self.values = None, None, None

        sg.theme('DarkTeal7')

        self.layout = [
            [sg.Text('Centro de Custo')]
        ]

        # Janela
        #self.janelaccusto = sg.Window('Centro de Custo', layout=layout, finalize=True)

    def retorna_janela(self):
        return sg.Window('Centro de Custo', layout=self.layout, finalize=True)

    def iniciar_tela(self):
        pass
        # while True:
        #     self.window, self.event, self.values = sg.read_all_windows()

            # if self.window == self.janelaccusto and self.event == sg.WINDOW_CLOSED:
            #     self.janelaccusto.hide()
            #     print('Escondeu')
                # mainform = JanelaPrincipal()
                # mainform.iniciar_tela()