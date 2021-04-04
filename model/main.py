from model.dao.centrodecustodao import CentroDeCustoDao
from model.entities.centrodecusto import CentroDeCusto
from model.entities.locais import Locais
from model.entities.descrpadrao import DescrPadrao
from model.entities.descrcomplementar import DescrComplementar
from model.entities.bens import Bens
from model.dao.locaisdao import LocaisDao

import os.path as file

from db.db import Db

import csv
import pandas as pd
import xlrd as excel

ccusto = CentroDeCustoDao()
locaisdao = LocaisDao()
#print(ccusto.get_ccusto_id())

locais = Locais()
print(locais.get_local_id())

descrpadrao = DescrPadrao()
print(descrpadrao.get_descricao_id())

descrcomplementar = DescrComplementar()
print(descrcomplementar.get_descricao_id())

bens = Bens()
print(bens.get_numero_bem())

# Carga a partir de arquivo Csv
teste = 'TESTE1;TESTE2'
# print(Db.load_properties())
locaisdao.carrega_local_excel(r'C:\SysInv\Dados\Carga\Inventario_Teste.xlsx', 'Local')
#locaisdao.carrega_local_csv(r'C:\SysInv\Dados\Carga\Locais.csv')
#ccusto.carrega_ccusto_csv(r'C:\SysInv\Dados\Carga\Locais.csv')
#ccusto.carrega_ccusto_excel(r'C:\SysInv\Dados\Carga\Inventario_Teste.xlsx', 'CentroCusto')
# with open('C:\SysInv\Dados\Carga\CentroCusto.csv') as csvfile:
#     registro = csv.reader(csvfile, delimiter=';')
#     for row in registro:
#         print(row)

# Carga a partir de arquivo Excel
#ccusto.carrega_ccusto_excel(r'C:\SysInv\Dados\Carga\CentroCusto.xlsx', 'CentroCusto')

# x = pd.read_excel(r'C:\SysInv\Dados\Carga\CentroCusto.xlsx',sheet_name='CentroCusto')
# lista_codigos = x['CODIGO'].tolist()
# lista_descricoes = x['DESCRICAO'].tolist()
# print(lista_descricoes[3])
# i = 0
# for codigo in lista_codigos:
#  print(str(codigo) + ' - ' + lista_descricoes[i])
#  i += 1
#print(lista)
#print(lista.count())
#with pd.read_excel(open(r'C:\SysInv\Dados\Carga\CentroCusto.xlsx') as teste:

# workbook = excel.open_workbook(r'C:\SysInv\Dados\Carga\CentroCusto.xlsx')
# planilha = workbook.sheet_by_name('CentroCusto')
# x = planilha.col_values(0)
# print(x)
# y = planilha.col_values(1)
# print(y)
#print(x['CODIGO'][0])
#print(x['DESCRICAO'][0])
# print(x[0][1])

# teste = teste.split(';')
# print(teste[0])
# print(teste[1])

# centrodao = CentroDeCustoDao()
# ccusto.set_ccusto_id(350)
# ccusto.set_descricao('TESTANDO')
# centrodao.insert(ccusto)


def load_properties(propriedade):
    arquivodb = open('C:\dev\SysInv\dbproperties.txt', 'r')
    texto = arquivodb.readline()
    #print('texto:', "'" + texto.replace("\n",'') + "'")
    print('texto:', "'" + texto.replace('\n',''))
    for line in arquivodb.readlines():
        str = line.split('=')
        if propriedade == str[0]:
            return str[1]


def ler_linhas_arquivo(propriedade):
    arquivodb = open('..\dbproperties.txt', 'r')   # 'C:\dev\SysInv\dbproperties.txt'
    for linha in arquivodb:
        str = linha.split('=')
        if propriedade == str[0]:
            return "'" + str[1].rstrip('\n') + "'"
    arquivodb.close()


print(ler_linhas_arquivo('dblocation'))
# print(load_properties('dblocation'))

#arquivodb = open('dbproperties.txt', 'r')

print(__file__)
print(file.abspath(__file__))
print(file.dirname(file.abspath('C:\dev\SysInv\model\main.py')))