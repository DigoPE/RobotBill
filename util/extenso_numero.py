from datetime import datetime

def numero_por_extenso(numero):

    if numero == 1:
        extnumero = 'Uma'
    if numero == 2:
        extnumero = 'Duas'
    if numero == 3:
        extnumero = 'três'
    if numero == 4:
        extnumero = 'quatro'
    if numero == 5:
        extnumero = 'cinco'
    if numero == 6:
        extnumero = 'seis'
    if numero == 7:
        extnumero = 'sete'
    if numero == 8:
        extnumero = 'oito'
    if numero == 9:
        extnumero = 'nove'
    if numero == 10:
        extnumero = 'dez'
    if numero == 11:
        extnumero = 'onze'
    if numero == 12:
        extnumero = 'doze'

    pnumero = extnumero
    return pnumero


def data_por_extenso(data):
    meses = [
        "janeiro", "fevereiro", "março", "abril",
        "maio", "junho", "julho", "agosto",
        "setembro", "outubro", "novembro", "dezembro"
    ]

    try:
        data_obj = datetime.strptime(data, "%Y-%m-%d")
        dia = data_obj.day
        mes = meses[data_obj.month - 1]
        ano = data_obj.year

        data_extenso = f"{dia} de {mes} de {ano}"
        return data_extenso
    except ValueError:
        return "Formato de data inválido. Use o formato AAAA-MM-DD."

# Exemplo de uso:
#data_input = "2023-09-03"
#data_extenso = data_por_extenso(data_input)
#print(data_extenso)
