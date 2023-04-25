import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import openai

import random
import socket

from Arduino.ControlaArduino import Arduino

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


def verificar_conexao_internet():
    try:
        # Tenta estabelecer uma conexão com um servidor remoto
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        pass
    return False

def abrir_YouTube(descricao):

    if verificar_conexao_internet():
        import pywhatkit
        pywhatkit.playonyt(descricao)
    try:
        return 'Tocando música: ' + descricao
    except Exception as e:
        return 'Erro ao tentar Tocar Música. Verifique sua Conexão.'

def executa_chatGPT(prompt):
    # Inicialize o API key do OpenAI
    #openai.api_key =
    # Defina o modelo a ser usado (no caso, o GPT-3)
    model_engine = "text-davinci-002"

    # Obtenha uma resposta do modelo
    params = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    answer = params.choices[0].text
    return answer

def  analisa_respostaGPT(resp):

    if len(resp) > 2500:
        maquina.say('Minha resposta é um pouco extensa, deseja escuta-la?')
        maquina.runAndWait()

        comando = executa_comando()
        if 'sim' in comando:
            return True
        else:
            return False

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
            9: "Zzzzz... há! Desculpe! Me distrai! "
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


def comando_voz_usuario():
    # Inicializa o contexto da conversa
    context = ""
    comando = executa_comando()

    if 'horas' in comando:
        hora = datetime.datetime.now().strftime('%H:%M')
        maquina.say('Agora são' + hora)
        maquina.runAndWait()
    elif 'procure por' in comando:
        procurar = comando.replace('procure por', '')
        wikipedia.set_lang('pt')
        resultado = wikipedia.summary(procurar,2)
        print(resultado)
        maquina.say(resultado)
        maquina.runAndWait()
    elif 'toque' in comando:
        # Só funciona on-line. Corrigir o erro quando o PC estiver off-line.
        musica = comando.replace('toque','')
        msn = abrir_YouTube(musica)
        #maquina.say('Tocando música: ' + musica)
        maquina.say(msn)
        maquina.runAndWait()

    elif 'quem é você' in comando:
        maquina.say('Eu sou a Bill.')
        maquina.runAndWait()
    elif 'quem és tu' in comando:
        maquina.say('Eu sou a Bill.')
        maquina.runAndWait()
    elif 'como se chamas' in comando:
        maquina.say('Eu me chamo Bill.')
        maquina.runAndWait()
    elif 'como se chama-se' in comando:
        maquina.say('Eu me chamo Bill.')
        maquina.runAndWait()
    elif 'qual o seu nome' in comando:
        maquina.say('Eu sou a Bill.')
        maquina.runAndWait()
    elif 'qual o teu nome' in comando:
        maquina.say('Eu sou a Bill.')
        maquina.runAndWait()
    elif 'error' in comando:
        maquina.say('Pode repetir, por favor?')
        maquina.runAndWait()

    elif 'bill' in comando:
        # Só funciona on-line. Corrigir o erro quando o PC estiver off-line.
        ordem = comando.replace('bill','')
        maquina.say(ordem)
        maquina.runAndWait()
        Arduino.ComandaNerf(ordem)

    elif 'bio' in comando:
        # Só funciona on-line. Corrigir o erro quando o PC estiver off-line.
        ordem = comando.replace('bio','')
        maquina.say(ordem)
        maquina.runAndWait()
        Arduino.ComandaNerf(ordem)

    elif 'viu' in comando:
        # Só funciona on-line. Corrigir o erro quando o PC estiver off-line.
        ordem = comando.replace('viu','')
        maquina.say(ordem)
        maquina.runAndWait()
        Arduino.ComandaNerf(ordem)

    elif 'vi o' in comando:
        # Só funciona on-line. Corrigir o erro quando o PC estiver off-line.
        ordem = comando.replace('vi o','')
        maquina.say(ordem)
        maquina.runAndWait()
        Arduino.ComandaNerf(ordem)

    else:
        # Gera a resposta utilizando o contexto atual
        resposta = executa_chatGPT(comando)

        if analisa_respostaGPT(resposta):
            print(resposta)
            maquina.say(resposta)
            maquina.runAndWait()


while True:
    comando_voz_usuario()

#maquina.say("Olá, eu sou um modelo de linguagem treinado pelo OpenAI.")

#maquina.runAndWait()