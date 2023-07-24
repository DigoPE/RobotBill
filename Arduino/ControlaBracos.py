import time

import serial #Importa a biblioteca
from data.ConfiguracaoBD import ConexaoDB

class Braco():

    def ComandaBracos(ordem):
        comando_executado = False
        Count = 0

        # ---Código Padrão para Consulta ao banco. ---------
        conexao = ConexaoDB()
        SQL = ('SELECT Portas.Nome AS PortaNome '
               'FROM Portas, Placas '
               'WHERE Portas.Id = Placas.Porta_id '
               'AND Placas.Nome = \'Nano_Bracos\'')
        rsPorta = conexao.executaQueryDB(SQL)
        porta = rsPorta[0][0]

        # ---Fim  ------------------------------------------

        while True:  # Loop para a conexão com o Arduino
            try:  # Tenta se conectar, se conseguir, o loop se encerra
                arduino = serial.Serial(porta, 9600)
                print('Arduino dos Braços conectado')
                break

            except:
                pass

        while True:  # Loop principal

            try:
                # if ordem == 'tchau':
                #print(ordem)
                arduino.write('tchau'.encode())
                comando_executado = True
                # elif ordem == 'aleatorio':
                # print(ordem)
                # arduino.write('2'.encode())
                # comando_executado = True
                arduino.flush()  # Limpa a comunicação
                time.sleep(2)
                Count = Count + 1
                # Sai do loop se o comando foi executado
                if comando_executado and Count >= 2:
                    break

            except:
                pass

