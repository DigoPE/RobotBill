import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import openai
#import pywhatkit

import requests
from bs4 import BeautifulSoup
import webbrowser

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

maquina.say('Olá! Teste de Voz! Tudo bem?')
maquina.runAndWait()