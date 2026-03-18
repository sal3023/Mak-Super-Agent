import os
import requests
import sys

def send_to_telegram(message):
    token = os.getenv('TELEGRAM_TOKEN')
    chat_id = os.getenv('TELEGRAM_CHAT_ID')
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    
    print(f"--- محاولة إرسال رسالة لتلجرام ---")
    response = requests.post(url, data={"chat_id": chat_id, "text": message, "parse_mode": "Markdown"})
    
    if response.status_code == 200:
        print("✅ نجحت عملية إرسال الإشعار لتلجرام")
    else:
        print(f"❌ فشل تلجرام: {response.text}")

def post_to_blogger(title, content):
    api_key = os.getenv('BLOGGER_API_KEY')
    blog_id = os.getenv('BLOGGER_BLOG_ID')
    url = f"https://www.googleapis.com/blogger/v3/blogs/{blog_id}/posts/"
    
    print(f"--- محاولة النشر في بلوجر (Blog ID: {blog_id}) ---")
    params = {'key': api_key}
    json_data = {"kind": "blogger#post", "title": title, "content": content}
    
    try:
        response = requests.post(url, params=params, json=json_data)
        if response.status_code == 200:
            print("✅ تم النشر في بلوجر بنجاح")
            return True
        else:
            print(f"❌ فشل بلوجر: {response.text}")
            return False
    except Exception as e:
        print(f"⚠️ خطأ غير متوقع: {e}")
        return False

if __name__ == "__main__":
    # محتوى اختباري
    test_title = "نظام Mak: فحص الاتصال النهائي 🚀"
    test_body = "إذا وصلت هذه الرسالة، فهذا يعني أن الربط بين GitHub وتلجرام وبلوجر أصبح سليماً 100%."
    
    success = post_to_blogger(test_title, test_body)
    
    if success:
        send_to_telegram("🚀 *نظام Mak يعمل!* \nتم النشر في مدونتك بنجاح.")
    else:
        send_to_telegram("⚠️ *نظام Mak متصل* ولكن هناك مشكلة في النشر. راجع سجلات GitHub (Actions).")
