import csv
import pandas as pd
from model.dao.centrodecustodao import CentroDeCustoDao
#import os.path


class CentroDeCusto:

    ##### Construtores ######
    def __init__(self,ccusto_id=0,descricao='',status=0,data_inicio='',data_fim='',pendentes=0,inventariados=0,novos=0):
        self.centrodao = CentroDeCustoDao()
        self._ccusto_id = ccusto_id
        self._descricao = descricao
        self._status = status
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

    def carrega_ccusto_csv(self, path):
        try:

            with open(path) as csvfile:
                registro = csv.reader(csvfile, delimiter=';')

                self.centrodao.delete_all()

                for row in registro:
                    self._ccusto_id = int(row[0])
                    self._descricao = row[1]
                    self.centrodao.insert(self)

                csvfile.close()

        except FileNotFoundError:
            raise ValueError(f'O arquivo CSV informado: {path} não existe!')
        except csv.Error as e:
            print(f'Erro na Importação: {path}, Linha: {registro.line_num} : {e}')
        finally:
            self.centrodao.banco.commit()

    def carrega_ccusto_excel(self, path, nome_aba=''):
        try:

            if nome_aba == '':
                planilha = pd.read_excel(path)
            else:
                planilha = pd.read_excel(path, sheet_name = nome_aba)

            self.centrodao.delete_all()

            colunas = planilha.columns.tolist()

            lista_codigos = planilha[colunas[0]].tolist()
            lista_descricoes = planilha[colunas[1]].tolist()

            i = 0
            for codigo in lista_codigos:
                self._ccusto_id = codigo
                self._descricao = lista_descricoes[i]
                self.centrodao.insert(self)
                i += 1

        except FileNotFoundError:
            raise ValueError(f'O arquivo Excel informado: {path} não existe!')
        finally:
            self.centrodao.banco.commit()
