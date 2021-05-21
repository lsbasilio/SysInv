import sqlite3
from db.db import Db
import csv
import pandas as pd
from model.entities.bens import Bens
from model.dao.impl.centrodecustodaoSqLite import CentroDeCustoDao
from model.dao.bensdao import BensDao


class BensDaoSqLite(BensDao):

    _nome_tabela = 'bens'

    def __init__(self, conn):
        self._banco = conn
        self.bens = Bens()

    def delete_all(self):
        cursor = self._banco.cursor()

        try:
            str_sql = f'DELETE FROM {self._nome_tabela}'
            cursor.execute(str_sql)
        except sqlite3.Error as erro:
            raise ValueError('Erro ao excluir todos os Bens: ', erro)
        finally:
            self._banco.commit()

    def insert(self, obj):

        cursor = self._banco.cursor()

        try:
            str_sql = f"INSERT INTO {self._nome_tabela} "
            str_sql += "(Numero_Bem,Numero_BemAnt,,Ccusto_Id,Status,Data_Inv,Conta,Data,Observacao,Local_Id,Usuario,Descricao,Marca,Modelo,Numero_Serie,Situacao)"
            str_sql += " VALUES "
            str_sql += f"({obj.get_numero_bem()},{obj.get_numero_bemant()},{obj.get_ccusto_id()},{obj.get_status_numerico()},'{obj.get_data_inv()}'," \
                       f"{obj.get_conta()},'{obj.get_data()}','{obj.get_observacao()}'," \
                       f"{obj.get_local_id()},'{obj.get_usuario()}'," \
                       f"'{obj.get_descricao()}','{obj.get_marca()}','{obj.get_modelo()}'," \
                       f"'{obj.get_numeroserie()}','{obj.get_situacao()}')"

            cursor.execute(str_sql)

        except sqlite3.Error as erro:
            raise ValueError('Erro ao inserir os Bens: ', erro)
        finally:
            self._banco.commit()

    def update(self, obj):

        cursor = self._banco.cursor()

        try:
            str_sql = f"UPDATE {self._nome_tabela} "
            str_sql += f"SET Ccusto_Id = {obj.get_ccusto_id()}, "
            str_sql += f"Numero_Bem = {obj.get_numero_bem()}, "
            str_sql += f"Numero_BemAnt = {obj.get_numero_bemant()}, "
            str_sql += f"Status = {obj.get_status_numerico()}, "
            str_sql += f"Data_Inv = '{obj.get_data_inv()}', "
            str_sql += f"Conta = {obj.get_conta()}, "
            str_sql += f"Data = '{obj.get_data()}', "
            str_sql += f"Observacao = '{obj.get_observacao()}', "
            str_sql += f"Local_Id = {obj.get_local_id()}, "
            str_sql += f"Usuario = '{obj.get_usuario()}', "
            str_sql += f"Descricao = '{obj.get_descricao()}', "
            str_sql += f"Marca = '{obj.get_marca()}', "
            str_sql += f"Modelo = '{obj.get_modelo()}', "
            str_sql += f"Numero_Serie = '{obj.get_numeroserie()}', "
            str_sql += f"Situacao = '{obj.get_situacao()}' "
            # if obj.get_numero_bemant == 0:
            str_sql += f"WHERE Numero_Bem = {obj.get_numero_bem()} OR Numero_Bem = {obj.get_numero_bemant()}"
            # else:
            #     str_sql += f"WHERE Numero_Bem = {obj.get_numero_bemant()}"

            # print(str_sql)
            cursor.execute(str_sql)

        except sqlite3.Error as erro:
            raise ValueError('Erro ao atualizar o Bem: ', erro)
        finally:
            self._banco.commit()

    def cancelar(self, obj):

        cursor = self._banco.cursor()

        try:
            str_sql = f"UPDATE {self._nome_tabela} "
            str_sql += f"SET Ccusto_Id = {obj.get_ccusto_ant()}, "
            str_sql += f"Status = {obj.get_status_numerico()}, "
            str_sql += f"Data_Inv = '{obj.get_data_inv()}', "
            str_sql += f"Observacao = '{obj.get_observacao()}', "
            str_sql += f"Local_Id = {obj.get_local_ant()}, "
            str_sql += f"Usuario = '{obj.get_usuario()}', "
            str_sql += f"Descricao = '{obj.get_descricao_ant()}', "
            str_sql += f"Marca = '{obj.get_marca_ant()}', "
            str_sql += f"Modelo = '{obj.get_modelo_ant()}', "
            str_sql += f"Numero_Serie = '{obj.get_numero_serieant()}', "
            str_sql += f"Situacao = '{obj.get_situacao_ant()}' "
            str_sql += f"WHERE Numero_Bem = {obj.get_numero_bem()}"

            cursor.execute(str_sql)

        except sqlite3.Error as erro:
            raise ValueError('Erro ao cancelar o Bem: ', erro)
        finally:
            self._banco.commit()

    def delete_by_id(self, id):

        cursor = self._banco.cursor()

        try:
            str_sql = f"DELETE FROM {self._nome_tabela} WHERE Numero_Bem = {id}"

            cursor.execute(str_sql)

        except sqlite3.Error as erro:
            raise ValueError('Erro ao excluir o Bem: ', erro)
        finally:
            self._banco.commit()

    def find_by_id(self, id):

        cursor = self._banco.cursor()

        try:
            str_sql = f"SELECT * FROM {self._nome_tabela} " \
                      f"WHERE Numero_Bem = {id}"

            cursor.execute(str_sql)

            lista = cursor.fetchall()

            if len(lista) > 0:
                return self.instantiate_bem(lista[0])

            return None

        except sqlite3.Error as erro:
            raise ValueError('Erro ao encontrar o Bem: ', erro)

    def existe(self, id):

        cursor = self._banco.cursor()

        try:
            str_sql = f"SELECT * FROM {self._nome_tabela} " \
                      f"WHERE Numero_Bem = {id}"

            cursor.execute(str_sql)

            lista = cursor.fetchall()

            if len(lista) > 0:
                return True
            else:
                return None

        except sqlite3.Error as erro:
            raise ValueError('Erro aoverificar se o Bem existe: ', erro)

    def find_all(self):

        lista = []

        cursor = self._banco.cursor()

        try:
            str_sql = f"SELECT * FROM {self._nome_tabela} ORDER BY Numero_bem"

            cursor.execute(str_sql)

            lista_bens = cursor.fetchall()

            for row in lista_bens:
                lista.append(self.instantiate_bem(row)) # Lista com os objetos de Centro de Custo

            return lista

        except sqlite3.Error as erro:
            raise ValueError('Erro ao encontrar todos os Bens: ', erro)

    def instantiate_bem(self, lista):
        self.bens_temp = Bens()
        self.bens_temp.set_numero_bem(int(lista[0]))
        self.bens_temp.set_ccusto_id(int(lista[1]))
        self.bens_temp.set_status(int(lista[2]))
        self.bens_temp.set_data_inv(lista[3])
        self.bens_temp.set_conta(int(lista[4]))
        self.bens_temp.set_data(lista[5])
        self.bens_temp.set_observacao(lista[6])
        self.bens_temp.set_local_id(int(lista[7]))
        self.bens_temp.set_usuario(lista[8])
        self.bens_temp.set_descricao(lista[9])
        self.bens_temp.set_marca(lista[10])
        self.bens_temp.set_modelo(lista[11])
        self.bens_temp.set_numeroserie(lista[12])
        self.bens_temp.set_situacao(lista[13])
        self.bens_temp.set_numero_bemant(lista[14])
        # Campos anteriores
        if lista[15] is not None:
            self.bens_temp.set_ccusto_ant(int(lista[15]))
        if lista[16] is not None:
            self.bens_temp.set_local_ant(int(lista[16]))
        self.bens_temp.set_descricao_ant(lista[17])
        self.bens_temp.set_marca_ant(lista[18])
        self.bens_temp.set_modelo_ant(lista[19])
        self.bens_temp.set_numero_serieant(lista[20])
        self.bens_temp.set_situacao_ant(lista[21])

        return self.bens_temp

    def salvar_campos_originais(self):

        cursor = self._banco.cursor()

        try:
            str_sql = "UPDATE BENS SET "
            str_sql += "Ccusto_Ant = Ccusto_Id,"
            str_sql += "Local_Ant = Local_Id,"
            str_sql += "Descricao_Ant = Descricao,"
            str_sql += "Marca_Ant = Marca,"
            str_sql += "Modelo_Ant = Modelo,"
            str_sql += "Numero_SerieAnt = Numero_Serie,"
            str_sql += "Situacao_Ant = Situacao"

            cursor.execute(str_sql)

        except sqlite3.Error as erro:
            raise ValueError('Erro ao inserir os Bens: ', erro)
        finally:
            self._banco.commit()

    def update_bens_pendentes(self):

        cursor_update = self._banco.cursor()
        cursor_ccusto = self._banco.cursor()

        try:
            cursor_ccusto.execute(f'SELECT Ccusto_Id FROM {self._nome_tabela}')

            for row in cursor_ccusto:
                str_sql = f"UPDATE {self._nome_tabela} SET Pendentes = (SELECT COUNT(*) FROM bens WHERE Ccusto_Id = " \
                          f"{row[0]}) WHERE Ccusto_Id = {row[0]}"
                cursor_update.execute(str_sql)

        except sqlite3.Error as erro:
            raise ValueError('Erro ao atualizar os Bens Pendentes dos Centros de Custo: ', erro)
        finally:
            self._banco.commit()

    def carrega_csv(self, path):
        try:

            with open(path) as csvfile:
                registro = csv.reader(csvfile, delimiter=';')

                self.delete_all()

                for row in registro:
                    self.bens.set_numero_bem(int(row[0]))
                    self.bens.set_ccusto_id(int(row[1]))
                    self.bens.set_local_id(int(row[2]))
                    self.bens.set_descricao(row[3])
                    self.bens.set_marca(row[4])
                    self.bens.set_modelo(row[5])
                    self.bens.set_numeroserie(row[6])
                    self.bens.set_conta(row[7])
                    self.bens.set_situacao(row[8])
                    self.bens.set_status(1)
                    self.insert(self.bens)

                # Salvando os campos originais na tabela de Bens
                self.salvar_campos_originais()

                # Atualizando os Bens pendentes de todos os Centro de Custo
                self.update_bens_pendentes()

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

            lista_Numeros_bem = planilha[colunas[0]].tolist()
            lista_ccustos = planilha[colunas[1]].tolist()
            lista_locais = planilha[colunas[2]].tolist()
            lista_descricao = planilha[colunas[3]].tolist()
            lista_marca = planilha[colunas[4]].tolist()
            lista_modelo = planilha[colunas[5]].tolist()
            lista_numeroserie = planilha[colunas[6]].tolist()
            lista_conta = planilha[colunas[7]].tolist()
            lista_situacao = planilha[colunas[8]].tolist()

            i = 0
            for codigo in lista_Numeros_bem:
                self.bens.set_numero_bem(codigo)
                self.bens.set_ccusto_id(lista_ccustos[i])
                self.bens.set_local_id(lista_locais[i])
                self.bens.set_descricao(lista_descricao[i])
                self.bens.set_marca(lista_marca[i])
                self.bens.set_modelo(lista_modelo[i])
                self.bens.set_numeroserie(lista_numeroserie[i])
                self.bens.set_conta(lista_conta[i])
                self.bens.set_situacao(lista_situacao[i])
                self.bens.set_status(1)
                self.insert(self.bens)
                i += 1

            # Salvando os campos originais na tabela de Bens
            self.salvar_campos_originais()

            # Atualizando os Bens pendentes de todos os Centro de Custo
            self.update_bens_pendentes()

        except FileNotFoundError:
            raise ValueError(f'O arquivo Excel informado: {path} não existe!')
        # finally:
        #     self._banco.commit()