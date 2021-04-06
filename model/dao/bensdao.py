import sqlite3
from db.db import Db
import csv
import pandas as pd
from model.entities.bens import Bens
from model.dao.centrodecustodao import CentroDeCustoDao

class BensDao:

    def __init__(self):
        self._db = Db()
        self._banco = self._db.get_connection()
        self.bens = Bens()
        self.CcustoDao = CentroDeCustoDao()

    def delete_all(self):
        cursor = self._banco.cursor()

        try:
            str_sql = 'DELETE FROM bens'
            cursor.execute(str_sql)
        except sqlite3.Error as erro:
            raise ValueError('Erro ao excluir todos os Bens: ', erro)
        finally:
            self._banco.commit()

    def insert(self, obj):

        cursor = self._banco.cursor()

        try:
            str_sql = "INSERT INTO bens "
            str_sql += "(Numero_Bem,Ccusto_Id,Status,Data_Inv,Conta,Data,Observacao,Local_Id,Usuario,Descricao,Marca,Modelo,Numero_Serie,Situacao)"
            str_sql += " VALUES "
            str_sql += f"({obj.get_numero_bem()},{obj.get_ccusto_id()},{obj.get_status()},'{obj.get_data_inv()}'," \
                       f"{obj.get_conta()},'{obj.get_data()}','{obj.get_observacao()}'," \
                       f"{obj.get_local_id()},'{obj.get_usuario()}'," \
                       f"'{obj.get_descricao()}','{obj.get_marca()}','{obj.get_modelo()}'," \
                       f"'{obj.get_numeroserie()}','{obj.get_situacao()}')"

            cursor.execute(str_sql)

        except sqlite3.Error as erro:
            raise ValueError('Erro ao inserir os Bens: ', erro)

    def salvar_campos_originais(self):

        cursor = self._banco.cursor()

        try:
            str_sql = "UPDATE BENS SET "
            str_sql += "Ccusto_Ant = Ccusto_Id,"
            str_sql += "Local_Ant = Local_Id,"
            str_sql += "Descricao_Ant = Descricao,"
            str_sql += "Marca_Ant = Marca,"
            str_sql += "Modelo_Ant = Modelo,"
            str_sql += "Numero_SerieAnt = Numero_Serie"

            cursor.execute(str_sql)

        except sqlite3.Error as erro:
            raise ValueError('Erro ao inserir os Bens: ', erro)
        finally:
            self._banco.commit()

    def carrega_bens_csv(self, path):
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
                    self.insert(self.bens)

                # Salvando os campos originais na tabela de Bens
                self.salvar_campos_originais()

                # Atualizando os Bens pendentes de todos os Centro de Custo
                self.CcustoDao.update_bens_pendentes()

                csvfile.close()

        except FileNotFoundError:
            raise ValueError(f'O arquivo CSV informado: {path} não existe!')
        except csv.Error as e:
            print(f'Erro na Importação do Centro de Custo: {path}, Linha: {registro.line_num} : {e}')
        finally:
            self._banco.commit()

    def carrega_bens_excel(self, path, nome_aba=''):
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
                self.insert(self.bens)
                i += 1

            # Salvando os campos originais na tabela de Bens
            self.salvar_campos_originais()

            # Atualizando os Bens pendentes de todos os Centro de Custo
            self.CcustoDao.update_bens_pendentes()

        except FileNotFoundError:
            raise ValueError(f'O arquivo Excel informado: {path} não existe!')
        finally:
            self._banco.commit()