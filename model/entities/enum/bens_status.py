from enum import IntEnum


class BensStatus(IntEnum):
    Nao_Encontrado = 0
    Pendente = 1
    Inventariado = 2
    Numero_Trocado = 3
    Novo = 4