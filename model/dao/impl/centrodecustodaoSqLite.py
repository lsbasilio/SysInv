import sqlite3
from db.db import Db
import csv
import pandas as pd
from model.entities.centrodecusto import CentroDeCusto
from model.dao.centrodecustodao import CentroDeCustoDao


class CentroDeCustoDaoSqLite(CentroDeCustoDao):

    _nome_tabela = 'centrodecusto'

    def __init__(self):
        self._db = Db()
        self._banco = self._db.get_connection()
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
            str_sql += f"({obj.get_ccusto_id()},'{obj.get_descricao()}',{obj.get_status()},'{obj.get_data_inicio()}','{obj.get_data_fim()}',{obj.get_pendentes()},{obj.get_inventariados()},{obj.get_novos()})"

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
            str_sql += f"Status = {obj.get_status()}, "
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
            raise ValueError('Erro ao encontrar o Local: ', erro)

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

    def instantiate_ccusto(self, lista):
        self.ccustos_temp = CentroDeCusto()
        self.ccustos_temp.set_ccusto_id(int(lista[0]))
        self.ccustos_temp.set_descricao(lista[1])
        self.ccustos_temp.set_status(int(lista[2]))
        self.ccustos_temp.set_data_inicio(lista[3])
        self.ccustos_temp.set_data_fim(lista[4])
        self.ccustos_temp.set_pendentes(int(lista[5]))
        self.ccustos_temp.set_inventariados(int(lista[6]))
        self.ccustos_temp.set_novos(int(lista[7]))
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
            raise ValueError(f'O arquivo CSV informado: {path} não existe!')
        except csv.Error as e:
            print(f'Erro na Importação do Centro de Custo: {path}, Linha: {registro.line_num} : {e}')
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
            raise ValueError(f'O arquivo Excel informado: {path} não existe!')
        # finally:
        #     self._banco.commit()
