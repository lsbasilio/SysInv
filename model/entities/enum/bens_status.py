from enum import IntEnum

status_texto = ['Bem Não Encontrado no Cadastro', 'Bem Pendente', 'Bem Inventariado', 'Número Trocado', 'Bem Novo']

class BensStatus(IntEnum):

    Nao_Encontrado = 0
    Pendente = 1
    Inventariado = 2
    Numero_Trocado = 3
    Novo = 4
