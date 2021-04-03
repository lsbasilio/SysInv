class DescrComplementar:

    ##### Construtores ######
    def __init__(self, descricao_id = '', descricao = ''):
        self._descricao_id = descricao_id
        self._descricao = descricao

    ##### Getters e Setters #####
    def get_descricao_id(self):
        return self._descricao_id

    def set_descricao_id(self, valor):
        self._descricao_id = valor

    def get_descricao(self):
        return self._descricao

    def set_descricao(self, valor):
        self._descricao = valor