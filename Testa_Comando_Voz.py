import speech_recognition as sr

def executa_comando():

    audio = sr.Recognizer()
    with sr.Microphone() as source:
        print('Ouvindo..')
        voz = audio.listen(source)

    try:
        comando = audio.recognize_google(voz, language='pt-BR')
        comando = comando.lower()

        #return 'Comando: ' + comando

    except sr.UnknownValueError:
        print('Não entendi!')
        return 'error'

    except sr.RequestError as e:
        print('Erro ao requisitar resultados; {0}'.format(e))
        return 'error'
    except:
        print('Microfone não está Funcionando.')
        return 'error'

    return 'Comando: ' + comando

print(executa_comando())
