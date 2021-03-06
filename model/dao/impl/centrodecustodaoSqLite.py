import sqlite3
from db.db import Db
import csv
import pandas as pd
from model.entities.centrodecusto import CentroDeCusto
from model.dao.centrodecustodao import CentroDeCustoDao
from model.entities.enum.ccusto_status import CcustoStatus
from model.entities.enum.bens_status import BensStatus


class CentroDeCustoDaoSqLite(CentroDeCustoDao):

    _nome_tabela = 'centrodecusto'

    def __init__(self, conn):
        self._banco = conn
        self.ccusto = CentroDeCusto()

    def delete_all(self):
        cursor = self._banco.cursor()

        try:
            str_sql = f'DELETE FROM {self._nome_tabela}'
            cursor.execute(str_sql)
        except sqlite3.Error as erro:
            raise ValueError('Erro ao excluir todos os Centros de Custo: ', erro)
        finally:
            self._banco.commit()

    def insert(self, obj):

        cursor = self._banco.cursor()

        try:
            str_sql = f"INSERT INTO {self._nome_tabela} "
            str_sql += "(Ccusto_id,Descricao,Status,Data_Inicio,Data_Fim,Pendentes,Inventariados,Novos)"
            str_sql += " VALUES "
            str_sql += f"({obj.get_ccusto_id()},'{obj.get_descricao()}',{obj.get_status_numerico()},'{obj.get_data_inicio()}','{obj.get_data_fim()}',{obj.get_pendentes()},{obj.get_inventariados()},{obj.get_novos()})"

            cursor.execute(str_sql)

        except sqlite3.Error as erro:
            raise ValueError('Erro ao inserir o Centro de Custo: ', erro)
        finally:
            self._banco.commit()

    def update(self, obj):

        cursor = self._banco.cursor()

        try:
            str_sql = f"UPDATE {self._nome_tabela} "
            str_sql += f"SET Descricao = '{obj.get_descricao()}', "
            str_sql += f"Status = {obj.get_status_numerico()}, "
            str_sql += f"Data_Inicio = '{obj.get_data_inicio()}', "
            str_sql += f"Data_Fim = '{obj.get_data_fim()}', "
            str_sql += f"Pendentes = {obj.get_pendentes()}, "
            str_sql += f"Inventariados = {obj.get_inventariados()}, "
            str_sql += f"Novos = {obj.get_novos()} "
            str_sql += f"WHERE Ccusto_id = {obj.get_ccusto_id()}"

            cursor.execute(str_sql)

        except sqlite3.Error as erro:
            raise ValueError('Erro ao atualizar o Centro de Custo: ', erro)
        finally:
            self._banco.commit()

    def delete_by_id(self, id):

        cursor = self._banco.cursor()

        try:
            str_sql = f"DELETE FROM {self._nome_tabela} WHERE Ccusto_id = {id}"

            cursor.execute(str_sql)

        except sqlite3.Error as erro:
            raise ValueError('Erro ao excluir o Centro de Custo: ', erro)
        finally:
            self._banco.commit()

    def find_by_id(self, id):

        cursor = self._banco.cursor()

        try:
            str_sql = f"SELECT * FROM {self._nome_tabela} " \
                      f"WHERE Ccusto_id = {id}"

            cursor.execute(str_sql)

            lista = cursor.fetchall()

            if len(lista) > 0:
                return self.instantiate_ccusto(lista[0])

            return None

        except sqlite3.Error as erro:
            raise ValueError('Erro ao encontrar o Centro de Custo: ', erro)

    def find_ccusto_ativo(self):

        cursor = self._banco.cursor()

        try:
            str_sql = f"SELECT * FROM {self._nome_tabela} " \
                      f"WHERE Status = " + str(int(CcustoStatus.Ativo))

            cursor.execute(str_sql)

            lista = cursor.fetchall()

            if len(lista) > 0:
                return self.instantiate_ccusto(lista[0])

            return None

        except sqlite3.Error as erro:
            raise ValueError('Erro ao encontrar o Centro de Custo Ativo: ', erro)

    def find_all(self):

        lista = []

        cursor = self._banco.cursor()

        try:
            str_sql = f"SELECT * FROM {self._nome_tabela} ORDER BY Descricao"

            cursor.execute(str_sql)

            lista_ccustos = cursor.fetchall()

            for row in lista_ccustos:
                lista.append(self.instantiate_ccusto(row)) # Lista com os objetos de Centro de Custo

            return lista

        except sqlite3.Error as erro:
            raise ValueError('Erro ao encontrar todos os Centro de Custo: ', erro)

    def get_total_bens(self, id, status_bem):

        cursor = self._banco.cursor()

        try:

            str_sql = f"SELECT COUNT(*) as QTDE FROM BENS WHERE CCUSTO_ID = {id} AND STATUS = {status_bem}"

            cursor.execute(str_sql)

            lista = cursor.fetchall()

            return lista[0][0]

        except sqlite3.Error as erro:
            raise ValueError('Erro ao encontrar bens do Centro de Custo: ', erro)

    def altera_status_ccusto_ativo(self):

        cursor = self._banco.cursor()

        try:
            str_sql = f"UPDATE {self._nome_tabela} "
            str_sql += f"SET Status = {int(CcustoStatus.Em_Andamento)} "
            str_sql += f'WHERE Status = {int(CcustoStatus.Ativo)}'

            cursor.execute(str_sql)

        except sqlite3.Error as erro:
            raise ValueError('Erro ao atualizar o Centro de Custo Ativo: ', erro)
        finally:
            self._banco.commit()

    def instantiate_ccusto(self, lista):
        self.ccustos_temp = CentroDeCusto()
        self.ccustos_temp.set_ccusto_id(int(lista[0]))
        self.ccustos_temp.set_descricao(lista[1])
        self.ccustos_temp.set_status(int(lista[2]))
        self.ccustos_temp.set_data_inicio(lista[3])
        self.ccustos_temp.set_data_fim(lista[4])
        # self.ccustos_temp.set_pendentes(int(lista[5]))
        self.ccustos_temp.set_pendentes(self.get_total_bens(self.ccustos_temp.get_ccusto_id(), BensStatus.Pendente))
        # self.ccustos_temp.set_inventariados(int(lista[6]))
        self.ccustos_temp.set_inventariados(self.get_total_bens(self.ccustos_temp.get_ccusto_id(),
                                                                BensStatus.Inventariado))
        # self.ccustos_temp.set_novos(int(lista[7]))
        self.ccustos_temp.set_novos(self.get_total_bens(self.ccustos_temp.get_ccusto_id(), BensStatus.Novo))

        return self.ccustos_temp

    def carrega_csv(self, path):
        try:

            with open(path) as csvfile:
                registro = csv.reader(csvfile, delimiter=';')

                self.delete_all()

                for row in registro:
                    self.ccusto.set_ccusto_id(int(row[0]))
                    self.ccusto.set_descricao(row[1])
                    self.insert(self.ccusto)

                csvfile.close()

        except FileNotFoundError:
            raise ValueError(f'O arquivo CSV informado: {path} n??o existe!')
        except csv.Error as e:
            print(f'Erro na Importa????o do Centro de Custo: {path}, Linha: {registro.line_num} : {e}')
        # finally:
        #     self._banco.commit()

    def carrega_excel(self, path, nome_aba=''):
        try:

            if nome_aba == '':
                planilha = pd.read_excel(path, na_filter=False)
            else:
                planilha = pd.read_excel(path, sheet_name=nome_aba, na_filter=False)

            self.delete_all()

            colunas = planilha.columns.tolist()

            lista_codigos = planilha[colunas[0]].tolist()
            lista_descricoes = planilha[colunas[1]].tolist()

            i = 0
            for codigo in lista_codigos:
                self.ccusto.set_ccusto_id(codigo)
                self.ccusto.set_descricao(lista_descricoes[i])
                self.insert(self.ccusto)
                i += 1

        except FileNotFoundError:
            raise ValueError(f'O arquivo Excel informado: {path} n??o existe!')
        # finally:
        #     self._banco.commit()
