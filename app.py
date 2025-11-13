import requests
from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# 🔹 WhatsApp
VERIFY_TOKEN = os.getenv("VERIFY_TOKEN", "MrochaTeste2025")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN", "")  # vem das variáveis de ambiente (Render/.env)
PHONE_ID = os.getenv("PHONE_ID", "24795012596794443")

# 🔹 Instagram (mantive como estava)
INSTAGRAM_VERIFY_TOKEN = os.getenv("INSTAGRAM_VERIFY_TOKEN", "MEUVERIFICAINSTA")
INSTAGRAM_ACCESS_TOKEN = os.getenv("INSTAGRAM_ACCESS_TOKEN", "IGQV...")
INSTAGRAM_PAGE_ID = os.getenv("INSTAGRAM_PAGE_ID", "1234567890")


# Função para enviar mensagem via API do WhatsApp
def send_whatsapp_text(to_number: str, text: str):
    if not ACCESS_TOKEN:
        raise RuntimeError("ACCESS_TOKEN não configurado nas variáveis de ambiente.")
    url = f"https://graph.facebook.com/v22.0/{PHONE_ID}/messages"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "messaging_product": "whatsapp",
        "to": to_number,
        "type": "text",
        "text": {"body": text}
    }
    resp = requests.post(url, headers=headers, json=payload, timeout=10)
    resp.raise_for_status()
    return resp.json()


# 📱 WHATSAPP WEBHOOK - verify
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


# webhook receiver
@app.route("/webhook", methods=["POST"])
def webhook_whatsapp():
    data = request.get_json()
    print("📩 WhatsApp recebido:", data)
    # Aqui você pode processar e responder; por enquanto só devolve 200
    return "EVENT_RECEIVED", 200


# endpoint para testar envio manual (chame via navegador /curl)
@app.route("/send_test", methods=["POST"])
def send_test():
    body = request.get_json() or {}
    to = body.get("to")
    text = body.get("text", "Mensagem de teste do bot")
    if not to:
        return jsonify({"error": "campo 'to' ausente (use formato 55DDDNÚMERO)"}), 400
    try:
        result = send_whatsapp_text(to, text)
        return jsonify(result), 200
    except Exception as e:
        print("Erro ao enviar mensagem:", str(e))
        return jsonify({"error": str(e)}), 500


# 📸 INSTAGRAM WEBHOOK (mantive)
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
