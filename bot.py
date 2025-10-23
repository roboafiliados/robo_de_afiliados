import time
import requests

# ===============================
# CONFIGURAÇÕES
# ===============================
WHATSAPP_API_URL = "https://graph.facebook.com/v15.0/<PHONE_ID>/messages"
WHATSAPP_TOKEN = "<SEU_TOKEN_AQUI>"
INSTAGRAM_API_URL = "https://graph.facebook.com/<INSTAGRAM_BUSINESS_ID>/messages"
INSTAGRAM_TOKEN = "<SEU_TOKEN_AQUI>"
AFILIADO_API_URL = "https://api.exemplo.com/produtos"
CHECK_INTERVAL = 60  # segundos

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
    # Aqui você pega produtos de afiliado
    # Exemplo: requests.get(AFILIADO_API_URL)
    print("🔍 Verificando produtos de afiliado...")
    produtos = ["Produto A", "Produto B", "Produto C"]  # exemplo
    return produtos

def publicar_anuncio(produto):
    # Aqui você publicaria o anúncio (Facebook, Instagram ou Mercado Livre)
    print(f"📢 Publicando anúncio do {produto}...")

def monitorar_pedidos():
    # Aqui você verifica se houve algum pedido ou lead
    print("📦 Verificando pedidos ou leads...")

def executar_vendas():
    produtos = pegar_produtos()
    for produto in produtos:
        publicar_anuncio(produto)
    monitorar_pedidos()

# ===============================
# LOOP PRINCIPAL
# ===============================

def start_bot():
    print("🤖 Bot iniciado com sucesso!")
    while True:
        executar_vendas()
        # Exemplo de envio de mensagem automática
        enviar_whatsapp("Confira nossos produtos!", "<NUMERO_DO_CLIENTE>")
        enviar_instagram("Confira nossos produtos!", "<USER_ID_INSTAGRAM>")
        time.sleep(CHECK_INTERVAL)  # espera antes de rodar novamente

if __name__ == "__main__":
    start_bot()

