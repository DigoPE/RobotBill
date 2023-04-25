'''
 Blog Eletrogate - Como conectar o Arduino com Python
 Miguel Sena
 blog.eletrogate.com
'''

import serial #Importa a biblioteca

while True: #Loop para a conexão com o Arduino
    try:  #Tenta se conectar, se conseguir, o loop se encerra
        arduino = serial.Serial('COM3', 9600)
        print('Arduino conectado')
        break

    except:
        pass

while True: #Loop principal
    #O cmd é onde será armazenado o comando serial e posteriormente enviado para o Arduino.
    cmd = str(input('Digite "a" para ligar e "s" para desligar. ')) #Pergunta ao usuário se ele deseja ligar ou desligar o led

    if cmd == 'a': #Se a resposta for "l", ele envia este comando ao Arduino
        #arduino.write('a'.encode())
        arduino.write('a'.encode())

    elif cmd == 's': #Senão, envia o "d"
        arduino.write('s'.encode())

    elif cmd == 'c':
        print(cmd.lower())
        arduino.write('c'.encode())

    elif cmd == 'd': #Senão, envia o "w" para o olho olhar para cima.
        arduino.write('d'.encode())

    elif cmd == 'p': #Prepara Nerf.
        print(cmd.lower())
        arduino.write('p'.encode())

    arduino.flush() #Limpa a comunicação