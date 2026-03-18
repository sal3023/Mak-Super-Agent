import os

def build_system():
    # قائمة المجلدات المطلوبة للريبوت الخارق
    folders = ['blogger_templates', 'cloud_scripts', 'telegram_bot', 'content']
    for folder in folders:
        if not os.path.exists(folder):
            os.makedirs(folder)
            with open(f"{folder}/.keep", "w") as f: f.write("") # إبقاء المجلد حيّاً
            print(f"✅ تم إنشاء مجلد: {folder}")

    # إنشاء ملف الإعدادات الأولي
    if not os.path.exists('config.json'):
        with open('config.json', 'w') as f:
            f.write('{"agent": "Mak", "version": "1.0.0", "status": "Ready"}')

if __name__ == "__main__":
    build_system()
    print("🧠 نظام Mak جاهز للعمل بكامل طاقته.")
