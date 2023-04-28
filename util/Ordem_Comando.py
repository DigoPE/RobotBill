
import speech_recognition as sr
import pyttsx3
import random

maquina = pyttsx3.init()

# Configurando a velocidade da fala:
rate = maquina.getProperty('rate')
maquina.setProperty('rate', rate-50)
################################################

# Configurando o volume da fala: O volume padrão é 1, nesse caso estamos aumentando em 50%
volume = maquina.getProperty('volume')
maquina.setProperty('volume', volume+0.50)
################################################

#Mudando a Voz.
voices = maquina.getProperty('voices')
maquina.setProperty('voice', voices[1].id)
maquina.setProperty('useCachedVoice', True)
################################################

def executa_comando():

    audio = sr.Recognizer()
    with sr.Microphone() as source:
        print('Ouvindo..')
        voz = audio.listen(source)

    try:
        comando = audio.recognize_google(voz, language='pt-BR')
        comando = comando.lower()
        if 'bill' in comando:
            comando = comando.replace('bill', '')
            maquina.say(comando)
            maquina.runAndWait()

    except sr.UnknownValueError:

        #Varia a resposta de Não entendimento variando randomicamente.
        num = random.randint(0, 9)

        switcher = {
            0: "Não entendi!",
            1: "Diga?!!! Não percebi! ",
            2: "Oi? Como disse?",
            3: "Olá? Tem alguém falando comigo?",
            4: "Como é?!!!",
            5: "Desculpe, mas eu não estou entendendo nada!!!",
            6: "Tem muito ruido! Acho que tem muita gente falando ao mesmo tempo.",
            7: "Acho que tem uma música ou muitas pessoas conversando ao fundo!",
            8: "Oi?!! Tem alguém ai?!!",
            9: "Zzzzz... há! Desculpe! Me distraí! "
        }
        resposta = switcher.get(num, "Número inválido")

        print(resposta)
        maquina.say(resposta)
        maquina.runAndWait()

        return 'error'

    except sr.RequestError as e:
        print('Erro ao requisitar resultados; {0}'.format(e))
        maquina.say('Erro ao requisitar resultados; Provavelmente a conexão está Off-line.')
        maquina.runAndWait()
        return 'error'
    except:
        print('Microfone não está Funcionando.')
        maquina.say('Microfone não está Funcionando.')
        maquina.runAndWait()
        return 'error'

    return comando
