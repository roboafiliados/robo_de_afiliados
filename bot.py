import os
import time
import requests
from flask import Flask

# ===============================
# CONFIGURAÇÕES
# ===============================
WHATSAPP_API_URL = "https://graph.facebook.com/v15.0/<PHONE_ID>/messages"
WHATSAPP_TOKEN = "<SEU_TOKEN_AQUI>"
INSTAGRAM_API_URL = "https://graph.facebook.com/<INSTAGRAM_BUSINESS_ID>/messages"
INSTAGRAM_TOKEN = "<SEU_TOKEN_AQUI>"
AFILIADO_API_URL = "https://api.exemplo.com/produtos"
CHECK_INTERVAL = 60  # segundos

app = Flask(__name__)

# ===============================
# FUNÇÕES DO BOT
# ===============================
def enviar_whatsapp(mensagem, numero):
    payload = {
        "messaging_product": "whatsapp",
        "to": numero,
        "type": "text",
        "text": {"body": mensagem}
    }
    headers = {"Authorization": f"Bearer {WHATSAPP_TOKEN}"}
    requests.post(WHATSAPP_API_URL, json=payload, headers=headers)
    print(f"✅ Mensagem enviada para {numero} via WhatsApp.")

def enviar_instagram(mensagem, user_id):
    payload = {"message": mensagem}
    headers = {"Authorization": f"Bearer {INSTAGRAM_TOKEN}"}
    requests.post(f"{INSTAGRAM_API_URL}/{user_id}/messages", json=payload, headers=headers)
    print(f"✅ Mensagem enviada para {user_id} via Instagram.")

def pegar_produtos():
    print("🔍 Verificando produtos de afiliado...")
    produtos = ["Produto A", "Produto B", "Produto C"]
    return produtos

def publicar_anuncio(produto):
    print(f"📢 Publicando anúncio do {produto}...")

def monitorar_pedidos():
    print("📦 Verificando pedidos ou leads...")

def executar_vendas():
    produtos = pegar_produtos()
    for produto in produtos:
        publicar_anuncio(produto)
    monitorar_pedidos()

# ===============================
# ROTA PRINCIPAL (para manter app ativo)
# ===============================
@app.route('/')
def home():
    return "🤖 Bot de Afiliados está ativo e rodando!"

# ===============================
# LOOP AUTOMÁTICO
# ===============================
def start_bot():
    print("🤖 Bot iniciado com sucesso!")
    while True:
        executar_vendas()
        enviar_whatsapp("Confira nossos produtos!", "<NUMERO_DO_CLIENTE>")
        enviar_instagram("Confira nossos produtos!", "<USER_ID_INSTAGRAM>")
        time.sleep(CHECK_INTERVAL)

# ===============================
# EXECUÇÃO
# ===============================
if __name__ == "__main__":
    import threading
    # Executa o bot em segundo plano
    bot_thread = threading.Thread(target=start_bot)
    bot_thread.daemon = True
    bot_thread.start()

    # Inicia o servidor Flask
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
