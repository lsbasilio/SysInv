class Locais:

    ##### Construtores ######
    def __init__(self, local_id = 0, descricao = ''):
        self._local_id = local_id
        self._descricao = descricao

    ##### Getters e Setters #####
    def get_local_id(self):
        return self._local_id

    def set_local_id(self, valor):
        self._local_id = valor

    def get_descricao(self):
        return self._descricao

    def set_descricao(self, valor):
        self._descricao = valor

    ##### Métodos #####

    def __str__(self):
        return str(self._local_id) + ' - ' + self._descricao
