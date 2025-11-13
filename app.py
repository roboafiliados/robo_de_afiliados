import requests
from flask import Flask, request
import os

app = Flask(__name__)

# 🔹 WhatsApp
VERIFY_TOKEN = os.getenv("VERIFY_TOKEN", "MrochaTeste2025")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN", EAAVsBP3iZCbEBPyN4vTsVe1Y7DgqLlUOX3M3ttI2vIUC24eVVTZCRZALcvz0uhdPnxQ87mZBePTHaGEkakuiKvMxEGBr598QeDumWuk3DE3WNyCutxUvSboyZAMqCcZCpZA5F9wsV9JC7ZBK8ZCrLCkLEm7iHbKY5A6QAzSYXtZCZBozaWvEZCW1fn7oTsKVcX6K6u0bdj3C3BuUwyJqBgDu5ELgQGfvAAtmaZALLD3kC66aTC7olwigY9fl8kFPuC9NJHAZDZD

PHONE_ID = os.getenv("PHONE_ID", "24795012596794443")

# 🔹 Instagram
INSTAGRAM_VERIFY_TOKEN = os.getenv("INSTAGRAM_VERIFY_TOKEN", "MEUVERIFICAINSTA")
INSTAGRAM_ACCESS_TOKEN = os.getenv("INSTAGRAM_ACCESS_TOKEN", "IGQV...")
INSTAGRAM_PAGE_ID = os.getenv("INSTAGRAM_PAGE_ID", "1234567890")

# 📱 WHATSAPP WEBHOOK
@app.route("/webhook", methods=["GET"])
def verify_whatsapp():
    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        print("✅ WhatsApp Webhook verificado com sucesso!")
        return challenge, 200
    else:
        print("❌ Erro na verificação WhatsApp!")
        return "Erro de verificação WhatsApp", 403


@app.route("/webhook", methods=["POST"])
def webhook_whatsapp():
    data = request.get_json()
    print("📩 WhatsApp recebido:", data)
    return "EVENT_RECEIVED", 200


# 📸 INSTAGRAM WEBHOOK
@app.route("/webhook_instagram", methods=["GET"])
def verify_instagram():
    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    if mode == "subscribe" and token == INSTAGRAM_VERIFY_TOKEN:
        print("✅ Instagram Webhook verificado com sucesso!")
        return challenge, 200
    else:
        print("❌ Erro na verificação Instagram!")
        return "Erro de verificação Instagram", 403


@app.route("/webhook_instagram", methods=["POST"])
def webhook_instagram():
    data = request.get_json()
    print("📩 Instagram recebido:", data)
    return "EVENT_RECEIVED", 200


@app.route("/")
def home():
    return "🤖 Bot WhatsApp + Instagram ativo no Render!"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
