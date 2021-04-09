from model.entities.enum.ccusto_status import CcustoStatus


class CentroDeCusto:

    ##### Construtores ######
    def __init__(self,ccusto_id=0,descricao='',status=CcustoStatus.Nao_Inicializado,data_inicio='',data_fim='',pendentes=0,inventariados=0,novos=0):
        self._ccusto_id = ccusto_id
        self._descricao = descricao
        self._status = CcustoStatus(status)
        self._data_inicio = data_inicio
        self._data_fim = data_fim
        self._pendentes = pendentes
        self._inventariados = inventariados
        self._novos = novos

    ##### Getters e Setters #####
    def get_ccusto_id(self):
        return self._ccusto_id

    def set_ccusto_id(self, valor):
        self._ccusto_id = valor

    def get_descricao(self):
        return self._descricao

    def set_descricao(self, valor):
        self._descricao = valor

    def get_status(self):
        return self._status

    def set_status(self, valor):
        self._status = valor

    def get_data_inicio(self):
        return self._data_inicio

    def set_data_inicio(self, valor):
        self._data_inicio = valor

    def get_data_fim(self):
        return self._data_fim

    def set_data_fim(self, valor):
        self._data_fim = valor

    def get_pendentes(self):
        return self._pendentes

    def set_pendentes(self, valor):
        self._pendentes = valor

    def get_inventariados(self):
        return self._inventariados

    def set_inventariados(self, valor):
        self._inventariados = valor

    def get_novos(self):
        return self._novos

    def set_novos(self, valor):
        self._novos = valor

    def __str__(self):
        pass

    ##### Métodos #####
    def ativar(self):
        pass

    def encerrar(self):
        pass

