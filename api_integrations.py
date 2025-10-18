import requests

def enviar_mensagem(api_url, dados):
    resposta = requests.post(api_url, json=dados)
    return resposta.json()
