import time

import serial #Importa a biblioteca
from data.ConfiguracaoBD import ConexaoDB

class Farol():

    def ComandaFarol(ordem):
        comando_executado = False
        Count = 0

        #---Código Padrão para Consulta ao banco. ---------
        conexao = ConexaoDB()
        SQL = ('SELECT billdb.portas.Nome AS PortaNome '
               'FROM billdb.portas, billdb.placas '
               'WHERE billdb.portas.Id = billdb.placas.Porta_id '
               'AND billdb.placas.Nome = \'Uno_Luzes\'')
        rsPorta = conexao.executaQueryDB(SQL)
        porta = rsPorta[0][0] if rsPorta else None
        # ---Fim  ------------------------------------------

        while True: #Loop para a conexão com o Arduino
            try:  #Tenta se conectar, se conseguir, o loop se encerra
                arduino = serial.Serial(porta, 9600)
                break

            except:
                pass

        while True: #Loop principal

            try:
                if ordem == 'acender':
                    print(ordem)
                    arduino.write('1'.encode())
                    comando_executado = True
                elif ordem == 'apagar':
                    print(ordem)
                    arduino.write('2'.encode())
                    comando_executado = True
                arduino.flush() #Limpa a comunicação
                time.sleep(2)
                Count = Count + 1
                # Sai do loop se o comando foi executado
                if comando_executado and Count >= 2:
                    break

            except:
                pass
