from model.dao.centrodecustodao import CentroDeCustoDao
from model.entities.centrodecusto import CentroDeCusto
from model.entities.locais import Locais
from model.entities.descrpadrao import DescrPadrao
from model.entities.descrcomplementar import DescrComplementar
from model.entities.bens import Bens
from model.dao.locaisdao import LocaisDao
from model.dao.descrpadraodao import DescrPadraoDao
from model.dao.descrcomplementardao import DescrComplementarDao
from model.dao.bensdao import BensDao

import os.path as file

from db.db import Db

import csv
import pandas as pd
import xlrd as excel

ccustodao = CentroDeCustoDao()
ccusto = CentroDeCusto()
# lista_ccusto = ccustodao.find_all()
# for ccusto in lista_ccusto:
#     print(ccusto.get_ccusto_id(), ccusto.get_descricao(),ccusto.get_status(),ccusto.get_pendentes())
# ccusto = ccustodao.find_by_id(308000)
# if ccusto is not None:
#     print(ccusto.get_ccusto_id(),ccusto.get_descricao(),ccusto.get_status(),ccusto.get_pendentes())
ccusto.set_ccusto_id(300000)
ccusto.set_descricao('TESTE')
ccustodao.delete_by_id(ccusto.get_ccusto_id())
#ccustodao.update(ccusto)

locaisdao = LocaisDao()
#print(ccusto.get_ccusto_id())

locais = Locais()
print(locais.get_local_id())

descrpadraodao = DescrPadraoDao()
# descrpadrao = descrpadraodao.find_by_id('VPD')
# if descrpadrao is not None:
#  print('Descr_Id:', descrpadrao.get_descricao_id())
#  print('DescrPadrao:', descrpadrao.get_descricao())
#print(descrpadrao.get_descricao_id())
# lista_descrpadrao = descrpadraodao.find_all()
# for descr in lista_descrpadrao:
#     print(descr.get_descricao_id(), descr.get_descricao())
# descpadrao = DescrPadrao()
# descpadrao.set_descricao_id('ABAF')
# descpadrao.set_descricao('ARMARIO DE ACO INOX')
# descrpadraodao.delete_by_id(descpadrao.get_descricao_id())

# descrcomplementardao = DescrComplementarDao()
# #descrcomplementar = DescrComplementar()
# lista_descrs = descrcomplementardao.find_all()
# for descr in lista_descrs:
#     print(descr.get_descricao_id(), descr.get_descricao())
# descrcomplementar = descrcomplementardao.find_by_id('ARM')
# print(descrcomplementar.get_descricao_id(),descrcomplementar.get_descricao())
# descrcomplementar.set_descricao_id('MOG')
# descrcomplementar.set_descricao('TESTANDO')
# descrcomplementardao.update(descrcomplementar)
# descrcomplementardao.delete_by_id('MAD')
#print(descrcomplementar.get_descricao_id())

bensdao = BensDao()
#print(bens.get_numero_bem())
bens = Bens()
lista_bens = bensdao.find_all()
for bens in lista_bens:
    print(bens.get_numero_bem(),bens.get_ccusto_id(),bens.get_descricao(),bens.get_marca(),bens.get_modelo(),bens.get_numeroserie())
# bens = bensdao.find_by_id(500)
# if bens is not None:
#     print(bens.get_numero_bem(),bens.get_ccusto_id(),bens.get_descricao(),bens.get_marca(),bens.get_modelo(),bens.get_numeroserie())
#bens.set_numero_bem(181)
# bens.set_ccusto_id(205000)
# bens.set_status(2)
# bens.set_data_inv('08/04/2021')
# bens.set_conta(666)
# bens.set_data('05/04/2005')
# bens.set_observacao('TESTANDO A OBSERVAÇÃO')
# bens.set_local_id(1220)
# bens.set_usuario('LEANDRO')
# bens.set_descricao('TESTANDO A DESCRIÇÃO')
# bens.set_marca('MARCA')
# bens.set_modelo('MODELO')
# bens.set_numeroserie('NUMSERIE')
# bens.set_situacao('SITUAÇÃO')
#bensdao.delete_by_id(1161)
#bensdao.update(bens)
# Carga a partir de arquivo Csv
teste = 'TESTE1;TESTE2'
#locais = locaisdao.find_all()
# lista_locais = locaisdao.find_all()
# for local in lista_locais:
#     print(local.get_local_id(), local.get_descricao())
# locais = locaisdao.find_by_id(1230)
# if locais is not None:
#  print('Local:', locais.get_local_id())
#  print('DescrLocal:', locais.get_descricao())
# locais.set_local_id(1213)
# locais.set_descricao('TESTE')
# locaisdao.delete_by_id(locais.get_local_id())
#locaisdao.update(locais)
# print(Db.load_properties())
#descrpadraodao.carrega_descrpadrao_csv(r'C:\SysInv\Dados\Carga\DescrPadrao.csv')
#descrcomplementardao.carrega_descrcomplementar_csv(r'C:\SysInv\Dados\Carga\DescrCompl.csv')
#descrcomplementardao.carrega_descrcomplementar_excel(r'C:\SysInv\Dados\Carga\Inventario_Teste.xlsx', 'Descr.Compl')
#descrpadraodao.carrega_descrpadrao_excel(r'C:\SysInv\Dados\Carga\Inventario_Teste.xlsx', 'Descr.Padrao')
#locaisdao.carrega_local_excel(r'C:\SysInv\Dados\Carga\Inventario_Teste.xlsx', 'Local')
#locaisdao.carrega_local_csv(r'C:\SysInv\Dados\Carga\Locais.csv')
#ccusto.carrega_ccusto_csv(r'C:\SysInv\Dados\Carga\CentroCusto.csv')
#ccusto.carrega_ccusto_excel(r'C:\SysInv\Dados\Carga\Inventario_Teste.xlsx', 'CentroCusto')
#ccusto.update_bens_pendentes()
#bens.carrega_bens_csv(r'C:\SysInv\Dados\Carga\Bens.csv')
#bens.carrega_bens_excel(r'C:\SysInv\Dados\Carga\Inventario_Teste.xlsx', 'Bens')
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

dict = {'Leandro': 30}
print(dict['Leandro'])
dict2 = {2250: 40}
dict2[2250] = dict2[2250] + 1
print(dict2[2250])