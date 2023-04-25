
from django.http import JsonResponse
import openai

def chat(request):
    prompt = request.GET.get('prompt')
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    ).choices[0].text
    return JsonResponse({'response': response})

def verResp(response):
    return response