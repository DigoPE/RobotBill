import time

import serial #Importa a biblioteca


class Farol():

    def ComandaFarol(ordem):
        comando_executado = False
        Count = 0

        while True: #Loop para a conexão com o Arduino
            try:  #Tenta se conectar, se conseguir, o loop se encerra
                arduino = serial.Serial('COM3', 9600)
                print('Arduino dos Farois conectado')
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
