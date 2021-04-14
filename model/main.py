from model.entities.centrodecusto import CentroDeCusto
from model.entities.locais import Locais
from model.entities.bens import Bens
from model.entities.descrpadrao import DescrPadrao
from model.entities.descrcomplementar import DescrComplementar
from model.dao.impl.descrpadraodaoSqLite import DescrPadraoDaoSqLite
from model.dao.impl.bensdaoSqLite import BensDaoSqLite
from model.dao.impl.centrodecustodaoSqLite import CentroDeCustoDaoSqLite
from model.dao.daofactory import DaoFactory
from model.services.locaisservice import LocaisService
from model.services.descrpadraoservice import DescrPadraoService
from model.services.descrcomplementarservice import DescrComplementarService
from model.services.centrodecustoservice import CentroDeCustoService
from model.services.bensservice import BensService
from model.entities.enum.ccusto_status import CcustoStatus
from model.entities.enum.bens_status import BensStatus
#from model.dao.impl.locaisdaoSqLite import LocaisDaoSqLite
from model.dao.impl.descrcomplementardaoSqLite import DescrComplementarDaoSqLite
import os.path as file

#ccustodao = CentroDeCustoDaoSqLite()
#daofactory = DaoFactory()
# locaisdao = daofactory.create_locais_dao()
# locais = locaisdao.find_by_id(5)
# if locais is not None:
#  print('Local:', locais.get_local_id())
#  print('DescrLocal:', locais.get_descricao())
 
# descrpadraodao = daofactory.create_descrpadrao_dao()
# descrpadrao = descrpadraodao.find_by_id('AA')
# if descrpadrao is not None:
#  print('Descr_id:', descrpadrao.get_descricao_id())
#  print('Descr:', descrpadrao.get_descricao())

# descrcomplementardao = daofactory.create_descrcomplementar_dao()
# descrcomplementar = descrcomplementardao.find_by_id('CAD')
# if descrcomplementar is not None:
#  print('Descr_id:', descrcomplementar.get_descricao_id())
#  print('Descr:', descrcomplementar.get_descricao())
# descrpadraodao = DescrPadraoDaoSqLite()
# descrcomplementardao = DescrComplementarDaoSqLite()
# bensdao = BensDaoSqLite()

# centrodecustodao = daofactory.create_centrodecusto_dao()
# centrodecusto = centrodecustodao.find_by_id(101000)
# if centrodecusto is not None:
#  print('Ccusto_id:', centrodecusto.get_ccusto_id())
#  print('Descr:', centrodecusto.get_descricao())

# bensdao = daofactory.create_bens_dao()
# bens = bensdao.find_by_id(436)
# if bens is not None:
#  print('Bens Id:', bens.get_numero_bem())
#  print('Descr:', bens.get_descricao())

#ccusto = CentroDeCusto()
# lista_ccusto = ccustodao.find_all()
# for ccusto in lista_ccusto:
#     print(ccusto.get_ccusto_id(), ccusto.get_descricao(),ccusto.get_status(),ccusto.get_pendentes())
# ccusto = ccustodao.find_by_id(308000)
# if ccusto is not None:
#     print(ccusto.get_ccusto_id(),ccusto.get_descricao(),ccusto.get_status(),ccusto.get_pendentes())
# ccusto.set_ccusto_id(300000)
# ccusto.set_descricao('TESTE')
# ccustodao.delete_by_id(ccusto.get_ccusto_id())
#ccustodao.update(ccusto)

#locaisdao = LocaisDaoSqLite()
#print(ccusto.get_ccusto_id())

# ccusto = CentroDeCusto()
# ccusto.set_ccusto_id(2)
# ccusto.ativar()
# print(ccusto.get_ccusto_id(), ccusto.get_status(), ccusto.get_data_inicio())
# ccusto.encerrar()
# print(ccusto.get_ccusto_id(), ccusto.get_status(), ccusto.get_data_inicio())

# locais = Locais(10, 'ALTERADO')
localservice = LocaisService()
#localservice.remove(locais)
#localservice.save_or_update(locais)
lista = localservice.find_all()
for local in lista:
    print(local)

# descrpadrao = DescrPadrao('CAF', 'CAFETEIRA TESTANDO')
# descrpadraoservice = DescrPadraoService()
#descrpadraoservice.remove(descrpadrao)
#descrpadraoservice.save_or_update(descrpadrao)
# lista = descrpadraoservice.find_all()
# for desc in lista:
#     print(desc)

# descrcomplementar = DescrComplementar('MAD', 'MADEIRA TESTANDO')
# descrcomplementarservice = DescrComplementarService()
# descrcomplementarservice.remove(descrcomplementar)
#descrcomplementarservice.save_or_update(descrcomplementar)
# lista = descrcomplementarservice.find_all()
# for descr in lista:
#     print(descr)

# ccusto = CentroDeCusto(302000, 'CCUSTO TESTANDO',CcustoStatus.Ativo,'','',3,3,3)
# ccustoservice = CentroDeCustoService()
#ccustoservice.remove(ccusto)
#ccustoservice.save_or_update(ccusto)
# lista = ccustoservice.find_all()
# for setor in lista:
#     print(setor)

# bens = Bens(431, 204000, BensStatus.Inventariado,'01/04/2020',123,'25/01/1999','OBS',2323,'Leandro','DETECTOR ALTERADO','MARCA','MODELO','NUM_SERIE','SITUAÇÃO')
# bensservice = BensService()
# bensservice.remove(bens)
#bensservice.save_or_update(bens)
# lista = bensservice.find_all()
# for bem in lista:
#     print(str(bem.get_numero_bem()) + ' - ' + bem.get_descricao())

# descrcomplementar = DescrComplementar('ARM', 'ARMÁRIO')
# print(descrcomplementar)
#
# descrpadraodao = DescrPadraoDao()
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

# bensdao = BensDao()
# #print(bens.get_numero_bem())
# bens = Bens()
# lista_bens = bensdao.find_all()
# for bens in lista_bens:
#     print(bens.get_numero_bem(),bens.get_ccusto_id(),bens.get_descricao(),bens.get_marca(),bens.get_modelo(),bens.get_numeroserie())
# # bens = bensdao.find_by_id(500)
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

