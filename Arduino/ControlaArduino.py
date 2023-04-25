'''
 Blog Eletrogate - Como conectar o Arduino com Python
 Miguel Sena
 blog.eletrogate.com
'''
import time

import serial #Importa a biblioteca



class Arduino():

    def SistemasArduino(comandos):
        ordem = comandos.replace(' ', '')
        ordem = ordem.lower()

        if ordem == 'cancela' or ordem == 'cancelar' or ordem == 'disparar' or ordem == 'dispara' \
            or ordem == 'atirar' or ordem == 'atira' or ordem == 'preparar' or ordem == 'prepara':
                Arduino.ComandaNerf(ordem)




    def ComandaNerf(ordem):
        comando_executado = False
        Count = 0

        while True: #Loop para a conexão com o Arduino
            try:  #Tenta se conectar, se conseguir, o loop se encerra
                arduino = serial.Serial('COM3', 9600)
                print('Arduino conectado')
                break

            except:
                pass

        while True: #Loop principal
            #O cmd é onde será armazenado o comando serial e posteriormente enviado para o Arduino.
            #cmd = str(input('Digite "a" para ligar e "s" para desligar. ')) #Recebe a Ordem vinda do Bill.
            #ordem = comanda.replace(' ', '')

            try:
                if ordem == 'cancela':
                    print(ordem)
                    arduino.write('c'.encode())
                    comando_executado = True
                elif ordem == 'cancelar':
                    print(ordem)
                    arduino.write('c'.encode())
                    comando_executado = True
                elif ordem == 'disparar':
                    comando_executado = True
                    arduino.write('d'.encode())
                elif ordem == 'dispara':
                    arduino.write('d'.encode())
                    comando_executado = True
                elif ordem == 'atirar':
                    arduino.write('d'.encode())
                    comando_executado = True
                elif ordem == 'atira':
                    arduino.write('d'.encode())
                    comando_executado = True
                elif ordem == 'preparar':
                    print(ordem)
                    arduino.write('p'.encode())
                    comando_executado = True
                elif ordem == 'prepara':
                    print(ordem)
                    arduino.write('p'.encode())
                    comando_executado = True
                arduino.flush() #Limpa a comunicação
                time.sleep(2)
                Count = Count + 1
                # Sai do loop se o comando foi executado
                if comando_executado and Count >= 2:
                    break

            except:
                pass
