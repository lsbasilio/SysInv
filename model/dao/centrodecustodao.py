import sqlite3
from db.db import Db
import csv
import pandas as pd
from model.entities.centrodecusto import CentroDeCusto


class CentroDeCustoDao:

    def __init__(self):
        self._db = Db()
        self._banco = self._db.get_connection()
        self.ccusto = CentroDeCusto()

    def delete_all(self):
        cursor = self._banco.cursor()

        try:
            str_sql = 'DELETE FROM centrodecusto'
            cursor.execute(str_sql)
        except sqlite3.Error as erro:
            raise ValueError('Erro ao excluir todos os Centros de Custo: ', erro)
        finally:
            self._banco.commit()

    def insert(self, obj):

        cursor = self._banco.cursor()

        try:
            str_sql = "INSERT INTO centrodecusto "
            str_sql += "(Ccusto_id,Descricao,Status,Data_Inicio,Data_Fim,Pendentes,Inventariados,Novos)"
            str_sql += " VALUES "
            str_sql += f"({obj.get_ccusto_id()},'{obj.get_descricao()}',{obj.get_status()},'{obj.get_data_inicio()}','{obj.get_data_fim()}',{obj.get_pendentes()},{obj.get_inventariados()},{obj.get_novos()})"

            cursor.execute(str_sql)

        except sqlite3.Error as erro:
            raise ValueError('Erro ao inserir o Centro de Custo: ', erro)
        finally:
            self._banco.commit()

    def update_bens_pendentes(self):

        cursor_update = self._banco.cursor()
        cursor_ccusto = self._banco.cursor()

        try:
            cursor_ccusto.execute('SELECT Ccusto_Id FROM centrodecusto')

            for row in cursor_ccusto:
                str_sql = "UPDATE centrodecusto SET Pendentes = (SELECT COUNT(*) FROM bens WHERE Ccusto_Id = " \
                          f"{row[0]}) WHERE Ccusto_Id = {row[0]}"
                cursor_update.execute(str_sql)

        except sqlite3.Error as erro:
            raise ValueError('Erro ao excluir todos os Centros de Custo: ', erro)
        finally:
            self._banco.commit()

    def carrega_ccusto_csv(self, path):
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

    def carrega_ccusto_excel(self, path, nome_aba=''):
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
