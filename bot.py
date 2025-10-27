import os
import time
import requests
from flask import Flask, request
import threading

# ===============================
# CONFIGURAÇÕES
# ===============================
WHATSAPP_API_URL = "https://graph.facebook.com/v15.0/<PHONE_ID>/messages"
WHATSAPP_TOKEN = "<SEU_TOKEN_WHATSAPP>"
INSTAGRAM_API_URL = "https://graph.facebook.com/<INSTAGRAM_BUSINESS_ID>/messages"
INSTAGRAM_TOKEN = "<SEU_TOKEN_INSTAGRAM>"
AFILIADO_API_URL = "https://api.exemplo.com/produtos"  # API do fornecedor ou afiliado
CHECK_INTERVAL = 60  # segundos entre cada execução do loop
VERIFY_TOKEN = "Mrocha@123"  # Token de validação do Meta

# Números e IDs para envio automático (preencher com os reais)
NUMEROS_WHATSAPP = ["+5511999999999"]  # lista de clientes
USER_IDS_INSTAGRAM = ["1234567890"]     # lista de IDs de Instagram

# ===============================
# INICIALIZAÇÃO DO FLASK
# ===============================
app = Flask(__name__)

# ===============================
# FUNÇÕES DE ENVIO DE MENSAGENS
# ===============================
def enviar_whatsapp(mensagem, numero):
    payload = {
        "messaging_product": "whatsapp",
        "to": numero,
        "type": "text",
        "text": {"body": mensagem}
    }
    headers = {"Authorization": f"Bearer {WHATSAPP_TOKEN}"}
    response = requests.post(WHATSAPP_API_URL, json=payload, headers=headers)
    if response.status_code == 200:
        print(f"✅ WhatsApp enviado para {numero}")
    else:
        print(f"❌ Erro ao enviar WhatsApp para {numero}: {response.text}")

def enviar_instagram(mensagem, user_id):
    payload = {"message": mensagem}
    headers = {"Authorization": f"Bearer {INSTAGRAM_TOKEN}"}
    response = requests.post(f"{INSTAGRAM_API_URL}/{user_id}/messages", json=payload, headers=headers)
    if response.status_code == 200:
        print(f"✅ Instagram enviado para {user_id}")
    else:
        print(f"❌ Erro ao enviar Instagram para {user_id}: {response.text}")

# ===============================
# FUNÇÕES DE AFILIADO E ANÚNCIO
# ===============================
def pegar_produtos():
    # Aqui você pode fazer requisição para API de afiliado ou retornar uma lista fixa
    print("🔍 Verificando produtos de afiliado...")
    produtos = ["Produto A", "Produto B", "Produto C"]
    return produtos

def publicar_anuncio(produto):
    # Aqui você colocaria a lógica real de publicar anúncio
    print(f"📢 Publicando anúncio do {produto}...")

def monitorar_pedidos():
    # Aqui você pode consultar pedidos ou leads
    print("📦 Verificando pedidos ou leads...")

def executar_vendas():
    produtos = pegar_produtos()
    for produto in produtos:
        publicar_anuncio(produto)
    monitorar_pedidos()

# ===============================
# ROTAS DO FLASK
# ===============================
@app.route('/')
def home():
    return "🤖 Bot de Afiliados ativo e rodando!"

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        token_enviado = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")
        if token_enviado == VERIFY_TOKEN:
            return challenge, 200
        else:
            return "Erro: token inválido", 403
    elif request.method == 'POST':
        data = request.get_json()
        print("📩 Mensagem recebida:", data)
        return "Evento recebido", 200

# ===============================
# LOOP AUTOMÁTICO DO BOT
# ===============================
def start_bot():
    print("🤖 Bot iniciado com sucesso!")
    while True:
        executar_vendas()
        for numero in NUMEROS_WHATSAPP:
            enviar_whatsapp("Confira nossos produtos e ofertas!", numero)
        for user_id in USER_IDS_INSTAGRAM:
            enviar_instagram("Confira nossos produtos e ofertas!", user_id)
        time.sleep(CHECK_INTERVAL)

# ===============================
# EXECUÇÃO PRINCIPAL
# ===============================
if __name__ == "__main__":
    # Executa o bot em segundo plano
    bot_thread = threading.Thread(target=start_bot)
    bot_thread.daemon = True
    bot_thread.start()

    # Inicia o servidor Flask
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
