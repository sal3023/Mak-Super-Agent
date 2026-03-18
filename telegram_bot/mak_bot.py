
  
import os
import requests

# دالة إرسال الرسائل لتلجرام
def send_to_telegram(message):
    token = os.getenv('TELEGRAM_TOKEN')
    chat_id = os.getenv('TELEGRAM_CHAT_ID')
    if token and chat_id:
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        data = {"chat_id": chat_id, "text": message, "parse_mode": "Markdown"}
        requests.post(url, data=data)

# دالة النشر التلقائي في بلوجر
def post_to_blogger(title, content):
    api_key = os.getenv('BLOGGER_API_KEY')
    blog_id = os.getenv('BLOGGER_BLOG_ID')
    url = f"https://www.googleapis.com/blogger/v3/blogs/{blog_id}/posts/"
    params = {'key': api_key}
    json_data = {
        "kind": "blogger#post",
        "title": title,
        "content": content
    }
    response = requests.post(url, params=params, json=json_data)
    if response.status_code == 200:
        return True
    return False

if __name__ == "__main__":
    # محتوى المقال الأول
    title = "انطلاق نظام Mak الخارق 🧠"
    body = "تم تفعيل نظام الأتمتة الذكي بنجاح. هذا المقال تم نشره آلياً عبر GitHub و Google Cloud."
    
    # تنفيذ النشر
    if post_to_blogger(title, body):
        msg = f"🚀 *نظام Mak متصل الآن!*\n\n✅ تم نشر مقالك الأول بنجاح في مدونتك."
    else:
        msg = f"⚠️ *نظام Mak متصل* ولكن فشل النشر في بلوجر. تأكد من صحة الـ API Key و Blog ID."
    
    send_to_telegram(msg)
    
