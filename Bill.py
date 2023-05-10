

import datetime
import wikipedia
import openai


import socket

from Arduino.ControlaArduino import Arduino

from util.Ordem_Comando import executa_comando, maquina

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
    openai.api_key = "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"
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
        resposta = executa_chatGPT(comando)

        if analisa_respostaGPT(resposta):
            print(resposta)
            maquina.say(resposta)
            maquina.runAndWait()


while True:
    comando_voz_usuario()

#maquina.say("Olá, eu sou um modelo de linguagem treinado pelo OpenAI.")

#maquina.runAndWait()