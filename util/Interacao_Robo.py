
import subprocess
import serial
from data.ConfiguracaoBD import ConexaoDB

#class Interacao():

def get_interageBill(questao):

    #---Código Padrão para Consulta ao banco. ---------
    conexao = ConexaoDB()
    SQL = "SELECT Nome FROM Portas"
    portas = conexao.executaQueryDB(SQL)
    # ---Fim  ------------------------------------------

    resultado_portas = []
    for porta in portas:
        try:
            ser = serial.Serial(porta[0], 9600)
            ser.close()
            resultado_portas.append((porta[0], True))
        except serial.SerialException:
            resultado_portas.append((porta[0], False))

    return resultado_portas

interage = 'Estrelas'
print(get_interageBill(interage))
