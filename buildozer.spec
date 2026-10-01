[app]
title = PhoneRemote
package.name = phoneremote
package.domain = org.ehsan
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy,requests
orientation = portrait
osx.kivy_version = 2.1.0
fullscreen = 1
android.permissions = INTERNET, RECORD_AUDIO, CAMERA, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE
android.api = 33
android.minapi = 21
android.ndk_api = 21
android.archs = arm64-v8a, armeabi-v7a
android.services = remoteservice:service.py
# --- سایر تنظیمات پیش‌فرض بیلدوزر ---
[buildozer]
log_level = 2
warn_on_root = 1
p4a.extra_args = --break-system-packages