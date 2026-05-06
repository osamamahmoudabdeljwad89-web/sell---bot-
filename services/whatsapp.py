import requests

def send_text(tenant, to, text):
    url = f"https://graph.facebook.com/v19.0/{tenant['PHONE_NUMBER_ID']}/messages"
    headers = {
        "Authorization": f"Bearer {tenant['WHATSAPP_TOKEN']}",
        "Content-Type": "application/json"
    }
    payload = {
        "messaging_product": "whatsapp",
        "to": to,
        "text": {"body": text}
    }
    requests.post(url, headers=headers, json=payload)

