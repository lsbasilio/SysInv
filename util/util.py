from datetime import date, datetime

width_combo = 45
height_combo = 15

size_input = 47

size_tela_inventario = (400, 400)

def get_data_atual():
    data_atual = date.today()
    data_formatada = data_atual.strftime('%d/%m/%Y')
    return data_formatada


def get_data_hora_atual():
    data_hora_atual = datetime.now()
    data_formatada = data_hora_atual.strftime('%d/%m/%Y %H:%M')
    return data_formatada


def get_tema_janelas():
    return 'DarkTeal7'


# def get_size_input():
#     return 47


def get_id(valor):
    valor_selecionado = valor
    id = valor_selecionado.split(' - ')
    return id[0]


def try_parse_to_int(string):
    try:
        return int(string)
    except (TypeError, ValueError):
        return None


def retira_caracteres_especiais(texto):
    aux = ''
    for letra in texto:
        if letra not in ['\n', '\t', '\r']:
            aux += letra

    return aux


