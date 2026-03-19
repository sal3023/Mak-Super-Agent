import os
import requests

def send_telegram():
    # جلب البيانات من أسرار GitHub
    token = os.getenv('TELEGRAM_TOKEN')
    chat_id = os.getenv('TELEGRAM_CHAT_ID')
    
    # نص الرسالة
    message = "🚀 نظام Mak: تم الاتصال بنجاح! صالح، أنا أسمعك الآن."
    
    # رابط الإرسال
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {"chat_id": chat_id, "text": message}
    
    print(f"محاولة الإرسال للـ ID: {chat_id}")
    response = requests.post(url, data=payload)
    
    if response.status_code == 200:
        print("✅ تم الإرسال بنجاح!")
    else:
        print(f"❌ فشل الإرسال. الخطأ: {response.text}")

if __name__ == "__main__":
    send_telegram()
    
