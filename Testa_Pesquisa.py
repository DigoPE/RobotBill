import requests


def search_duckduckgo(query):
    base_url = "https://api.duckduckgo.com/?format=json&pretty=1"
    params = {"q": query}

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        #return response.text
        data = response.json()
        abstract = data.get("Abstract")
        return abstract
    else:
        return None

query = input("Digite sua consulta: ")
search_result = search_duckduckgo(query)
if search_result:
    print(search_result)
else:
    print("Não foi possível realizar a pesquisa.")
