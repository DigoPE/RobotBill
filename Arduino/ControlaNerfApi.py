
import time

import serial #Importa a biblioteca
from data.ConfiguracaoBD import ConexaoDB

class Nerf:

    def ComandaNerf(ordem):
        comando_executado = False
        Count = 0

        #---Código Padrão para Consulta ao banco. ---------
        conexao = ConexaoDB()
        SQL = ('SELECT billdb.portas.Nome AS PortaNome '
               'FROM billdb.portas, billdb.placas '
               'WHERE billdb.portas.Id = billdb.placas.Porta_id '
               'AND billdb.placas.Nome = \'Nano_Nerf\'')
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
                if ordem == 'cancelar':
                    arduino.write('c'.encode())
                    comando_executado = True
                elif ordem == 'atirar':
                    arduino.write('d'.encode())
                    comando_executado = True
                elif ordem == 'preparar':
                    arduino.write('p'.encode())
                    comando_executado = True
                elif ordem == 'liga_laser':
                    arduino.write('li'.encode())
                    comando_executado = True
                elif ordem == 'desliga_laser':
                    arduino.write('di'.encode())
                    comando_executado = True

                elif ordem == 'frente':
                    arduino.write('f'.encode())
                    comando_executado = True
                elif ordem == 'direita':
                    arduino.write('dir'.encode())
                    comando_executado = True
                elif ordem == 'esquerda':
                    arduino.write('esq'.encode())
                    comando_executado = True
                elif ordem == 'cima':
                    arduino.write('up'.encode())
                    comando_executado = True
                elif ordem == 'baixo':
                    arduino.write('down'.encode())
                    comando_executado = True

                arduino.flush()  # Limpa a comunicação
                time.sleep(2)
                Count = Count + 1
                # Sai do loop se o comando foi executado
                if comando_executado and Count >= 2:
                    break

            except:
                pass
