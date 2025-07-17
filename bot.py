import requests

TOKEN = "8094459276:AAEt1kn9ns_6AQmGR4fiJQy2SjCPdP5meD8"
URL = f"https://api.telegram.org/bot{TOKEN}"

def get_updates():
    resp = requests.get(f"{URL}/getUpdates")
    return resp.json()

def send_message(chat_id, text):
    requests.post(f"{URL}/sendMessage", data={"chat_id": chat_id, "text": text})

updates = get_updates()

for update in updates.get("result", []):
    message = update.get("message", {})
    chat_id = message.get("chat", {}).get("id")
    text = message.get("text")

    if text == "/start":
        send_message(chat_id, "أهلاً بك من بوت تيليجرام يعمل من GitHub ✅")
    elif text:
        send_message(chat_id, f"لقد أرسلت: {text}")
