

import datetime
import wikipedia
import requests

import socket

from Arduino.ControlaArduino import Arduino

from util.Ordem_Comando import executa_comando, maquina
from util.extenso_numero import numero_por_extenso, data_por_extenso


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

def executa_Pesquisa(query):

    wikipedia.set_lang('pt')
    try:
        resultado = wikipedia.summary(query, 2)
        return resultado
    except wikipedia.exceptions.DisambiguationError as e:
        msnError = f'Erro na pesquisa. Houve uma ambiguidade na sua pergunta. Tente ser mais específico.'
        return msnError
    except wikipedia.exceptions.HTTPTimeoutError as e:
        msnError = 'Erro na pesquisa. A busca demorou muito para responder. Tente novamente mais tarde.'
        return msnError
    except wikipedia.exceptions.PageError as e:
        msnError = 'Erro na pesquisa. A página solicitada não foi encontrada.'
        return msnError
    except Exception as e:
        msnError = 'Erro desconhecido na pesquisa. Favor refaça a pergunta.'
        return msnError

def  analisa_Pesquisa(resp):

    if len(resp) > 2500:
        maquina.say('Minha resposta é um pouco extensa, deseja escuta-la?')
        maquina.runAndWait()

        comando = executa_comando()
        if 'sim' in comando:
            return True
        else:
            return False

def comando_voz_usuario():
    # Inicializa o contexto da conversa
    context = ""
    comando = executa_comando()

    if 'horas' in comando:
        agora = datetime.datetime.now()
        hora = numero_por_extenso(agora.hour)
        minutos = agora.minute
        segundos = agora.second

        hora_por_extenso = f"{hora} horas, {minutos} minutos e {segundos} segundos."
        print(hora_por_extenso)
        maquina.say('Agora são' + hora_por_extenso)
        maquina.runAndWait()
    elif 'dia' in comando:
        data_atual = datetime.datetime.now().strftime('%Y-%m-%d')
        data_extenso = data_por_extenso(data_atual)
        print('Hoje é o dia ' + data_extenso)
        maquina.say('Hoje é o dia ' + data_extenso)
        maquina.runAndWait()
    elif 'data de hoje' in comando:
        agora = datetime.datetime.now()
        hora = numero_por_extenso(agora.hour)
        minutos = agora.minute
        segundos = agora.second

        hora_por_extenso = f"{hora} horas, {minutos} minutos e {segundos} segundos."

        data_atual = datetime.datetime.now().strftime('%Y-%m-%d')
        data_extenso = data_por_extenso(data_atual)

        print('Agora são ' + hora_por_extenso +' Do dia ' +  data_extenso)
        maquina.say('Agora são ' + hora_por_extenso +' Do dia ' +  data_extenso)
        maquina.runAndWait()

    elif 'procure por' in comando:
        procurar = comando.replace('procure por', '')
        wikipedia.set_lang('pt')
        resultado = wikipedia.summary(procurar,2)
        print(resultado)
        maquina.say(resultado)
        maquina.runAndWait()
    elif 'pesquise por' in comando:
        procurar = comando.replace('pesquise por', '')
        wikipedia.set_lang('pt')
        resultado = wikipedia.summary(procurar,2)
        print(resultado)
        maquina.say(resultado)
        maquina.runAndWait()
    elif 'fale sobre' in comando:
        procurar = comando.replace('fale sobre', '')
        wikipedia.set_lang('pt')
        resultado = wikipedia.summary(procurar,2)
        print(resultado)
        maquina.say(resultado)
        maquina.runAndWait()
    elif 'me fale sobre' in comando:
        procurar = comando.replace('me fale sobre', '')
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

    elif 'bill' in comando.lower():
        # Só funciona on-line. Corrigir o erro quando o PC estiver off-line.
        ordem = comando.replace('bill','')
        maquina.say(ordem)
        maquina.runAndWait()
        #Arduino.ComandaNerf(ordem)
        Arduino.SistemasArduino(ordem)

    elif 'bil' in comando.lower():
        # Só funciona on-line. Corrigir o erro quando o PC estiver off-line.
        ordem = comando.replace('bil','')
        maquina.say(ordem)
        maquina.runAndWait()
        #Arduino.ComandaNerf(ordem)
        Arduino.SistemasArduino(ordem)

    elif 'bio' in comando.lower():
        # Só funciona on-line. Corrigir o erro quando o PC estiver off-line.
        ordem = comando.replace('bio','')
        maquina.say(ordem)
        maquina.runAndWait()
        Arduino.SistemasArduino(ordem)

    elif 'viu' in comando.lower():
        # Só funciona on-line. Corrigir o erro quando o PC estiver off-line.
        ordem = comando.replace('viu','')
        maquina.say(ordem)
        maquina.runAndWait()
        Arduino.SistemasArduino(ordem)

    elif 'eu' in comando.lower():
        # Só funciona on-line. Corrigir o erro quando o PC estiver off-line.
        ordem = comando.replace('eu','')
        maquina.say(ordem)
        maquina.runAndWait()
        Arduino.SistemasArduino(ordem)

    elif 'vi o' in comando.lower():
        # Só funciona on-line. Corrigir o erro quando o PC estiver off-line.
        ordem = comando.replace('vi o','')
        maquina.say(ordem)
        maquina.runAndWait()
        Arduino.SistemasArduino(ordem)

    elif 'dio' in comando.lower():
        # Só funciona on-line. Corrigir o erro quando o PC estiver off-line.
        ordem = comando.replace('dio','')
        maquina.say(ordem)
        maquina.runAndWait()
        Arduino.SistemasArduino(ordem)

    elif 'tio' in comando.lower():
        # Só funciona on-line. Corrigir o erro quando o PC estiver off-line.
        ordem = comando.replace('tio','')
        maquina.say(ordem)
        maquina.runAndWait()
        Arduino.SistemasArduino(ordem)

    elif 'deu' in comando.lower():
        # Só funciona on-line. Corrigir o erro quando o PC estiver off-line.
        ordem = comando.replace('deu','')
        maquina.say(ordem)
        maquina.runAndWait()
        Arduino.SistemasArduino(ordem)

    elif 'meu' in comando.lower():
        # Só funciona on-line. Corrigir o erro quando o PC estiver off-line.
        ordem = comando.replace('meu','')
        maquina.say(ordem)
        maquina.runAndWait()
        Arduino.SistemasArduino(ordem)

    elif 'mio' in comando.lower():
        # Só funciona on-line. Corrigir o erro quando o PC estiver off-line.
        ordem = comando.replace('mio','')
        maquina.say(ordem)
        maquina.runAndWait()
        Arduino.SistemasArduino(ordem)

    elif 'digo' in comando.lower():
        # Só funciona on-line. Corrigir o erro quando o PC estiver off-line.
        ordem = comando.replace('digo','')
        maquina.say(ordem)
        maquina.runAndWait()
        Arduino.SistemasArduino(ordem)

    else:
        # Gera a resposta utilizando o contexto atual
        resposta = executa_Pesquisa(comando)

        print(resposta)
        maquina.say(resposta)
        maquina.runAndWait()



while True:
    comando_voz_usuario()

#maquina.say("Olá, eu sou um modelo de linguagem treinado pelo OpenAI.")

#maquina.runAndWait()