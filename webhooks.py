from flask import request

def receber_webhook():
    dados = request.json
    print("Webhook recebido:", dados)
    return {"status": "ok"}
