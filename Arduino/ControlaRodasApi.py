import time

import serial #Importa a biblioteca
from data.ConfiguracaoBD import ConexaoDB

class Rodas:
    def ComandaRodas(ordem):

        comando_executado = False
        Count = 0

        #---Código Padrão para Consulta ao banco. ---------
        conexao = ConexaoDB()
        SQL = ('SELECT billdb.portas.Nome AS PortaNome '
               'FROM billdb.portas, billdb.placas '
               'WHERE billdb.portas.Id = billdb.placas.Porta_id '
               'AND billdb.placas.Nome = \'ESP32_Rodas\'')
        rsPorta = conexao.executaQueryDB(SQL)
        porta = rsPorta[0][0] if rsPorta else None
        # ---Fim  ------------------------------------------

        while True:  # Loop para a conexão com o Arduino
            try:  # Tenta se conectar, se conseguir, o loop se encerra
                arduino = serial.Serial(porta, 9600)
                break

            except:
                pass

        while True:  # Loop principal

            try:
                if ordem == 'frente':
                    arduino.write('1'.encode())
                    comando_executado = True
                elif ordem == 'tras':
                    arduino.write('2'.encode())
                    comando_executado = True
                elif ordem == 'esquerda':
                    arduino.write('3'.encode())
                    comando_executado = True
                elif ordem == 'direita':
                    arduino.write('4'.encode())
                    comando_executado = True
                elif ordem == 'explorar':
                    arduino.write('6'.encode())
                    comando_executado = False
                elif ordem == 'stop':
                    arduino.write('5'.encode())
                    comando_executado = True

                arduino.flush() #Limpa a comunicação

                if comando_executado:
                    time.sleep(2)
                    break
                else:
                    time.sleep(60)
                    break

            except:
                pass
