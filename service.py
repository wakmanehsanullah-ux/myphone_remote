import time
import requests
from jnius import autoclass

DEVICE_CODE = "ehsanebrahim12"
DB_URL = f"https://npoint.io"

class PhoneRemoteService:
    def __init__(self):
        self.mic_status = "🎤 Microphone: OFF"
        self.camera_status = "📷 Camera: OFF"

    def start(self):
        while True:
            try:
                response = requests.get(DB_URL)
                if response.status_code == 200:
                    res_json = response.json()
                    cmd = res_json.get("command", "NONE")
                    
                    if cmd == "mic_button_clicked":
                        self.toggle_microphone()
                    elif cmd == "camera_button_clicked":
                        self.toggle_camera()
                        
                    if cmd != "NONE":
                        # ریست کردن وضعیت فرمان در سرور ابری
                        requests.post(DB_URL, json={"command": "NONE"})
            except:
                pass
            time.sleep(2)

    def toggle_microphone(self):
        if self.mic_status == "🎤 Microphone: OFF":
            self.mic_status = "🔴 Microphone: ACTIVE"
        else:
            self.mic_status = "🎤 Microphone: OFF"

    def toggle_camera(self):
        if self.camera_status == "📷 Camera: OFF":
            self.camera_status = "🔴 Camera: ACTIVE"
        else:
            self.camera_status = "📷 Camera: OFF"

if __name__ == '__main__':
    service = PhoneRemoteService()
    service.start()