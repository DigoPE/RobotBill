import time

import serial #Importa a biblioteca


class Rodas:
    def ComandaRodas(ordem):

        comando_executado = False
        Count = 0

        while True:  # Loop para a conexão com o Arduino
            try:  # Tenta se conectar, se conseguir, o loop se encerra
                arduino = serial.Serial('COM6', 9600)
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
