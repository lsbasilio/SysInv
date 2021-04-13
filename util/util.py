from datetime import date, datetime


def get_data_atual():
    data_atual = date.today()
    data_formatada = data_atual.strftime('%d/%m/%Y')
    return data_formatada

def get_data_hora_atual():
    data_hora_atual = datetime.now()
    data_formatada = data_hora_atual.strftime('%d/%m/%Y %H:%M')
    return data_formatada