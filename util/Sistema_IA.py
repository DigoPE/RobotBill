import pathlib
import textwrap
import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown

# Use a library like keyring to securely store your API key
import keyring

def executa_IA(comando):
  """Executes the AI model and returns the generated response."""
  comando = comando.replace('•', ' *')  # Replace bullet point symbol
  response = chat.send_message(comando)  # Send message through the chat object
  return response.text  # Return the generated text response

# Get the API key from a secure storage (replace 'your_app_name' with your app name)
API_KEY = 'AIzaSyBcbXdjMHQ4-h9RJ-AqkGQ37Zzpy5j9EQo'

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

