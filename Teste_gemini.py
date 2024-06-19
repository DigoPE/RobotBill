import pathlib
import textwrap
import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown

# Use a library like keyring to securely store your API key
import keyring

def to_markdown(text):
  text = text.replace('•', ' *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

# Get the API key from a secure storage (replace 'your_app_name' with your app name)
API_KEY = 'AIzaSyBcbXdjMHQ4-h9RJ-AqkGQ37Zzpy5j9EQo'
#API_KEY = 'AIzaSyCLWDrqNe8uUlTT20-7OyeqDt2qC3OtgcI'

genai.configure(api_key=API_KEY)

#for m in genai.list_models():
#  if 'generateContent' in m.supported_generation_methods:
#    print(m.name)

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

bem_vindo = "# Bem vindo a minha conversa. #"
print(len(bem_vindo) * "#")
print(bem_vindo)
print(len(bem_vindo) * "#")
print("###   Digite 'sair' para encerrar a conversa.   ###")
print("Fui!")

while True:
  texto = input("Escreva sua mensagem: ")

  if texto == "sair":
    break

  response = chat.send_message(texto)
  print("Gemini: ", response.text, "\n")

print("Encerrando Chat")

