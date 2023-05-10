import time

import serial #Importa a biblioteca

from util.Ordem_Comando import executa_comando


class Arduino():

    #Função que chama outras funções para controlar outras placas de Arduino ou ESP32.
    def SistemasArduino(comandos):
        ordem = comandos.replace(' ', '')
        ordem = ordem.lower()

        if ordem == 'cancela' or ordem == 'cancelar' or ordem == 'disparar' or ordem == 'dispara' \
            or ordem == 'atirar' or ordem == 'atira' or ordem == 'preparar' or ordem == 'prepara':
                Arduino.ComandaNerf(ordem)

        if ordem == 'frente' or ordem == 'friend' or ordem == 'fred' or ordem == 'para frente' or ordem == 'para a frente' or ordem == 'esquerda' \
            or ordem == 'frank' or ordem == 'direita' or ordem == 'para' or ordem == 'parar' or ordem == 'stop' or ordem == 'tras' or ordem == 'trás' \
                or ordem == 'para tras' or ordem == 'auto' or ordem == 'alto' or ordem == 'automático' or ordem == 'explorar':
                    Arduino.ComandaRodas(ordem)

        if ordem == 'aceder' or ordem == 'acende' or ordem == 'acender' or ordem == 'apaga' or ordem == 'apagar':
                    Arduino.ComandaFarol(ordem)

    def ComandaRodas(ordem):
        executa_ordem = ordem
        comando_executado = False
        Count = 0

        while True: #Loop para a conexão com o Arduino
            try:  #Tenta se conectar, se conseguir, o loop se encerra
                arduino = serial.Serial('COM6', 9600)
                print('Arduino das Rodas conectado')
                break

            except:
                pass

        while True: #Loop principal

            limpa_comunicacao = True

            try:
                if executa_ordem == 'frente':
                    print(executa_ordem)
                    arduino.write('1'.encode())
                    comando_executado = True
                elif executa_ordem == 'friend':
                    print(executa_ordem)
                    arduino.write('1'.encode())
                    executa_ordem = True
                elif executa_ordem == 'para frente':
                    print(executa_ordem)
                    arduino.write('1'.encode())
                    comando_executado = True
                elif executa_ordem == 'para a frente':
                    print(executa_ordem)
                    arduino.write('1'.encode())
                    comando_executado = True
                elif executa_ordem == 'fred':
                    print(executa_ordem)
                    arduino.write('1'.encode())
                    comando_executado = True
                elif executa_ordem == 'frank':
                    print(executa_ordem)
                    arduino.write('1'.encode())
                    comando_executado = True
                elif executa_ordem == 'tras':
                    print(executa_ordem)
                    arduino.write('2'.encode())
                    comando_executado = True
                elif executa_ordem == 'para tras':
                    print(executa_ordem)
                    arduino.write('2'.encode())
                    comando_executado = True
                elif executa_ordem == 'trás':
                    print(executa_ordem)
                    arduino.write('2'.encode())
                    comando_executado = True
                elif executa_ordem == 'esquerda':
                    print(executa_ordem)
                    arduino.write('3'.encode())
                    comando_executado = True
                elif executa_ordem == 'direita':
                    print(executa_ordem)
                    arduino.write('4'.encode())
                    comando_executado = True

                elif executa_ordem == 'explorar':
                    print(executa_ordem)
                    arduino.write('6'.encode())
                    comando_executado = True
                    limpa_comunicacao = False
                elif executa_ordem == 'auto':
                    print(executa_ordem)
                    arduino.write('6'.encode())
                    comando_executado = True
                    limpa_comunicacao = False
                elif executa_ordem == 'alto':
                    print(executa_ordem)
                    arduino.write('6'.encode())
                    comando_executado = True
                    limpa_comunicacao = False
                elif executa_ordem == 'automático':
                    print(executa_ordem)
                    arduino.write('6'.encode())
                    comando_executado = True
                    limpa_comunicacao = False

                elif executa_ordem == 'parar':
                    print(executa_ordem)
                    comando_executado = False
                elif executa_ordem == 'para':
                    print(executa_ordem)
                    comando_executado = False
                elif executa_ordem == 'stop':
                    print(executa_ordem)
                    comando_executado = False
                #arduino.flush() #Limpa a comunicação
                #time.sleep(2)

                comando = executa_comando('arduino')
                if 'parar' in comando:
                    executa_ordem = comando
                    comando_executado = False
                elif 'para' in comando:
                    executa_ordem = comando
                    comando_executado = False
                elif 'stop' in comando:
                    executa_ordem = comando
                    comando_executado = False

                if limpa_comunicacao:
                    arduino.flush() #Limpa a comunicação
                time.sleep(0.5)


                # Sai do loop se o comando foi executado
                if not comando_executado:
                    break

            except:
                pass


    def ComandaNerf(ordem):
        comando_executado = False
        Count = 0

        while True: #Loop para a conexão com o Arduino
            try:  #Tenta se conectar, se conseguir, o loop se encerra
                arduino = serial.Serial('COM7', 9600)
                print('Arduino do Nerf conectado')
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