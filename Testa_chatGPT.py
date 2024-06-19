import openai

def executa_chatGPT(prompt):
    # Inicialize o API key do OpenAI
    openai.api_key = "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"
    # Defina o modelo a ser usado (no caso, o GPT-3)
    model_engine = "text-davinci-002"
#git teste
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
