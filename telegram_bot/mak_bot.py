import os
import requests

def send_to_telegram(message):
    token = os.getenv('TELEGRAM_TOKEN')
    chat_id = os.getenv('TELEGRAM_CHAT_ID')
    if token and chat_id:
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        data = {"chat_id": chat_id, "text": message, "parse_mode": "Markdown"}
        requests.post(url, data=data)
        print("✅ Message sent to Telegram")

if __name__ == "__main__":
    msg = "🧠 *نظام Mak الخارق متصل الآن*\nالمستودع: `sal3023/Mak-Super-Agent` جاهز لتلقي الأوامر."
    send_to_telegram(msg)
  
