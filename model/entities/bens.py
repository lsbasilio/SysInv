from model.entities.enum.bens_status import BensStatus


class Bens:

    ##### Construtores ######
    def __init__(self,numero_bem=0,ccusto_id=0,status=BensStatus.Nao_Encontrado,data_inv='',conta=0,data='',observacao='',local_id=0,usuario='',descricao='',marca='',modelo='',numeroserie='',situacao='',numero_bemant=0,ccusto_ant=0,local_ant=0,descricao_ant='',marca_ant='',modelo_ant='',numero_serieant=''):
        self._numero_bem = numero_bem
        self._ccusto_id = ccusto_id
        self._status = BensStatus(status)
        self._data_inv = data_inv
        self._conta = conta
        self._data = data
        self._observacao = observacao
        self._local_id = local_id
        self._usuario = usuario
        self._descricao = descricao
        self._marca = marca
        self._modelo = modelo
        self._numeroserie = numeroserie
        self._situacao = situacao
        self._numero_bemant = numero_bemant
        self._ccusto_ant = ccusto_ant
        self._local_ant = local_ant
        self._descricao_ant = descricao_ant
        self._marca_ant = marca_ant
        self._modelo_ant = modelo_ant
        self._numero_serieant = numero_serieant

    ##### Getters e Setters #####
    def get_numero_bem(self):
        return self._numero_bem

    def set_numero_bem(self, valor):
        self._numero_bem = valor

    def get_ccusto_id(self):
        return self._ccusto_id

    def set_ccusto_id(self, valor):
        self._ccusto_id = valor

    def get_status(self):
        return self._status

    def set_status(self, valor):
        self._status = valor

    def get_data_inv(self):
        return self._data_inv

    def set_data_inv(self, valor):
        self._data_inv = valor

    def get_conta(self):
        return self._conta

    def set_conta(self, valor):
        self._conta = valor

    def get_data(self):
        return self._data

    def set_data(self, valor):
        self._data = valor

    def get_observacao(self):
        return self._observacao

    def set_observacao(self, valor):
        self._observacao = valor

    def get_local_id(self):
        return self._local_id

    def set_local_id(self, valor):
        self._local_id = valor

    def get_usuario(self):
        return self._usuario

    def set_usuario(self, valor):
        self._usuario = valor

    def get_descricao(self):
        return self._descricao

    def set_descricao(self, valor):
        self._descricao = valor

    def get_marca(self):
        return self._marca

    def set_marca(self, valor):
        self._marca = valor

    def get_modelo(self):
        return self._modelo

    def set_modelo(self, valor):
        self._modelo = valor

    def get_numeroserie(self):
        return self._numeroserie

    def set_numeroserie(self, valor):
        self._numeroserie = valor

    def get_situacao(self):
        return self._situacao

    def set_situacao(self, valor):
        self._situacao = valor

    def get_numero_bemant(self):
        return self._numero_bemant

    def set_numero_bemant(self, valor):
        self._numero_bemant = valor

    def get_ccusto_ant(self):
        return self._ccusto_ant

    def set_ccusto_ant(self, valor):
        self._ccusto_ant = valor

    def get_local_ant(self):
        return self._local_ant

    def set_local_ant(self, valor):
        self._local_ant = valor

    def get_descricao_ant(self):
        return self._descricao_ant

    def set_descricao_ant(self, valor):
        self._descricao_ant = valor

    def get_marca_ant(self):
        return self._marca_ant

    def set_marca_ant(self, valor):
        self._marca_ant = valor

    def get_modelo_ant(self):
        return self._numero_bemant

    def set_modelo_ant(self, valor):
        self._numero_bemant = valor

    def get_numero_serieant(self):
        return self._numero_serieant

    def set_numero_serieant(self, valor):
        self._numero_serieant = valor

#    numero_bemant = 0, ccusto_ant = 0, local_ant = 0, descricao_ant = '', marca_ant = '', modelo_ant = '', numero_serieant

    ##### Métodos #####
    def inventariar(self):
        pass

    def cancelar_inventario(self):
        pass

    def trocar_numero(self):
        pass